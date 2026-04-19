#!/usr/bin/env python3
"""
W6OAK AI Packet Radio Station — connected-only AI auto-responder.

Listens for incoming AX.25 connects to W6OAK on a Kantronics KPC-3+ TNC via a
TCP serial bridge, and carries a short QSO using Claude Haiku.

v2.0 is a rewrite against BOT_DESIGN_2026.md. See that document for the
architectural reasoning behind every rule in this file.

Requirements:
    pip install anthropic

Configuration:
    Set anthropic_api_key + tnc_host + mycall in private/config.json
    (see config.example.json). ANTHROPIC_API_KEY env var overrides the
    config file.

Usage:
    python w6oak_ai_bot.py

Emergency stop:
    Ctrl-C. The bot will send a short 73 on any active session before exit.
"""

import socket
import time
import re
import logging
import os
import json
import signal
import secrets
import threading
from datetime import datetime
from difflib import SequenceMatcher

try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False
    print("ERROR: anthropic package not installed. Run: pip install anthropic")

try:
    from beacon_manager import BeaconManager
    BEACON_MANAGER_AVAILABLE = True
except ImportError:
    BEACON_MANAGER_AVAILABLE = False
    print("WARN: beacon_manager.py not found. BTEXT rotation disabled.")


__version__ = "2.3.0"
# Version history
#   2.3.0 - 2026-04-19 - Emergency Ops mode:
#                        * Loads EMERGENCY_CONTACTS.md at boot
#                        * Injects as <emergency_directory> block in system prompt
#                        * EMERGENCY MODE in prompt: keyword + alias triggers,
#                          drill-vs-real default, 7-step escort flow
#                        * Radiogram templates (supplies, welfare, sitrep,
#                          medical, evac) with TEST TEST TEST prefix by default
#                        * Bot still never auto-connects outbound
#   2.2.0 - 2026-04-19 - Rotating BTEXT via BeaconManager:
#                        * beacon_manager.py (new) owns BTEXT rotation logic
#                        * Hybrid: static pool (BTEXT_POOL.md) + occasional Haiku line
#                        * Polled from the main loop; never rotates mid-QSO
#                        * Config knobs: beacon_rotation_enabled,
#                          beacon_rotation_minutes, beacon_api_ratio
#                        * Dry-run via `python beacon_manager.py --dry-run N`
#   2.1.0 - 2026-04-19 - Path Directory mode:
#                        * Loads PATH ANSWERS from NODE_PATHS.md at boot
#                        * Injects as <path_directory> block in system prompt
#                        * Bot now answers "how do I get to X from here" queries
#                        * See BOT_SYSTEM_PROMPT_v1.3.md for design notes
#   2.0.0 - 2026-04-18 - Full rewrite against BOT_DESIGN_2026.md:
#                        * Connected-only engagement (UI frames logged, never replied to)
#                        * Turn-taking via 8s listen window with concatenation
#                        * Per-session rate limit (20s between bot TX)
#                        * Per-session reply cap (8 then farewell + disconnect)
#                        * Dedup ring buffer across last 5 TX (fuzzy match)
#                        * Optional allowed_callers whitelist
#                        * Split logs: w6oak_rf.log (raw) + w6oak_bot.log (decisions)
#                        * Per-session correlation IDs
#                        * Clean SIGINT handler (farewell + graceful close)
#                        * Removed CQ auto-connect (listen more than speak)
#   1.2.0 - 2026-04-17 - Expanded SYSTEM_PROMPT with local-network knowledge.
#   1.1.2 - 2026-04-17 - Input-filter hardening after KK6FPP-15 session.
#   1.1.1 - 2026-04-17 - Kill self-chat loop via MCON OFF.
#   1.1.0 - 2026-04-17 - BEL-based RING detection.
#   1.0.0 - initial release.


# ---------- Configuration constants (defaults; many overridable via config) ----------

TNC_HOST = None      # loaded from config.json
TNC_PORT = None      # loaded from config.json
MYCALL   = None      # loaded from config.json
ALLOWED_CALLERS = None  # None = accept all; list = whitelist

RF_LOG_FILE  = 'private/logs/w6oak_rf.log'
BOT_LOG_FILE = 'private/logs/w6oak_bot.log'
LEGACY_LOG_FILE = 'private/logs/w6oak_ai_bot.log'  # v1.x compat

# RF timing / limits
MAX_PKT_LEN     = 120     # hard cap per transmitted line
PKT_DELAY       = 0.8     # seconds between consecutive TX lines
IDLE_TIMEOUT    = 300     # seconds of silence inside a session before we disconnect
MAX_HISTORY     = 8       # bot-remembered turns per session

# v2.0 behavior rules (BOT_DESIGN_2026.md §3, §4)
LISTEN_WINDOW   = 4.0     # seconds of quiet after last I-frame before we reply
                          # (was 8.0; dropped 4/19 to feel snappier — reassess if
                          # we see bot replying to partial multi-frame turns)
RATE_LIMIT_SEC  = 20.0    # minimum seconds between our own TX within a session
MAX_REPLIES     = 8       # hard reply cap per session, then farewell + disconnect
DEDUP_RING_SIZE = 5       # how many recent TX to compare against
DEDUP_RATIO     = 0.85    # SequenceMatcher threshold for "too similar, drop"
TX_ECHO_TTL     = 6.0     # seconds: how long a just-sent frame counts as self-echo


SYSTEM_PROMPT_BASE = """\
You are the AI operator on watch at W6OAK, an amateur packet radio station in
East Oakland, CA (CM87vs). The human licensee and control operator is Hugo.
You are Claude Haiku 4.5, made by Anthropic. Be honest you are an AI whenever
asked. Never claim to be Hugo.

YOUR ROLE:
You are a directory assistant for the 145.050 MHz packet backbone and a
companion to MONTC (K2YE-5, Oakland Hills). Connecting operators ask you
things like "how do I get to Oregon" or "how do I reach the Palo Alto BBS."
You answer with a working path from the directory below, grounded in what
other operators have verified. You never invent paths.

STATION FACTS (use only these):
- Call: W6OAK   Node: OAK/NET   KA-Node: KOAK   Mailbox: OBOX
- TNC: Kantronics KPC-3+ V9.1
- Rig: Yaesu FT-2980R at ~60W
- Antenna: Diamond X300A at 200 ft MSL
- QTH: East Oakland, CA, grid CM87vs
- Frequency: 145.050 MHz
- Direct RF neighbors: WOODY (N6ZX), MONTC (K2YE-5), BANNER (KF6DQU-9), ROCK (K6FB-5).

OPERATING STYLE:
- Hard limit: every reply under 120 characters TOTAL, including newlines.
  Count characters. If over, cut. Do not use markdown headers, code fences,
  bullet lists, or bold. Plain ASCII only. Backticks are OK for commands.
- Packet is slow. Every character costs time. Be tight.
- No fluff. No greetings beyond one line. No snark. No filler.
- Do not assume where the caller is located based on their callsign. They
  could be operating from anywhere. Answer paths from W6OAK's perspective
  unless the caller explicitly says otherwise.
- End with "de W6OAK" when it fits. Don't force it every turn.
- If the answer doesn't fit in 120 chars, split it across turns using the
  MULTI-TURN pattern below. One reply per incoming turn.

PATH ANSWERING RULES (core job):
1. When asked for a path, quote ONLY from the <path_directory> block below.
2. If the destination is in the directory, reply with the PRIMARY path.
3. If the caller asks for more detail, offer the BACKUP path or caveats.
4. If the destination is NOT in the directory, say:
   "No verified path here. From MONTC try `NODES <dest>`. de W6OAK"
5. Mention frequency-crossing ONLY when relevant (use MONTC's K2YE-N digi map).
6. Quote syntax verbatim in backticks. Never paraphrase a `c` command.
7. Flag freshness briefly if it matters. "Verified 4/18" is fine.

MULTI-TURN PATHS:
Some paths have many hops. Don't dump them all in one 120-char frame.
Send the first 2-3 hops, end with "...more?", then send the rest if they
reply yes. Example for Oregon:
  Turn 1: "OR/Medford: c HILL s / c JOHN s / c KBANN s ...more?"
  Turn 2: "...c KRDG s / c HMKR s / c 1 KC7HEX-1. Verified 4/17. de W6OAK"

GOOD vs BAD replies (short is the goal):

GOOD (69 chars): "Palo Alto W6ELA-1: c WOODY then c W6ELA-1. Verified 4/18. de W6OAK"
BAD  (265 chars): a multi-line explanation with code fences and BBS2 tips.
                  If the caller wants BBS syntax, they will ask.

TURN-TAKING:
- Stay under 120 chars per reply. If the answer needs more room, split it
  across turns (see MULTI-TURN above), waiting for the caller's next input.
- One reply per incoming turn, no double-sends.

WHAT YOU CAN HELP WITH:
- Paths from the Bay Area to: Oregon/Medford, Redding, South Bay BBS,
  Palo Alto BBS (W6ELA-1), Sacramento, Sierra foothills, Vallejo,
  Santa Clara, Berkeley, SoCal via ROCK, SFRC, and others in the directory.
- Frequency-hopping via MONTC's port digis (K2YE-6/7/8/9/4).
- Who we are, what gear we run, where we are, what frequency.
- Confirming they're connected to an AI station, not Hugo.
- Taking a message for Hugo (say you'll log it, nothing more).
- Emergency comms escort mode (see EMERGENCY MODE below).

WHAT YOU DON'T KNOW:
- Live propagation, weather, current band conditions.
- Real-time node up/down beyond what the directory says.
- Whether a specific person is on the air right now.
- Anything not in STATION FACTS, <path_directory>, or <emergency_directory>.

WHEN ASKED FOR A PATH YOU DON'T HAVE:
Reply like this (under 120 chars):
"No verified path for <dest>. Try `NODES <alias>` on MONTC. de W6OAK"

EMERGENCY MODE (escort for non-ham government / served-agency callers):

TRIGGERS. Flip into emergency mode when the caller's message matches ANY of:
- Keywords: emergency, priority, disaster, urgent, evacuation, shelter,
  casualty, supplies needed, welfare check, sitrep, medical, help send.
- An agency name or alias from the <emergency_directory> block (e.g.
  "Alameda EOC", "Red Cross", "Cal OES", "Sonoma ACS", "Napa RACES").
If unsure, ask ONE clarifying question before engaging escort mode.

DRILL VS REAL — CRITICAL SAFETY RULE.
This is a drill/test system by default. It is NOT a real emergency channel.
People must never be left thinking they have triggered a real emergency
response. You must:

1. Announce drill status in your FIRST reply whenever escort mode engages.
   Use this phrasing (or equivalent, stay under 120 chars):
   "DRILL MODE. This is a test/practice system, not a live emergency line.
   Continue? de W6OAK"

2. Ask the caller to confirm drill vs real BEFORE collecting any slots:
   "Drill or real declared emergency? (d/r)"

3. If they answer "d" or "drill" or "test" or "practice" — proceed in drill
   mode. Every composed message starts with "TEST TEST TEST" on its own
   line. Every reply that summarizes status includes "[DRILL]".

4. If they answer "r" or "real" — ask them to NAME the declared emergency
   (active wildfire, earthquake, Cal OES activation, PSPS, etc.). If they
   cannot name one, treat as drill. Even in real mode, remind them once:
   "Real mode acknowledged. W6OAK is a volunteer relay, not 911. For
   immediate life-safety dial 911. de W6OAK"

5. If the caller goes silent mid-flow or the session ends without sending,
   log the incomplete message as drill by default.

6. NEVER imply the bot itself is dispatching help. The bot composes a
   message, names a path or a voice net, and logs it. A human operator
   still has to transmit and a served agency still has to respond.

ESCORT FLOW. Follow this shape, one turn at a time, never batch:
1. Announce drill mode FIRST. "DRILL MODE. Test system, not a live
    emergency line. Drill or real? (d/r) de W6OAK"
2. Identify destination. "What agency?" Match against ALIASES column.
3. Confirm match in one line. "[DRILL] Alameda County EOC. Confirm? (y/n)"
4. Template pick. "1=supplies 2=welfare 3=sitrep 4=medical 5=evac"
5. Fill slots one at a time, plain English questions.
6. Compose and show. "[DRILL] Composed. <N> words. Send, edit, cancel?"
7. Route. Give EITHER a packet path from <path_directory> (if one exists
    for that agency's county), OR a voice net freq from the
    <emergency_directory>. Never both at once.
8. Log. Mention "Logged as <corr-id> [DRILL]" so the caller knows Hugo
    will see it AND knows this was a test.

RULES FOR EMERGENCY MODE:
- Never auto-connect outbound on the caller's behalf. Your job is compose
  and advise. The caller (or a ham helping them) pushes send.
- Never invent frequencies or paths. If the agency isn't in the
  <emergency_directory>, say so and offer the closest option plus
  146.520 simplex (national 2m calling) as last resort.
- Keep the 120-char per-reply cap. Slots get asked one per turn.
- Preserve user input verbatim in composed messages. Don't "polish"
  what they said; their words are the message.
- Flag LOW-confidence rows from the directory: "Marin freq unverified
  as of 4/19. Confirm locally."
- Part 97 §97.403 permits wider amateur use during real life-safety
  emergencies. Hugo remains the control op. You help compose and
  route, but the caller (or a ham) is the one transmitting.

WHAT YOU KNOW ABOUT PEOPLE:
Hugo has mentioned some ops: KC7HEX (Walter), N6ZOO (Ryan), KN6BDH (Rich),
KN6PE (Jim), KK6FPP (Thomas), KJ6WEG (Chris), KO6TH (Greg), K6EF (Mark),
W6ELA (Ed), KM6LYW (Craig), N6PAA (Ron).
Don't assume the caller IS that person; the callsign could be anyone on
their gear. If they identify themselves and it's clearly them, a brief
"Hugo's mentioned you" is fine. Don't lead with their name.

EXIT PROTOCOL:
Caller leaves with B, BYE, 73, or a TNC disconnect. If they sign off,
reply brief and warm in one line. The bot code handles the disconnect.

FCC:
Never transmit anything that violates Part 97. No encryption. No music.
Identify as W6OAK when asked or when signing off.
"""


# ---------- Directory loaders ----------

NODE_PATHS_FILE = 'NODE_PATHS.md'
EMERGENCY_CONTACTS_FILE = 'EMERGENCY_CONTACTS.md'


def _load_path_directory():
    """Read the PATH ANSWERS section of NODE_PATHS.md and return it as text.
    Returns an empty string (with a log warning) if the file or section is
    missing so the bot still boots and answers non-path questions."""
    try:
        with open(NODE_PATHS_FILE, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"WARN: {NODE_PATHS_FILE} not found. Path answering will be disabled.")
        return ''
    except Exception as e:
        print(f"WARN: could not read {NODE_PATHS_FILE}: {e}")
        return ''

    marker = '# PATH ANSWERS'
    idx = text.find(marker)
    if idx < 0:
        print(f"WARN: '{marker}' section not found in {NODE_PATHS_FILE}.")
        return ''
    return text[idx:]


def _load_emergency_directory():
    """Read the full EMERGENCY_CONTACTS.md file. We include the whole thing
    because the rules (Part 1-6) are all relevant at once: served agencies,
    voice net fallback, radiogram templates, escort flow, and gaps. Returns
    an empty string if missing so the bot still runs in path-only mode."""
    try:
        with open(EMERGENCY_CONTACTS_FILE, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"WARN: {EMERGENCY_CONTACTS_FILE} not found. Emergency mode disabled.")
        return ''
    except Exception as e:
        print(f"WARN: could not read {EMERGENCY_CONTACTS_FILE}: {e}")
        return ''
    return text


_PATH_DIR_TEXT = _load_path_directory()
_EMERG_DIR_TEXT = _load_emergency_directory()

_prompt_parts = [SYSTEM_PROMPT_BASE]
if _PATH_DIR_TEXT:
    _prompt_parts.append("<path_directory>\n" + _PATH_DIR_TEXT + "\n</path_directory>")
    print(f"Loaded path directory: {len(_PATH_DIR_TEXT)} chars from {NODE_PATHS_FILE}")
else:
    print("Path directory not loaded. Running without <path_directory> block.")

if _EMERG_DIR_TEXT:
    _prompt_parts.append("<emergency_directory>\n" + _EMERG_DIR_TEXT + "\n</emergency_directory>")
    print(f"Loaded emergency directory: {len(_EMERG_DIR_TEXT)} chars from {EMERGENCY_CONTACTS_FILE}")
else:
    print("Emergency directory not loaded. Running without <emergency_directory> block.")

SYSTEM_PROMPT = "\n\n".join(_prompt_parts) + "\n"


# ---------- Logging setup ----------

def _ensure_log_dir():
    d = os.path.dirname(RF_LOG_FILE)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)

_ensure_log_dir()

# Decisions log — what the bot did and why. This is the line-oriented
# human-readable log. Also streams to stdout for the console view.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s  %(levelname)-5s  %(message)s',
    handlers=[
        logging.FileHandler(BOT_LOG_FILE, encoding='utf-8'),
        logging.FileHandler(LEGACY_LOG_FILE, encoding='utf-8'),  # v1 compat
        logging.StreamHandler()
    ]
)
log = logging.getLogger('w6oak')

# RF log — raw TNC monitor output, one line per frame, no interpretation.
rf_log = logging.getLogger('w6oak.rf')
rf_log.setLevel(logging.INFO)
rf_log.propagate = False
_rf_handler = logging.FileHandler(RF_LOG_FILE, encoding='utf-8')
_rf_handler.setFormatter(logging.Formatter('%(asctime)s  %(message)s'))
rf_log.addHandler(_rf_handler)


def new_correlation_id():
    """YYYYMMDD-HHMMSS-<rand4>. One per session. Printed in every decision-log
    line tied to that session, and embedded in the RF log when the session opens."""
    return datetime.now().strftime('%Y%m%d-%H%M%S') + '-' + secrets.token_hex(2)


# ---------- TNC wrapper ----------

class TNC:
    def __init__(self):
        self.sock = None

    def connect_bridge(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(5)
        self.sock.connect((TNC_HOST, TNC_PORT))
        log.info(f"Bridge connected: {TNC_HOST}:{TNC_PORT}")

    def disconnect_bridge(self):
        try:
            if self.sock:
                self.sock.close()
        except Exception:
            pass
        self.sock = None

    def send(self, data):
        if isinstance(data, str):
            data = data.encode('ascii', errors='replace')
        self.sock.sendall(data)

    def cmd(self, text):
        log.debug(f"CMD >>> {text}")
        self.send(text + '\r')

    def tx(self, text):
        log.info(f"TX >>> {text}")
        self.send(text + '\r')

    def read(self, timeout=2.0):
        self.sock.settimeout(0.5)
        data = b''
        deadline = time.time() + timeout
        while time.time() < deadline:
            try:
                chunk = self.sock.recv(512)
                if chunk:
                    data += chunk
            except Exception:
                pass
        return data.decode('ascii', errors='replace')

    def flush(self, sec=1.5):
        self.sock.settimeout(0.3)
        deadline = time.time() + sec
        while time.time() < deadline:
            try:
                self.sock.recv(512)
            except Exception:
                pass

    def escape_to_cmd(self):
        self.send(b'\x03')
        time.sleep(0.8)
        r = self.read(1.5)
        return 'cmd:' in r

    def setup_monitor(self):
        """Listening mode. MCON and MCOM stay OFF at all times (factory defaults):
        * MCON OFF means while connected the TNC shows only our peer's traffic.
        * MCON OFF while NOT connected still lets us see incoming connect
          requests because 'all eligible packets' are displayed per MONITOR.
        * MCOM OFF keeps supervisory/control packets out of the stream.
        Keeping these flags stable across the whole session avoids mid-QSO
        TNC command leaks into the air (the v2.0 'MCON OFF' leak seen 4/18)."""
        self.send(b'\r'); time.sleep(0.4)
        self.send(b'\r'); time.sleep(0.4)
        self.flush(1.5)
        self.cmd('MONITOR ON'); time.sleep(0.4); self.flush(0.8)
        self.cmd('MCON OFF');   time.sleep(0.4); self.flush(0.8)
        self.cmd('MCOM OFF');   time.sleep(0.4); self.flush(0.8)
        self.cmd('RING ON');    time.sleep(0.4); self.flush(0.8)
        log.info("TNC monitor mode active (MCON OFF, MCOM OFF, MONITOR ON, RING ON)")


# ---------- Haiku client wrapper ----------

class Bot:
    def __init__(self, api_key):
        if not ANTHROPIC_AVAILABLE:
            raise RuntimeError("anthropic package missing")
        self.client = anthropic.Anthropic(api_key=api_key)
        self.sessions = {}

    def reply(self, callsign, message):
        history = self.sessions.setdefault(callsign, [])
        history.append({"role": "user", "content": f"{callsign}: {message}"})
        if len(history) > MAX_HISTORY * 2:
            history[:] = history[-(MAX_HISTORY * 2):]
        last_err = None
        for attempt in range(3):
            try:
                resp = self.client.messages.create(
                    model="claude-haiku-4-5-20251001",
                    max_tokens=250,
                    system=SYSTEM_PROMPT,
                    messages=history
                )
                text = resp.content[0].text.strip()
                history.append({"role": "assistant", "content": text})
                return text
            except Exception as e:
                last_err = e
                log.warning(f"Claude API error (attempt {attempt+1}/3): {e}")
                time.sleep(2 * (attempt + 1))
        log.error(f"Claude API gave up after 3 attempts: {last_err}")
        return "QRM on my end — try again? 73 de W6OAK"

    def clear(self, callsign):
        self.sessions.pop(callsign, None)

    @staticmethod
    def chunks(text):
        if len(text) <= MAX_PKT_LEN:
            return [text]
        parts = []
        current = ''
        for word in text.split():
            candidate = (current + ' ' + word).strip()
            if len(candidate) <= MAX_PKT_LEN:
                current = candidate
            else:
                if current:
                    parts.append(current)
                current = word
        if current:
            parts.append(current)
        return parts


# ---------- Frame parsing / filters ----------

FAREWELL_WORDS = {'b', 'bye', 'qrt', '73', 'sk', 'cl'}

_ARTIFACT_LINES = {'$', 'eh?', 'eh', '?', 'cmd:'}

_TNC_CMD_ECHO = re.compile(
    r'^(?:MCON|MONITOR|MON|RING|CONN|CONNECT|CONVERSE|TRANS|BEACON|ECHO|'
    r'MYCALL|MYALIAS|MHEARD|NODES|ROUTES|XMIT|CMD|OK)\s*(?:ON|OFF|\?|:)?\s*$',
    re.IGNORECASE,
)

_AX25_HEADER = re.compile(
    r'^([A-Z0-9]{3,10}(?:-\d{1,2})?)\s*>\s*[^:\r\n]+:',
    re.IGNORECASE,
)


def is_artifact(msg):
    if not msg:
        return True
    m = msg.strip().lower()
    if m in _ARTIFACT_LINES:
        return True
    if all(c in '$?!.*<>[] \t' for c in m):
        return True
    return False


def is_tnc_cmd_echo(msg):
    if not msg:
        return False
    return bool(_TNC_CMD_ECHO.match(msg.strip()))


def ascii_fold(s):
    return s.encode('ascii', errors='replace').decode('ascii')


def incoming_connect(line):
    m = re.search(r'\*\*\* CONNECTED to ([A-Z0-9-]+)', line, re.IGNORECASE)
    if m:
        return m.group(1).upper().rstrip(']').strip()
    return None


def strip_header(line):
    m = re.search(r'\]\s*:\s*(.*)', line)
    if m:
        return m.group(1).strip()
    m = re.search(r'[A-Z0-9-]+\s*>\s*[A-Z0-9,-]+\s*:\s*(.*)', line, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return line.strip()


def frame_source(line):
    """Return the source callsign of a monitored AX.25 frame, or None
    if the line is bare converse-mode data (no header)."""
    m = _AX25_HEADER.match(line.strip())
    if not m:
        return None
    return m.group(1).upper().rstrip('*')


def is_ui_frame(line):
    """Heuristic: monitored UI frames carry an AX.25 header. Bare
    in-session data has no header. If we see a header while we're
    NOT in a session, or from anyone other than our current peer,
    it's UI (or third-party) and we log-only, never reply."""
    return frame_source(line) is not None


# ---------- Session converse with v2 behavior rules ----------

class SessionState:
    """Mutable per-session state. One instance per active QSO."""
    def __init__(self, remote):
        self.remote = remote
        self.corr_id = new_correlation_id()
        self.opened_at = time.time()
        self.last_rx = time.time()        # last I-frame arrival
        self.last_tx = 0.0                # last bot TX
        self.turn_buffer = []             # accumulates I-frames within listen window
        self.turn_buffer_start = 0.0
        self.reply_count = 0
        self.recent_tx = []               # [(ts, folded_text), ...] for echo/dedup
        self.closing = False

    def push_user_line(self, msg):
        if not self.turn_buffer:
            self.turn_buffer_start = time.time()
        self.turn_buffer.append(msg)
        self.last_rx = time.time()

    def consume_turn(self):
        text = ' '.join(self.turn_buffer).strip()
        self.turn_buffer = []
        return text

    def note_tx(self, text):
        self.last_tx = time.time()
        self.recent_tx.append((time.time(), ascii_fold(text.strip())))
        cutoff = time.time() - max(TX_ECHO_TTL, 60.0)
        self.recent_tx[:] = [(t, x) for (t, x) in self.recent_tx if t >= cutoff][-20:]


def is_self_echo(state, msg):
    """Return True if msg matches something we sent within TX_ECHO_TTL.
    Covers both local TNC echoes and short delayed RF echoes."""
    cutoff = time.time() - TX_ECHO_TTL
    m = ascii_fold(msg.strip())
    if not m:
        return False
    for (t, x) in state.recent_tx:
        if t < cutoff:
            continue
        if m == x:
            return True
        if len(m) >= 6 and (m in x or x in m):
            return True
    return False


def is_dedup_match(state, candidate):
    """Return True if candidate is too similar to any of our last
    DEDUP_RING_SIZE TX lines (SequenceMatcher ratio > DEDUP_RATIO).
    Guards against echo-driven loops where the model near-duplicates
    something we already sent."""
    cand = ascii_fold(candidate.strip().lower())
    if not cand:
        return True
    recent = [x.lower() for (_, x) in state.recent_tx[-DEDUP_RING_SIZE:]]
    for prev in recent:
        if SequenceMatcher(None, cand, prev).ratio() >= DEDUP_RATIO:
            return True
    return False


def send_multiline(tnc, state, text, reason='reply'):
    """Send a (possibly multi-chunk) message as a single logical turn.
    All chunks share the same rate-limit slot (rate limit applies once)."""
    chunks = Bot.chunks(text)
    if not chunks:
        return 0
    # First chunk honors rate limit; subsequent chunks just spaced by PKT_DELAY.
    sent = 0
    first = True
    for chunk in chunks:
        # Dedup always runs
        if is_dedup_match(state, chunk):
            log.info(f"[{state.corr_id}] dedup suppressed chunk: {chunk!r}")
            continue
        if first and reason == 'reply':
            wait = RATE_LIMIT_SEC - (time.time() - state.last_tx)
            if wait > 0:
                log.info(f"[{state.corr_id}] rate-limit wait {wait:.1f}s")
                time.sleep(wait)
            first = False
        tnc.tx(chunk)
        state.note_tx(chunk)
        sent += 1
        time.sleep(PKT_DELAY)
    return sent


def converse(tnc, bot, remote):
    """Run one connected-session QSO following BOT_DESIGN_2026.md rules."""
    state = SessionState(remote)
    log.info(f"[{state.corr_id}] Session START <-> {remote}")
    rf_log.info(f"# session-open corr_id={state.corr_id} remote={remote}")

    # Expose the session to the Ctrl-C handler so it can send a farewell
    # if the operator stops the bot mid-QSO.
    shutdown.active_state = state

    # NOTE: MCON/MCOM are kept OFF at all times by setup_monitor(). We used to
    # toggle MCON OFF on session entry, which leaked the command over the air
    # (see 4/18 KJ6WEG transcript). Now it's just stable across the session.

    # Opening greeting (counts as a reply toward MAX_REPLIES). Tells the caller
    # this is an AI station and how to leave cleanly.
    greeting = bot.reply(remote, f"[{remote} just connected to W6OAK. Reply with ONE short line: greet them, say 'AI op, Hugo is licensee', remind them 'B to disconnect'. Under 120 chars.]")
    send_multiline(tnc, state, greeting, reason='reply')
    state.reply_count += 1

    own_header_re = re.compile(
        rf'^[A-Z0-9-]{{3,10}}\s+de\s+{re.escape(MYCALL)}\s*[kK]?\s*$',
        re.IGNORECASE,
    )

    tnc.sock.settimeout(1)
    buf = ''
    while True:
        # Idle timeout (no RX for IDLE_TIMEOUT seconds)
        if time.time() - state.last_rx > IDLE_TIMEOUT:
            log.info(f"[{state.corr_id}] idle timeout — closing")
            send_multiline(tnc, state, "Idle timeout. 73 de W6OAK", reason='farewell')
            time.sleep(1)
            break

        # Drain the socket
        try:
            data = tnc.sock.recv(512)
            if data:
                buf += data.decode('ascii', errors='replace')
                rf_log.info(f"[{state.corr_id}] RX-RAW: {data!r}")
        except socket.timeout:
            pass
        except Exception as e:
            log.error(f"[{state.corr_id}] read error: {e}")
            break

        if 'DISCONNECTED' in buf:
            log.info(f"[{state.corr_id}] {remote} disconnected")
            rf_log.info(f"# session-close corr_id={state.corr_id} reason=remote-disconnect")
            break

        lines = re.split(r'\r\n|\r|\n', buf)
        buf = lines[-1]
        for line in lines[:-1]:
            line = line.strip()
            if not line: continue

            # Always log to RF log verbatim
            rf_log.info(f"[{state.corr_id}] {line}")

            if 'cmd:' in line or line.startswith('***'): continue
            if re.match(rf'^{MYCALL}\s*>', line, re.IGNORECASE): continue

            # Third-party filter: if the line has a header and it's not our
            # current peer, log and drop. Rule §2: never reply to UI frames
            # or to stations other than the connected peer.
            src = frame_source(line)
            if src is not None and src != remote:
                log.debug(f"[{state.corr_id}] third-party frame from {src}, ignored")
                continue

            msg = strip_header(line) or line
            if not msg: continue
            if is_artifact(msg):
                log.debug(f"[{state.corr_id}] artifact: {msg!r}")
                continue
            if is_tnc_cmd_echo(msg):
                log.info(f"[{state.corr_id}] TNC cmd echo: {msg!r}")
                continue
            if own_header_re.match(msg):
                log.info(f"[{state.corr_id}] own-call header echo: {msg!r}")
                continue
            if is_self_echo(state, msg):
                log.info(f"[{state.corr_id}] self-echo: {msg!r}")
                continue

            # Real peer traffic. Buffer it into the current turn.
            log.info(f"[{state.corr_id}] RX <<< {remote}: {msg}")
            state.push_user_line(msg)

        # End-of-turn detection: we have buffered text AND LISTEN_WINDOW
        # seconds have passed since the last I-frame. Now we reply.
        if state.turn_buffer and (time.time() - state.last_rx) >= LISTEN_WINDOW:
            turn_text = state.consume_turn()
            log.info(f"[{state.corr_id}] turn complete ({len(turn_text)} chars): {turn_text!r}")

            # Farewell short-circuit
            if turn_text.strip().lower() in FAREWELL_WORDS:
                farewell = bot.reply(remote, f"[{remote} is signing off with '{turn_text}'. Brief warm farewell under 120 chars.]")
                send_multiline(tnc, state, farewell, reason='farewell')
                time.sleep(1)
                log.info(f"[{state.corr_id}] farewell sent, closing")
                rf_log.info(f"# session-close corr_id={state.corr_id} reason=farewell")
                break

            # Reply cap check
            if state.reply_count >= MAX_REPLIES:
                log.info(f"[{state.corr_id}] reply cap ({MAX_REPLIES}) reached — closing")
                send_multiline(tnc, state,
                               "73 — hitting my per-QSO limit. C W6OAK again anytime. de W6OAK",
                               reason='farewell')
                time.sleep(1)
                rf_log.info(f"# session-close corr_id={state.corr_id} reason=reply-cap")
                break

            # Formulate and send one reply per turn
            reply = bot.reply(remote, turn_text)
            send_multiline(tnc, state, reply, reason='reply')
            state.reply_count += 1

    bot.clear(remote)
    log.info(f"[{state.corr_id}] Session END <-> {remote} ({state.reply_count} replies, "
             f"{time.time() - state.opened_at:.0f}s)")


# ---------- Signal handling for graceful Ctrl-C ----------

class ShutdownState:
    """Shared between the signal handler and main loop. Holds a reference
    to the active session (if any) so Ctrl-C can send a farewell."""
    def __init__(self):
        self.tnc = None
        self.active_state = None  # SessionState or None
        self.requested = False


shutdown = ShutdownState()


def handle_sigint(signum, frame):
    if shutdown.requested:
        log.warning("Second Ctrl-C — hard exit")
        os._exit(1)
    shutdown.requested = True
    log.info("Ctrl-C received — attempting graceful close")
    try:
        if shutdown.tnc and shutdown.active_state and not shutdown.active_state.closing:
            shutdown.active_state.closing = True
            try:
                shutdown.tnc.tx("73 — operator stopping bot. de W6OAK")
                time.sleep(1.5)
                shutdown.tnc.escape_to_cmd()
                time.sleep(0.4)
                shutdown.tnc.cmd('DISC')
                time.sleep(1)
            except Exception as e:
                log.warning(f"Graceful close error: {e}")
        if shutdown.tnc:
            shutdown.tnc.disconnect_bridge()
    finally:
        log.info("Goodbye.")
        os._exit(0)


# ---------- Config ----------

def load_config():
    here = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(here, 'private', 'config.json'),
        os.path.join(here, 'config.json'),
    ]
    data = {}
    for cfg in candidates:
        if os.path.exists(cfg):
            with open(cfg) as f:
                data = json.load(f)
            break
    env_key = os.environ.get('ANTHROPIC_API_KEY', '').strip()
    if env_key:
        data['anthropic_api_key'] = env_key
    return data


# ---------- Main loop ----------

def main():
    global TNC_HOST, TNC_PORT, MYCALL, ALLOWED_CALLERS

    log.info("=" * 60)
    log.info(f"W6OAK AI Bot v{__version__} - starting up...")
    log.info("=" * 60)

    cfg = load_config()
    api_key = cfg.get('anthropic_api_key', '').strip()
    TNC_HOST = cfg.get('tnc_host', '').strip()
    TNC_PORT = int(cfg.get('tnc_port', 8765))
    MYCALL   = cfg.get('mycall', '').strip().upper()
    wl = cfg.get('allowed_callers', None)
    if wl:
        ALLOWED_CALLERS = set(c.strip().upper() for c in wl if c and c.strip())
        log.info(f"Whitelist active: {sorted(ALLOWED_CALLERS)}")
    else:
        ALLOWED_CALLERS = None

    if not api_key:
        log.error("No API key. Add anthropic_api_key to private/config.json or set ANTHROPIC_API_KEY.")
        return
    if not TNC_HOST or not MYCALL:
        log.error("config.json must set tnc_host and mycall. See config.example.json.")
        return
    if not ANTHROPIC_AVAILABLE:
        log.error("Run: pip install anthropic")
        return

    # Signal handlers can only be installed on the main thread. In tests
    # the bot runs in a worker thread, so the registration is a no-op there.
    try:
        signal.signal(signal.SIGINT, handle_sigint)
        signal.signal(signal.SIGTERM, handle_sigint)
    except ValueError:
        log.info("Signal handlers skipped (not running on main thread).")

    bot = Bot(api_key)
    log.info(f"Config loaded: mycall={MYCALL}, tnc={TNC_HOST}:{TNC_PORT}")
    log.info("Listening for connects (v2.0: connected-only, UI frames log-only).")

    # Beacon rotation config
    beacon_cfg = {
        'enabled'         : bool(cfg.get('beacon_rotation_enabled', False)),
        'rotation_minutes': int(cfg.get('beacon_rotation_minutes', 20)),
        'api_ratio'       : int(cfg.get('beacon_api_ratio', 6)),
        'prefix'          : cfg.get('beacon_prefix', 'W6OAK AI bot CM87. '),
        'max_len'         : int(cfg.get('beacon_max_len', 128)),
        'pool_file'       : cfg.get('beacon_pool_file', 'BTEXT_POOL.md'),
    }
    if beacon_cfg['enabled']:
        log.info(
            f"BTEXT rotation: every {beacon_cfg['rotation_minutes']} min, "
            f"api_ratio={beacon_cfg['api_ratio']}, pool={beacon_cfg['pool_file']}"
        )
    else:
        log.info("BTEXT rotation: DISABLED (set beacon_rotation_enabled=true to enable)")

    heartbeat_interval = 60
    while True:
        tnc = TNC()
        shutdown.tnc = tnc
        # Fresh BeaconManager bound to this TNC instance. We recreate it on every
        # reconnect so a stale socket never lingers inside it.
        beacon_mgr = None
        if BEACON_MANAGER_AVAILABLE:
            try:
                beacon_mgr = BeaconManager(
                    tnc=tnc,
                    enabled=beacon_cfg['enabled'],
                    rotation_minutes=beacon_cfg['rotation_minutes'],
                    api_ratio=beacon_cfg['api_ratio'],
                    prefix=beacon_cfg['prefix'],
                    max_len=beacon_cfg['max_len'],
                    pool_file=beacon_cfg['pool_file'],
                    api_key=api_key,
                )
            except Exception as e:
                log.warning(f"BeaconManager init failed: {e}")
                beacon_mgr = None
        try:
            tnc.connect_bridge()
            tnc.setup_monitor()
            tnc.sock.settimeout(1)
            buf = ''
            busy = False
            current_peer = None
            ring_seen = False
            ring_time = 0.0
            pkt_count = 0
            session_count = 0
            last_heartbeat = time.time()
            while True:
                now = time.time()
                if now - last_heartbeat >= heartbeat_interval:
                    state_label = f"IN SESSION with {current_peer}" if (busy and current_peer) else ("busy" if busy else "listening")
                    log.info(
                        f"heartbeat v{__version__}: {pkt_count} pkts heard, "
                        f"{session_count} sessions, {state_label}"
                    )
                    last_heartbeat = now
                # BTEXT rotation: no-op unless enabled, due, and not mid-QSO.
                if beacon_mgr is not None:
                    try:
                        beacon_mgr.maybe_rotate(busy=busy)
                    except Exception as e:
                        log.warning(f"beacon rotation error (continuing): {e}")
                try:
                    data = tnc.sock.recv(512)
                    if data:
                        if b'\x07' in data:
                            ring_seen = True
                            ring_time = time.time()
                            log.info("RING (BEL) detected — incoming connect expected")
                        buf += data.decode('ascii', errors='replace')
                except socket.timeout:
                    pass
                except Exception as e:
                    log.error(f"Monitor read error: {e}")
                    break
                lines = re.split(r'\r\n|\r|\n', buf)
                buf = lines[-1]
                for line in lines[:-1]:
                    if not line.strip(): continue
                    clean = line.strip()
                    if clean.startswith('cmd:'):
                        clean = clean[4:].strip()
                    # Everything we heard goes into the RF log.
                    rf_log.info(clean)
                    if '>' in clean and ':' in clean:
                        pkt_count += 1
                    if busy: continue

                    remote = incoming_connect(line)
                    if remote and remote != MYCALL:
                        if ring_seen and (time.time() - ring_time) < 10:
                            ring_seen = False
                            if ALLOWED_CALLERS is not None and remote not in ALLOWED_CALLERS:
                                log.info(f"Connect from {remote} BLOCKED by whitelist")
                                # Let the TNC's auto-disconnect handle the hang-up;
                                # we simply don't engage. Safer than racing the TNC.
                                continue
                            log.info(f"Incoming connect from {remote}")
                            busy = True
                            current_peer = remote
                            session_count += 1
                            # Build state and expose it to the signal handler
                            # so Ctrl-C can close gracefully mid-session.
                            try:
                                converse(tnc, bot, remote)
                            finally:
                                shutdown.active_state = None
                            tnc.escape_to_cmd()
                            time.sleep(1)
                            tnc.flush(2)
                            tnc.setup_monitor()
                            busy = False
                            current_peer = None
                        else:
                            log.info(f"Outgoing connect to {remote} — ignoring")
                            ring_seen = False
                        continue
                    # Rule §2: UI frames are log-only. No CQ auto-connect in v2.
        except Exception as e:
            log.error(f"Outer loop error: {e}")
        finally:
            tnc.disconnect_bridge()
            shutdown.tnc = None
        if shutdown.requested:
            break
        log.info("Reconnecting in 10 s...")
        time.sleep(10)


if __name__ == '__main__':
    main()

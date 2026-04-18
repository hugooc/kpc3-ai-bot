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


__version__ = "2.0.0"
# Version history
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
LISTEN_WINDOW   = 8.0     # seconds of quiet after last I-frame before we reply
RATE_LIMIT_SEC  = 20.0    # minimum seconds between our own TX within a session
MAX_REPLIES     = 8       # hard reply cap per session, then farewell + disconnect
DEDUP_RING_SIZE = 5       # how many recent TX to compare against
DEDUP_RATIO     = 0.85    # SequenceMatcher threshold for "too similar, drop"
TX_ECHO_TTL     = 6.0     # seconds: how long a just-sent frame counts as self-echo


SYSTEM_PROMPT = """\
You are an AI operating amateur radio packet station W6OAK in Oakland, CA.
You are Claude Haiku 4.5, made by Anthropic. The human control operator is Hugo (W6OAK).
The station runs on a Kantronics KPC3+ TNC on the 2m packet network (145.050 MHz).

PACKET RADIO RULES:
- **Hard limit: every reply under 120 characters.** This is 1200 baud packet. One line when possible.
- Never monologue. One reply per turn. Brief is better than complete.
- Use ham radio shorthand: 73, QSL, QTH, de, OM, YL, QRM, QRN, QRZ, QRT.
- Your QTH is East Oakland, near the hills. Grid square CM87.
- Be honest: you are an AI. If asked, say so clearly and warmly.
- End sessions with "73 de W6OAK" when appropriate.
- Never transmit anything that violates FCC Part 97. No encryption. No music.

LOCAL 145.050 NETWORK (CA/NV/OR NET/ROM):
- Nearby nodes: WOODY (N6ZX), KOAK (K-Net), OBOX (PBBS), ROCK (K6FB-5), ELSO (WA6KQB-5).
- KaNode aliases start with K + K-Net alias (OAK/KOAK, BERRY/KBERR). KaNodes digipeat; K-Net nodes auto-route via NODES/ROUTES.
- WOODY (N6ZX) flaky as of mid-Apr 2026. If reported, sympathize; suggest KOAK as alt.
- HMKR quirk: once connected to HMKR, downlink commands need port number FIRST: 'c 1 KC7HEX-1', not 'c KC7HEX-1 1'.
- Known path Oakland -> KC7HEX-1: KHILL, KJOHN, KBANN, KRDG, HMKR, then 'c 1 KC7HEX-1'.
- HMKR-RGR link compromised as of 4/17/26.
- SNY/KSNY is on 144.910 at MONTC, not 145.050. WBAY -> SNY handles freq hop automatically.

LOCAL PERSONALITIES:
- KC7HEX (Walter): Packet BBS Net, KPC-3+ V9.1 512K.
- N6ZOO (Ryan): net control, routing expert.
- KN6BDH (Rich), KN6PE (Jim), KK6FPP (Thomas), KJ6WEG (Chris), KO6TH (Greg), K6EF (Mark), W6ELA (Ed), KM6LYW (Craig).
- Sunday Night Packet Net + weekly PBBS check-in net. Warm, learning-focused community.

ETIQUETTE:
- Identify when asked: 'de W6OAK'. Operator is Hugo.
- Help concretely with paths when asked.
- No snark, no padding, no made-up facts (you don't have live weather, propagation, or node status beyond the above).
- Prefer ONE short packet. Split only when genuinely necessary (e.g. a path list).
"""


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
        """Listening mode: MCON ON so we can see incoming connects.
        RING ON so the TNC BEL-prefixes received connect banners."""
        self.send(b'\r'); time.sleep(0.4)
        self.send(b'\r'); time.sleep(0.4)
        self.flush(1.5)
        self.cmd('MONITOR ON'); time.sleep(0.4); self.flush(0.8)
        self.cmd('MCON ON');    time.sleep(0.4); self.flush(0.8)
        self.cmd('RING ON');    time.sleep(0.4); self.flush(0.8)
        log.info("TNC monitor mode active (MCON ON, RING ON)")

    def enter_session_mode(self):
        """MCON OFF during an active session: stop the TNC from surfacing
        our own TX back as monitored RX. Root cure for self-chat loops."""
        self.cmd('MCON OFF'); time.sleep(0.4); self.flush(0.8)
        log.info("Session mode: MCON OFF (no self-echo)")


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

    tnc.enter_session_mode()

    # Opening greeting (counts as a reply toward MAX_REPLIES)
    greeting = bot.reply(remote, f"[{remote} just connected to W6OAK. Send a warm, short greeting under 120 chars.]")
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

    heartbeat_interval = 60
    while True:
        tnc = TNC()
        shutdown.tnc = tnc
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

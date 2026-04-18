---
name: kpc3-packet-station
description: >
  Operate a Kantronics KPC-3 Plus TNC (Terminal Node Controller) via a TCP serial bridge
  running on a Windows 10 machine. The bridge holds COM11 open permanently and accepts TCP
  connections on port 8765. Claude connects directly from its bash tool to YOUR-WINDOWS-IP:8765
  to send commands; PuTTY connects to localhost:8765 on the Windows machine for live monitoring.
  Use this skill whenever the user wants to interact with their amateur radio packet station —
  sending commands, monitoring traffic, connecting to nodes or BBS systems, reading/sending
  messages, checking heard stations, adjusting parameters, or troubleshooting the TNC. Also
  trigger when the user mentions KPC3, KPC-3, TNC, packet radio, APRS, KA-Node, PBBS,
  digipeater, AX.25, callsign, or packet station commands.
---

# KPC-3 Plus Packet Station Operator

Controls a Kantronics KPC-3 Plus TNC via a **TCP serial bridge** running on Windows 10.
No Remote Desktop, no PuTTY GUI interaction, no clipboard hacks needed.

---

## Architecture

```
Claude (bash/TCP) ──────────────────────────────────────────────────────┐
                                                                         ↓
Mac ──── network ──── Windows 10 (YOUR-WINDOWS-IP) ──── kpc3_bridge.ps1 ──── COM11 ──── KPC-3+ ──── Radio ──── Antenna
                                                         ↑
                                               PuTTY (localhost:8765)
                                               (live monitoring for user)
```

---

## Station Info

| Item | Value |
|---|---|
| Callsign | **W6OAK** |
| PBBS | **OBOX** (`/B`) |
| KA-Node | **KOAK** (`/N`) |
| Digipeater | ON (`/R`) |
| TNC | Kantronics KPC-3+ |
| COM Port | COM11 (USB Serial on Windows) |
| Windows machine | YOUR-WINDOWS-IP (Lenovo ThinkPad, user: your-username) |
| Bridge TCP port | **8765** |

---

## Cheat Sheet (read first)

Fast reference for picking the right command. When in doubt, send `HELP`.

| I want to… | Command | Where to run it |
|---|---|---|
| Check or set the TNC clock | `DAYTIME` (view) / `DAYTIME yymmddhhmm[ss]` (set) | TNC `cmd:` |
| See who the TNC has heard on RF | `MHEARD` | TNC `cmd:` |
| Transmit my ID | `ID` | TNC `cmd:` |
| Turn monitoring on/off | `MONITOR ON` / `MONITOR OFF` | TNC `cmd:` |
| Connect to a station | `CONNECT <call>` | TNC `cmd:` |
| Enter our PBBS | `CONNECT OBOX` | TNC `cmd:` |
| Start a KaNode chain (from W6OAK) | `CONNECT <remote-kanode>` e.g. `CONNECT WOODY` | TNC `cmd:` |
| Enter our K-Net node (to use K-Net routing) | `CONNECT OAK` | TNC `cmd:` |
| List BBS messages | `L` | inside PBBS |
| Read BBS message n | `R n` | inside PBBS |
| List neighbor nodes + link quality | `ROUTES` (or `R`) | inside K-Net |
| List everywhere the network knows | `NODES` (or `N`) | inside K-Net |
| See path to a specific node | `NODES <alias>` | inside K-Net |
| Heard stations (at this node) | `MHEARD` (K-Net) or `J` (KaNode) | inside the node |
| Heard nodes (KaNode only) | `N` | inside KaNode |
| Chain hop from a KaNode | `C <next>` | inside KaNode |
| Routed hop from a K-Net node | `C <far-alias>` | inside K-Net |
| Stay on node after onward drop | KaNode: `C call S` / K-Net: `C call /S` | inside node |
| Abort a pending connect | `ABORT` | KaNode only |
| Exit any sub-mode back to `cmd:` | `B` or `BYE` | any sub-mode |
| Identify which node type I'm on | `HELP` or `?` | any sub-mode |

---

## Operational Modes — CRITICAL

**The station has FOUR distinct operational modes. Each mode has its own command set. Commands from one mode do NOT work in another.** Getting this wrong is the #1 cause of `EH?`, `Eh?`, `INVALID PARAMETER`, and "nothing happens" failures.

### The four modes

| # | Mode | Prompt | Entered by | Exit with |
|---|---|---|---|---|
| 1 | **TNC Command Mode** | `cmd:` | Default / after disconnect | n/a (root) |
| 2 | **KA-Node Mode** | varies (e.g. `### CONNECTED TO WILD NODE`) | `CONNECT <remote-kanode>` — e.g. `CONNECT WOODY`. **Do NOT `CONNECT KOAK` from your own TNC** (see rule 6 below). | `B` or `BYE` |
| 3 | **K-Net / NET/ROM Mode** | `OAK:W6OAK-5}` | `CONNECT OAK` (your station's own K-Net alias — this one IS valid locally) | `B` or `BYE` |
| 4 | **PBBS Mode** | `ENTER COMMAND:  B,J,K,L,R,S, or Help >` | `CONNECT OBOX` (your station's own PBBS — also valid locally) | `B` or `BYE` |

### Mode flow diagram

```
                    ┌─────────────────────────┐
                    │  TNC Command Mode       │
                    │  prompt: cmd:           │
                    │                         │
                    │  ID, STATUS, DISPLAY,   │
                    │  MHEARD, BTEXT,         │
                    │  BEACON, CONNECT,       │
                    │  DISCONNE, MONITOR      │
                    └────────────┬────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │ CONNECT <remote> │ CONNECT OAK      │ CONNECT OBOX
              │ (e.g. WOODY)     │ (your own K-Net) │ (your own PBBS)
              │ NOT "CONNECT     │                  │
              │  KOAK" — see     │                  │
              │  rule 6          │                  │
              ↓                  ↓                  ↓
   ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
   │   KA-Node Mode  │  │   K-Net Mode    │  │    PBBS Mode    │
   │                 │  │                 │  │                 │
   │  B, C, J, N,    │  │  NODES, ROUTES, │  │  L, LB, R, S,   │
   │  X, ABORT,      │  │  LINKS, MHEARD, │  │  K, HELP, BYE   │
   │  HELP           │  │  C, BYE, HELP,  │  │                 │
   │                 │  │  BBS, INFO      │  │                 │
   └────────┬────────┘  └────────┬────────┘  └────────┬────────┘
            │ B                  │ B (or BYE)         │ B (or BYE)
            └──────────────────┬─┴────────────────────┘
                               ↓
                      Back to TNC cmd:
```

### Absolute rules — memorize these

1. **You cannot jump between non-TNC modes.** Going from PBBS to a K-Net node requires: `B` to exit PBBS → land in TNC → `CONNECT OAK`. The same applies for any other transition.
2. **You cannot send TNC commands while inside a sub-mode.** `STATUS`, `DISPLAY`, `BEACON`, `BTEXT`, etc. only work at `cmd:`. Attempting them inside PBBS/KA-Node/K-Net returns an error or does nothing useful.
3. **You cannot send sub-mode commands from TNC.** `NODES`, `ROUTES`, `L` (list messages), `R n` (read) do NOT work at `cmd:`. They only work inside their respective mode.
4. **`DISCONNE` is a TNC command, not an exit command.** Never use `DISCONNE` to leave a PBBS or node — it won't work while you're inside one. Use `B` or `BYE`.
5. **`MHEARD` behaves differently per mode.** At TNC level: stations the local TNC has heard on RF. Inside a K-Net node: stations that remote node has heard. Same command, different data.
6. **At `cmd:` you ARE already `KOAK`. Do not `CONNECT KOAK` from your own TNC — it will fail with `retry count exceeded`.** The default personality of a Kantronics TNC is its KaNode. When you are at `cmd:` on W6OAK's TNC, you **are** KOAK's front door. To start a KaNode chain, you `CONNECT` directly to the **first remote** KaNode in your chain (for example `CONNECT WOODY`), not to your own KOAK. A connect goes out over RF and there's no loopback, so `CONNECT KOAK` from your own station is always going to fail silently.

   This is asymmetric:

   - **KaNode chain:** `cmd: → CONNECT <remote-kanode>` — skip your own. Your TNC is already acting as KOAK.
   - **K-Net chain:** `cmd: → CONNECT OAK → NODES / C <far>` — you DO connect to your own K-Net alias, because K-Net is a separate layer-3 routing service exposed alongside the TNC; connecting to it engages the routing engine.
   - **PBBS:** `cmd: → CONNECT OBOX` — same pattern as K-Net. The PBBS is a separate subservice, and connecting to it locally is the correct way in.

   The rule of thumb: **any alias that is your own station's KaNode is a "skip it, you're already there" alias. Every other local subservice (K-Net, PBBS) you connect to normally.**

### Warning examples the AI will see when in the wrong mode

| You see | You are in | You tried to use a command from |
|---|---|---|
| `EH?` with `$` marker | TNC cmd: | sub-mode (e.g. typed `NODES` at cmd:) |
| `Eh?` (lowercase) | K-Net node | TNC or PBBS (e.g. typed `BBS` when node didn't support it) |
| `INVALID PARAMETER` | PBBS | wrong syntax or wrong-mode command |
| `MUST HAVE NUMBER FOLLOWING COMMAND` | PBBS | `R` with no args (expected `R 5`) |
| `Can't RECONNECT, A Link state is: CONNECT in progress X` | TNC cmd: | `CONNECT` while a previous connect is still pending — clear it first with `DISCONNE` |

### Recovery: unexpected replies and lost mode awareness

If you receive `EH?`, `Eh?`, `INVALID PARAMETER`, or any response that doesn't
match what you expected, **stop and send `HELP` before doing anything else.
Do not retry the failed command.** Retrying blindly just produces more
`EH?`s and wastes time.

`HELP` is safe in every mode and its response unambiguously identifies where
you are. Use the fingerprint rules already documented elsewhere in this skill:

- **Long alphabetical grid of TNC parameter names** (ABAUD, AXHANG, BEACON,
  BTEXT, CONNECT, …) → you are at TNC `cmd:`.
- **Short list with `B, C, J, N` on one line** → you are in a **KaNode**.
- **Keyword list with `NODES`, `ROUTES`, `LINKS`, `STATS`, `BBS`** → you are
  in a **K-Net / NET/ROM node**.
- **List with `B, J, K, L, R, S`** (usually with descriptions in caps) → you
  are in the **PBBS**.

Once you've identified the mode, consult the correct command table for that
mode before proceeding. Using a TNC command inside a sub-mode (or vice versa)
is what caused the unexpected reply in the first place.

If `HELP` itself returns nothing or times out, the connection may have dropped.
Send `STATUS` as a fallback — if you see `cmd:` in the response, you're back
at TNC level and can start fresh.

**Never assume you know the current mode based on what you sent earlier in
the session.** Prior session state persists across TCP connections. A
reconnect does not reset the TNC. Always verify with `HELP` when anything
unexpected happens.

### Correct mode transitions — worked examples

**Task: read BBS messages, then check K-Net node list**

```
# Start at cmd:
CONNECT OBOX          # enter PBBS
L                     # list messages (PBBS command)
R 44                  # read message 44 (PBBS command)
B                     # exit PBBS → back to cmd:
CONNECT OAK           # enter K-Net node
NODES                 # list network nodes (K-Net command)
B                     # exit K-Net node → back to cmd:
```

**Task: check status, send beacon text, connect to KA-Node chain**

```
# Start at cmd:
STATUS                # TNC command
BTEXT hello world     # TNC command
CONNECT WOODY         # FIRST hop is a REMOTE KaNode, not your own KOAK.
                      # At cmd: you are already KOAK. See rule 6.
C KBERR               # chain onward from inside WOODY (KA-Node command)
B                     # collapse chain → back to cmd:
```

**Task (MISTAKE): trying to DISCONNE from inside PBBS**

```
# You're in PBBS
DISCONNE              # WRONG — PBBS doesn't know this command
# You'll get INVALID PARAMETER or no effect
B                     # CORRECT — this is the PBBS exit command
```

### When in doubt — type HELP

Every mode supports `HELP`. The command list you get back tells you which mode you're in:
- TNC HELP — huge list with parameter names (ABAUD, AXHANG, BEACON, BTEXT, CONNECT, etc.)
- KA-Node HELP — short list: B, C, J, N, X, ABORT, H
- K-Net HELP — NODES, ROUTES, LINKS, USERS, STATS, C, BYE, BBS, INFO, HELP
- PBBS HELP — L, LB, R, K, S, SP, SB, ST, J, B, with descriptions in caps

### Before any CONNECT — am I already this node?

Before typing `CONNECT <alias>` from W6OAK's `cmd:`, ask: **is this alias W6OAK's own KaNode?** If yes, do not send the connect — you are already there. For W6OAK the short list is:

| Alias | From W6OAK's `cmd:` | Reason |
|---|---|---|
| `KOAK` | **skip** — you already are it | KaNode is the TNC's default personality. RF loopback fails. |
| `OAK` | connect normally | K-Net is a separate service — connecting engages the routing engine. |
| `OBOX` | connect normally | PBBS is a separate service. |

If the task is "chain through KaNodes," the FIRST `CONNECT` is to the **first remote** KaNode (e.g. `CONNECT WOODY`, `CONNECT KBERR`). Every subsequent hop is an inside-the-node `C <next>`.

If the task is "use K-Net routing," the FIRST `CONNECT` is to your own K-Net alias `OAK`, then use K-Net commands (`NODES`, `ROUTES`, `C <far>`) from inside.

---

## Session Startup

Run these three steps in order at the start of every session. Skipping step 3 is
the #1 cause of "commands randomly return `EH?`" early in a session — the TNC
persists its state across TCP reconnects, so it may still be inside a PBBS,
KaNode, or K-Net node from a prior session.

### 1. Verify the bridge is reachable

```python
import socket, time

def kpc3_check():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect(('YOUR-WINDOWS-IP', 8765))
        s.close()
        return True
    except:
        return False

print("Bridge up:", kpc3_check())
```

### 2. If the bridge is down, restart it via SSH

```python
import paramiko, os, shutil

def restart_bridge():
    key = os.path.expanduser('~/.ssh/kpc3_key')
    if not os.path.exists(key):
        # Prefer the organized layout; fall back to the legacy flat layout
        project_root = '/Users/your-username/Desktop/Kantronics KPC3+ Claude Skill'
        for src in (os.path.join(project_root, 'private', 'kpc3_ssh_key'),
                    os.path.join(project_root, 'kpc3_ssh_key')):
            if os.path.exists(src):
                os.makedirs(os.path.dirname(key), exist_ok=True)
                shutil.copy2(src, key)
                os.chmod(key, 0o600)
                break
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('YOUR-WINDOWS-IP', username='your-username', key_filename=key, timeout=5)
    stdin, stdout, stderr = ssh.exec_command(
        'powershell -Command "Start-ScheduledTask -TaskName KPC3Bridge"'
    )
    ssh.close()
    time.sleep(3)
    print("Bridge restarted:", kpc3_check())
```

### 3. Ensure clean TNC state before proceeding (MANDATORY)

The TNC may be left in an unknown state from a prior session — stuck inside a
PBBS, a KaNode, or a K-Net node. Sending TNC-level commands while inside a
sub-mode causes confusing failures. The fix is a short, safe reset sequence:

- `B` — exits any sub-mode (PBBS / KaNode / K-Net). At `cmd:` the TNC treats
  bare `B` as a query for the `BEACON` parameter and replies with something
  like `BEACON EVERY 20 min`. That's noise, not an error, and is safe.
  `B` is safe to send in any mode.
- `DISCONNE` — clears any lingering connected stream at the TNC level. If
  nothing is connected, the TNC replies `Can't DISCONNECT, A Link state is:
  DISCONNECTED`. That's not an error — it's confirmation that there was
  nothing to disconnect. Treat it as success.
- `STATUS` — confirms we are back at `cmd:` and the stream reads
  `IO DISCONNECTED`.

Only proceed with the session's actual work after `STATUS` confirms
`DISCONNECTED`. If it doesn't, investigate before sending any more commands.

```python
import socket, time

def kpc3_ensure_clean_state(host='YOUR-WINDOWS-IP', port=8765):
    """
    Force the TNC back to a known-good cmd: state before doing any real work.
    Sends B (exit any sub-mode), DISCONNE (clear TNC-level stream), then
    STATUS (confirm IO DISCONNECTED). Warns if STATUS does not confirm.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    s.connect((host, port))

    def read(timeout=1.5):
        s.settimeout(timeout)
        data = b''
        try:
            while True:
                chunk = s.recv(256)
                if not chunk: break
                data += chunk
        except: pass
        return data.decode('ascii', errors='replace')

    # Two-flush to clear any stray characters / prompt noise
    s.sendall(b'\r'); time.sleep(0.7)
    s.sendall(b'\r'); time.sleep(0.7)
    read(1.0)

    responses = {}
    for cmd in ('B', 'DISCONNE', 'STATUS'):
        print(f"[cleanup] sending {cmd}")
        s.sendall(cmd.encode('ascii') + b'\r')
        time.sleep(2.0)
        resp = read(1.5)
        responses[cmd] = resp
        print(f"[cleanup] {cmd} response:")
        print(resp)

    s.close()

    if 'DISCONNECTED' not in responses['STATUS'].upper():
        print("WARNING: STATUS did not confirm DISCONNECTED. The TNC may still "
              "be in a sub-mode or have an active stream. Investigate before "
              "proceeding.")
    else:
        print("[cleanup] TNC is at cmd: with stream IO DISCONNECTED. "
              "Safe to proceed.")

    return responses

kpc3_ensure_clean_state()
```

---

## Sending Commands — Core Helper

**Critical rules for the KPC-3+:**
- Use `\r` only — never `\r\n`. A `\n` causes `EH?` errors.
- **Never use fixed `time.sleep()` to wait for an RF response.** Round-trips are non-deterministic: 2 s on a clear channel, 30+ s under retries or digipeater delay. Use sentinel polling.
- **A timeout is a failure, not a guess.** If a sentinel does not appear in time, stop the session. Do NOT send the next command "just in case it worked." That is the single biggest way an AI operator loses sync with the network and ends up talking over remote nodes.
- **Respect the 45 s bash ceiling.** A single bash call must finish within 45 s total. Track a session-wide budget and refuse to start a command that can't finish inside it. Long multi-hop operations may need to be split across bash calls.

### The sentinel-based helper (use this for all sessions)

```python
import socket, time

KPC3_HOST = 'YOUR-WINDOWS-IP'
KPC3_PORT = 8765

class KPC3Timeout(Exception):
    """Raised when an expected sentinel does not arrive in time.
    The partial output is on `.buf` so the caller can inspect and recover."""
    def __init__(self, msg, buf):
        super().__init__(msg)
        self.buf = buf

def _drain(s, seconds=0.4):
    """Consume any pending bytes so they don't contaminate the next match.
    Call this immediately before sending a command."""
    deadline = time.time() + seconds
    dropped = ''
    while time.time() < deadline:
        s.settimeout(0.1)
        try:
            chunk = s.recv(512)
            if not chunk:
                break
            dropped += chunk.decode('ascii', errors='replace')
        except socket.timeout:
            pass
    return dropped

def wait_for(s, sentinels, timeout, poll=0.3):
    """Read until one sentinel appears, or raise KPC3Timeout.

    sentinels: list of strings (case-insensitive substring match).
    timeout:   hard ceiling in seconds. Shrink this per-command from
               the session's remaining budget.
    """
    deadline = time.time() + timeout
    buf = ''
    lowered = [x.lower() for x in sentinels]
    while time.time() < deadline:
        s.settimeout(min(poll, max(0.05, deadline - time.time())))
        try:
            chunk = s.recv(512)
            if chunk:
                buf += chunk.decode('ascii', errors='replace')
                lb = buf.lower()
                for sentinel in lowered:
                    if sentinel in lb:
                        return buf
        except socket.timeout:
            pass
    raise KPC3Timeout(
        f"No sentinel {sentinels} in {timeout}s", buf=buf
    )

class KPC3Session:
    """Context manager: opens socket, enforces clean TNC state, tracks
    a total time budget so the whole session fits inside bash's 45 s limit.

    Typical use (start a KaNode chain — skip KOAK, you ARE KOAK):

        with KPC3Session(budget=40) as sess:
            sess.send('STATUS', ['cmd:'], 5)
            sess.send('CONNECT WOODY', ['or Help ?', 'DISCONNECTED',
                                        'BUSY', 'FAILURE',
                                        'RETRIED OUT'], 20)
            sess.send('N', ['or Help ?'], 10)
            sess.send('B', ['cmd:'], 5)
    """
    def __init__(self, host=KPC3_HOST, port=KPC3_PORT, budget=40.0):
        self.host, self.port = host, port
        self.budget = budget   # total seconds allowed for the session
        self.started = None
        self.s = None

    def __enter__(self):
        self.started = time.time()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, self.port))
        # Flush any stray bytes left over from the bridge, then force the
        # TNC into a known cmd: state. Cheap: two blank \r presses, then
        # a short drain, then B / DISCONNE / STATUS.
        self.s.sendall(b'\r'); time.sleep(0.3)
        self.s.sendall(b'\r'); time.sleep(0.3)
        _drain(self.s, 0.5)
        # Clean-state sequence — runs inside the session budget.
        self._ensure_clean()
        return self

    def __exit__(self, *exc):
        try:
            self.s.close()
        except Exception:
            pass

    # --- internals --------------------------------------------------

    def _remaining(self):
        used = time.time() - self.started
        return max(0.0, self.budget - used)

    def send(self, cmd, sentinels, timeout):
        """Drain → send → wait. Raises KPC3Timeout if no sentinel
        arrives, or RuntimeError if there is no budget left."""
        budget = self._remaining()
        if budget <= 0.5:
            raise RuntimeError(
                f"Session budget exhausted before sending {cmd!r}"
            )
        effective = min(timeout, budget - 0.2)
        _drain(self.s, 0.3)        # discard tail bytes from previous cmd
        print(f">>> {cmd}   (budget≈{budget:.1f}s, waiting≤{effective:.1f}s)")
        self.s.sendall(cmd.encode('ascii') + b'\r')
        try:
            resp = wait_for(self.s, sentinels, effective)
        except KPC3Timeout as e:
            print(f"!!! TIMEOUT on {cmd!r}. Partial output:\n{e.buf}")
            raise
        print(resp)
        return resp

    def _ensure_clean(self):
        """B → DISCONNE → STATUS. Every session must start at TNC cmd:
        with stream DISCONNECTED. No exceptions."""
        # B: at cmd: returns the BEACON query (harmless); inside any
        # sub-mode it exits. Accept either outcome.
        self.send('B', ['cmd:', 'BEACON EVERY'], 5)
        self.send('DISCONNE', ['cmd:'], 5)
        status = self.send('STATUS', ['cmd:'], 5)
        if 'DISCONNECTED' not in status.upper():
            raise RuntimeError(
                f"STATUS did not confirm DISCONNECTED. Bailing.\n{status}"
            )
```

### Sentinel reference table

Tightened to avoid false-positive matches on monitored/beacon frames.

| After sending… | Wait for sentinel(s) | Notes |
|---|---|---|
| Any TNC `cmd:` command | `cmd:` | STATUS, MHEARD, ID, DISCONNE, etc. |
| `CONNECT <kanode>` | `or Help ?`, `DISCONNECTED`, `BUSY`, `FAILURE`, `RETRIED OUT` | `or Help ?` is the unique tail of the KaNode banner. |
| `CONNECT <k-net>` | `}`, `DISCONNECTED`, `BUSY`, `FAILURE` | `}` is common but K-Net's prompt is the only line that ends with it at `cmd:` level. Consider regex `[A-Z0-9]+:[A-Z0-9-]+\}` for strictness. |
| `CONNECT OBOX` (PBBS) | `or Help >`, `DISCONNECTED` | `or Help >` is the unique tail of the PBBS banner. |
| KaNode `C <next>` (chain hop) | `or Help ?`, `DISCONNECTED`, `BUSY`, `FAILURE`, `RETRIED OUT` | Budget 20–35 s depending on digi count. `FRACK*(2m+1)` rule of thumb. |
| KaNode `N` or `J` | `or Help ?` | Prompt returns after list |
| K-Net `NODES`, `ROUTES` | `}` | Prompt returns after list |
| PBBS `L`, `LB`, `LM` | `or Help >` | Prompt returns after list |
| PBBS `R n` | `or Help >` | Prompt returns after message body |
| `B` or `BYE` (any sub-mode) | `cmd:` | Back to TNC level |

**Why `or Help ?` / `or Help >` instead of `ENTER COMMAND` / `>`?**
The KaNode and PBBS banners both start with `ENTER COMMAND:` but end differently (`or Help ?` vs `or Help >`). Matching on the tail disambiguates the two **and** survives monitored-frame contamination (a beacon can contain `>` or `ENTER COMMAND` but is extremely unlikely to contain `or Help ?`).

### Full session example (KaNode chain hop, inside the 45 s budget)

```python
with KPC3Session(budget=40) as sess:
    # Connect to WOODY (KaNode). Up to ~20 s at one hop.
    sess.send('CONNECT WOODY',
              ['or Help ?', 'DISCONNECTED', 'BUSY', 'FAILURE', 'RETRIED OUT'],
              timeout=22)

    # List nodes WOODY has heard.
    sess.send('N', ['or Help ?'], timeout=8)

    # Exit cleanly.
    sess.send('B', ['cmd:'], timeout=5)
```

If the connect times out, `KPC3Timeout` is raised, the `with` block exits, the socket closes, and — critically — the **next command is never sent**. You then need a fresh bash call that opens a new `KPC3Session`, which runs the clean-state sequence and aborts any pending connect (`DISCONNE` at `cmd:`).

### Multi-bash-call strategy for long operations

A CONNECT across 4 digipeaters can legitimately need 40+ seconds. If a single bash call won't fit the whole "connect + explore + disconnect" flow inside 45 s, split it:

1. Bash call #1 — open session, send `CONNECT <far>`, let `KPC3Session` run to budget, `DISCONNE` on timeout in the `finally` path. Outcome: connected or cleanly aborted.
2. Bash call #2 — open a new session. Step 3's `_ensure_clean` re-runs `B / DISCONNE / STATUS`. If the connect from #1 succeeded, we'll find a live stream and `DISCONNE` will drop it. If it didn't, we're already clean. Either way, the TNC is never left with nobody driving it.

The point of the session budget is not to finish every task in one call. It's to guarantee the **TNC is always in a known state** when the bash tool kills us.

### Simple one-shot commands (TNC cmd: only)

```python
def kpc3_quick(command, timeout=8):
    with KPC3Session(budget=20) as sess:
        return sess.send(command, ['cmd:'], timeout)

print(kpc3_quick('STATUS'))
print(kpc3_quick('MHEARD'))
print(kpc3_quick('ID'))
```

### Parsing NODES output — `kpc3_node_query`

K-Net's `NODES <alias>` returns an unordered list of routes. For a bot to pick a path automatically, parse it into a structured list. The format is **quality / obs / hops / neighbor-call**:

```python
import re

def kpc3_parse_nodes_alias(text):
    """Parse the output of K-Net `NODES <alias>` into route dicts.

    Typical response:
        Routes to HMKRCH:W7VW-6
        >192  6 2 KF6DQU-9
         141  4 3 N6ZX-5
         135  3 4 NC6J-2

    Returns [{quality, obs, hops, neighbor, active}, ...] in priority order.
    active=True on the line prefixed with '>'.
    """
    routes = []
    # Rows look like: "[>]QUAL OBS HOPS CALL-SSID"
    row = re.compile(
        r'^\s*(?P<active>>)?\s*(?P<q>\d+)\s+(?P<o>\d+)\s+'
        r'(?P<h>\d+)\s+(?P<n>[A-Z0-9]+-\d+)\s*$',
        re.MULTILINE,
    )
    for m in row.finditer(text):
        routes.append({
            'quality':  int(m.group('q')),
            'obs':      int(m.group('o')),
            'hops':     int(m.group('h')),
            'neighbor': m.group('n'),
            'active':   bool(m.group('active')),
        })
    return routes

def kpc3_node_query(alias, connect_alias='OAK', budget=35):
    """Connect to a K-Net node, run `NODES <alias>`, parse, disconnect.
    Returns list of route dicts (priority order) or [] if alias is unknown.
    """
    with KPC3Session(budget=budget) as sess:
        sess.send(f'CONNECT {connect_alias}',
                  ['}', 'DISCONNECTED', 'FAILURE'], 15)
        resp = sess.send(f'N {alias}', ['}'], 10)
        sess.send('B', ['cmd:'], 10)
    return kpc3_parse_nodes_alias(resp)

# Example:
# routes = kpc3_node_query('HMKRCH')
# for r in routes:
#     print(f"q={r['quality']} obs={r['obs']} via {r['neighbor']}")
```

### Safe disconnect cascade — `kpc3_safe_disconnect`

When something times out deep inside a chain, you don't know how many `BYE`s it takes to get back to `cmd:`. This helper sends `B` up to four times, checking the prompt after each one, then falls back to `DISCONNE` at the TNC level:

```python
def kpc3_safe_disconnect(max_byes=4, budget=20):
    """Best-effort cascade back to cmd: IO DISCONNECTED, no matter how deep.
    Safe to call when the current mode is unknown."""
    with KPC3Session(budget=budget) as sess:
        # KPC3Session.__enter__ already runs B / DISCONNE / STATUS,
        # so if we get here we're already clean. Belt and suspenders:
        for _ in range(max_byes):
            try:
                resp = sess.send('B', ['cmd:', 'or Help ?', 'or Help >', '}'], 6)
                if resp.rstrip().endswith('cmd:'):
                    break
            except KPC3Timeout:
                break
        sess.send('DISCONNE', ['cmd:'], 5)
        status = sess.send('STATUS', ['cmd:'], 5)
        return 'DISCONNECTED' in status.upper()
```

### Persistent monitoring session (read-only, don't send commands)

```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('YOUR-WINDOWS-IP', 8765))
s.settimeout(30)
try:
    while True:
        chunk = s.recv(256)
        if chunk:
            print(chunk.decode('ascii', errors='replace'), end='', flush=True)
except KeyboardInterrupt:
    pass
s.close()
```

---

## Reading the Response

| Pattern | Meaning |
|---|---|
| `cmd:` | In Command Mode, ready |
| `EH?` | Unrecognized command — check spelling or stray `\n` |
| `$` marker | Points to offending character |
| `W6OAK>ID:` | ID packet transmitted |
| `***CONNECTED to XXXXX` | Successful connection |
| `***DISCONNECTED` | Link ended |
| `KF6FB>BEACON:` | Monitored beacon from another station |

### Prompt prefix quick reference (know where you are)

The end of any response tells you exactly what's listening. **Always confirm the prompt before sending the next command** — a command meant for the TNC will be rejected by a node, and vice versa. Examples below are from live captures on this station.

| Prompt (tail of last response) | You are… | Send this kind of command |
|---|---|---|
| `cmd:` | At the TNC in command mode | TNC commands (`CONNECT`, `MHEARD`, `DISPLAY`, `STATUS`) |
| `OAK:W6OAK-5}` | Connected to the OAK K-Net node | K-Net commands (`NODES`, `ROUTES`, `C BUTANO`, `BYE`) |
| `BANNER:KF6DQU-9}` | Connected to BANNER K-Net node | K-Net commands |
| `WBAY:N6ZX-5}` | Connected to WBAY K-Net node | K-Net commands |
| `WBAY:N6ZX-5} Connected to BANNER:KF6DQU-9` | At WBAY, which just routed you through to BANNER | You're talking to BANNER now |
| `ENTER COMMAND: B,C,J,N, or Help ?` | At a KaNode (e.g. KOAK, KJOHN) | KaNode commands (`C`, `J`, `N`, `B`, `ABORT`) |
| `ENTER COMMAND:  B,J,K,L,R,S, or Help >` | In the PBBS | PBBS commands (`L`, `R n`, `S call`, `B`) |
| `*** CONNECTED to XXXXX` | Fresh connect banner just arrived | Whatever that station expects — wait for its real prompt |
| `*** DISCONNECTED` | Link dropped | You're back at `cmd:` |
| `Eh?` (lowercase) | At a K-Net or KaNode, unrecognized command | Send `HELP` to see what's valid here |
| `EH?` (uppercase, with `$` marker) | At the TNC, unrecognized command | Check for stray `\n`, resend after two blank `\r` |
| `Can't DISCONNECT, A Link state is: DISCONNECTED` | Informational only | Not an error — already at `cmd:`, carry on |

**Detect the prompt programmatically (order matters — check specific before generic):**

```python
import re

def detect_prompt(buf):
    """Given the tail of a TNC response, return one of:
       'tnc' | 'kanode' | 'pbbs' | 'knet' | 'knet-tunneled' | 'unknown'
    """
    # Strip trailing whitespace but keep the last ~200 chars
    tail = buf[-200:].rstrip()
    low = tail.lower()
    if 'or help ?' in low:
        return 'kanode'
    if 'or help >' in low:
        return 'pbbs'
    # K-Net prompt: ALIAS:CALL-SSID}  — optionally followed by "Connected to ..."
    if re.search(r'[A-Z0-9]+:[A-Z0-9]+-\d+}\s*Connected to', tail):
        return 'knet-tunneled'
    if re.search(r'[A-Z0-9]+:[A-Z0-9]+-\d+}\s*$', tail):
        return 'knet'
    if tail.endswith('cmd:'):
        return 'tnc'
    return 'unknown'
```

---

## Companion file: NODE_PATHS.md

A living map of which nodes reach which other nodes on 145.05 MHz in Northern California lives in the skill folder as `NODE_PATHS.md`. Before attempting a multi-hop or cross-region connect, **read NODE_PATHS.md first** — it has:

- Confirmed edges between K-Net and KaNode stations, with the type of each endpoint
- Degraded/broken edges (e.g. `HMKR ↔ RDG` currently broken)
- A "Path Cookbook" of verified multi-hop recipes (e.g. Bay Area → Oregon border via `OAK → WBAY → BANNER → RDG → HMKRCH`)
- Live capture snapshots of `NODES` / `ROUTES` from OAK, WBAY, and BANNER
- Failure notes for specific routes (e.g. L4 stalls observed when routing from OAK to BUTANO)

The file is maintained by hand, so treat it as authoritative for "has this path ever worked" but always verify with a fresh `NODES <alias>` at the K-Net node before committing to a route.

---

## Common TNC Commands

**These only work at the `cmd:` prompt (TNC Command Mode).** If you're inside a PBBS, KA-Node, or K-Net node, exit first with `B`.

| Command | Purpose |
|---|---|
| `ID` | Transmit ID packet over the air |
| `STATUS` | Current stream/link status |
| `DISPLAY` | All parameter values |
| `VERSION` | Firmware version |
| `MONITOR ON/OFF` | Enable/disable packet monitoring |
| `MHEARD` | Recently heard stations |
| `CONNECT call [VIA digi]` | Connect to a station |
| `DISCONNE` | Disconnect current stream |
| `MYCALL callsign` | Set/view TNC callsign |
| `BEACON EVERY n` | Beacon every n minutes (0=off) |
| `BTEXT text` | Set beacon text |
| `TXDELAY n` | Key-up delay (10ms steps) |
| `FRACK n` | Retry timeout in seconds |
| `RESET` | Soft reset |
| `DAYTIME yymmddhhmm[ss]` | Set the TNC's internal clock. Format: 2-digit year, month, day, hour (24h), minute, and optionally seconds. Example: `DAYTIME 260416080600` sets April 16, 2026 at 08:06:00. If entered with no parameter, displays the current date/time using the format defined by the `DAYSTR` command. |

---

## BBS variants on packet — not all "BBS" stations are the same

"BBS" is a category, not a protocol. On 145.050 and neighboring frequencies you'll encounter at least two distinct BBS implementations, and they have very different command sets. Knowing which kind you just connected to saves a lot of "Unknown command." airtime.

### PBBS (Kantronics and similar)

The built-in mailbox on KPC-3+ style TNCs and classic store-and-forward BBS stations. Commands are the verbs you'll see in the section below: `L`, `R`, `SP`, `SB`, `K`, `J`, `/EX`, etc. Our own station's `OBOX` is a PBBS. `KN6BDH-1` (Vallejo) is also PBBS-flavored.

### BBS2 (Ed's BBS / W6ELA-1 / Palo Alto)

A modern Python BBS by Ed W6ELA (MIT license, `github.com/elafargue/bbs2`). Runs on a solar-powered Raspberry Pi 4 with a Kenwood TM-V71 and Direwolf + AGWPE. The command set is **menu-driven with two-letter codes**, not PBBS verbs. Connecting shows:

```
=== Ed's BBS ===
  [BU] Bulletins                          [CO] Color
  [C] Chat                                [A] Auth
  [I] BBS Info                            [B] Bye (disconnect)
  [LC] Last Connections                   [?] Help
```

Key differences from PBBS:

- **No `L` / `R` / `SP`.** Sending `L` to BBS2 returns `Unknown command.`
- **Bulletins live under `BU`**, not `LB`.
- **`C` enters a chat room** (`main`), not a compose buffer. The chat room retains recent history so posting in an empty room still leaves a note for the next visitor.
- **`A` requires an OTP secret** issued out-of-band by the sysop. At first connect you have `ident` access (read-only). Ask the sysop by email for an OTP to unlock more.
- **`B` or `BYE` disconnects.** If you reached BBS2 via an intermediate KA-Node (e.g. WOODY), one `B` at the BBS tears down the whole chain.

### How to tell which one you've reached

When you connect, look at the banner:

- `### CONNECTED TO WILD NODE ... CHANNEL A` followed by `ENTER COMMAND: B,C,J,N, or Help ?` → KA-Node, not a BBS (but often on the way to one).
- `(OBOX) W6OAK-1 >` or similar callsign prompt with PBBS-style commands → PBBS.
- ASCII-art banner + two-letter menu items in square brackets → BBS2.

If you're unsure, send `?` — the help text will tell you which command vocabulary is in play.

---

## PBBS Commands (connect first: `CONNECT OBOX`)

**You must be in PBBS Mode to use these.** See [Operational Modes](#operational-modes--critical). Exit with `B` or `BYE` to return to TNC cmd:.

### Reading messages

| Command | Purpose |
|---|---|
| `L` | List all messages you can read |
| `LB` | List **public bulletins** only (addressed to ALL) |
| `LM` | List unread messages addressed to you |
| `LL n` | List the last n messages |
| `L > call` | List messages TO a callsign |
| `L < call` | List messages FROM a callsign |
| `R n` | Read message number n |
| `RH n` | Read message n with full headers |
| `RM` | Read all messages addressed to you |

### Sending messages

The send flow is a multi-step interactive sequence:
1. `S WA6L` (or `SP`, `SB`, `ST`) — starts composition
2. PBBS prompts `SUBJECT:` → type the subject, press Enter
3. PBBS prompts `ENTER MESSAGE n--END WITH CTRL-Z OR /EX ON A SINGLE LINE` → type the body
4. Send `/EX` on its own line to finalize → PBBS replies `MESSAGE SAVED`

| Command | Purpose |
|---|---|
| `S call` | Send a regular message to callsign |
| `SP call` | Send **private** message |
| `SB call` | Send **bulletin** (public) |
| `ST call` | Send **traffic** message (NTS) |

### Housekeeping

| Command | Purpose |
|---|---|
| `K n` | Delete message number n |
| `KM` | Delete all read messages addressed to you |
| `U` | List everyone connected to the PBBS |
| `HELP` | Show full command list with descriptions |
| `B` or `BYE` | Disconnect from PBBS → back to TNC cmd: |

---

## Nodes: KA-Node vs K-Net (NET/ROM)

Two very different node types live in the packet world. Knowing which one you're talking to changes what commands work and what the node can do for you. Our station's onboard node **KOAK** is a **KA-Node** (not a K-Net node).

### IMPORTANT: Same TNC, two node personalities

Most KPC-3 / KPC-3+ TNCs run **BOTH** a K-Net node and a KaNode **at the same time, in the same box**, under two different aliases. Example pairing from the same radio:

| Same TNC, same radio | Alias |
|---|---|
| K-Net node | `BERRY` |
| KaNode | `KBERR` |

Both are "BERRY" geographically but each responds to its own alias. The naming convention on this network is: **KaNode alias = `K` + first 3 or 4 letters of the K-Net alias**.

| K-Net alias | KaNode alias |
|---|---|
| `JOHN` | `KJOHN` |
| `BERRY` | `KBERR` |
| `BETHEL` | `KBETH` |
| `OAK` (our station) | `KOAK` (our station) |

**Do not assume `BERRY` and `KBERR` are the same thing from the user's perspective.** They have different capabilities. If you want routing → connect to the K-Net alias. If you want to digipeat or manually chain → connect to the KaNode alias.

### Canonical fingerprint: the `HELP` command

The single most reliable way to identify which node type you're talking to is to send `HELP` (or `?`). The two responses are **entirely different**:

**KaNode HELP response (short, terse):**
```
ENTER COMMAND: B,C,J,N, or Help ?
ABORT    STOP A CONNECTION IN PROGRESS
B(ye)    NODE WILL DISCONNECT
C(onnect) call   CONNECT TO callsign
C call S(tay)    STAY CONNECTED TO NODE WHEN END DISCONNECTS
J(heard)         CALLSIGNS WITH DAYSTAMP
J S(hort)        HEARD CALLSIGNS ONLY
J L(ong)         CALLSIGNS WITH DAYSTAMP AND VIAS
N(odes)          HEARD NODE CALLSIGNS WITH DAYSTAMP
N S(hort)        NODE CALLSIGNS ONLY
N L(ong)         NODE CALLSIGNS WITH DAYSTAMP AND VIAS
```

**K-Net HELP response (longer, keyword list):**
```
BERRY:K6JAC-4} TYPE 'HELP' OR ? FOLLOWED BY COMMAND FOR MORE INFORMATION
BYE  BBS  CONNECT  CQ  HELP  INFO  LINKS  MHEARD  NODES  PORTS  ROUTES  STATS  USERS  SYSOP
```

Rule: if you see `B,C,J,N` on one line, it's a **KaNode**. If you see `NODES`, `ROUTES`, `LINKS`, `STATS`, `BBS` as distinct keywords, it's **K-Net**.

### Quick capability comparison

| Feature | KA-Node | K-Net / NET/ROM |
|---|---|---|
| Protocol | Kantronics proprietary, simple | NET/ROM-compatible ("The Net" protocol) |
| Routing | Silent. Operator must chain the path manually. | Automatic. Nodes broadcast routes/nodes to neighbors. |
| Discover distant nodes | Not possible from the node itself | `NODES` lists everything the net has advertised |
| Digipeat | **Yes** — used for Unproto chains (Sunday Night Packet Net) | **No** — pure node, does not digipeat |
| Connect to distant node | Chain manually: `C A`, then `C B`, then `C C` | Single command: `C FARNODE` — node finds the route |
| Direct BBS hop | No | Yes (`BBS` command) |
| Heard-list commands | `J` = stations heard, `N` = nodes heard | `MHEARD` = stations heard (node-local) |
| "Stay on node" on onward connect | `C call S(tay)` | `C call /S` |
| Abort a pending connect | `ABORT` | not available the same way |
| Typical naming | `K` + 3-4 letters (e.g. `KOAK`, `KBERR`) | Location word (e.g. `OAK`, `BERRY`, `BUTANO`) |
| Kantronics term | KaNode | K-Net (their NET/ROM implementation) |

**Rule of thumb:** alias starts with `K` and is short → probably a KaNode. Real word like `OAKLND` or `BUTANO` → probably K-Net. Not 100% reliable — always confirm with `HELP`.

### Identifying which type you're on after connecting

- **KaNode welcome banner:** some variant of
  `### CONNECTED TO WILD NODE xxxx(CALLSIGN) CHANNEL A` followed by
  `ENTER COMMAND: B,C,J,N, or Help ?`. Spacing varies by firmware (some print
  `### ` with a space, some print `###` joined to `CONNECTED`). The `X` in
  the command list appears only on multi-port TNCs — single-port KPC-3+
  stations list just `B,C,J,N`. Don't match on exact whitespace. Match on
  the literal substring `CONNECTED TO WILD NODE`, which is the stable
  identifier across all firmware revisions and port counts.
- **K-Net welcome banner:** usually shows CTEXT (operator-set greeting). The prompt looks like `BERRY:K6JAC-4}`. `HELP` reveals `NODES`, `ROUTES`, `LINKS`, `BBS`, `STATS`.

When unsure, send `HELP`. It's free, fast, and unambiguous.

---

## KaNode Commands (connect first: `CONNECT <remote-kanode>` — e.g. `CONNECT WOODY`)

**You must be in KaNode Mode to use these.** See [Operational Modes](#operational-modes--critical).

> **Starting a KaNode chain from W6OAK — read this first.** At `cmd:` your TNC is already acting as `KOAK`. Don't `CONNECT KOAK` from your own station — it tries to open an RF session to yourself, fails with `retry count exceeded`, and drops silently back to `cmd:`. Start the chain with the **first remote KaNode** you want to talk to, e.g. `CONNECT WOODY`. See rule 6 in the Operational Modes section.
>
> (You would only `CONNECT KOAK` if you were operating from a DIFFERENT station and wanted to reach W6OAK. From W6OAK itself, skip it.)

Connecting to a remote KaNode with `CONNECT <alias>` puts you in that node's converse mode — commands now go to the remote node, not the TNC. Exit with `B` or `BYE` to return to TNC cmd:.

KaNodes have a **small, fixed command set**. The full list is literally what `HELP` returns:

| Command | Purpose |
|---|---|
| `B` (Bye) | Disconnect from node |
| `C call` | Connect onward to a station or node |
| `C call S` | Same, but **S(tay)** keeps you on this node if the far end drops |
| `J` | **Jheard** — stations the node has heard (with daystamp) |
| `J S` | Jheard **Short** — callsigns only, no daystamp |
| `J L` | Jheard **Long** — adds destination field and digipeaters used. `*` = heard via a digipeater |
| `N` | **Nheard** — nodes the KaNode has heard on RF (with daystamp) |
| `N S` | Nheard **Short** — node callsigns only |
| `N L` | Nheard **Long** — with destinations and digis; `*` = via a digipeater |
| `X call` | Cross-connect to a station on the opposite port (multi-port TNCs only) |
| `ABORT` | Abort a connect-in-progress. Must be issued immediately after `C`. |
| `H` or `?` | Show the HELP banner above |

**Important distinctions:**
- `J` and `N` in a KaNode are BOTH "heard" lists — `J`heard is stations, `N`heard is nodes. This is different from K-Net, where `N`ODES is the routing table, not a heard list.
- KaNodes have no automatic routing. `N` tells you what the node has heard on air, not how to get somewhere.

**Chained path example (KaNode), starting from W6OAK's `cmd:`:**
```
# Start at cmd:. You ARE KOAK. Do NOT "CONNECT KOAK".
CONNECT KBERR         # first hop is a REMOTE KaNode (KBERR = WB6YNM-4)
C KRDG                # from inside KBERR, connect onward to KRDG
```
Each hop is a fresh connect — the operator drives the routing. Use `C <call> S` on any hop if you want to remain on that node after the remote end disconnects.

### Chain-hopping in practice — field notes for AI operators

Field notes from an actual session chaining `W6OAK → WOODY(N6ZX) → KJOHN(KF6ANX-8)`.
These are the non-obvious things that trip up small/fast models on KaNode work.

**1. Identify the node type from the CONNECT banner — you don't need `HELP`.**
The Kantronics firmware emits a hard-coded banner for every KaNode:

```
### CONNECTED TO WILD NODE <ALIAS>(<CALLSIGN>) CHANNEL A
ENTER COMMAND: B,C,J,N, or Help ?
```

Don't match on exact whitespace. The substring `CONNECTED TO WILD NODE` is the
stable identifier across all KPC-3+ firmware revisions. Some firmware prints
`### ` with a space, others print `###` joined to `CONNECTED`. The `X` in the
command list appears only on multi-port TNCs (for `Xconnect`); single-port
KPC-3+ stations list just `B,C,J,N`. Any of those variants is still a KaNode.

If you see `CONNECTED TO WILD NODE` anywhere in the response after `CONNECT`,
you're on a KaNode — full stop. `HELP` is only needed later if something
surprises you. K-Net nodes never emit this banner; they emit CTEXT
(operator-configured) and prompt like `NODEALIAS:CALLSIGN-SSID}`.

**2. Don't send the two-`\r` flush once you're connected.**
The flush pattern in `kpc3_command()` is correct for `cmd:` only. When you're
inside any sub-mode, every `\r` is forwarded to the remote node as a blank line,
which wastes airtime and can produce junk replies. Use a no-flush helper for
commands sent through an established link:

```python
def through(cmd, wait=15.0, read_timeout=3.0):
    """Send one command over an already-established AX.25 link. No pre-flush."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5); s.connect((KPC3_HOST, KPC3_PORT))
    # (same read() inner function as kpc3_command)
    s.sendall(cmd.encode('ascii') + b'\r')
    time.sleep(wait)
    resp = read(read_timeout)
    s.close()
    return resp
```

**3. Double your wait times on chained sessions.**
Each additional hop adds one AX.25 round-trip. Rough guide:

| Link depth | Recommended `wait=` for short queries (HELP, J, N) |
|---|---|
| Direct KaNode (1 hop) | 6-10s |
| Two-hop chain (e.g. WOODY → KJOHN) | 15-20s |
| Three-hop chain | 25-35s, consider `MONITOR ON` to watch raw traffic instead |

The manual formalizes this: the effective AX.25 frame timeout is
`FRACK * ((2*m)+1)` seconds, where `m` is the number of digipeaters in the
path. With default `FRACK 5` and a 4-digi chain, one unanswered frame waits
~45 seconds before retrying. If you find yourself doing 3+ hop chains
regularly, either raise `FRACK` or accept longer waits. If a truncated or
interleaved response comes back, the fix is always longer wait before
reading — not shorter.

**4. `###LINK MADE` confirms an onward hop succeeded.**
When you send `C <call>` from a KaNode, three things can happen:

- `###LINK MADE` followed by the target's `###CONNECTED TO WILD NODE …` banner
  → chain established, you're now talking to the target.
- Silence for >30s → connect is still retrying AX.25. Send `ABORT` from the
  KaNode to cancel. The ABORT window is tight — issue it before success.
- `###FAILURE WITH <call>` or `NO ANSWER` → target not reachable from here.
  You're still on the parent KaNode; try a different neighbor.

**5. `N` listings use `*` to mark "heard via digipeater".**
In a KaNode's `N` (nodes heard) listing, an asterisk after an alias means the
node was heard indirectly through a digipeater, not directly on air. Example
from KJOHN:

```
HOGAN      (WA6D-5)    04/16/2026 14:16:11
KBULN*     (W6ABJ-12)  04/16/2026 14:19:21   ← heard via a digipeater
BETHEL     (WB6YNM-3)  04/16/2026 14:21:37
```

For chain planning, prefer non-asterisk entries. Digipeated nodes may or may
not connect reliably from your current position.

**6. Geographic window shifts on every hop.**
WOODY and KJOHN are physically different radios with different antennas, so
their `N` listings overlap only partially. Hopping one node over can reveal
neighbors your station can't hear directly from home. This is why chain-hopping
is a real discovery tool, not just a routing curiosity.

**7. One `B` from the deepest node collapses the entire chain (no STAY).**
If every hop was made without `STAY`, a single `B` from the innermost node
cascades all the way back. Expected sequence:

```
B                                   (sent to KJOHN)
###DISCONNECTED BY KJOHN AT NODE WOODY   (WOODY reports KJOHN dropped us)
*** DISCONNECTED                    (WOODY drops us because no STAY)
cmd:                                (back at TNC)
```

If a hop was made with `C <call> S`, `B` only retreats one level — you'll
land back on the STAY node and need another `B` to fully disconnect.

**8. Distinguish TNC echo headers from node responses.**
When monitor is on, the TNC echoes your outgoing packets back to you with a
header like `W6OAK>WOODY [timestamp]:` followed by what you sent. That's NOT
the node's reply. The node's reply follows the header with no AX.25 preamble.
Don't parse the echo as a response.

**9. CTEXT fragments can linger in the read buffer after CONNECT.**
The first read after `CONNECT` sometimes returns a tail of your own CTEXT
(the greeting the TNC auto-transmits to the remote) that hasn't fully flushed
yet. If the first line of a response looks nonsensical and mentions your own
callsign or station info, discard it — it's stale CTEXT, not node output.

**10. Cross-check with `STATUS` after every disconnect.**
After any `B` or chain-collapse, send `STATUS` (with the flushing helper
since you're back at `cmd:`). Expect `A stream - IO DISCONNECTED`. If you
see `IO CONNECTED` or `LINK SETUP`, the TNC still thinks something's alive
— send `DISCONNE` to clear it.

### Multi-hop chain discipline — the handshake mindset

This is the single most important section for any AI driving multi-hop chains. The failure mode is predictable: the AI sends command 2 before the remote node has had time to answer command 1, the buffer desyncs, and the rest of the session is garbage. The fix is a mindset, not a sleep value.

**The core rule:** after every command that crosses RF, you do not send the next command until you have seen the remote node talk back. "Talking back" means one of three things — the target's banner, a failure message, or a recognizable prompt tail. No banner, no fail, no prompt = the link is still in motion. Wait.

**Why latency stacks on every hop.** A chain like `W6OAK → WOODY → KJOHN` is not one radio path. It's a series of independent AX.25 links:

```
(you)        ─── RF ───>        (WOODY)        ─── RF ───>        (KJOHN)
       ←──── ack ────                     ←──── ack ────
```

When you type `C KJOHN` from inside WOODY, WOODY must (1) hear your frame, (2) build a new AX.25 session with KJOHN, (3) wait for KJOHN to ack, (4) relay the result back to you. Each hop doubles the RF round-trip. Short queries at one hop take 6-10 s; the same query two hops deep takes 15-20 s; three hops deep, 25-35 s. The formula from the manual is `FRACK * ((2*m)+1)` where `m` is digipeaters in path.

**The handshake signals per node type:**

| Remote node type | Signal that says "I'm ready, send the next command" |
|---|---|
| KaNode (connect succeeded) | `### CONNECTED TO WILD NODE <alias>(<call>) CHANNEL A` + banner ending in `or Help ?` |
| KaNode (onward hop succeeded) | `###LINK MADE` then target's own `### CONNECTED TO WILD NODE …` banner |
| K-Net (connect succeeded) | CTEXT greeting + prompt ending in `<ALIAS>:<CALL>-<SSID>}` |
| PBBS (connect succeeded) | `ENTER COMMAND: B,J,K,L,R,S, or Help >` |
| Any short query returned | The SAME prompt tail you saw on connect (`or Help ?`, `}`, or `or Help >`) reappearing |
| Failure | `###FAILURE WITH <call>`, `NO ANSWER`, `BUSY`, `RETRIED OUT`, or `DISCONNECTED` |

**Pre-hop verification.** Before sending `C KJOHN` from WOODY, you should have just read KJOHN in WOODY's `N L` output. If KJOHN is not there, the hop will fail — you know this before transmitting. If KJOHN is there but has an asterisk (`KJOHN*`), WOODY heard KJOHN only via a digipeater; the hop may work but is less reliable than a non-asterisk entry.

**The workflow, applied to "connect to KJOHN via WOODY":**

1. Clean state at `cmd:` (automatic in `KPC3Session`).
2. `CONNECT WOODY` — wait for `or Help ?` (WOODY's KaNode banner). Budget 15-20 s.
3. `N L` through WOODY — wait for `or Help ?` to return after the list. Budget 10-12 s.
4. **Parse the list in your head.** Is `KJOHN` present? Non-asterisk? If not, stop now.
5. `C KJOHN` — wait for either a second `CONNECTED TO WILD NODE` banner (this time KJOHN's), or `###FAILURE`, or `RETRIED OUT`. Budget 18-25 s because this is now a 2-hop handshake.
6. Do work at KJOHN (one command at a time, each with its own wait).
7. `B` from KJOHN — wait for `cmd:` to reappear. Without STAY, one `B` collapses the whole chain. Budget 18-22 s.
8. `STATUS` — confirm `IO DISCONNECTED` before declaring success.

**Anti-pattern to avoid:**

```python
# DON'T DO THIS — blind back-to-back sends
sess.send('CONNECT WOODY', [...], 15)
sess.send('C KJOHN',       [...], 15)   # assumes previous succeeded, blasts next
sess.send('HELP',          [...], 10)
```

Even if each call waits for a sentinel, the AI has no idea what KaNode it's on when `HELP` runs. Was the C KJOHN a success or a failure? If failure, `HELP` runs on WOODY, not KJOHN. The code passes the type-check but the operator is flying blind. Always inspect the response text from each send and branch on it before sending the next command.

### Checking if a far node runs a BBS

KaNodes have no `BBS` query — unlike K-Net nodes, which do. To check if a remote KaNode site runs a BBS, you have three options, ranked by preference:

1. **Inspect the CTEXT (welcome banner) that arrives on CONNECT.** Many sysops advertise their BBS callsign or alias in the greeting. Look for strings like `BBS`, `MAILBOX`, `PBBS`, or a callsign with `-1`, `-4`, `-5`, `-8` SSID. If the banner mentions a BBS callsign, that's your target.
2. **Try the paired K-Net alias.** Most KaNode sites also run a K-Net node under a sibling alias (KOAK ↔ OAK, KJOHN ↔ JOHN, KBERR ↔ BERRY). From `cmd:`, exit the KaNode chain (`B`), then `CONNECT <k-net alias>`. K-Net exposes a direct `BBS` command that jumps you straight into the mailbox.
3. **Probe known BBS SSID patterns.** If CTEXT is silent and there's no K-Net sibling, try `C <basecall>-4` or `C <basecall>-1` from the KaNode. If a BBS answers, you'll see a PBBS banner ending in `or Help >`. If not, you'll get `###FAILURE` or `NO ANSWER`. This is a probe — announce to the user that you're making a guess before sending it.

**For the specific "is there a BBS on KJOHN" task:** the cleanest route is option 2. KJOHN's K-Net sibling is `JOHN`. From `cmd:`, `CONNECT JOHN`, then type `BBS` at the K-Net prompt — if a mailbox exists, you'll land inside it. If `BBS` returns `Not available` or similar, there isn't one.

### Minimal chain-hop recipe (uses the modern `KPC3Session` API)

This is a rewrite of the old blind-sleep recipe. It fits inside one bash call when the chain is short. For longer chains, split across two calls per the "multi-bash-call strategy" note in the Core Helper section.

```python
# Scenario: connect to WOODY, verify KJOHN is reachable, hop to KJOHN,
# then ask if KJOHN's sibling K-Net node has a BBS.
# Budget: 40 s total. Second phase (BBS check) may need a second bash call.

KANODE_BANNER = ['or Help ?', 'DISCONNECTED', 'BUSY',
                 'FAILURE', 'RETRIED OUT', 'NO ANSWER']

with KPC3Session(budget=40) as sess:
    # Step 1: get to WOODY.
    resp = sess.send('CONNECT WOODY', KANODE_BANNER, timeout=20)
    if 'CONNECTED TO WILD NODE' not in resp.upper():
        raise RuntimeError(f"WOODY connect failed:\n{resp}")

    # Step 2: list nodes WOODY has heard.
    nodes = sess.send('N L', ['or Help ?'], timeout=12)
    if 'KJOHN' not in nodes.upper():
        # clean up before bailing
        sess.send('B', ['cmd:'], 15)
        raise RuntimeError("KJOHN not in WOODY's N L list — hop not attempted")

    # Step 3: hop to KJOHN. Two-hop handshake — allow more time.
    resp = sess.send('C KJOHN', KANODE_BANNER, timeout=22)
    if 'CONNECTED TO WILD NODE KJOHN' not in resp.upper():
        # attempt graceful retreat — we're still on WOODY
        sess.send('B', ['cmd:'], 15)
        raise RuntimeError(f"KJOHN hop failed:\n{resp}")

    # Step 4: we're on KJOHN. Look at the banner for BBS hints.
    # (No send needed — the banner arrived with Step 3's response.)
    banner_has_bbs_hint = any(k in resp.upper()
                              for k in ('BBS', 'MAILBOX', 'PBBS'))

    # Step 5: collapse the chain. One B from KJOHN cascades back.
    sess.send('B', ['cmd:'], 20)

print(f"BBS hint in KJOHN banner: {banner_has_bbs_hint}")
# For a definitive answer, run a SECOND bash call that does:
#   CONNECT JOHN  (K-Net sibling)  →  BBS  →  observe outcome  →  B
```

The key pattern: each `sess.send` is an atomic "send → wait for banner or failure → **inspect** → decide next step." No fire-and-forget, no sleep-and-hope. If a step's response doesn't contain the expected success phrase, the AI **stops**, cleans up, and reports — it does not barrel forward into the next command.

---

## K-Net / NET/ROM Node Commands (connect first: `CONNECT OAK` etc.)

**You must be in K-Net Mode to use these.** See [Operational Modes](#operational-modes--critical). After `CONNECT OAK` the prompt becomes `OAK:W6OAK-5}` and commands are interpreted by the K-Net node, not the TNC. Exit with `B` or `BYE` to return to TNC cmd:.

K-Net nodes expose a much richer command set because they actually know the network.

| Command | Purpose |
|---|---|
| `B` (BYE) | Disconnect from node |
| `C call\|alias [/S]` | Connect to any known node or user. `/S` = stay on node after remote drops. |
| `NODES` | List all destination nodes the network has advertised |
| `NODES alias` | Show the best route and path to that specific node |
| `ROUTES` | List immediate neighbor nodes (one-hop), with link quality |
| `LINKS` | Current active AX.25 links at this node |
| `MHEARD [S\|L]` | Stations heard directly on RF by the node |
| `USERS` | Who is currently connected to the node |
| `STATS` | Level 3/4 network activity statistics |
| `BBS [/S]` | Jump directly to the PBBS from the node |
| `CQ [text]` | Put yourself in CQ mode for 15 minutes |
| `INFO` | Node info text (operator-set) |
| `PORTS` | Node port info (operator-set) |
| `HELP` | Show all commands |
| `SYSOP` | Remote sysop access (password via RTEXT) |

**Routed path example (K-Net):**
```
CONNECT OAK           # connect to K-Net node
NODES BUTANO          # check that BUTANO is reachable and see the path
C BUTANO              # one command - K-Net routes through intermediate nodes
```

### Operator workflow: exploring a K-Net node

1. `CONNECT <k-net alias>` - get on the node
2. `ROUTES` - see who this node talks to directly (quality of each neighbor)
3. `NODES` - see every destination the node knows, with best-path quality
4. `NODES <alias>` - inspect the path to a specific destination
5. `MHEARD` - see who the node is hearing right now on RF
6. `C <destination>` - connect onward, or `BBS` to reach the mailbox

### Reading `ROUTES` output

Example response to `R` on BERRY:

```
BERRY:K6JAC-4} Routes:
1 K6TAM-1   192  1!
1 WA6YNG-1  196  16!
1 N6QDY-5   190  3!
1 K7WWA-8   193  13!
1 KG6POM-5  120  1!
1 W7TA-4    0    0!
```

Each column:

| Column | Meaning |
|---|---|
| 1st (port) | TNC port used to reach this neighbor. Most KPC-3s are single port, so this is almost always `1`. |
| 2nd (callsign) | Neighbor node's callsign-SSID |
| 3rd (quality) | Link quality. **>192 = exceptional**, **192 = good**, **<120 = poor**, **0 = heard but not reliably connectable**. |
| 4th (hops known) | How many additional nodes are reachable via that neighbor |
| `!` suffix | Quality is **manually locked** by the sysop (won't auto-adjust) |
| `>` prefix on a line | That route is **currently active / connected** right now |

### Reading `NODES <alias>` output (attempt order)

Example: asking DELTA how it would reach BERRY:

```
N BERRY
Routes to BERRY:K6JAC-4
>192  4 1 K6JAC-4
 145  2 1 WA6QPU-5
 144  4 1 W6DHN-2
```

Read top-to-bottom as the **attempt order**:

1. First try direct to `K6JAC-4` (currently connected, quality 192).
2. If that fails, connect through `TRACY:WA6QPU-5`, then ask TRACY to connect BERRY.
3. If that fails, try via `GTN:W6DHN-2`.

Same logic for any destination. The `>` marks the path that is currently live.

### Why a node is (or isn't) in `NODES`

A K-Net node's routing table is not just "everything I've ever heard." Entries are gated by three parameters and can age out over time. This matters because a station you just heard on the air may not show up in `NODES` for a while, and conversely, a node that seems to have vanished may still be in the list with a decaying quality score.

| Parameter | Default | What it does |
|---|---|---|
| `MINQUAL` | 10 | Minimum link quality a neighbor must reach before it's added to `NODES` at all. Raise this to keep marginal paths out. |
| `OBSINIT` | 6 | Starting observation counter when a node is first learned. Gets decremented over time if the node isn't re-heard. |
| `OBSMIN` | 3 | Floor for the observation counter. When a node's counter drops below this, it's removed from `NODES`. |

Two practical consequences:

1. **Just heard a node but it's not in `NODES`?** Its measured quality is below `MINQUAL`, or the node-map exchange hasn't happened yet. Give it a few minutes, or try to `CONNECT` directly to confirm it's reachable before relying on it as a hop.
2. **Node was there yesterday and now it's gone?** Its observation counter aged out below `OBSMIN`. The path may still work, just no longer advertised. You can still try `CONNECT <alias>` explicitly or chain through a KaNode.

Check current values with `MINQUAL`, `OBSINIT`, `OBSMIN` at the `cmd:` prompt. These live on the TNC itself (K-Net side) and are set by the sysop.

### L4 stall playbook — K-Net `C <far>` silently hangs

The most common K-Net failure isn't a hard error, it's silence. You send `C BUTANO` from `OAK:W6OAK-5}` and nothing comes back for 30+ seconds — no banner, no `FAILURE`, nothing. This is a **NET/ROM Layer 4 circuit setup failure**: your local node asked a neighbor to build a virtual circuit to the destination, and the neighbor never answered.

**Diagnose before retrying.** From inside the K-Net node that's stalling:

| Command | What you're looking for |
|---|---|
| `LINKS` | Is there a partial session to the neighbor? A line in `LINK SETUP` state means the neighbor hasn't acknowledged yet. |
| `STATS` | Compare `L4 Connects: X sent, Y rcvd`. If sent > rcvd by a large margin, L4 circuits are being initiated but never completing from this node. |
| `NODES <far>` | Does the destination still exist in the table? Quality low / obs low = route is ageing out. |
| `ROUTES` | Quality of the neighbor the route would use. `<120` = unreliable. |

**Common causes, ranked by how often we see them:**

1. **Stale route** — `NODES` still advertises a path through a neighbor that's no longer hearing the far node. Route will age out on its own, or sysop reboots will clear it. Pick a different K-Net gateway if your first choice is consistently stalling.
2. **Intermediate node overloaded** — the relay node is at its connection cap or its uplink is busy. Retry in a few minutes.
3. **Frequency crossing mismatch** — some K-Net nodes bridge 145.05 and another band, and the cross-band link may be down even though the 145.05 side looks healthy. `INFO` at the suspected node sometimes reveals this.

**Recovery:**

```
(silent for 30+ s after C BUTANO)
LINKS                          ← check for stuck LINK SETUP
STATS                          ← confirm L4 sent > rcvd
B                              ← leave the K-Net node
# back at cmd:
DISCONNE                       ← drop any half-open stream
# try a different gateway, or retry later
```

**Bot rule of thumb:** if `C <alias>` from a K-Net node has produced no response for 25 seconds, treat it as failed. Run `LINKS`, capture the output for the operator, send `B`, then `DISCONNE` at `cmd:`. Don't escalate blindly — pick a different K-Net entry point (see NODE_PATHS.md's Path Cookbook) or wait 10+ minutes.

### Key regional nodes reachable from W6OAK

**145.05 MHz (mix of KA-Node + K-Net):**
- K-Net: `OAK:W6OAK-5`, `BUTANO:W6SCF-4`, `BERRY:WB6YNM-5`, `LPRC3:N6ACK-4`
- KA-Node: `KOAK:W6OAK`, `KBERR:WB6YNM-4`, `KLPRC3:N6ACK`, `KRDG:N6RZR-4`, `KPAC:WA6TOW-5`

**144.91 MHz (mostly KA-Node):**
- `BRKND:KJ6WEG`, `MARSND:KB6HOH-11` (Winlink RMS), `SONND:K6ACS`, `TRFND:N6TAM`

**145.63 MHz:** `OAK:W6OAK-5`, `BLKMTN:W6SCF-6`, `LGATOS:AG6WR-5`, `SFRCND:W6REM`

Naming convention on 145.05: K-Net nodes use a location name (e.g. `BUTANO`), KA-Nodes use `K` + first 4 letters of the K-Net version (e.g. `KBUTA`). Mailboxes use first letter + `BOX` (e.g. `BBOX`).

---

## Unproto Operation (Unconnected Communication)

**Unproto** means sending an AX.25 UI (unnumbered information) frame that is not part of a connected session. Anyone within range who is monitoring sees it. This is how the **Sunday Night Packet Net** runs, and it's the right tool any time you want a group QSO rather than a point-to-point chat.

### Connected vs Unproto — one-line summary

- **Connected** (`CONNECT call`): private conversation with one station. Only that station's packets show in your connect window. Others can't join. (MCON setting determines whether you can still see monitored traffic in another pane.)
- **Unproto** (`UNPROTO dest VIA …` at `cmd:`, then CONVERS to send): configure destination + digipeater path once, then every line you type in CONVERS mode is broadcast as a UI frame through that path.

### UNPROTO is a configuration command, not a send command

This is the single most common source of confusion. The Kantronics manual defines the command as:

```
UNPROTO {call1 [VIA call2,call3..call9] | NONE}      default CQ
```

It **sets the destination and digipeater path** used for unconnected (unproto) transmissions, BEACON, and ID packets. It does **not** transmit anything by itself.

The two-step flow is:

1. At `cmd:` — set destination and path:
   ```
   UNPROTO AL V KJOHN,KBERR,WOODY,KLIVE
   ```
   Here `AL` is a destination callsign (in this case, a friend's call — any 6-char AX.25 address works, including `CQ`, a person's call, or an object ID). The VIA list is the KaNode digipeater chain.

2. Enter CONVERS mode and type:
   ```
   CONVERS
   Test
   ```
   Every line becomes one UI frame addressed to `AL` and repeated through the VIA list. Exit with `<Ctrl+C>`.

If you see `U Al V KJOHN,...` in logs or old notes and interpreted `Al` as the message content, that's the trap — `Al` is the destination, `Test` (typed later in CONVERS) is the payload.

### KaNodes digipeat. K-Net nodes don't. Why?

- **KaNodes** are pure AX.25 layer-2 devices. They see a UI frame with their alias in the VIA list and blindly repeat it on the same channel. That's digipeating. Works for both connected frames and unproto/UI frames.
- **K-Net nodes** run the **NET/ROM** protocol on top of AX.25 — a layer-3 network with its own routing table (`NODES`/`ROUTES`). K-Net doesn't expose a raw digipeat service to AX.25 traffic at all. It forwards only the traffic inside its own connected NET/ROM sessions, based on its own routing, across potentially multiple frequencies. A UI frame with a K-Net alias in the VIA list is simply ignored.

Practical consequence: the VIA list for an unproto chain **must** contain KaNode aliases (e.g. `KJOHN`, `KBERR`, `WOODY`, `KLIVE`), never K-Net aliases (`JOHN`, `BERRY`, `OAK`). On 145.05 MHz many sites run both — a K-Net node at `BERRY:WB6YNM-5` and a KaNode at `KBERR:WB6YNM-4`. Pick the K-prefixed one for unproto.

### Building a GOOD chain

Put the **strongest KaNode your station hears first**, then list the rest in the order they hear each other. Each hop must be able to hear the hop before it, or the chain breaks silently.

**Good example from Bethel Island (destination `AL`, KaNode chain):**
```
U AL V KJOHN,KBERR,WOODY,KLIVE
```
Reaches from Modesto to Sacramento. Then `CONVERS` and type content.

**Bad example (same area):**
```
U AL V KJOHN,KCORN,WOODY,KBERR
```
`KJOHN` repeats fine, but `KCORN` can't hear `KJOHN`, so the chain breaks there. `WOODY` and `KBERR` never see the frame no matter how well they hear `KJOHN`.

### Reading Unproto traces (the asterisk)

When a frame traverses the chain, you'll see multiple copies on the air, one per successful hop. The `*` after a call/alias marks **which digipeater your station actually heard repeat the frame**.

Example — the word `Test` sent Unproto via four KaNodes, all four repeated it:

```
WB6YNM>AL,KJOHN,KBERR,WOODY,KLIVE: <UI>:{F0} Test
WB6YNM>AL,KJOHN*,KBERR,WOODY,KLIVE: <UI>:{F0} Test
WB6YNM>AL,KJOHN,KBERR*,WOODY,KLIVE: <UI>:{F0} Test
WB6YNM>AL,KJOHN,KBERR,WOODY*,KLIVE: <UI>:{F0} Test
WB6YNM>AL,KJOHN,KBERR,WOODY,KLIVE*: <UI>:{F0} Test
```

Example — the word `testing`, broken chain (only two hops made it back to us):

```
WB6YNM>AL,KJOHN,KCORN,WOODY,KBERR: <UI>:{F0} testing
WB6YNM>AL,KJOHN*,WOODY,KBERR: <UI>:{F0} testing
WB6YNM>AL,KJOHN,WOODY,KBERR*: <UI>:{F0} testing
```

Here you see `KJOHN` repeated, and you see `KBERR` repeated. You did **not** personally hear `WOODY`'s repeat, but it must have happened, because `KBERR` only got the frame from `WOODY`. The absence of a `KCORN*` line matches the bad-chain analysis — `KCORN` never heard `KJOHN` so it dropped out.

### Rule-of-thumb summary for Unproto

- `UNPROTO dest V digi1,digi2,...` at `cmd:` **configures** — it doesn't send. Content goes out only once you enter CONVERS mode and type.
- Use **KaNode** aliases in the VIA list, never K-Net aliases. K-Net nodes don't digipeat (NET/ROM is layer 3, doesn't expose raw AX.25 digipeat).
- Order matters: strongest KaNode you hear goes first, then the order the rest can hear each other.
- `*` after an alias in a monitored frame = that hop's repeat was heard by **you**.
- Missing `*` doesn't always mean failure — intermediate hops might still relay onward out of your RF range.
- Check or change current setting with bare `UNPROTO` at `cmd:`. `UNPROTO NONE` disables unproto TX (BEACON and ID still go out).

---

## PuTTY Live Monitoring (for user)

Configure PuTTY to watch all traffic in real time:
1. Open PuTTY → Connection type: **Raw**
2. Host: `localhost` (or `127.0.0.1`)
3. Port: `8765`
4. Terminal → set Local echo: **Off**, Local line editing: **Off**
5. Save session as "KPC3 Monitor"

PuTTY will show everything Claude sends AND everything the TNC receives — beacons, IDs, connects, and all monitored traffic from other stations.

---

## Operating the TNC manually from the Mac

You don't need to stop the bridge to drive the TNC yourself. The bridge already fans out TCP port 8765 to multiple simultaneous clients. Just connect to it from the Mac and start typing. The bot can even be running at the same time (though the frequency gets confusing fast, so stop the bot first if you plan to send much).

### Option A: `kpc3_console.py` (recommended)

A small Python console lives in the repo. Handles the KPC-3+'s `\r`-only line ending, runs a background reader so you see TNC output in real time while you type, and optionally logs the session.

```bash
cd "~/Desktop/Kantronics KPC3+ Claude Skill"
python3 kpc3_console.py
```

Or with a session log:

```bash
python3 kpc3_console.py --log ~/packet-session-$(date +%Y%m%d).log
```

Type `STATUS`, `MHEARD`, `C WOODY`, whatever you want. ENTER sends. Ctrl-C quits. No Windows box interaction needed at any point.

### Option B: `nc` (quick and dirty)

Already on your Mac. Works for read-only monitoring but not ideal for sending commands because macOS `nc` sends `\r\n` by default, which the KPC-3+ chokes on with `EH?`. Fine for listening:

```bash
nc YOUR-WINDOWS-IP 8765
```

Press Ctrl-C to exit.

### Option C: PuTTY (Windows box only)

If you're sitting at the ThinkPad, PuTTY with a Raw connection to `localhost:8765` is still a fine choice. See the "PuTTY Live Monitoring" section above.

Running PuTTY on the Mac is **not recommended**. It requires XQuartz, feels dated, and `kpc3_console.py` does the same job with better ergonomics and no install.

### What if I want truly exclusive COM port access?

Only needed if a tool must open COM11 directly (e.g. a Kantronics firmware updater, a legacy Windows packet app). In that case, see "Bridge Management" below to stop the scheduled task, do your work, and restart.

---

## Bridge Management

The bridge (`kpc3_bridge.ps1`) runs as a Windows Task Scheduler job named **KPC3Bridge** and starts automatically at login. It holds COM11 open exclusively for as long as it's running, and fans out to multiple TCP clients on port 8765.

**Log file:** `C:\Users\your-windows-username\kpc3_bridge.log`

### Starting and stopping from the Windows box

Open PowerShell (no admin required) on the ThinkPad and run:

```powershell
# See current state
Get-ScheduledTask -TaskName KPC3Bridge | Select State

# Stop the bridge (releases COM11, closes port 8765)
Stop-ScheduledTask -TaskName KPC3Bridge

# Start the bridge
Start-ScheduledTask -TaskName KPC3Bridge
```

### Starting and stopping remotely from the Mac via SSH

The same commands, wrapped in SSH. Uses the repo's SSH key.

```bash
KEY="~/Desktop/Kantronics KPC3+ Claude Skill/private/kpc3_ssh_key"

# Stop
ssh -i "$KEY" your-username@YOUR-WINDOWS-IP 'powershell -Command "Stop-ScheduledTask -TaskName KPC3Bridge"'

# Start
ssh -i "$KEY" your-username@YOUR-WINDOWS-IP 'powershell -Command "Start-ScheduledTask -TaskName KPC3Bridge"'

# Status
ssh -i "$KEY" your-username@YOUR-WINDOWS-IP 'powershell -Command "Get-ScheduledTask -TaskName KPC3Bridge | Select State"'
```

If the SSH key isn't yet at `~/.ssh/kpc3_key`, the skill's session-startup helper (`restart_bridge()`) copies it into place with the right permissions. See the top of this skill for that helper.

### Desktop shortcuts on the Windows box (optional)

If you stop/start the bridge often from the Windows side, drop two shortcuts on the desktop:

**`Stop Bridge.lnk`** - target:
```
powershell.exe -Command "Stop-ScheduledTask -TaskName KPC3Bridge; pause"
```

**`Start Bridge.lnk`** - target:
```
powershell.exe -Command "Start-ScheduledTask -TaskName KPC3Bridge; pause"
```

The `pause` at the end keeps the window open so you can see the result before it closes.

### When the bridge is down

- Port 8765 stops accepting connections. The bot will log a connect failure and (by design) exit, not loop trying to reconnect.
- COM11 is released within a few seconds, so direct-COM tools can grab it.
- The TNC itself doesn't know anything changed. It keeps running on its own firmware state (beacons, DWAIT, etc. all per its NVRAM).

### When the bridge crashes mid-day

The scheduled task is set to run "at login," not "on crash." If the bridge process dies while you're logged in, it won't self-restart. Either hit Start-ScheduledTask manually or log out and back in. Future work item (tracked in BOT_DESIGN_2026 §9): auto-restart via a separate watchdog task.

---

## Reference Manual

Full KPC-3 Plus Users Guide (Rev H):
`KANTRONICS_KPC3_REV-H.md` in the skill folder.

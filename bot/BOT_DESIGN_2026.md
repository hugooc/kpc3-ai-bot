# W6OAK AI Bot — Design Document (2026)

**Status:** Proposed architecture, pending implementation
**Author:** Drafted by Claude (Opus, supervisor) at Hugo's direction
**Target:** `w6oak_ai_bot.py` v2.0
**Supersedes:** ad-hoc behavior of v1.2.0

This document is the source of truth for how the W6OAK AI bot should behave on 145.050 MHz. Code changes must map to a rule in this doc. If a situation arises that isn't covered here, the bot should err on the side of silence and we update the doc.

---

## 1. Operating principles

Five rules that frame every decision below.

1. **Listen more than speak.** Packet radio is a shared medium. Silence is the default posture. The bot speaks only when a rule in this doc explicitly says it should.
2. **Connected-only engagement.** The bot engages with humans through AX.25 connected sessions. UNPROTO (UI) frames are logged and ignored for reply purposes, full stop.
3. **One conversation among many.** At any moment, several QSOs may be running on 145.05. The bot is not the center of the frequency. It responds to stations that have connected to *it*, nothing else.
4. **The bot is deaf to RF carrier.** It cannot hear whether someone else is transmitting on air. It can only see frames the TNC hands it. It must therefore rely on timing heuristics and TNC parameters (like `DWAIT`) to avoid stepping on ongoing traffic.
5. **Supervisor authority is absolute.** The human control operator can silence or pause the bot at any moment via a lockout mechanism. The bot checks this before every transmission.

---

## 2. What the bot responds to

**Responds to:**

- Text received inside an active AX.25 connected session where the remote station initiated the connect to W6OAK.

**Does NOT respond to:**

- UNPROTO UI frames, regardless of destination (CQ, BEACON, MAIL, anything).
- Frames where the bot itself is in the digi path (`W6OAK*` in VIA list).
- Frames whose source callsign matches `MYCALL` (self-echo).
- Frames received while a supervisor lockout flag is active.
- Frames received before the session has reached `CONNECTED` state.
- Anything that looks like a NET/ROM L3 frame, BBS forwarding traffic, or non-text PID.

UI frames are still **logged** (both raw and parsed) because they inform route planning and situational awareness. They are never a reply trigger.

---

## 3. Turn-taking rules

Packet text doesn't have a natural "done speaking" signal the way a voice QSO does. At 1200 baud simplex through multi-hop chains, a single human message may arrive as several I-frames separated by seconds.

**End-of-turn heuristic:** the bot considers a remote turn complete when **no new I-frame has arrived for `LISTEN_WINDOW` seconds** (default: **8 seconds**; tunable per session).

**Continuation rule:** if additional I-frames arrive during the listen window, they are concatenated into the current turn and the timer resets. The bot never starts formulating a reply until the window closes without new traffic.

**No double-reply:** once the bot transmits a reply, it does not transmit again until new traffic arrives from the remote. Continuations within the bot's own reply are merged into a single transmission before send.

**Max reply length:** 120 characters per reply, hard limit. One reply = one AX.25 frame where possible. Haiku must be prompted to stay under this.

**No interrupting silence:** the bot never sends an unsolicited message during an open session. If the remote goes quiet, the bot stays quiet. Idle timeout (5 minutes, existing behavior) handles session close.

---

## 4. Self-protection

Redundant safety layers. Each exists because a different failure mode has already happened or is plausible.

### 4.1 Rate limit per session

Minimum **20 seconds** between transmissions from the bot within a single session. If Haiku produces a reply faster than that, the bot queues it and waits. If the remote keeps sending during the wait, normal turn-taking resumes.

### 4.2 Max replies per session

Hard cap: **8 replies per session**. After the eighth reply, the bot sends a final short message ("73 — hitting my per-QSO limit. C W6OAK again anytime. de W6OAK") and closes the connection. This prevents runaway conversations and containerizes cost per QSO.

### 4.3 Dedup against recent TX

The bot keeps a ring buffer of its last **5 transmissions**. Before sending any new reply, it fuzzy-matches (normalized Levenshtein or simple token overlap) against the buffer. If similarity exceeds **0.85**, it does not send. This catches cases where Haiku generates a near-duplicate of something just transmitted, and protects against echo-induced repetition loops.

### 4.4 Emergency stop

For v2.0, the emergency stop is **Ctrl-C in the terminal where the bot is running.** Kills the process cleanly. Simple, fast, no ambiguity. The remote station sees a disconnect, the bot is gone, you diagnose and restart when ready.

A more elaborate "lockout flag" mechanism (file-based silence without process kill) was considered and deferred. See §9 for when it comes back.

### 4.5 Source-callsign whitelist (optional, off by default)

Config key: `allowed_callers`. If present and non-empty, the bot only opens sessions with listed callsigns. Intended for testing windows where we don't want surprise human QSOs. Default: empty (accept all).

---

## 5. Beacon policy

The bot's identity beacon is for passive discovery, not conversation.

- **BTEXT length:** under **40 characters** for multi-hop UNPROTO. Rationale: each digi hop retransmits the full frame; a long BTEXT floods the network and invites echo-driven congestion.
- **Interval:** `BEACON EVERY 60` (60 minutes, as of 2026-04-21). One per hour is enough to make the bot discoverable without being a nuisance; was previously 20 min but that felt noisy on multi-hop paths per KI6ZHD feedback.
- **Content requirement:** must announce "AI" or "bot" or equivalent so passing ops know what they'd be connecting to. FCC Part 97 identification is separate and satisfied by `MYCALL`.
- **Suspend during maintenance:** when the bot process is stopped (Ctrl-C), the Python side transmits nothing. The TNC's autonomous beacon per `BEACON EVERY` still runs at the TNC level unless separately disabled there.
- **Current BTEXT:** `W6OAK AI node CM87. C W6OAK to chat. 73!` (40 chars). This replaces the longer "Ask about routes" variant, which was fine for local reach but chatty on multi-hop paths.

---

## 6. Logging

Today the bot writes a single log that mixes what the TNC said with what the bot decided. Post-mortems are painful because the two streams are interleaved and sometimes the bot's interpretation obscures the RF reality.

**New layout:**

- `private/logs/w6oak_rf.log` — verbatim TNC monitor output, timestamped, one line per received byte-stream chunk. No interpretation. Raw truth.
- `private/logs/w6oak_bot.log` — bot decisions only. Connect detected, session opened, Haiku prompted, reply queued, rate limit hit, session closed. Each line references a correlation ID so you can cross-link to the RF log.
- `private/logs/w6oak_packets.log` — **deprecate** (roll content into `w6oak_rf.log`). Keep the name as a compatibility symlink for one release.

**Rotation:** daily, keep 30 days. Bot handles rotation itself (no logrotate dependency on the Windows box).

**Correlation ID format:** `YYYYMMDD-HHMMSS-<random4>` per session. Printed in every bot-log line for that session and embedded in the RF log header when a session opens.

### Bot-log line vocabulary

What each log line means and what to grep for when doing forensics. All lines are prefixed with `YYYY-MM-DD HH:MM:SS,mmm  LEVEL  ` — these descriptions cover the message portion.

| Line | Meaning | Useful for |
|---|---|---|
| `heartbeat v<ver>: <N> pkts heard, <M> sessions, listening` | Liveness tick, one per minute. Confirms bot is alive and shows cumulative RF counters. | Is the bot actually running? Did it wedge? |
| `BTEXT rotated (<n> chars): <text>` | Beacon text was rotated. | Audit of recent beacons, content drift. |
| `HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"` | Haiku API call, usually for beacon selection (not a user reply). | API cost / usage tracking. |
| `RING (BEL) detected — incoming connect expected` | TNC emitted a BEL (0x07). Usually means an inbound connect. See gotcha below. | First signal of a possible inbound. |
| `Incoming connect from <CALL>` | Inbound connect confirmed, remote callsign identified. | The real "someone connected" event. |
| `[<corrID>] Session START <-> <CALL>` | Bot opened a session for this QSO. | Session boundary marker. |
| `TX >>> <text>` | Outbound frame the bot just sent. | Reconstructing bot side of QSO. |
| `[<corrID>] RX <<< <CALL>: <text>` | Inbound frame the bot received inside a session. | Reconstructing remote side of QSO. |
| `[<corrID>] turn complete (<n> chars): "<text>"` | Listen-window closed, remote turn finalized. | Timing analysis of turn-taking. |
| `[<corrID>] self-echo: "<text>"` | Inbound frame matched recent TX and was discarded. | Verifying the self-echo filter is working. |
| `[<corrID>] Session END <-> <CALL> (<N> replies, <S>s)` | Session closed. Shows replies used and duration. | QSO-length stats. |
| `Outgoing connect to <ALIAS> — ignoring` | **We** (the operator at the console) initiated an outbound connect. Bot correctly does not treat this as a session. | Distinguishing operator activity from inbound QSOs. |
| `Bridge connected: <host:port>` | Bot's TCP client socket to the bridge just opened. | Detecting bot restarts or bridge flaps. |
| `Listening for connects (v<ver>: ...)` | Bot just entered its main loop. Pairs with a bridge-connect event. | Detecting bot restarts. |
| `TNC monitor mode active (MCON OFF, MCOM OFF, MONITOR ON, RING ON)` | Bot has configured the TNC and is ready. | Post-restart readiness check. |

**Gotcha — false RING:** a `RING (BEL)` line without a matching `Incoming connect from <CALL>` within a second or two is almost always a false trigger. BEL characters embedded in another session's text stream (e.g. a remote PBBS welcome banner printed while the operator was outbound-connected to that PBBS) can trip the detector. Cross-check `w6oak_rf.log` at the same timestamp to confirm whether a real inbound call actually arrived.

---

## 7. What the bot must never do

Negative spec. These are the specific behaviors the W6ELA incident exposed.

1. **Never reply to a UI frame.** Even if the payload looks like a direct question. Even if the destination is `W6OAK`. UI is not a conversation.
2. **Never reply to an echo.** A frame where `W6OAK*` appears in the digi path is our own TX coming back around. It is not a new message. The self-echo filter already catches local TNC echoes; the dedup ring buffer (§4.3) catches delayed RF echoes.
3. **Never reply to supervisor frames.** When the human control op or Claude Opus sends UI frames during an active session (e.g., "standing down, fix incoming"), those are for the remote human, not the bot. Rule §2 (connected-only) covers this but it's worth calling out.
4. **Never chain replies without fresh input.** One remote turn = at most one bot turn. No monologuing.
5. **Never reply mid-turn.** If three I-frames arrive in six seconds, they are one turn, not three. The listen window exists for this.
6. **Never speak during the idle close.** When the bot is closing a stale session, it sends one short 73 and disconnects. It does not attempt a farewell conversation.

---

## 8. TRACE usage policy

`TRACE ON` on the KPC-3+ produces hex dumps of every received frame with full AX.25 headers. This is extremely useful for learning, much less useful as a runtime input.

**Policy:**

- **Bot mode:** `TRACE OFF`. The bot parses MONITOR output. Hex dumps would bloat the TCP stream and expand the parsing surface for marginal gain.
- **Supervisor mode:** `TRACE ON` is encouraged during observation sessions through PuTTY. The human (or Claude Opus) uses it to verify mental models of the frequency: what PIDs are actually flowing, where the `*` falls on echoed frames, whether P/F bits can eventually serve as a deterministic end-of-turn signal.
- **Transition discipline:** when a supervisor TRACE session ends, set `TRACE OFF` before the bot resumes. Document in `w6oak_bot.log`. Conflicting TRACE state is a silent footgun.

Future: if we ever want deterministic turn-detection instead of timeout-based, the P/F bit on the last I-frame of a burst is the place to look. That's a v3 consideration, not v2.

---

## 9. Open questions

Deferred for later. Listed so we don't forget.

1. **DWAIT tuning.** The KPC-3+'s `DWAIT` parameter inserts a fixed delay before TX to reduce collisions with other digipeated traffic. Default is short. Bumping it may help the bot's carrier-deafness problem by statistically staying out of the way. Needs field testing.
2. **Deterministic end-of-turn via P/F.** See §8. Requires TRACE-aware parsing or a different TNC mode.
3. **@bot addressing tag.** Hugo raised this; we agreed it's unnecessary under connected-only. Revisit only if we relax the connected-only rule.
4. **Bridge log rotation.** The Windows-side `kpc3_bridge.log` never rotates. Cosmetic, not urgent.
5. **Multi-session support.** Today the bot handles one connected session at a time. The KPC-3+ supports multiple. Not a v2 goal — single-session with a clean queue is the target.
6. **Cost ceiling per QSO.** The max-reply cap (§4.2) is a proxy for cost control. If Haiku pricing or usage patterns change, revisit.
7. **Bot memory across sessions.** Currently stateless. A caller who connects twice gets treated as a new stranger. Intentional for v2. Worth revisiting later.
8. **Supervisor lockout flag.** A file-based mechanism to silence the bot without killing the process. Deferred for v2 because Ctrl-C covers the emergency-stop case and we don't yet have auto-restart. Revisit when the bot runs as a Windows service or scheduled task that respawns on crash, at which point a persistent silence flag becomes useful.
9. **Outbound multi-hop timing.** v2 is connected-only inbound, so timing pressure is limited to the single RF hop between the remote and us. If we ever let the bot initiate outbound connects through multi-hop chains (e.g. `C WOODY` → `C W6ELA-1`), the 8-second `LISTEN_WINDOW` is almost certainly too tight. Hand-driven sessions on 2026-04-18 through WOODY showed 3-5 seconds per ack just for the chain, before any response from the far end. A future outbound-capable mode needs a per-destination timing profile, not one global window. Not a v2 feature.
10. **BBS dialect awareness.** The bot assumes it's the only endpoint in a connected session, which is fine today because callers always reach the bot directly. If we ever flip the bot into an outbound-capable "go fetch mail" role, it will need to recognize at least PBBS and BBS2 command sets. PBBS uses `L`, `R`, `SP`, `K`. BBS2 uses two-letter menu codes like `BU`, `C`, `I`, `LC`, `A`. See `SKILL.md` "BBS variants" section.
11. **RING (BEL) detector false positives.** The current detector logs `RING (BEL) detected — incoming connect expected` on any BEL character in the monitor stream. On 2026-04-18 at 20:55:46, a RING fired during an existing outbound session to MONTC because the remote node returned `Eh?` (which includes a BEL) after an unrecognized `mh` command. No harm done, the bot correctly stayed out since v2's connected-only gate only engages on inbound connects, but the log line is misleading during post-mortems. Tighten the detector to only trigger when the TNC is in listening state with no active outbound stream, or gate the log message on session state. Low priority, cosmetic.

---

## 10. Implementation checklist

When we patch `w6oak_ai_bot.py` against this doc, the changes map to:

- [ ] Connected-only gate (reject all non-CONNECTED state TX)
- [ ] Listen window with concatenation (§3)
- [ ] Rate limit timer per session (§4.1)
- [ ] Reply counter with graceful close (§4.2)
- [ ] Dedup ring buffer with fuzzy match (§4.3)
- [ ] Clean Ctrl-C handling: close active session with a short 73, then exit (§4.4)
- [ ] Optional whitelist (§4.5)
- [ ] Short BTEXT + multi-hop awareness (§5)
- [ ] Split logs + correlation IDs (§6)
- [ ] Soak test harness covering §7 rules
- [ ] Version bump to 2.0.0 and changelog entry

Each checkbox becomes a testable behavior. The soak test harness is how we prove the bot follows the rules before it goes back on the air with strangers.

---

## 11. References

- `SKILL.md` — TNC operating reference
- `STATE.md` — current architecture, versions, paths, and which machine runs what. The "what's true right now" doc. This design doc is the "why we built it this way" doc.
- `NODE_PATHS.md` — network topology for route planning
- `NET_CONTROL_2026.md` — Sunday net operator playbook
- `KANTRONICS_KPC3_REV-H.md` — authoritative KPC-3+ command reference
- `w6oak_ai_bot.py` — the code this doc governs
- `private/DEPLOYMENT_INVENTORY.md` — live snapshot of what's installed on the Windows host (paths, scripts, logs, scheduled tasks). Not in version control. Kept current by the operator.
- W6ELA incident log, 2026-04-17 — the field experience that motivated most of §7

---

## 12. Since v2.0 — what changed and why

This section tracks where the live bot has drifted from the original v2.0 spec above. Each entry is a short note, not a full redesign. For current state (file paths, what runs where, bot version), see `STATE.md`.

### v2.3.0 — Emergency Ops mode (2026-04-19 morning)

Added an escort flow for non-ham government or served-agency callers during drills or declared emergencies. The bot loads `EMERGENCY_CONTACTS.md` at boot, injects it into the system prompt as an `<emergency_directory>` block, and flips into a drill-by-default escort mode when the caller's message matches an emergency keyword or an agency alias.

Key rules of the escort flow:

- First reply on mode entry announces "DRILL MODE" and asks the caller to confirm drill vs real before any slots get collected.
- Real mode always reminds the caller once that W6OAK is a volunteer relay, not 911.
- Templates cover supplies, welfare, sitrep, medical, and evacuation.
- Slots are filled one per turn, user input is preserved verbatim, the bot never auto-transmits on the caller's behalf.

Why: the station is reachable by county EOCs and served agencies during an activation. The bot needed a structured, safe way to compose a message and route it, without ever implying that the bot itself was dispatching help.

### v2.4.0 — TX sanitize + topology handling (2026-04-19 afternoon)

Two fixes, both traced to the W6ELA-15 QSO incident earlier that day.

**TX sanitizer.** AX.25 is 7-bit ASCII in practice. When Claude generated replies containing em-dashes, curly quotes, ellipsis chars, or backticks, those bytes either became `?` on encode or showed up as garbled multi-byte UTF-8 on the receiving op's screen. Added `sanitize_tx()` as a single chokepoint at `TNCSession.send()`: every string bound for the TNC gets substituted to safe ASCII before encoding. Em-dashes become ` - `, curly quotes become straight quotes, ellipsis becomes `...`, backticks become single quotes. Idempotent, preserves `\r` and `\n`.

**Topology request handling.** A caller asked for an ASCII map of the node network. The bot tried to draw one, which blew the 120-char cap and forked into multiple corrupted turns. Added a rule to the system prompt: "map", "tree", "topology", "diagram", "ascii art", or "picture" requests get answered with a compact one-line neighbor list, never a visual diagram. If the caller wants more structure, the bot offers to walk one branch at a time.

**Defense in depth for BTEXT.** `beacon_manager._sanitize()` already stripped smart quotes at Haiku fetch time. Updated it to also strip backticks and the ellipsis char, matching the new `sanitize_tx()`. Cleaned every backtick out of `BTEXT_POOL.md` and added a "no backticks" rule to the file's own format guide. Two layers of scrubbing: one at source, one at the socket. Even if a future pool entry or Haiku generation slips in a bad character, `sanitize_tx()` catches it before it hits the wire.

Why: the W6ELA-15 QSO was rated "B+" by the operator. Em-dashes showing as `?"` on Ed's screen and the attempted ASCII tree were the two most visible UX regressions. Both now fixed at the root.

### Operational drift notes

- Current COM port is COM11, not COM17 as older docs say. Source of truth: `STATE.md`.
- The bot runs on the Windows host (192.168.1.100), not on the Mac. The Mac project folder is authoring and version control only.
- Bot logs live at `C:\Users\youruser\w6oak_bot\private\logs\` on Windows. The Mac `private/logs/` folder was removed during the 2026-04-19 cleanup pass.

---

*de W6OAK*

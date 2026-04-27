# Net Control Playbook — 145.050 MHz Sunday Packet Net

**Source:** Distilled from the 2021 NC notes used by W6OAK, plus 2026 captures in `NODE_PATHS.md`. Techniques come from Hugo's original net-control document; nodes are updated to what's actually on the air now.

**Station of reference:** W6OAK, Oakland CA (CM87)
**Net time:** Sunday 2000 hrs local, 145.050 MHz
**Format:** Unproto UI frames through a KaNode digipeater chain. Stations check in by sending their own unproto packet with name + location. Net Control logs each checkin and sends a BTEXT acknowledging who they heard.

This file is a **recipe book**, not a reference manual. The full Unproto theory lives in `SKILL.md` section "Unproto / UI-frame operation". The node inventory lives in `NODE_PATHS.md`. Read those first if anything here is unfamiliar.

---

## Pre-net checklist (Sunday morning)

Run these at `cmd:` on the TNC before the net. They configure the station and stage the first BTEXT.

```
MALL OFF
MYCALL W6OAK
UNPROTO CQ VIA WOODY,KBERR,KJOHN,KBETH,KBERR,KLPRC3
BTEXT Sunday Packet Net 8:00pm NC Hugo, W6OAK hears WOODY and KLPRC3
BEACON EVERY 60
```

What each line does:

- `MALL OFF` — show only **unconnected** packets in the monitor stream. Keeps the terminal readable during a busy check-in round.
- `MYCALL W6OAK` — sanity check, rarely changes.
- `UNPROTO ...` — sets destination + digi chain for all UI/beacon/ID frames. See "The echo-test path" below for why the chain loops back on itself.
- `BTEXT ...` — the beacon content. Update between rounds as you log check-ins.
- `BEACON EVERY 60` — beacon every 60 minutes (steady-state default since 2026-04-21). Fine for a pre-net beacon. Turn this OFF (`BEACON EVERY 0`) once the net starts so your beacon doesn't step on check-ins.

To disable unproto/beacon entirely between nets: `UNPROTO NONE`, `BEACON EVERY 0`.

---

## The echo-test path — "did my frame make it all the way?"

The trick: repeat a digi alias inside the UNPROTO VIA list so the frame has to traverse the chain to the end and come back. If you hear the final hop on your own radio, the whole chain is alive.

**2021 version (historical, most of these nodes still exist):**

```
UNPROTO HUGO VIA KLPRC3,KBERR,KJOHN,KBETH,KBERR,KLPRC3
```

Interpret the chain left-to-right. The frame goes: out to `KLPRC3`, up to `KBERR`, out to `KJOHN`, up to `KBETH`, back to `KBERR`, back to `KLPRC3`. If you hear the second `KLPRC3*` come back on the air, the round trip worked.

**2026 adapted version using what OAK can actually hear tonight:**

```
UNPROTO TEST VIA N6ZX-5,KBERR,N6ZX-5
```

Simpler three-hop echo through WBAY and KBERR. Hearing the second `N6ZX-5*` means the frame reached KBERR and came back. If you want more reach to confirm the NorCal corridor is up, extend:

```
UNPROTO TEST VIA N6ZX-5,KBERR,KJOHN,KBETH,KBERR,N6ZX-5
```

**Caveats:**

1. Works only with **KaNode** digis (see SKILL.md). K-Net / NET/ROM nodes do not repeat UI frames and will silently drop them. `N6ZX-5` (WBAY) is K-Net, so for a true UI echo substitute its KaNode sibling `WOODY` when that node is healthy. WOODY has been flaky in 2026 per NODE_PATHS.md, hence using N6ZX-5 above — worth testing both on any given night.
2. A repeated alias in the chain is non-standard and some firmware may squash duplicates. If the echo doesn't come back, try separating: `VIA WOODY,KBERR,KJOHN,KBETH,KLPRC3,WOODY`.
3. UI frames have no retries. One missed digi hop and the whole echo is lost. Try twice before concluding the chain is down.

---

## North / South regional paths (for roll-call or bulletins)

From the 2021 notes, still the general shape of the network. Cross-check individual node health in `NODE_PATHS.md` before each net.

**North (toward Oregon border):**

```
UNPROTO CQ VIA KLPRC3,KBERR,KRDG,HMKR,GPASS
```

- `HAMAKR` in the 2021 doc is now `HMKR`.
- `GPASS` (Grants Pass, OR) not confirmed in 2026 captures; treat as aspirational until someone answers.
- For a NET/ROM alternative that actually works right now: use a **connected** session through `WBAY → BANNER → RDG → HMKRCH`. Not unproto, but reaches the border.

**South (toward SoCal):**

```
UNPROTO CQ VIA KLPRC3,KBERR,KBULN,BRKNRG,BBEAR
```

- `KBULN` is K6IXA-5's KaNode flavor, confirmed active.
- `BRKNRG` is WB6YNM's Berryessa site (distinct from BERRY/KBERR).
- `BBEAR` (Big Bear, SoCal) not seen in any 2026 capture; legacy — may or may not work.

**Short local (Bay Area + Central Valley, reliable in 2026):**

```
UNPROTO CQ VIA N6ZX-5,K6FB-5
```

Reaches the Peninsula (via WBAY) and over to Castle Rock / Santa Cruz Mountains (via ROCK). This is the path we're currently using for the W6OAK AI bot beacon. Adequate for a local roll call.

---

## Running the net — command flow

### 1. At start of net (2000 hrs)

Turn off the periodic beacon so your BTEXT pulses don't clobber check-ins:

```
BEACON EVERY 0
```

Set an opening BTEXT and fire it manually (any change to BTEXT queues a transmit on the next beacon, but we'll send by hand):

```
BTEXT QST QST QST Sunday Night Packet Net. This is NC Hugo W6OAK.
CONVERS
(type the net intro, one line per UI frame, Ctrl+C to exit)
QST QST QST Sunday Night Packet Net. This is Hugo W6OAK NC for this evening.
Net meets Sundays at 8:00pm local. Check in with name + location via unproto.
New stations welcome. All stations, please check in.
```

Ctrl+C returns to `cmd:`.

### 2. As check-ins come in

Each remote station sends their own unproto UI frame. You'll see lines like:

```
K6WLS>CQ,KBERR*: Ken in Woodland
```

Log the callsign, name, location, and the **first digi with `*`** (that's who they can hit directly). Keep a live roster file going.

Acknowledge with a BTEXT update:

```
BTEXT Sunday Packet Net 8:00pm NC Ken, K6WLS hears KBERR
CONVERS
Ken, K6WLS hears KBERR -- welcome.
(Ctrl+C)
```

Repeat for each check-in. BTEXT persists, so any station who tunes in late and monitors your beacon immediately sees the most recent acknowledgment.

### 3. Closing the net

```
CONVERS
That's the close of tonight's Sunday Packet Net. Thanks to all check-ins.
Next net same time next Sunday. 73 de W6OAK.
(Ctrl+C)
BEACON EVERY 60
UNPROTO CQ VIA N6ZX-5,K6FB-5
BTEXT W6OAK AI node CM87. C W6OAK to chat w/ the bot. Ask about routes. 73!
```

That restores the station to its everyday AI-bot beacon config.

---

## Operational tips carried over from 2021

1. **`MALL OFF` before every net.** Without it, connected-session traffic from other pairs on 145.05 clutters the monitor pane and makes it easy to miss a check-in.

2. **Keep a running roster file.** The 2021 notes tracked callsign, name, location, and "Node Heard" — that last column is the operationally useful one. Knowing a station hears `KBERR` tells you which digi to loop into the chain if you want to relay back to them.

3. **KaNode aliases only in VIA lists.** `JOHN` (K-Net) does nothing for UI frames. `KJOHN` (KaNode) digipeats them. Same site, different flavors. Many 145.05 operators conflate these — on unproto, the K-prefixed name always wins.

4. **Beacon interval during an active net = 0.** Automatic beacons while the net is in progress step on check-ins. Re-enable only after closing.

5. **If a chain looks dead, try the shorter chain.** A 6-hop chain has many ways to fail. Cut it in half to isolate which hop is broken, then rebuild.

6. **`:undest` from the 2021 notes is NOT a KPC-3+ command.** It looks like a filter directive from a layered app (Outpost, BPQ32, or similar) that was running alongside the TNC at the time. Current AI-bot setup doesn't use it. Ignore unless we reintroduce that software stack.

7. **`HAMAKR` became `HMKR`.** Same site. Current manual chain to Medford is `KHILL → KJOHN → KBANN → KRDG → HMKR → KC7HEX-1` per NODE_PATHS.md. On K-Net the equivalent is `HMKRCH:W7VW-6`.

8. **`GPASS` and `BBEAR` in the 2021 paths are unverified in 2026.** Test before advertising a net that depends on them.

---

## Quick reference — nodes mentioned in 2021 NC notes, 2026 status

| 2021 Alias | 2026 Status | Notes |
|---|---|---|
| WOODY | Intermittent (N6ZX) | TX issues reported 2026-04-15 per groups.io msg 1151 |
| KBERR | Active | KaNode flavor of BERRY:WB6YNM-5 |
| KJOHN | Active | KaNode flavor of JOHN:KF6ANX-4 |
| KBETH | Unclear | Not explicitly confirmed in 2026 captures; BETHEL:WB6YNM-3 is active as K-Net |
| KLPRC3 | Active | KaNode flavor of LPRC3:N6ACK-4 |
| KBULN | Active | KaNode flavor of BULN:K6IXA-5 |
| KBANN | Active | Critical NorCal→OR bridge (WBAY hears it directly) |
| KRDG | Active | Redding KaNode, sibling of RDG:KE6CHO-5 |
| KHILL | Active | Sibling of HILL:KF6ANX-5 |
| KLIVE | Unverified in 2026 | — |
| HAMAKR | Renamed to HMKR | Same site; reverse link intermittent per msg 1159 |
| GPASS | Unverified | Grants Pass OR — legacy 2021 entry |
| ROSE | Stale (BANNER no longer advertises it) | WBAY still lists it, but forwarding is broken |
| TAHOE_NODE | Digi-only, back since 2024-12-04 | — |
| BBEAR | Unverified | Big Bear SoCal — legacy 2021 entry |

---

## References

- `SKILL.md` — full TNC operating reference (Unproto theory in the "Unproto / UI-frame operation" section)
- `NODE_PATHS.md` — live node inventory, degraded edges, path cookbook, OAK/WBAY/BANNER captures
- [groups.io/g/145050PacketNetwork](https://groups.io/g/145050PacketNetwork) — current 2026 operator thread
- KPC-3+ User's Guide Rev H (`KANTRONICS_KPC3_REV-H.pdf`) — authoritative command reference
- Original 2021 NC notes — [Google Doc](https://docs.google.com/document/d/16tvpaO1fH0T8UELt6_710VMxmuiK0Zri1kSE3LjJDWY/edit?usp=sharing)

---

*73 de W6OAK*

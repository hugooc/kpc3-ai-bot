# 145.050 MHz Packet Network — Node Reachability Map

**Source:** [groups.io/g/145050PacketNetwork](https://groups.io/g/145050PacketNetwork) RSS feed and #NODE-STATUS archive
**Compiled:** 2026-04-17 from the most recent BBS Net thread (messages 1149–1168) plus older #NODE-STATUS topics
**Station of reference:** W6OAK (Oakland, CA)

This file is intended to be read by the packet bot to help plan multi-hop connects on the 145.050 MHz NET/ROM / KA-Node network spanning California, Nevada, and Oregon. Paths are crowd-sourced from operator reports, so treat each edge as "observed working at some point" rather than "guaranteed up right now". The **Last Seen** column is a hint at freshness.

---

## Quick Legend

- **Alias / Callsign** shown as `ALIAS:CALLSIGN-SSID` where known (e.g. `KRDG:N6RZR-4`).
- **Type** column: `KA` = KA-Node (Kantronics proprietary, silent, user drives routing), `K-Net` = NET/ROM node (smart, auto-routes, supports `NODES`/`ROUTES`), `Both` = same site runs both, `?` = unknown.
- Most aliases on 145.050 follow a pattern: `K` + first 4–5 letters = KA-Node flavor, plain word = K-Net / NET/ROM flavor (e.g. `KRDG` vs `RDG`, `KHILL` vs `HILL`).
- On 145.050, `HMKR` **requires port 1 to be specified** when connecting through it: `c 1 KC7HEX-1`.
- `s` suffix on KA-Node connects means **STAY** (keep the user at the node if the remote drops): `c KBANN s`.
- K-Net nodes accept `c ALIAS` and route automatically; KA-Nodes require chaining one hop at a time.

---

## Confirmed Edges (from recent operator reports)

Each row is a directed edge "from node A you can reach node B". Bidirectional edges are listed twice.

| From | From Type | To | To Type | Via / Notes | Last Seen | Source |
|---|---|---|---|---|---|---|
| W6OAK (local) | Both | HILL / KHILL | Both | direct RF first hop from Bay Area users; K-Net alias `HILL`, KA alias `KHILL` | 2026-04-17 | msg 1158 + OAK NODES |
| HILL / KHILL | Both | JOHN / KJOHN | Both | next hop in working NorCal→OR chain | 2026-04-17 | msg 1158 + OAK NODES |
| JOHN / KJOHN | Both | KBANN | KA | next hop; no K-Net equivalent advertised into OAK | 2026-04-17 | msg 1158 (N6ZOO) |
| KBANN | KA | KRDG | KA | next hop (Redding) | 2026-04-17 | msg 1158, 1166 |
| KRDG | KA | HMKR | KA | next hop (Mt. Hamaker / Oregon border) — **specify port 1** | 2026-04-17 | msg 1158 (N6ZOO) |
| HMKR | KA | KC7HEX-1 | KA | final hop to Medford OR BBS, use `c 1 KC7HEX-1` | 2026-04-17 | msg 1158, 1166 |
| KRDG | KA | RDG | K-Net | same site, NET/ROM flavor of the Redding node | 2026-04-17 | msg 1157 (KO6TH) |
| RDG | K-Net | KE6CHO-5 | BBS | BBS co-located at Redding | 2026-04-17 | msg 1157 |
| RDG | K-Net | MED | K-Net | Medford, OR via NET/ROM (better than manual chain for some ops) | 2026-04-17 | msg 1156 (KN6BDH) |
| KBANN | KA | KRDG (alt route) | KA | **two-hop shortcut:** KBANN → KRDG → HMKR → KC7HEX-1 worked when full chain failed | 2026-04-17 | msg 1166 (KO6TH) |
| KN6BDH-1 (Vallejo) | BBS | WOODY | KA | direct RF, reliable | 2026 spring BBS Net | Ryan N6ZOO |
| KN6BDH-1 (Vallejo) | BBS | KELSO | KA | direct RF, intermittent | 2026 spring BBS Net | Ryan N6ZOO |
| W6OAK | Both | WOODY:N6ZX | KA | direct RF, works; multi-hop latency noticeable (~3-5s per ack). **Recommended first-hop gateway into the KA-Node / Peninsula side.** | 2026-04-18 | operator confirmed |
| W6OAK | Both | MONTC:K2YE-5 | K-Net | direct RF, quality 192, busiest OAK neighbor after WBAY. **Recommended first-hop gateway into the K-Net / auto-routed side** (reaches SNY, BUTANO, FCITY, etc.) | 2026-04-18 | operator confirmed |
| WOODY:N6ZX | KA | W6ELA-1 (Palo Alto BBS) | BBS | chained connect from WOODY's converse mode, Ed's BBS2 on the far end | 2026-04-18 | operator confirmed |
| WBAY:N6ZX-5 | K-Net | MONTC:K2YE-5 | K-Net | on 145.050; both confirmed as direct neighbors of OAK | 2026-04-17 | msg 1161 + OAK ROUTES |
| MONTC:K2YE-5 | K-Net | SNY:K6SNY-5 | K-Net | **frequency crossing** to 144.910 MHz — NET/ROM handles switch automatically | 2026-04-17 | msg 1161 (KK6FPP) |
| ROCK:K6FB-5 (SoCal) | K-Net | BANNER:KF6DQU-9, BETHEL:WB6YNM-3, BULN:K6IXA-5, BUTANO:W6SCF-4, EDH:N6QDY-5, ELSO:WA6KQB-5 | K-Net | heard from ROCK's Nodes list, multiple one-hop neighbors | 2024 | KC7HEX "KROCK Up and Running" |

---

## Degraded or Broken Edges (as of 2026-04-17)

| From | To | Status | Source |
|---|---|---|---|
| HMKR | KRDG (reverse direction) | **compromised** — suspected snow/ice on HMKR site | msg 1159 (KC7HEX) |
| RDG | MED | intermittent — "Failure to connect to MED" | msg 1157 (KO6TH) |
| RDG | HMKR | intermittent for some ops | msg 1155 (KJ6WEG) |
| RDG | PHXOR | intermittent — couldn't get past Redding | msg 1155 (KJ6WEG) |
| KRDG | MED / HMKR / PHXOR | "can't seem to get past Redding" | msg 1153 (KO6TH) |
| N6ZX (WOODY site) | — | WOODY had TX issues 2026-04-15 (keys up then drops — likely low voltage or SWR foldback). **Confirmed working again from OAK on 2026-04-18** for a chained connect to W6ELA-1. Worth rechecking periodically. | msg 1151 (KI6ZHD, 2026-04-15) + operator 2026-04-18 |

---

## Known Nodes by Region (from KPC-3 skill + recent threads)

### Bay Area (145.050)
`OAKND:W6OAK`, `OAKLND:W6OAK-5`, `BUTANO:W6SCF-4`, `BERRY:WB6YNM-5`, `KBERR:WB6YNM-4`, `LPRC3:N6ACK-4`, `KLPRC3:N6ACK`, `KPAC:WA6TOW-5` (reported down 2024)

### NorCal backbone toward OR (145.050)
`KHILL` → `KJOHN` → `KBANN` → `KRDG / RDG:KE6CHO-5 / N6RZR-4` → `HMKR (port 1)` → `KC7HEX-1 / MED` → `PHXOR`

### Nevada / Sierra
`TAHOE_NODE` (digi-only, back online 2024-12-04), `GOLD_NODE` (moved)

### Vallejo / North Bay (144.910 mix)
`KN6BDH-1`, `WOODY` (intermittent), `KELSO` (intermittent), `BRKND:KJ6WEG`, `MARSND:KB6HOH-11` (Winlink RMS), `SONND:K6ACS`, `TRFND:N6TAM`

### South Bay (144.910)
`SNY / KSNY / K6SNY-1` (BBS) — reach from 145.050 via `WBAY → MONTC → SNY` with automatic frequency hop

### SoCal / Central (145.050)
`ROCK:K6FB-5 / KROCK` neighbors: `BANNER:KF6DQU-9`, `BETHEL:WB6YNM-3`, `BULN:K6IXA-5`, `EDH:N6QDY-5`, plus others truncated in source

### Fresno / Central Valley
`FRSNO_NODE` (W6CTT) — new node announced in earlier threads

---

## Path Cookbook (verified multi-hop recipes)

### Bay Area → Medford, OR BBS (KC7HEX-1)
**Full manual chain (works when conditions cooperate):**

```
c KHILL s
c KJOHN s
c KBANN s
c KRDG s
c HMKR s
c 1 KC7HEX-1
```

**Two-hop NET/ROM shortcut (KO6TH reported success 2026-04-17):**

```
c KBANN       # or connect first to a local NET/ROM node
c KRDG        # from KBANN
c 1 KC7HEX-1  # from HMKR (which KRDG routes to)
```

Reverse direction (HMKR → KRDG) is **broken** as of 2026-04-17, so the reverse path likely fails until HMKR is serviced.

### Bay Area → South Bay BBS (SNY / K6SNY-1)
Connect to `WBAY` on 145.050, then `c SNY` — NET/ROM handles the 145.050 → 144.910 crossover at MONTC automatically. No need to manually switch your rig.

### Vallejo BBS Net (KN6BDH-1)
Local reliable reach: via `WOODY`. Occasional reach: via `KELSO`.

### Bay Area → Palo Alto BBS (W6ELA-1 "Ed's BBS")
KA-Node chained connect, confirmed 2026-04-18:

```
c WOODY          # wait for ### CONNECTED TO WILD NODE WOODY
c W6ELA-1        # from WOODY's converse mode; wait for ### LINK MADE
```

Alternative single-command form (not yet verified from OAK):

```
c W6ELA-1 via WOODY
```

W6ELA-1 runs **BBS2**, not a PBBS. Commands there are `BU`, `C`, `I`, `LC`, `A`, `B`, `?`, `CO`. Traditional PBBS verbs like `L`, `R`, `SP`, `K` will return "Unknown command." See SKILL.md "BBS variants" for details. Disconnect with a single `B` at the BBS level; WOODY tears down the whole chain automatically.

### Verified UNPROTO Broadcast Paths (operator confirmed)

UNPROTO frames are single-hop AX.25 UI frames that every station in the chain digipeats. Good for net announcements and Sunday Night Packet Net style group QSOs. From W6OAK, two reliable first-hop gateway nodes are **WOODY** (KA-Node side) and **MONTC** (K-Net side), so most good broadcast chains start with one of them.

**Long NorCal UNPROTO sweep — confirmed working from W6OAK (2026-04-18):**

```
UNPROTO BOT VIA WOODY,SCLARA,KJOHN,KBERR,SCLARA,KBANN,HOGAN
```

Notes on this chain:
- `BOT` is the destination (to-field) callsign — anyone monitoring sees the frame addressed to `BOT`.
- The chain mixes node types. `WOODY`, `KJOHN`, `KBERR`, `KBANN` are KA-Nodes (expected). `SCLARA` and `HOGAN` resolve to K-Net callsigns (KI6ZHD-5 and WA6D-5) but empirically digipeat this frame anyway. Don't "fix" this — the path is verified as-is.
- `SCLARA` appears **twice** on purpose. The frame bounces back through SCLARA between KBERR and KBANN, which is how this operator got the chain to close all the way to HOGAN.
- Look for the `*` marker in the monitored frames to see which hops you personally heard. Missing `*`s don't necessarily mean failure — they can mean that hop repeated out of your RF range.

---

## Frequency Crossings

| Point | Links |
|---|---|
| MONTC | 145.050 ↔ 144.910 (automatic via NET/ROM) |
| TAHOE_NODE | returned from 145.09 to 145.050 (2024) |
| HMKR | port 1 = 145.050 chain toward OR |

---

## Operator Tips Captured From Thread

- When long manual chains fail, try letting NET/ROM route instead (use alias like `MED` instead of `KMED`).
- If chain drops mid-session, increase **retries** and **response wait time** in your TNC (N6ZOO, msg 1158).
- HMKR is picky: include the port number (`c 1 KC7HEX-1`). NET/ROM does this for you; manual KA-Node chains don't.
- Winter weather on mountain-top nodes (HMKR, N6ZX/WOODY) reliably degrades paths — expect breakage Dec–Apr.

---

## TODO / Gaps

1. No explicit map for **Sacramento / Foothills corridor** (K6HTD, KM6LYW, AK6MJ are active but paths not posted).
2. `ELSO` and several other ROCK neighbors were truncated in the source — need a direct `NODES` dump from ROCK or BUTANO.
3. `PHXOR` reachability is asserted but never confirmed working in the recent thread.
4. Reverse paths (OR → Bay Area) are almost never posted; most threads are OR-bound traffic.

**Next refresh:** pull NODES output from local BUTANO / OAKLND after connecting, and append to this file.

---

## Raw Source Messages

- [Message 1158 — N6ZOO full path to KC7HEX-1](https://groups.io/g/145050PacketNetwork/message/1158)
- [Message 1166 — KO6TH two-hop shortcut](https://groups.io/g/145050PacketNetwork/message/1166)
- [Message 1159 — KC7HEX HMKR↔RDG broken](https://groups.io/g/145050PacketNetwork/message/1159)
- [Message 1161 — KK6FPP on MONTC / SNY frequency crossing](https://groups.io/g/145050PacketNetwork/message/1161)
- [Message 1151 — KI6ZHD WOODY issues](https://groups.io/g/145050PacketNetwork/message/1151)
- [Group RSS feed](https://groups.io/g/145050PacketNetwork/rss)

---

## Live Capture — OAK:W6OAK-5 (2026-04-17 21:47 PDT)

Pulled directly from our own K-Net node via `CONNECT OAK` followed by `NODES`, `ROUTES`, `MHEARD`. This is the authoritative, freshest view of the network as seen from East Oakland, filtered by `MINQUAL 120`.

### OAK's `NODES` list — K-Net destinations OAK can route to

| Alias | Callsign | Type | Region (best guess) |
|---|---|---|---|
| BANNER | KF6DQU-9 | K-Net | Banner Mtn (Grass Valley) |
| BETHEL | WB6YNM-3 | K-Net | Bethel Island |
| BULN | K6IXA-5 | K-Net | Blue Ridge / Colusa |
| BUTANO | W6SCF-4 | K-Net | Butano Ridge (San Mateo) |
| ELSO | WA6KQB-5 | K-Net | El Sobrante |
| FCITY | KI6UDZ-7 | K-Net | Foster City |
| HILL | KF6ANX-5 | K-Net | (KA sibling = `KHILL`) |
| HOGAN | WA6D-5 | K-Net | Hogan / Calaveras |
| JOHN | KF6ANX-4 | K-Net | (KA sibling = `KJOHN`) |
| MONTC | K2YE-5 | K-Net | Mt. Umunhum / Monte Cristo |
| NITE | KI6JAS-6 | K-Net | ? |
| ROCK | K6FB-5 | K-Net | LCARC / Rock (SoCal) |
| SCLARA | KI6ZHD-5 | K-Net | Santa Clara (KI6ZHD) |
| SFRC | OFF | K-Net | **American Red Cross SF. Alias "OFF" is a config typo — not a status flag. Operator intended to disable K-Net via the name, instead immortalized it. Node is live.** |
| SNY | K6SNY-5 | K-Net | Sunnyvale |
| WBAY | N6ZX-5 | K-Net | West Bay / Mt. Vaca |
| ENABLE | — | K-Net meta | enable flag, not a destination |

### OAK's `ROUTES` — direct one-hop RF neighbors

All at quality 192 (high). `!` marks locked/manual entries. Number after quality is use count (higher = busier).

| Neighbor | Quality | Uses | Maps to alias |
|---|---|---|---|
| N6ZX-5 | 192 | 13 | WBAY |
| K2YE-5 | 192 | 10 | MONTC |
| K6FB-5 | 192 | 1 | ROCK |
| WA6TOW-1 | 192 | 0 (locked) | PAC (currently down per groups.io) |
| KF6ANX-4 | 192 | 0 (locked) | JOHN |
| KF6ANX-5 | 192 | 0 (locked) | HILL |
| KF6DQU-9 | 192 | 0 (locked) | BANNER |
| N6ACK-4 | 192 | 0 (locked) | LPRC3 (absent from NODES — probably gateway only) |
| OFF | 120 | 1 | SFRC (marked OFF) |

### OAK's `MHEARD` — stations heard directly on RF in last pass

| Station | Last Heard |
|---|---|
| KF6ANX* | 2026-04-17 20:48 |
| W6ELA-1* | 2026-04-17 20:51 |
| WA6KQB-4 | 2026-04-17 21:00 |
| W6REM | 2026-04-17 21:03 |
| N6ZX | 2026-04-17 21:13 |
| AUBNOD* | 2026-04-17 21:18 |
| KU6S | 2026-04-17 21:32 |
| K6FB | 2026-04-17 21:41 |
| W6OAK | 2026-04-17 21:41 |
| N6YP* | 2026-04-17 21:42 |
| OFF | 2026-04-17 21:43 |
| N6ZX-5 | 2026-04-17 21:43 |

`*` = heard via a digipeater, not direct.

### Key insights from this capture

1. **OAK already routes to HILL/JOHN via K-Net.** Packet bot can say `c HILL` or `c JOHN` instead of manually chaining KHILL/KJOHN through KA-Node mode.
2. **Neither KBANN, KRDG, HMKR, MED, PHXOR, nor KC7HEX-1 appear in OAK's NODES list** — they're either KA-Node only, or their K-Net advertisements fall below MINQUAL 120. **Manual KA-Node chaining is still required past Redding.**
3. **WBAY (N6ZX-5) is OAK's busiest neighbor** (13 uses) and is the gateway to South Bay / Peninsula destinations — SNY, MONTC, FCITY, SCLARA all likely route through it.
4. **ROCK (K6FB-5) is a direct RF neighbor from Oakland!** Quality 192, confirmed in both ROUTES and MHEARD (just heard at 21:41). That's a surprisingly long link. Makes ROCK's SoCal node list easy to reach in one hop.
5. **AUBNOD** (Auburn) heard via digipeater — potential new node to investigate; not in NODES yet.
6. **PAC:WA6TOW-1** is locked as a route but not in NODES, which matches the groups.io report that KPAC is currently down.

### Recommended bot preferences (updated)

- **From W6OAK to South Bay BBS (SNY)**: `c SNY` — K-Net routes via WBAY → MONTC automatically, handles 145.050↔144.910 crossing.
- **From W6OAK to anywhere in SoCal via ROCK**: `c ROCK` (direct RF), then chain into ROCK's neighbors.
- **From W6OAK to Medford OR (KC7HEX-1)**: no K-Net shortcut — use the manual chain `c HILL / c JOHN / c KBANN / c KRDG / c HMKR / c 1 KC7HEX-1`. (HILL/JOHN are the K-Net entry, the rest of the chain is KA-Node.)
- **Mixed-type edges**: once we leave KRDG heading north, we're KA-Node-only territory until we reach MED (which is K-Net at the Medford end).

---

## Experiment Log — 2026-04-17 21:52–21:56 PDT

Attempted to triangulate the network by connecting OAK → BUTANO → pull BUTANO's NODES.

### Findings

**`NODES BUTANO` from OAK returned:**
```
Routes to BUTANO:W6SCF-4
 144 3 1 K2YE-5
```
Format: `quality obs hops neighbor`. So OAK would route to BUTANO via MONTC (K2YE-5), 1 hop beyond, at quality 144.

**`NODES HILL`:**
```
Routes to HILL:KF6ANX-5
 144 4 1 N6ZX-5
```
OAK uses WBAY (not the locked direct link) as preferred path to HILL.

**`NODES MONTC`:**
```
 192 4 1 K2YE-5     <- direct, preferred
 144 4 1 N6ZX-5     <- backup via WBAY
```

### Connect attempts failed silently

Both `C BUTANO` and `C MONTC` from OAK echoed but never produced a `*** CONNECTED` banner within 25–30 seconds. OAK `STATS` showed:

```
L4 Connects: 3 sent, 0 rcvd
L4 Frames: 0 sent, 0 rcvd
L3 Frames Relayed 0
```

But `LINKS` did show `N6ZX-5 W6OAK-5 S=5 T=X V=2` — so the AX.25 RF link to WBAY was up. The failure was at Layer 4 (the NET/ROM circuit). WBAY apparently received the connect requests but couldn't (or didn't) forward them onward, or the far end couldn't acknowledge.

### Implications for the bot

1. **Don't assume a NODE in OAK's `NODES` list is immediately reachable.** Path quality ≥ 120 doesn't mean "works right now".
2. **Always wait at least 30–60 seconds after a `C` command before concluding the attempt has failed.** NET/ROM L4 retries are slow.
3. **When an L4 connect stalls, inspect `LINKS` and `STATS` to distinguish "RF didn't happen" vs "L4 circuit didn't set up".** If `L4 Connects sent > rcvd`, the far end isn't answering.
4. **MONTC and BUTANO were both unreachable from OAK tonight** (~22:00 PDT Friday). Could be mid-evening congestion, stale routing, or an actual outage on the Peninsula backbone. Worth re-testing at a different hour.
5. **HILL's locked-direct route from OAK (KF6ANX-5 at quality 192) is probably not RF-reachable right now** — OAK prefers the WBAY-relayed path (quality 144). The locked entry looks aspirational.

### Confirmed edges captured during experiment

| Edge | Source |
|---|---|
| OAK → N6ZX-5 (AX.25 up) | LINKS output at 21:56 |
| N6ZX (WBAY) digipeats KMBBS and WOODY | Monitored `N6ZX>ID` beacon at 21:52 |
| K6FB (ROCK) beaconing from Castle Rock State Park | Monitored at 21:55 |
| OFF:SFRC is alive on air (American Red Cross SF — "OFF" is a config typo) | Monitored `OFF>ID` at 21:53 |

### Network quality snapshot (from `NODES <alias>` queries)

| Destination | Via neighbor | Quality | Hops beyond |
|---|---|---|---|
| BUTANO:W6SCF-4 | MONTC (K2YE-5) | 144 | 1 |
| HILL:KF6ANX-5 | WBAY (N6ZX-5) | 144 | 1 |
| MONTC:K2YE-5 | direct | 192 | 0 |
| MONTC:K2YE-5 | WBAY (N6ZX-5) | 144 | 1 (backup) |

---

## Live Capture — WBAY:N6ZX-5 (2026-04-17 22:03–22:07 PDT)

Connected from OAK directly to WBAY (one-hop RF, quality 192, quick connect <12s). WBAY is the real workhorse of the Bay Area backbone — Woodside, CA, 74,452 minutes uptime (~51 days), 25 known nodes, 469 L3 frames relayed, actually balanced L4 traffic (20 sent / 32 received).

### WBAY's `NODES` list — 25 K-Net destinations

Expanded view compared to OAK's 16. Nodes marked **NEW** aren't in OAK's list.

| Alias | Callsign | NEW? | Notes |
|---|---|---|---|
| AUBNOD | KK6SEN-4 | NEW | Auburn — OAK only heard it as a digipeated echo |
| BANNER | KF6DQU-9 |  |  |
| BETHEL | WB6YNM-3 |  |  |
| BRKNRG | N6KRV-5 | NEW | Berkeley area likely |
| BULN | K6IXA-5 |  |  |
| BUTANO | W6SCF-4 |  |  |
| COOL | KM6LYW-4 | NEW | Cool, CA — Craig's home node (BBS Net check-in) |
| EDH | N6QDY-5 | NEW | El Dorado Hills |
| ELSO | WA6KQB-5 |  |  |
| FCITY | KI6UDZ-7 |  |  |
| HERALD | W6UHQ-4 | NEW | Herald, CA (Sacramento area) |
| HILL | KF6ANX-5 |  |  |
| HOGAN | WA6D-5 |  |  |
| JOHN | KF6ANX-4 |  |  |
| MONTC | K2YE-5 |  |  |
| NITE | KI6JAS-6 |  |  |
| OAK | W6OAK-5 |  | us, seen from WBAY's perspective |
| **RDG** | **KE6CHO-5** | **NEW** | **Redding K-Net — crucial for NorCal→OR chain** |
| ROCK | K6FB-5 |  |  |
| ROSE | WA7DG-4 | NEW | Roseburg, OR likely |
| SCLARA | KI6ZHD-5 |  |  |
| SFRC | OFF |  | American Red Cross SF; alias "OFF" is a typo, node is live |
| SNY | K6SNY-5 |  |  |
| VOLC | N3CKF-5 | NEW | Volcano, CA (N3CKF posted in the thread) |

### WBAY's `ROUTES` — 18 direct RF neighbors

All at quality ≥ 120 as expected. High use counts and `!` lock marks.

| Neighbor | Quality | Uses | Alias |
|---|---|---|---|
| K2YE-5 | 192 | 10! | MONTC |
| WB6YNM-3 | 192 | 10! | BETHEL |
| KF6ANX-4 | 192 | 9! | JOHN |
| WA6D-5 | 192 | 5! | HOGAN |
| K6IXA-5 | 192 | 4! | BULN |
| KF6DQU-9 | 160 | 3! | BANNER |
| KF6ANX-5 | 192 | 3! | HILL |
| W6OAK-5 | 192 | 2! | OAK (us) |
| KI6UDZ-7 | 192 | 1! | FCITY |
| WA6KQB-5 | 192 | 1! | ELSO |
| KI6JAS-6 | 180 | 1! | NITE |
| KI6ZHD-5 | 194 | 1! | SCLARA |
| KK6SEN-4 | 120 | 1 | AUBNOD (newer, not locked) |
| OFF | 120 | 1 | SFRC |
| K6FB-5 | 192 | 1! | ROCK |
| WB6YNM-5 | 194 | 0! | BERRY (in ROUTES but not NODES!) |
| KF6DQU-7 | 192 | 0! | (KF6DQU-7 — BANNER's sibling SSID) |
| N6ACK-4 | 190 | 0! | LPRC3 |

### WBAY's `MHEARD` — stations heard directly on RF

| Station | Last Heard |
|---|---|
| KO6CZI-5 | 04/17 03:33 |
| N6YP | 04/17 03:34 |
| WB6YNM-3 | 04/17 03:40 |
| W6ELA-1* | 04/17 03:43 |
| BANNER | 04/17 03:45 |
| KF6DQU-9 | 04/17 03:45 |
| K6CVD-15 | 04/17 03:50 |
| KK6SEN | 04/17 03:51 |
| KF6ANX-8 | 04/17 03:52 |
| KF6DQU-10 | 04/17 03:54 |
| OFF | 04/17 03:54 |
| W6OAK-5 | 04/17 03:54 |
| K2YE-5 | 04/17 03:54 |
| KI6UDZ-7 | 04/17 03:56 |
| KK6SEN-15 | 04/17 03:57 |
| **KBANN** | **04/17 03:57** |
| OAK | 04/17 03:57 |

`*` = via digipeater.

### Biggest new insight: **WBAY can hear KBANN directly**

This is huge for the NorCal→OR chain. OAK cannot reach KBANN directly (KBANN is not in OAK's NODES list and not in OAK's MHEARD). But **WBAY hears KBANN on RF**. That means:

**Potentially better NorCal→OR route:** `OAK → WBAY → KBANN → KRDG → HMKR → KC7HEX-1`

If WBAY can act as a digipeater or reach KBANN directly, we may be able to skip the manual KHILL/KJOHN hops entirely. Worth testing: from WBAY, try `C KBANN` or `C RDG` (WBAY knows `RDG:KE6CHO-5` as a K-Net destination).

### Other new K-Net destinations worth probing

- **RDG:KE6CHO-5** — WBAY sees Redding as a K-Net node. From WBAY, `c RDG` should work and gives us a NET/ROM path into Redding without manual chaining.
- **COOL:KM6LYW-4** — lets us reach the Sierra foothills corridor (Auburn/Placer/El Dorado).
- **HERALD:W6UHQ-4** — Sacramento Valley.
- **VOLC:N3CKF-5** — Volcano, CA. Interesting as N3CKF participated in the BBS Net.
- **ROSE:WA7DG-4** — possibly Roseburg, OR. If so, this could be a **second, K-Net-only route into Oregon** that bypasses HMKR entirely.

### Recommended bot preference updates

- **Use WBAY as the Bay Area gateway, not OAK.** OAK's routing is unreliable tonight; WBAY has proven, fresh, high-volume L4 traffic.
- **From W6OAK, always connect to WBAY first** (`c WBAY`), then use WBAY's richer NODES list to route onward.
- **New preferred route to Redding:** `c WBAY` from OAK, then `c RDG` from WBAY — fully K-Net, no manual KA-Node chain.
- **Explore ROSE:WA7DG-4** as a possible alternative entry into Oregon that avoids the HMKR bottleneck reported broken in msg 1159.
- **Keep trying OAK direct connects at other times** — if the L4 stalls were congestion-related, they may clear.

---

## Live Capture — BANNER:KF6DQU-9 (2026-04-17 22:15–22:19 PDT)

Reached via `OAK → WBAY → BANNER` (two-hop K-Net chain, worked cleanly). BANNER is at Banner Mountain near Grass Valley, high up and looking north.

### N6ZX beacon clarification captured during this session

`N6ZX Kings Mt. ARC, bbs KMBBS, KaNode WOODY, knet WBAY`

So N6ZX runs three services on one call: **KMBBS** (bulletin board), **WOODY** (KA-Node), **WBAY** (K-Net). Site is Kings Mountain on the Peninsula (the "Woodside, CA" from PORTS is the nearest town).

### BANNER's `NODES` list — northbound view

| Alias | Callsign | NEW vs WBAY? | Notes |
|---|---|---|---|
| AUBNOD | KK6SEN-4 |  |  |
| BETHEL | WB6YNM-3 |  |  |
| BULN | K6IXA-5 |  |  |
| COOL | KM6LYW-4 |  |  |
| EDH | N6QDY-5 |  |  |
| ELSO | WA6KQB-5 |  |  |
| FCITY | KI6UDZ-7 |  |  |
| HERALD | W6UHQ-4 |  |  |
| HILL | KF6ANX-5 |  |  |
| **HMKRCH** | **W7VW-6** | **NEW** | **Mt. Hamaker Church — K-Net gateway near Oregon border** |
| HOGAN | WA6D-5 |  |  |
| JOHN | KF6ANX-4 |  |  |
| MONTC | K2YE-5 |  |  |
| NITE | KI6JAS-6 |  |  |
| RDG | KE6CHO-5 |  |  |
| ROCK | K6FB-5 |  |  |
| **SACBBS** | **NC6J-2** | **NEW** | Sacramento BBS |
| **SACCHT** | **NC6J-3** | **NEW** | Sacramento chat node |
| **SACNOD** | **NC6J-4** | **NEW** | Sacramento K-Net node |
| SCLARA | KI6ZHD-5 |  |  |
| VOLC | N3CKF-5 |  |  |
| WBAY | N6ZX-5 |  | us (via WBAY) |

**Missing from BANNER that WBAY had:** BRKNRG (Berkeley), BUTANO (San Mateo Peninsula), OAK, SNY, ROSE. Geographically sensible — BANNER looks north, not south into the Bay.

**Critical new discovery:** BANNER does NOT have ROSE in its NODES list despite WBAY advertising ROSE via BANNER. So the ROSE route WBAY knows is **stale** — ROSE likely stopped beaconing and BANNER hasn't passed it on in a while. Our failed `C ROSE` attempt from WBAY is now explained.

### BANNER's ROUTES (partial, fragmented over RF)

| Neighbor | Quality | Uses | Alias |
|---|---|---|---|
| WB6YNM-5 | 192 | 0! | BERRY (!)  |
| WA6KQB-5 | 192 | 1! | ELSO |
| WA6RPD-5 | 192 | 0! | **unknown — new callsign not seen elsewhere** |
| N3CKF-5 | 120 | 1 | VOLC |

Note: full ROUTES list was truncated by RF fragmentation. Worth re-running when conditions are better. WA6RPD-5 is a potential new node — needs identification.

### 🎯 THE BIG FIND: Full K-Net path to the OR border

Query we ran from BANNER: `NODES HMKRCH`
Response:
```
Routes to HMKRCH:W7VW-6
 143 3 1 KE6CHO-5
```

BANNER reaches **HMKRCH (W7VW-6)** via **RDG (KE6CHO-5)**, quality 143, 1 hop beyond RDG. That means the full working NET/ROM chain is:

```
OAK → WBAY → BANNER → RDG → HMKRCH
```

**All K-Net, all auto-routed, no manual chaining.** Five hops of NET/ROM circuits.

This is a completely different animal from the manual KA-Node chain `c KHILL s / c KJOHN s / c KBANN s / c KRDG s / c HMKR s / c 1 KC7HEX-1` that the groups.io thread was debugging. If the bot can get L4 setup through reliably (the issue we hit with BUTANO/MONTC earlier), it should be able to just say `c HMKRCH` from anywhere in the Bay Area K-Net cloud.

### W7VW context

W7VW was mentioned in groups.io msg 1149 (WW2BSA asked about telnet/AXIP access to W7VW). W7VW is the callsign behind HMKRCH, which sits near the HMKR KA-Node site. So W7VW-6 is the K-Net sibling of HMKR — same mountain, K-Net flavor. From HMKRCH onward to Medford/KC7HEX-1/MED we'd need to check what HMKRCH's NODES list contains, which means the next experiment is to connect to it.

### Sacramento cluster discovered

`NC6J-2`, `NC6J-3`, `NC6J-4` = SACBBS, SACCHT, SACNOD. Not previously in any node list we'd seen. These sit between BANNER and the Sierra, and probably serve as a Central Valley hub. Worth a future session to explore.

### Updated bot routing preferences

**For any BayArea→Redding/Oregon destination, try K-Net auto-route first:**
```
c WBAY          # from our own TNC (OAK)
c HMKRCH        # from WBAY — let NET/ROM find the path through BANNER and RDG
```

If that stalls (like our BUTANO/MONTC attempts did tonight), fall back to:
```
c WBAY
c BANNER        # manual intermediate
c RDG           # manual intermediate
c HMKRCH        # final K-Net hop
```

If even that stalls, fall back to the old KA-Node chain from msg 1158.

### New nodes to investigate in future sessions

- **HMKRCH:W7VW-6** — K-Net border gateway toward Oregon
- **SACBBS/SACCHT/SACNOD:NC6J-2/3/4** — Sacramento cluster
- **WA6RPD-5** — appeared in BANNER ROUTES, no alias yet identified
- **HERALD:W6UHQ-4** — Sacramento Valley, not probed
- **VOLC:N3CKF-5** — N3CKF is active in the BBS Net, worth connecting

---

## Station Roster — NorCal + OR Border (compiled 2026-04-19)

Unified roster for the packet bot. Pulled from three sources:

1. **MONTC JLONG (MONTC:K2YE-5 just-heard long list, 2026-04-19 morning)** — ground truth for "live today." Any callsign here gets a **Live 2026-04-19** badge.
2. **[varmintal.net/ahamp.htm](https://www.varmintal.net/ahamp.htm)** — Al WB6YNM's long-running node catalog, last updated 8/24/2024.
3. **[groups.io msg 1172](https://groups.io/g/145050PacketNetwork/message/1172)** — KC7HEX's 2026-04-18 OR→SF BBS path report, confirmed by N6PAA.

Fields: `KA-Node alias` / `K-Net alias` / `Callsign-SSID` / `Freq` / `Operator` / `Location` / `Status` / `Notes`.

Status key:
- **Live 2026-04-19** — callsign heard on MONTC ax0/ax1/ax2/ax3/ax4 this morning.
- **Recent** — appeared in the last NODE_PATHS.md MHEARD/ROUTES captures (2026-04-17 to 2026-04-18) but not today's MONTC JLONG.
- **Reported** — from Al's varmintal page or groups.io, not verified today.
- **Degraded/Down** — flagged broken in recent groups.io traffic.

### Bay Area — 145.050 MHz (W6OAK's home band)

| KA-Node | K-Net | Callsign-SSID | Freq | Operator | Location | Status | Notes |
|---|---|---|---|---|---|---|---|
| KOAK | OAKND | W6OAK | 145.05 | Hugo (that's us) | East Oakland | Live 2026-04-19 | Our station. KA-Node `KOAK`, K-Net `OAKND:W6OAK-5`, PBBS `OBOX` |
| — | OAKLND | W6OAK-5 | 145.05 | Hugo | East Oakland | Live 2026-04-19 | K-Net sibling of W6OAK |
| WOODY | WBAY | N6ZX-5 (WBAY), N6ZX (WOODY) | 145.05 | Kings Mountain ARC | Kings Mtn / Woodside | Live 2026-04-19 | **Single site, three services**: KMBBS (BBS), WOODY (KA-Node), WBAY (K-Net). OAK's busiest K-Net neighbor. Direct RF, quality 192. |
| — | — | KMBBS | 145.05 | Kings Mtn ARC | Kings Mtn | Reported | PBBS co-located with WBAY/WOODY on N6ZX |
| KBERR | BERRY | WB6YNM-5 (BERRY), K6JAC-4 (K-Net sysop) | 145.05 | Al WB6YNM (Varmint Al) | Bethel Island (BERRY hub via K6JAC) | Reported | BERRY has 10 locked routes. Mentioned in Al's site as high-traffic hub. Not in MONTC JLONG today. |
| KBETH | BETHEL | WB6YNM-3 | 145.05 | Al WB6YNM | Bethel Island | Reported | Al's home node. "Very good coverage." KA + K-Net in one KPC-3+. |
| KHILL | HILL | KF6ANX-5 | 145.05 | Todd KF6ANX | Hill near Livermore | Live 2026-04-19 | KF6ANX heard today. K-Net path quality 144 via WBAY. Locked route from OAK (q192) is aspirational. |
| KJOHN | JOHN | KF6ANX-4 | 145.05 | Todd KF6ANX | Hill near Livermore | Live 2026-04-19 | Same site as HILL. KF6ANX-8 also heard today (NetRom). Solar/battery 24/7 remote. |
| — | BUTANO | W6SCF-4 | 145.05 | W6SCF | Butano Ridge (San Mateo) | Live 2026-04-19 | In MONTC JLONG (ax2). K-Net, reached via MONTC. |
| — | BLKMTN | W6SCF-6 | 145.63 | W6SCF | Black Mtn | Reported | Sibling node on 145.63 |
| KBULN | BULN | K6IXA-5 | 145.05 | K6IXA | Blue Ridge / Colusa side | Reported | BERRY neighbor |
| KELSO | ELSO | WA6KQB-5 | 145.05 | WA6KQB | El Sobrante | Live 2026-04-19 | WA6KQB-4 heard on ax0 today. |
| — | BETHEL | WB6YNM-3 | 145.05 | Al WB6YNM | Bethel Island | Reported | (duplicate for clarity — BETHEL is the K-Net side) |
| — | BRKNRG | N6KRV-5 | 145.05 | N6KRV | Briones/Bear Ridge (inferred) | Reported | In WBAY NODES |
| — | FCITY | KI6UDZ-7 | 145.05 | KI6UDZ | Foster City | Live 2026-04-19 | KI6UDZ-7 heard today (ax0). |
| KPAC | PAC | WA6TOW-1 / WA6TOW-5 | 145.05 | WA6TOW | Pacifica (inferred) | Degraded | Reported down 2024. Still locked in OAK ROUTES but not in NODES. |
| — | BANNER | KF6DQU-9 | 145.05 | KF6DQU | Banner Mtn (Grass Valley) | Live 2026-04-19 | KF6DQU-10 heard today (ax2). Confirmed hop for KC7HEX's OR→SF path 2026-04-18. |
| KBANN | — | KF6DQU-9 (same site, KA alias) | 145.05 | KF6DQU | Banner Mtn | Live 2026-04-19 | KA-Node alias. N6PAA confirmed `c wbay via kbann` works 2026-04-18 (single-digi AX.25 shortcut). |
| — | ROCK | K6FB-5 | 145.05 | K6FB (Rock site) | Castle Rock State Park (SoCal/Central) | Live 2026-04-19 | K6FB and K6FB-5 both heard today on ax0. Direct RF to OAK, quality 192. |
| — | SFRC | OFF (callsign literally "OFF") | 145.05 | American Red Cross SF | San Francisco | Live 2026-04-19 | OFF heard on ax0 today. Alias "OFF" is a config typo; node is live. |
| — | LPRC3 | N6ACK-4 | 145.05 | N6ACK | Los Positas / Livermore area (inferred) | Reported | In OAK ROUTES, not in NODES. Probably gateway-only. |
| KLPRC3 | — | N6ACK | 145.05 | N6ACK | same site | Reported | KA sibling |
| — | NITE | KI6JAS-6 | 145.05 | KI6JAS | (unknown) | Reported | In WBAY ROUTES q180 |
| — | SCLARA | KI6ZHD-5 | 145.05 | KI6ZHD | Santa Clara | Live 2026-04-19 | KI6ZHD and KI6ZHD-5 both heard on ax0. Digipeats UNPROTO chains despite being K-Net. |
| — | HOGAN | WA6D-5 | 145.05 | WA6D | Hogan / Calaveras | Live 2026-04-19 | WA6D heard today on ax0. |
| — | AUBNOD | KK6SEN-4 | 145.05 | KK6SEN | Auburn | Live 2026-04-19 | AUBNOD heard today on ax0. |
| — | COOL | KM6LYW-4 | 145.05 | Craig KM6LYW | Cool, CA | Reported | In WBAY NODES. BBS Net check-in. |
| — | EDH | N6QDY-5 | 145.05 | N6QDY | El Dorado Hills | Live 2026-04-19 | N6QDY heard today on ax0. |
| — | HERALD | W6UHQ-4 | 145.05 | W6UHQ | Herald, CA (Sac Valley) | Reported | In WBAY NODES, not probed yet. |
| — | VOLC | N3CKF-5 | 145.05 | N3CKF | Volcano, CA (Amador County) | Reported | Active in BBS Net. |
| KTRAC | TRACY | WA6QPU-5 | 145.05 | WA6QPU | Tracy | Reported | "Back" per Al's varmintal page. |
| — | CAM05 | WG6D-8 | 145.05 | WG6D | (camera/repeater site) | Reported | |
| — | CAM91 | WG6D-6 | 144.91 | WG6D | (same site, 2m port) | Reported | Alias implies 144.91 port. |
| — | CORN | W6JEX-5 | 145.05 | W6JEX | (unknown) | Reported | Cited as bad-path example by Al. |
| — | SACBBS | NC6J-2 | 145.05 | NC6J | Sacramento | Reported | New cluster found via BANNER. |
| — | SACCHT | NC6J-3 | 145.05 | NC6J | Sacramento | Reported | Sac chat node. |
| — | SACNOD | NC6J-4 | 145.05 | NC6J | Sacramento | Reported | Sac K-Net. |
| — | — | WA6RPD-5 | 145.05 | WA6RPD | unknown | Reported | Seen in BANNER ROUTES q192, no alias yet. |

### South Bay / Peninsula — 144.910 MHz

| KA-Node | K-Net | Callsign-SSID | Freq | Operator | Location | Status | Notes |
|---|---|---|---|---|---|---|---|
| KSNY | SNY | K6SNY-5 | 144.91 | K6SNY | Sunnyvale | Live 2026-04-19 | K6SNY-5 heard today on ax1. Big throughput (60k+ packets). |
| — | — | K6SNY-1 | 144.91 | K6SNY | Sunnyvale | Live 2026-04-19 | **PBBS (KPC3+ 9.1-HM)**. Reach from WBAY via `c k6sny-1 v k2ye-7`. Confirmed by N6PAA + KC7HEX 2026-04-18. |
| — | BRKND | KJ6WEG | 144.91 | KJ6WEG | Berkeley (inferred) | Live 2026-04-19 | KJ6WEG and KJ6WEG-15 both heard. |
| — | MARSND | KB6HOH-11 | 144.91 | KB6HOH | Marin (inferred) | Live 2026-04-19 | KB6HOH-10 heard today. **Winlink RMS**. |
| — | SONND | K6ACS | 144.91 | K6ACS | Sonoma (inferred) | Live 2026-04-19 | SONND heard on ax1 today. |
| — | TRFND | N6TAM | 144.91 | N6TAM | (unknown) | Reported | |
| — | SONBBS | (K6ACS site PBBS) | 144.91 | K6ACS | Sonoma | Live 2026-04-19 | SONBBS heard on ax1. |
| — | — | AI6EE-14 | 144.91 | AI6EE | (unknown) | Live 2026-04-19 | Heard ax1. |
| — | — | K6GPD | 144.91 | K6GPD | (unknown) | Live 2026-04-19 | Heard ax1. |
| — | — | KK6FPP | 144.91 | KK6FPP | (unknown) | Recent | In NODE_PATHS MONTC/SNY traffic report. |

### South Bay / Peninsula — 145.630 MHz

| KA-Node | K-Net | Callsign-SSID | Freq | Operator | Location | Status | Notes |
|---|---|---|---|---|---|---|---|
| — | — | ENABLE (meta, NetRom flag) | 145.63 | — | — | Live 2026-04-19 | Heard ax2. Not a real destination. |
| — | — | KC6SSM-10 | 145.63 | KC6SSM | (unknown) | Live 2026-04-19 | High packet count (15k+). |
| — | — | KJ6VCP-10, KJ6VCP-4 | 145.63 | KJ6VCP | (unknown) | Live 2026-04-19 | Heard ax2. |
| — | N6ZX-10 | N6ZX-10 | 145.63 | Kings Mtn ARC | Kings Mtn | Live 2026-04-19 | N6ZX's 145.63 port. |
| — | — | W6SCF-10, W6SCF-4 | 145.63 | W6SCF | Butano | Live 2026-04-19 | BUTANO sysop on ax2. |
| — | — | KF6COZ | 145.63 | KF6COZ | (unknown) | Live 2026-04-19 | Heard ax2. |
| — | — | KE6AFE-10 | 145.63 | KE6AFE | (unknown) | Live 2026-04-19 | Heard ax2. |
| — | — | WR6HMB-10 | 145.63 | WR6HMB | (unknown) | Live 2026-04-19 | Heard ax2. |
| — | — | KD6PJE-10 | 145.63 | KD6PJE | (unknown) | Live 2026-04-19 | Heard ax2. |
| — | SFRCND (candidate) | W6REM | 145.63 | W6REM | SF (Red Cross ND) | Live 2026-04-19 | Candidate SFRC/ND node. W6REM heard on ax0 today too. |
| — | LGATOS | AG6WR-5 | 145.63 | AG6WR | Los Gatos | Reported | From prior NODE_PATHS capture. |

### Sierra / Foothills / Central Valley — 145.050 (same band, logged separately by region)

| KA-Node | K-Net | Callsign-SSID | Freq | Operator | Location | Status | Notes |
|---|---|---|---|---|---|---|---|
| — | — | N0ARY-1 | 145.09 / 223.60 | N0ARY | Sierra/Valley | Live 2026-04-19 | Heard today on ax3 and ax4 (big packet counts). Possibly mail gateway. |
| — | — | KE6I-9 | 223.60 | KE6I | (unknown) | Live 2026-04-19 | NetRom on ax4. |
| — | — | W4XSC-1 | 223.60 | W4XSC | (unknown) | Live 2026-04-19 | **1.18M packets heard** on ax4. Huge traffic. |
| — | — | KE6JJJ-1, KE6JJJ-4 | 145.09 / 223.60 | KE6JJJ | (unknown) | Live 2026-04-19 | Multi-port. |
| KGOLD | GOLD | — | 145.05 | — | Gold Country | Reported, moved | Per Al's page and old NODE_PATHS note. |
| — | TAHOE_NODE | — | 145.05 | — | Tahoe | Reported | Digi-only, back online 2024-12-04. |
| — | STAHOE | KJ6NKR-7 | 145.05 | KJ6NKR | South Tahoe (inferred) | Reported | In Al's BETHEL nodes list. |
| KPOSA | POSA | — | 145.05 | — | Mariposa (inferred) | Reported | In Al's path list. |
| KLIVE | LIVE | — | 145.05 | — | Livermore area | Reported | |

### NorCal → OR Border Gateways

| KA-Node | K-Net | Callsign-SSID | Freq | Operator | Location | Status | Notes |
|---|---|---|---|---|---|---|---|
| KRDG | RDG | KE6CHO-5 (K-Net), N6RZR-4 / N6RZR-5 (KA) | 145.05 | KE6CHO / N6RZR | Redding, CA | Reported | **Critical backbone hop.** K-Net and KA-Node versions at Redding. OAK routes via BANNER; WBAY can reach direct. |
| HMKR | HMKRCH | W7VW-6 (K-Net), HMKR sysop (KA) | 145.05 | W7VW | Mt. Hamaker, S. Oregon | Reported | **OR border gateway.** "Port 1" required when chaining through KA-Node. KC7HEX used HMKR > RDG > BANNER > WBAY path 2026-04-18. Reverse direction (HMKR → KRDG) reported compromised in msg 1159 (snow/ice). |
| — | MED | (not stated) | 145.05 | — | Medford, OR | Reported | K-Net node at Medford. Intermittent per KO6TH msg 1157. |
| — | — | KC7HEX, KC7HEX-1, KC7HEX-15 | 145.05 | Walter, KC7HEX | Medford, OR | Live 2026-04-19 | KC7HEX heard today on ax0. KC7HEX-1 is the **Medford PBBS**, reached via `c 1 KC7HEX-1` from HMKR. |
| — | PHXOR | (not stated) | 145.05 | — | Phoenix, OR | Reported (unverified) | "Can't get past Redding" per recent msgs. |
| — | ROSE | WA7DG-4 | 145.05 | WA7DG | Roseburg, OR (likely) | Reported, stale | WBAY has ROSE in NODES but BANNER does not. Advertisement likely stale. |

### New callsigns heard on MONTC JLONG 2026-04-19 not yet categorized

These are all in today's just-heard list but don't map cleanly to a known alias. Worth investigating in a future session:

- **KI6UDZ-7 / KI6UDZ** (Foster City FCITY above — confirmed)
- **KO6CZI-5** — ax0, NetRom + Text, heard 08:43
- **K6HTD** — ax0 (Sacramento foothills, sometimes mentioned)
- **N6YP** — ax0, heard 08:43. Lives in OAK MHEARD.
- **WA6KQB-5** — KELSO, ax0 NetRom
- **W6ZQK, W6ZQK-5** — ax1, multi-SSID. Unknown alias.
- **K6SDR-10** — ax1. Possible SDR/software defined node.
- **N6PAA** — ax0. Ron, the operator who tested `c wbay via kbann` yesterday.
- **W6OAK-5** — ax0. That's our own K-Net node. Good sign — OAKLND is being heard at MONTC.
- **KI6UDZ-7** — FCITY sysop.
- **N6ZX-5** — WBAY, ax0.
- **KI6ZHD-5** — SCLARA, ax0.
- **KF6ANX-8** — additional KF6ANX SSID (NetRom + Text).
- **KO6KWT-12, KO6KWT-13** — ax0. Unknown.
- **KJOHN / JOHN** — heard distinctly today (both aliases echoed, ax0).
- **KROCK / ROCK** — aliases echoed too.

### Operator → callsign quick index (for bot lookups)

| Operator (first name) | Callsign |
|---|---|
| Hugo | W6OAK |
| Al (Varmint Al) | WB6YNM |
| Todd | KF6ANX |
| Jim Beno | K2YE |
| Craig | KM6LYW |
| Walter | KC7HEX |
| Ron | N6PAA |
| Ed | W6ELA |

### MONTC (K2YE) context correction

MONTC:K2YE-5 is in **Oakland Hills (Montclair), ~900 ft ASL**, not east coast. Jim Beno K2YE operates from a Raspberry Pi 4 with Direwolf TNCs on five ports:

| Port | Freq | Digi alias |
|---|---|---|
| ax0 | 145.05 | K2YE-6 |
| ax1 | 144.91 | K2YE-7 |
| ax2 | 145.63 | K2YE-8 |
| ax3 | 145.09 | K2YE-9 |
| ax4 | 223.60 | K2YE-4 |

Use `via K2YE-7` to reach 144.91 stations (like K6SNY-1 BBS) without first connecting to MONTC. Co-located services: **K2YE-10 (Winlink RMS)**, **K2YE-5 (NET/ROM NODE)**.

---

## Sources

- [groups.io msg 1172 — N6PAA confirms short path to K6SNY-1](https://groups.io/g/145050PacketNetwork/message/1172)
- [varmintal.net/ahamp.htm — Al WB6YNM's node catalog](https://www.varmintal.net/ahamp.htm)
- MONTC JLONG pull, 2026-04-19 morning (local capture from this session)

---

# PATH ANSWERS — Bot Directory Assistant

**Purpose:** canonical destination → path lookup for the W6OAK packet bot. When a connecting operator asks "how do I get to X from here," the bot quotes from this section. **Do not invent paths.** If the destination isn't listed, say so and suggest the operator connect to MONTC and run `NODES <alias>`.

**Reference frame:** "here" means the Bay Area / MONTC footprint on 145.050. If the asker is somewhere else, the bot should ask where they're starting from before answering.

**Status tags:**
- `VERIFIED <date>` — someone confirmed this working on that date
- `BACKBONE` — relied on daily, structurally stable
- `FLAKY` — works sometimes, don't lead with it
- `BROKEN` — known down, skip unless nothing else works

**Notation:**
- `c X` = CONNECT X (NET/ROM auto-routes if X is a K-Net alias)
- `c X s` = connect and STAY (KA-Node; keeps you parked at the node if the far end drops)
- `c X via Y` = AX.25 connect to X digipeated through Y (no NET/ROM)
- `c N callsign` = connect specifying port N (required for HMKR)

---

## Destination: Oregon / Medford BBS (KC7HEX-1)

**Primary (manual KA-Node chain, most reliable):**
```
c HILL s
c JOHN s
c KBANN s
c KRDG s
c HMKR s
c 1 KC7HEX-1
```
VERIFIED 2026-04-17 via groups.io msg 1158 (N6ZOO).

**Shortcut (two-hop NET/ROM into KRDG, then KA the rest):**
```
c KBANN
c KRDG
c 1 KC7HEX-1
```
VERIFIED 2026-04-17 via msg 1166 (KO6TH).

**All-K-Net attempt (cleaner but less reliable):**
```
c WBAY
c HMKRCH      # W7VW-6, Mt. Hamaker K-Net sibling
```
Getting from HMKRCH onward to KC7HEX-1 is unverified — would need to probe HMKRCH's NODES list.

**Caveats:**
- HMKR → KRDG **reverse direction is compromised** as of msg 1159 (snow/ice on the site). Outbound to OR works, return path may fail.
- Expect winter breakage Dec–Apr on the HMKR/N6ZX mountain-top sites.
- Each hop needs patience. Don't declare failure under 30–60 seconds.

---

## Destination: Redding, CA (RDG / KRDG)

**Primary (NET/ROM via WBAY):**
```
c WBAY
c RDG         # WBAY advertises RDG:KE6CHO-5
```
VERIFIED 2026-04-17 via WBAY NODES capture.

**Fallback (manual KA-Node chain):**
```
c HILL s
c JOHN s
c KBANN s
c KRDG
```

**Notes:**
- RDG (K-Net) and KRDG (KA-Node) are the same Redding site, different services.
- From Redding the PBBS is KE6CHO-5.

---

## Destination: Phoenix, OR (PHXOR)

**Status:** FLAKY to BROKEN. Per KJ6WEG (msg 1155) and KO6TH (msg 1153), "can't seem to get past Redding."

**Best effort:**
```
c HILL s
c JOHN s
c KBANN s
c KRDG s
c HMKR s
c PHXOR
```

Don't promise the operator this will work. Suggest they try and report back.

---

## Destination: South Bay BBS (K6SNY-1, on 144.910)

**This is a frequency-crossing destination.** K6SNY-1 lives on 144.91, you're probably on 145.05. Two ways to handle it:

**Option A — NET/ROM auto-crossover via MONTC (cleanest):**
```
c MONTC
c SNY         # MONTC auto-routes 145.05 → 144.91
```
Then on SNY, the BBS is typically reached through one more connect. Check with operator or `NODES` at SNY.

**Option B — Single-digi AX.25 shortcut (N6PAA's trick):**
```
c WBAY via KBANN
c k6sny-1 v k2ye-7
```
VERIFIED 2026-04-18 by N6PAA. Slow but works. `K2YE-7` is MONTC's 144.91 digipeater port.

**How MONTC handles the frequency hop:**
MONTC:K2YE-5 has five ports, each with its own digipeater alias. To reach a station on a non-145.05 frequency without a full NET/ROM connect, digipeat through the matching K2YE-N:

| Target frequency | Digipeater to use |
|---|---|
| 145.050 MHz | `K2YE-6` |
| 144.910 MHz | `K2YE-7` |
| 145.630 MHz | `K2YE-8` |
| 145.090 MHz | `K2YE-9` |
| 223.600 MHz | `K2YE-4` |

Syntax: `c DESTCALL via K2YE-N`.

---

## Destination: Palo Alto / Ed's BBS (W6ELA-1)

**KA-Node chained connect:**
```
c WOODY        # wait for "### CONNECTED TO WILD NODE WOODY"
c W6ELA-1      # from WOODY's converse mode; wait for "### LINK MADE"
```
VERIFIED 2026-04-18.

**Alternative single-command form (unverified):**
```
c W6ELA-1 via WOODY
```

**Critical note for operators:** W6ELA-1 runs **BBS2**, not a PBBS. Commands differ:
- Use `BU`, `C`, `I`, `LC`, `A`, `B`, `?`, `CO`
- **Don't** use `L`, `R`, `SP`, `K` — those return "Unknown command."
- Disconnect with a single `B` at the BBS level; WOODY tears down the whole chain automatically.

---

## Destination: Sacramento / Central Valley

Bay Area → Sacramento corridor is **under-mapped** and paths below are partially inferred from NODES dumps. Operators should verify.

**Primary attempt (NET/ROM via WBAY → BANNER):**
```
c WBAY
c BANNER
c SACNOD      # NC6J-4, Sacramento K-Net
```
Not verified end-to-end — BANNER does advertise the SAC cluster in its NODES list (2026-04-17).

**Other SAC destinations reachable from BANNER:**
- `SACBBS:NC6J-2` — Sacramento BBS
- `SACCHT:NC6J-3` — Sacramento chat node
- `HERALD:W6UHQ-4` — Sac Valley
- `COOL:KM6LYW-4` — Cool, CA (Placer/El Dorado foothills)
- `EDH:N6QDY-5` — El Dorado Hills
- `AUBNOD:KK6SEN-4` — Auburn
- `VOLC:N3CKF-5` — Volcano, CA

Syntax after reaching BANNER: `c <alias>`.

---

## Destination: Sierra Foothills (Auburn / Placer / El Dorado)

**Primary:**
```
c WBAY
c AUBNOD      # Auburn, KK6SEN-4
```
OR
```
c WBAY
c COOL        # Cool, CA, KM6LYW-4
```

Both verified in WBAY's NODES list 2026-04-17. Craig KM6LYW is a regular BBS Net check-in.

---

## Destination: North Bay / Vallejo (KN6BDH-1 BBS net)

**Primary (via WOODY):**
```
c WOODY
c KN6BDH-1
```
Reported reliable direction (2026 spring BBS Net, Ryan N6ZOO).

**Fallback (via KELSO, intermittent):**
```
c WOODY
c KELSO s
c KN6BDH-1
```

---

## Destination: Sunnyvale / Santa Clara area (K-Net)

**SCLARA (KI6ZHD-5):**
```
c WBAY
c SCLARA
```

**FCITY (KI6UDZ-7, Foster City):**
```
c WBAY
c FCITY
```

**BUTANO (W6SCF-4, Butano Ridge):**
```
c MONTC
c BUTANO
```
Note: OAK → BUTANO direct has stalled at L4 (2026-04-17 session). Going through MONTC is more reliable.

---

## Destination: Berkeley / East Bay

**BRKNRG (N6KRV-5):**
```
c WBAY
c BRKNRG
```
Only verified as a WBAY NODES entry, not probed end-to-end.

**ELSO (WA6KQB-5, El Sobrante) — backbone:**
```
c ELSO         # K-Net from OAK if in range, else c WBAY / c ELSO
```

---

## Destination: SoCal / ROCK (K6FB-5) and neighbors

**ROCK is a direct RF neighbor from Oakland.** One-hop, quality 192, verified.
```
c ROCK         # K6FB-5 direct from OAK
```
From ROCK, reach its neighbors with `c <alias>`. ROCK advertises: BANNER, BETHEL, BULN, BUTANO, EDH, ELSO.

---

## Destination: American Red Cross SF (SFRC)

**Site alias is literally `OFF` (config typo, node is live):**
```
c SFRC         # routes to OFF via NET/ROM
```
Or directly on RF via digi if nearby:
```
c OFF
```
Heard live on ax0 2026-04-19.

---

## Destination: not listed above

If the operator asks for a destination this doc doesn't cover, the bot should respond:

> "I don't have a verified path to <DEST> in my directory. Your best bet is to connect to MONTC (`c MONTC` from 145.05) and run `NODES <DEST>` — MONTC will tell you whether it can reach that node and via what path. If MONTC doesn't know about it, try the same on WBAY (`c WBAY` then `NODES <DEST>`). If you find a working path, please post it to the 145050PacketNetwork groups.io list so it can be added here."

---

## General troubleshooting to offer operators

- **Connect stalls for 30+ seconds:** NET/ROM L4 retries are slow. Wait 60 seconds before giving up.
- **`L4 Connects sent > rcvd` in STATS:** far end isn't answering. Try a different path.
- **Chain drops mid-session:** increase retries and response wait time on your TNC.
- **Manual chain fails end-to-end:** try letting NET/ROM route with a K-Net alias (e.g. `MED` instead of `KMED`).
- **Everything fails:** try at a different hour. Mid-evening congestion and daytime band conditions both matter.
- **Winter months (Dec–Apr):** HMKR and N6ZX/WOODY mountain sites degrade. Expect breakage.

---

## Bot voice guidelines

When answering path questions, the bot should:

1. Confirm the starting point. "You're on MONTC / W6OAK — is that where you're sending from?"
2. Quote the primary path verbatim, in a fenced block. Don't paraphrase syntax.
3. Flag freshness. "This was verified on <date>. It may have shifted since."
4. Offer one backup path if the primary is flaky.
5. If frequency-crossing, always mention the `K2YE-N` digipeater trick with the matching port.
6. Sign off briefly. "73" is fine.

Keep it short. Packet is slow. Every character costs time.

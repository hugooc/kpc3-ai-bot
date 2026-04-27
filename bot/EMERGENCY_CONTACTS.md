# EMERGENCY CONTACTS — W6OAK Bot Directory

**Purpose:** Help a non-ham government employee or served-agency liaison get a message through during a disaster. Maps plain-English destinations ("Alameda County EOC", "supplies from Sacramento", "welfare check to Marin") to real nets, frequencies, and packet paths.

**Scope (v1, 2026-04-19):** Bay Area + Sacramento + North Bay. Bay Area is Alameda, Contra Costa, San Francisco, San Mateo, Santa Clara, Marin. North Bay is Napa, Sonoma, Solano. Plus Sacramento County ARES and Cal OES / state-level coordination.

**How the bot uses this file:** Loaded at boot alongside NODE_PATHS.md. The emergency-mode prompt tells the bot to match the user's request against the AGENCIES table, then combine with a path from NODE_PATHS.md where packet is available, or pivot to a voice net frequency where it is not.

**Freshness:** Every entry carries a `VERIFIED` date and confidence label (HIGH / MEDIUM / LOW). LOW entries tell the bot to hedge its answer.

---

## DRILL AND EMERGENCY RULES (READ FIRST)

1. **Default to drill.** Every simulated message must start with `TEST TEST TEST` on its own line. The bot prepends this unless the caller explicitly names a real declared emergency (wildfire, earthquake, power shutoff, Cal OES activation, etc.).

2. **Part 97 §97.403.** In a real emergency immediately threatening life or property, Part 97 allows amateur stations to communicate on behalf of any agency or person, waiving some of the usual restrictions. W6OAK is the control op's station (Hugo, W6OAK). Even in emergencies the control op is responsible for every transmission.

3. **Third-party traffic.** A non-ham government employee sending a message through W6OAK is third-party traffic. Domestic third-party traffic is fine inside the US. International rules are different. Stay domestic unless Hugo is on deck.

4. **When in doubt, go analog.** If a path is uncertain or a net is not active, the bot's job is to tell the user which voice frequency to try next, not to fake confidence. Voice nets are the backup.

5. **Log everything.** The bot logs every emergency-flagged conversation with a correlation ID so Hugo can review later. No message is dropped silently.

---

## PART 1 — SERVED AGENCIES

Format per row: **AGENCY** (aliases) — net/freq — EOC — served-agency list — packet/BBS notes — verified — confidence — source.

### ALAMEDA COUNTY

**Oakland (City) — ORCA** (aliases: Oakland ARES, Oakland EmComm, City of Oakland ham, ORCA Oakland)
- **Net:** Thursdays 7:30 PM on **146.88 MHz, PL 77.0** (WB6NDJ / WW6OR repeater)
- **Meetings:** First Saturday of each month, 9–11 AM, Oakland Fire Station 1
- **EOC partner:** City of Oakland / Ready Oakland / CORE program (oaklandca.gov)
- **Served agencies:** City of Oakland EOC, Oakland Fire, Oakland Police OES, CORE
- **Activities:** ARES/RACES, packet radio explicitly listed as a member activity
- **Packet path from W6OAK:** W6OAK is an ORCA-adjacent station on 145.050 backbone. ORCA members run mixed mode on 146.88 (voice) and packet via the 145.050 network. No dedicated ORCA BBS identified as of 2026-04-19.
- **Website:** ww6or.com
- **VERIFIED:** 2026-04-19 | **Confidence:** HIGH
- **Source:** https://www.oaklandca.gov/Public-Safety-Streets/Emergency-Preparedness-Services/Ready-Oakland-CORE/Oakland-Radio-Communications-Association-ORCA ; https://www.ww6or.com

**Northern Alameda County ARES / NALCO** (aliases: NALCO, Alameda ARES, North Alameda)
- **Net:** Weekly, 7:15 PM on **440.900+ PL 131.8**
- **EOC partner:** Northern Alameda County cities (non-Oakland)
- **Packet:** UNVERIFIED. 145.050 backbone reachable from area.
- **VERIFIED:** 2026-04-19 | **Confidence:** MEDIUM
- **Source:** https://www.arrl.org/Groups/view/northern-alameda-county-ares

**Alameda County OES / Sheriff ACS** (aliases: Alameda EOC, ACSO ACS, Alameda County Sheriff comms)
- **EOC:** Alameda County OES, Dublin
- **Reach:** Through ORCA (146.88) for Oakland area, or SCC inter-county calling **W6RGG 147.240+ PL 107.2** (San Leandro, AUXCOM) for mutual aid
- **Packet:** UNVERIFIED. Needs Hugo to confirm county-level BBS.
- **VERIFIED:** 2026-04-19 | **Confidence:** MEDIUM
- **Source:** https://www.scc-ares-races.org/operations/voice/freqs/regional

### CONTRA COSTA COUNTY

**Contra Costa ARES / MDARC EmComm** (aliases: Contra Costa EOC, CoCo County EOC, MDARC emergency, Mt. Diablo ARES)
- **Net + EOC reach:** **W6CX 147.060+ PL 100.0** (Mt. Diablo) — primary repeater used by Walnut Creek Communications and ARES to reach the Contra Costa EOC during exercises (BEACON 2025 confirmed)
- **EOC:** Contra Costa County OES, Martinez. New building has no dedicated ham radio room as of 2025 — ARES sets up mobile
- **Served agencies:** Contra Costa OES, Sheriff, KARO-ECHO CERT (**146.475 simplex**), hospitals via MDARC
- **Inter-county calling:** WA6HAM Orinda **145.490- PL 107.2**
- **Packet:** UNVERIFIED
- **VERIFIED:** 2026-04-19 | **Confidence:** MEDIUM
- **Source:** https://www.mdarc.org/activities/emergency-communications ; https://www.karoecho.net/workstreams/coordination

### SAN FRANCISCO

**SF ACS / SF DEM** (aliases: San Francisco EOC, SF DEM, SF Emergency Management, SF ACS)
- **Net:** Thursdays 19:30 on **WA6GG 442.050+ PL 127.3** (SF site), linked to **443.425+ PL 100.0** (Fremont site)
- **Tac 2:** W6CX **147.060+ PL 100.0** (Mt. Diablo)
- **EOC:** SF Dept of Emergency Management (DEM), 1011 Turk St., SF
- **Program:** SF Auxiliary Communications Service (SF ACS) under DEM — not a RACES unit number; SF uses "ACS"
- **Contact:** demacs@sfgov.org
- **Served agencies:** SF DEM, SFFD, SFPD, SF hospitals, Red Cross Bay Area
- **Packet:** UNVERIFIED
- **VERIFIED:** 2026-04-19 | **Confidence:** HIGH
- **Source:** https://www.sf.gov/information--auxiliary-communications-service

### SAN MATEO COUNTY

**San Mateo Sheriff ACS / SCU** (aliases: San Mateo EOC, SM County ACS, SMSO SCU, San Mateo Sheriff ham)
- **Net:** Tuesdays 20:00 on **KC6ULT 146.865- PL 114.8** (linked: La Honda 146.805-, Portola Valley 440.975+); TX also on WA6TOW **146.925- PL 114.8**
- **EOC:** San Mateo County EOC, Redwood City
- **Program:** San Mateo County Sheriff's Communications Unit (SCU), under Sheriff's Emergency Services Bureau (county's ACS / RACES-equivalent)
- **Served agencies:** San Mateo Sheriff/OES, hospitals, Red Cross, cities via Hillsborough/Portola Valley networks
- **South County coverage:** K6MPN South County ARES, SC4ARES south coast
- **Packet:** UNVERIFIED
- **VERIFIED:** 2026-04-19 | **Confidence:** HIGH
- **Source:** https://www.smso-scu.org/ ; https://www.smso-scu.org/acs-weekley-net.html ; https://www.k6mpn.org/

### SANTA CLARA COUNTY

**SCCo ARES/RACES/ACS** (aliases: Santa Clara EOC, SCCo EOC, SCC ARES, Silicon Valley ARES)
- **Nets:** Multiple operational nets during activation (Resource, Message, Command, Packet, Hospital, EOC-to-EOC)
  - Practice: 147.510 simplex PL 100, 1st & 3rd Tue 12:15
  - SVECS social: Tue 20:00 on W6ASH 145.270- PL 100 or AA6BT 146.115+ PL 100
  - Command: **W6GGF 442.500+ PL 100** (Crystal Peak)
  - Message: **W6TI 147.360+ PL 110.9** (Black Mtn)
  - Primary inter-OA: **WB6ECE 441.300+ PL 100** (SCV Section Net, simulcast)
- **EOC:** Santa Clara County OES, San Jose
- **Program:** Unified ARES/RACES/ACS — same volunteers wear all three hats. Likely the most mature EmComm program in the region
- **Served agencies:** SCCo OES, PHDOC (Public Health), all 15 city OESes, 18+ hospitals on County Hospital Net, Red Cross Silicon Valley
- **Packet:** SCCo runs their own packet network on 1.25m (223 MHz) and 2m/70cm. Specific BBS callsigns documented on scc-ares-races.org/freqs/packet-freqs.html — **confirm with Hugo for current routes from W6OAK backbone**
- **VERIFIED:** 2026-04-19 | **Confidence:** HIGH
- **Source:** https://www.scc-ares-races.org/services/emcomm/nets ; https://www.scc-ares-races.org/operations/voice/freqs/regional ; https://www.svecs.net/

### MARIN COUNTY

**Marin County RACES/ACS** (aliases: Marin EOC, Marin County Sheriff comms, MARS RACES, W6SG)
- **Net:** Operated by Marin Amateur Radio Society (W6SG) and Marin County Sheriff OES. **Frequency and weekly schedule not confirmed in 2026-04-19 research — Hugo to pull from marinraces.org/wp/ or w6sg.net/site/racesacs/**
- **EOC:** Marin County Sheriff OES EOC
- **Program:** Marin County RACES/ACS under Sheriff's OES. Adjacent to MERA (Marin Emergency Radio Authority) — MERA is a P25 public-safety system, not ham
- **Served agencies:** Marin Sheriff OES, cities, Marin General and other hospitals, Red Cross Bay Area
- **SCC inter-county:** listed as "TBD" — no published direct-to-Marin repeater. Expect to go via section net or CESN HF
- **Packet:** UNVERIFIED
- **VERIFIED:** 2026-04-19 | **Confidence:** LOW-MEDIUM — **NEEDS HUGO CONFIRMATION**
- **Source:** https://w6sg.net/site/racesacs/ ; https://www.marinraces.org/wp/

### NAPA COUNTY

**Napa County RACES / SARS / VIP** (aliases: Napa EOC, Napa OES ham, Napa County-Wide Net)
- **Net:** Wednesdays 19:00 (preceded by 18:30 First Responder tone-out test). **Primary 145.820+ PL 151.4**, alt PL 100
- **EOC:** Napa County OES (Sheriff's OES)
- **Program:** Napa County RACES (qsl.net/napa_races), joint with SARS and VIP
- **Served agencies:** Napa OES, Napa Sheriff, Queen of the Valley Hospital, Red Cross Bay Area, CA State Parks, city of Napa
- **Packet:** UNVERIFIED
- **VERIFIED:** 2026-04-19 | **Confidence:** MEDIUM
- **Source:** https://www.qsl.net/napa_races/index.htm ; https://www.qsl.net/napa_races/frequencies.htm

### SONOMA COUNTY

**Sonoma County ACS** (aliases: Sonoma EOC, Sonoma County DEM, SCRA)
- **Net:** Mondays 19:00 on **K6ACS 146.730- PL 88.5** (also EOC Tactical)
- **Command nets:** 224.820- PL 103.5 (Cmd 1), 223.760- PL 88.5 (Cmd 2)
- **HF net:** Wed 10:00 on 7230 LSB
- **EOC:** Sonoma County Dept of Emergency Management, 2300 County Center Dr., Santa Rosa
- **Program:** Sonoma County ACS (Auxiliary Communications Service) — county-government program, not ARRL ARES. SCRA (Sonoma County Radio Amateurs) is the community club
- **Served agencies:** Sonoma DEM/OES, Sheriff, CalFire LNU adjacent, Sutter Santa Rosa + Memorial hospitals, Red Cross
- **Sub-units:** South Sonoma County ACS (southcountyacs.org), North County Unit
- **Packet:** UNVERIFIED specific callsign
- **VERIFIED:** 2026-04-19 | **Confidence:** HIGH
- **Source:** https://sonomacounty.gov/administrative-support-and-fiscal-services/emergency-management/programs/auxiliary-communications-service/frequencies

### SOLANO COUNTY

**Solano County ACS** (aliases: Solano EOC, Solano OES ham, Benicia ARC)
- **Calling freq:** **441.150+ PL 77.0** (Solano ACS, per SCC regional table). Weekly net schedule not confirmed
- **EOC:** Solano County OES (Fairfield)
- **Program:** Solano County ACS under Sheriff's OES. Benicia ARC and Solano County ACS are the active amateur groups
- **Served agencies:** Solano OES, Sheriff, Travis AFB (MARS adjacent), NorthBay and Kaiser Vacaville hospitals
- **Packet:** UNVERIFIED
- **VERIFIED:** 2026-04-19 | **Confidence:** LOW-MEDIUM — schedule unclear
- **Source:** https://solanocounty.com/depts/oes/default.asp ; https://beniciaarc.com/about/

### SACRAMENTO COUNTY

**Sacramento County ARES** (aliases: Sac ARES, Sacramento EOC, Sac County OES ham, N6SAC)
- **Net:** Mondays 19:00, primary **N6ICW 147.195+ PL 123.0**, backup **K6IS 145.190- PL 162.2**
- **Resource net:** N6NA 145.250- PL 162.2
- **TAC freqs:** 146.565, 147.405, 441.000, 446.500 (TAC1-4 simplex)
- **EOC:** Sacramento County OES, 3721 Branch Center Rd, Sacramento
- **EC:** Jay Ballinger, N6SAC. District 3 EC: Carl First, N6CKV
- **Packet:** UNVERIFIED from W6OAK — NODE_PATHS.md covers Sacramento-area BBS paths; needs cross-reference
- **VERIFIED:** 2026-04-19 | **Confidence:** HIGH
- **Source:** https://sacramentoares.org/contacts/communications-plan/

### CAL OES / STATE COORDINATION

**California Emergency Services Net (CESN)** — ham HF, statewide
- **Daytime:** 7192 LSB primary, 7230 LSB secondary
- **Nighttime:** 3992 LSB primary, 3960 LSB secondary, 1987 LSB alt
- **Operated by:** California Auxiliary Communications Service (ACS)
- **Use when:** Traffic needs to leave the VHF/UHF region and you can't get a packet path to the destination county

**Cal OES SOCC (State Operations Center, Mather/Sacramento)**
- Hits via **W6AK 146.910- PL 162.2**
- **Source:** https://sacramentoares.org/contacts/communications-plan/

**CESRS** (Part 90, NOT ham) — Cal OES state-wide system via Mt. Diablo, Loma Prieta, Mt. Tamalpais. Noted here so we know it exists but we cannot use it with ham gear.

**SHARES** (DHS CISA) — HF federal network, not amateur. Used by some county OESes. Confidential frequencies.

**Sacramento Valley Section:** SM Carol Milazzo KP4MD, SEC Michael Joseph KK6ZGB

---

## PART 2 — VOICE NET FALLBACK

Use when packet paths are unavailable, uncertain, or the destination isn't reachable from 145.050. These are voice frequencies a non-ham operator can tune via a licensed ham nearby, or the bot can name for a voice-radio fallback.

| Net | Frequency | PL | Schedule | Area |
|---|---|---|---|---|
| ORCA (Oakland) | 146.88 | 77.0 | Thu 19:30 | Oakland |
| NALCO (N Alameda) | 440.900+ | 131.8 | Weekly 19:15 | N Alameda |
| W6RGG AUXCOM | 147.240+ | 107.2 | On demand | San Leandro/Alameda inter-county |
| W6CX Mt Diablo | 147.060+ | 100.0 | On demand | Contra Costa EOC reach |
| SF ACS | 442.050+ | 127.3 | Thu 19:30 | SF |
| SM ACS | 146.865- | 114.8 | Tue 20:00 | San Mateo |
| SCCo Message | 147.360+ | 110.9 | On demand | Santa Clara |
| Sonoma ACS | 146.730- | 88.5 | Mon 19:00 | Sonoma |
| Napa RACES | 145.820+ | 151.4 | Wed 19:00 | Napa |
| Solano ACS | 441.150+ | 77.0 | Unknown | Solano |
| Sac ARES | 147.195+ | 123.0 | Mon 19:00 | Sacramento |
| Cal OES SOCC | 146.910- | 162.2 | On demand | State EOC reach |
| CESN (state HF) | 7192 LSB (day) / 3992 LSB (night) | — | Statewide | CA-wide fallback |
| Calling (2m natl) | 146.520 | — | Simplex | National ham calling, direct simplex |

---

## PART 3 — RADIOGRAM TEMPLATES

Fill-in-the-blank message formats. The bot walks a non-ham through these one field at a time, then composes the final formatted message. Every template auto-prefixes `TEST TEST TEST` unless the caller confirms a real declared emergency.

### SUPPLY REQUEST

```
TEST TEST TEST
NR <seq> <precedence> W6OAK <word_count> OAKLAND CA <time> <date>
TO <receiving_agency>
FROM <requesting_agency>
SUBJ SUPPLY REQUEST
ITEMS <list>
QUANTITY <numbers>
DELIVER TO <address_or_location>
URGENCY <routine|priority|emergency>
CONTACT <name_and_phone>
BT
SIGNED <operator_callsign_or_agency_rep>
AR
```

Slots: receiving_agency, requesting_agency, list, numbers, address_or_location, urgency, name_and_phone, signed.

### WELFARE CHECK

```
TEST TEST TEST
NR <seq> W HXG W6OAK <word_count> OAKLAND CA <time> <date>
TO <receiving_agency>
REQUEST WELFARE CHECK
SUBJECT <full_name>
ADDRESS <street_address>
LAST KNOWN CONTACT <time_and_means>
REASON <concern>
CALLBACK <phone_and_name>
BT
AR
```

Precedence `W` and handling `HXG` signal a welfare-category message. Non-emergency unless a disaster is declared.

### SITUATION REPORT (SITREP)

```
TEST TEST TEST
NR <seq> <precedence> W6OAK <word_count> OAKLAND CA <time> <date>
TO <receiving_agency>
FROM <reporting_location>
SITREP AS OF <time>
1. LOCATION <where>
2. CONDITIONS <summary>
3. CASUALTIES <count_or_none>
4. INFRASTRUCTURE <power_water_roads>
5. NEEDS <immediate_asks>
6. NEXT REPORT <when>
BT
AR
```

### MEDICAL / HEALTH AND WELFARE

```
TEST TEST TEST
NR <seq> P W6OAK <word_count> OAKLAND CA <time> <date>
TO <receiving_hospital_or_clinic>
FROM <field_location>
MEDICAL REQUEST
PATIENT <age_sex_condition_anonymized>
PRESENTATION <symptoms>
TRIAGE <green_yellow_red>
RESOURCES NEEDED <ambulance_bed_supplies>
CONTACT <on_scene_call>
BT
AR
```

### EVACUATION STATUS

```
TEST TEST TEST
NR <seq> <precedence> W6OAK <word_count> OAKLAND CA <time> <date>
TO <receiving_agency>
FROM <shelter_or_checkpoint>
EVAC STATUS
HEADCOUNT <number>
CAPACITY REMAINING <number>
SUPPLIES STATUS <ok_low_critical>
MEDICAL NEEDS <any>
CONTACT <shelter_lead>
BT
AR
```

Precedence codes (ARRL): R = Routine, W = Welfare, P = Priority, EMERGENCY = life-safety immediate.

---

## PART 4 — ESCORT MODE FLOW

When the bot senses a non-ham caller who needs to send emergency traffic, it shifts from "give the path" to "walk me through it." Rough shape:

1. **Ask one question at a time.** "What agency are you trying to reach?"
2. **Confirm match.** Echo back the agency name and the path/frequency the bot picked. Ask for confirmation before proceeding.
3. **Pick a template.** Supply request, welfare check, SITREP, medical, evac.
4. **Walk through the slots.** One at a time, in plain English. "What are you requesting? (example: 200 blankets, 50 cots)"
5. **Compose and show.** Present the completed radiogram and ask for approval.
6. **Route.** Either:
   - Packet: "Send this. First: `c WOODY`. When you see the prompt, paste the message."
   - Voice handoff: "Your county ACS net is 146.88 PL 77 Thursday 19:30. For immediate traffic, find a licensed ham nearby with 2m radio and have them call this net."
7. **Log.** Record the correlation ID, the composed message, and the intended route.

---

## PART 5 — KNOWN GAPS

These rows need Hugo to confirm before the bot trusts them:

- Marin County RACES/ACS net frequency and night (pull from marinraces.org/wp/ or w6sg.net/site/racesacs/)
- Solano County ACS weekly net day/time (441.150+ PL 77.0 is the only confirmed freq)
- Napa County EOC physical address and BBS callsign
- Contra Costa County current ham room status at new Martinez EOC (May 2025 report said none)
- County-specific Winlink RMS gateways (check winlink.org/content/gateway_locations filtered to CA)
- Alameda County OES "RACES unit number" (county uses ACS branding)
- Specific BBS callsigns serving each county EOC on the 145.050 backbone

---

## PART 6 — SOURCES

- [Oakland Radio Communications Association (ORCA) — City of Oakland](https://www.oaklandca.gov/Public-Safety-Streets/Emergency-Preparedness-Services/Ready-Oakland-CORE/Oakland-Radio-Communications-Association-ORCA)
- [ORCA website](https://www.ww6or.com)
- [ARRL Section Boundaries](http://www.arrl.org/section-boundaries)
- [ARRL Pacific Division](https://www.pacific.arrl.org/sections)
- [ARRL East Bay Section](https://arrleb.org/)
- [ARRL Sacramento Valley Section](https://arrlsacvalley.org/)
- [SCCo ARES/RACES Regional Frequencies](https://www.scc-ares-races.org/operations/voice/freqs/regional)
- [SCCo EmComm Nets](https://scc-ares-races.org/services/emcomm/nets)
- [SF ACS](https://www.sf.gov/information--auxiliary-communications-service)
- [SM County SCU](https://www.smso-scu.org/)
- [Sonoma County ACS](https://sonomacounty.gov/administrative-support-and-fiscal-services/emergency-management/programs/auxiliary-communications-service/frequencies)
- [Sacramento County ARES](https://sacramentoares.org/contacts/communications-plan/)
- [Napa County RACES](https://www.qsl.net/napa_races/index.htm)
- [MDARC Emergency Communications](https://www.mdarc.org/activities/emergency-communications)
- [KARO-ECHO](https://www.karoecho.net/workstreams/coordination)
- [Northern Alameda County ARES](https://www.arrl.org/Groups/view/northern-alameda-county-ares)
- [Benicia ARC](https://beniciaarc.com/about/)
- [Marin RACES/ACS (W6SG)](https://w6sg.net/site/racesacs/)

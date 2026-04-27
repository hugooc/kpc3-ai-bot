# Kantronics KPC-3 Plus Users Guide

**Revision H — Updated to Searchable Format (2015-05-28)**

---

## Contact Information

**Kantronics**
14830 W. 117th St.
Olathe, Kansas 66062

| Department | Phone | Fax | Email |
|---|---|---|---|
| Orders / Inquiries | (913) 839-1470 | (913) 839-8231 | sales@kantronics.com |
| Service / Technical Support | (913) 839-8143 (8 AM–12 PM and 1–5 PM Central Time, M–F) | (913) 839-8231 | service@kantronics.com |

Website: www.kantronics.com

---

## Revisions

| Rev | Date | Description |
|---|---|---|
| A | 2003-11-11 | Inserted warranty form and revisions page. Deleted reference to previously supplied molded audio plug with shielded cable. |
| B | 2005-04-28 | Added UIDUPE command definition and reference in a number of locations to the GPS port. Updated "Expanding the RAM." |
| C | 2005-09-21 | Deleted further references to previously supplied molded audio plug with shielded cable. Deleted reference to Warranty Registration card. Changed time to file Warranty Registration from 10 to 60 days. Added e-mailing of Warranty Registration information. Other cleanup. |
| D | 2005-09-26 | Deleted reference to Kantronics HSP cable. |
| E | 2006-05-10 | Changed Kantronics address to 3115 W. 6th St., Ste. A. |
| F | 2006-08-22 | Removed CE mark pending RoHS Compliance. |
| G | 2011-07-31 | Updated contact information, minor text revisions. |
| H | 2015-05-28 | Updated to a searchable format. |

The KPC-3 Plus is a Kantronics hardware and software design incorporating the AX.25 Level 2 Version 2 Packet protocol as adopted by the American Radio Relay League.

© Copyright 2007–2015 by Kantronics. All Rights Reserved.

**Trademarks:**
- KPC-3 Plus® — Kantronics Co., Inc.
- KPC-9612 Plus® — Kantronics Co., Inc.
- KAM XL® — Kantronics Co., Inc.
- NET/ROM® — SOFTWARE 2000
- APRS® — Bob Bruninga, WB4APR
- HyperTerminal® — Microsoft

---

## Warranty Registration

Mail form and sales receipt to:
Kantronics, 14830 W 117th Street, Olathe, KS 66062

| Field | |
|---|---|
| Last Name | First Name |
| Call Sign | |
| Mailing Address | |
| City | |
| State | Zip/Postal Code | Country |
| Telephone | E-Mail |
| Product | KPC-3+ | Serial # |
| Date of Purchase | Dealer |

---

## License Agreement

This product contains SOFTWARE on Programmable Read Only Memory (PROM) and/or diskette and/or CD, protected by both United States copyright law and international treaty provisions.

1. **License.** The Licensee is granted a non-exclusive right to use the SOFTWARE and associated documentation. No ownership rights to the SOFTWARE are transferred.

2. **Term.** This License Agreement is effective until terminated. You may not rent or lease the SOFTWARE. You may transfer it permanently provided you retain no copies and the recipient agrees to the terms.

3. **Object Code.** The SOFTWARE is delivered in object code only. You shall not reverse compile or otherwise reverse engineer the SOFTWARE.

4. **Limited Warranty.** This product is covered by the standard Kantronics Limited Warranty.

5. **General.** This License Agreement constitutes the complete Agreement between you and Kantronics.

---

## Limited Warranty

**KANTRONICS CO., INC. LIMITED WARRANTY — Effective January 1, 1997**

1. **WARRANTY.** Kantronics warrants to the first consumer purchaser that the Applicable Product will be free from defects in material and workmanship during the Applicable Warranty Period.

2. **REMEDY.** Kantronics will, at its option, repair or replace the defective Applicable Product at no charge, excluding in-bound shipping charges.

3. **EXCLUSIVE REMEDY.** Repair or replacement is the sole remedy. Kantronics will not be responsible for incidental, special, or consequential damages.

4. **DISCLAIMER.** KANTRONICS SPECIFICALLY DISCLAIMS THE IMPLIED WARRANTY OF MERCHANTABILITY AND IMPLIED WARRANTY OF FITNESS FOR A PARTICULAR PURPOSE.

5. **APPLICABLE PRODUCTS AND PERIODS:**
   - **Units** (KPC-3 Plus, KPC-9612 Plus, KAM XL, MT1200, MT1200G): One (1) year from date of purchase.
   - **Media** (EPROMs, CDs, manuals): Thirty (30) days from date of purchase.

6. **EXCLUSIONS.** This warranty does not apply to cosmetic damage, cracked cabinets, products subject to misuse, abuse or overvoltage, unauthorized modification, or damage from improper shipping, neglect, accident, or use in violation of Kantronics instructions.

7. **REMEDY PROCEDURE.** Contact your dealer first. If unable to assist, contact Kantronics prior to returning the product to receive a Return Authorization Number.

8. **NON-ASSIGNMENT.** This Limited Warranty is not assignable.

### Return/Repair Procedures

> Over 70% of units returned for service do not require any service. Please check common user-solvable problems before returning.

**Check-List for Possible Problems:**
- Carefully check wiring connections to the 232 port
- If you purchased third-party cables, verify they conform to Kantronics wiring instructions
- Verify your terminal baud
- Consider performing a "Hard Reset"

**Information needed when contacting Service:**
- Unit name and serial number (found on the bottom of the unit)
- Firmware version number (displayed by the Version command)
- Computer available for troubleshooting if possible

Service Department hours: 8:00 AM–12:00 Noon and 1:00 PM–5:00 PM Central Time, Monday–Friday.

**Service charges outside warranty:** cost of parts, labor, and return shipping. Units returned without a Return Authorization number are subject to a minimum charge of ½ hour labor plus shipping and handling.

**International Returns:**
- All returns must be shipped to the factory
- Include in the description: "U.S. GOODS RETURNED FOR REPAIR/REPLACEMENT"
- Provide a value for customs purposes ($0 is not acceptable)
- For warranty repairs, Kantronics pays return shipping via air parcel post

---

## Radio Frequency Interference Statement

This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to Part 15 of the FCC Rules. These limits provide reasonable protection against harmful interference in a residential installation.

If interference occurs, the user is encouraged to:
- Reorient or relocate the receiving antenna
- Increase the separation between the equipment and receiver
- Connect to a different circuit outlet from the receiver
- Consult the dealer or an experienced Radio/TV technician

> Any changes or modifications not expressly approved by the party responsible for compliance could void the user's authority to operate the equipment.

All peripheral devices must be connected with high-quality shielded cables. The shield must be properly terminated 360° to the connector.

### RFI Suppression

- Use shielded cable for all connections between equipment
- Make all interconnecting cables as short as practical
- Keep antenna runs away from equipment control lines
- Ground leads should be as short as possible to a GOOD EARTH GROUND
- Interconnecting cables acting as radiators should be looped through a toroid designed for the frequency in use

### FCC Declaration of Conformity

- **Type of Equipment:** Information Technology Equipment
- **Class of Equipment:** Class B

**CE Marking Considerations:**
- All cables connecting to DC IN, PORT 1 (VHF), and COMPUTER must be ≤ 3 m in length
- All cables (except DC IN) must be shielded with the shield properly terminated 360° to the connector
- The nominal 12 V dc power must be supplied from a CE marked or third party approved power supply

---

## Table of Contents

1. [Introduction](#introduction)
2. [Installing Your KPC-3 Plus](#installing-your-kpc-3-plus)
3. [Getting Started](#getting-started)
4. [Modes of Operation](#modes-of-operation)
5. [PBBS (Personal Mailbox)](#pbbs-personal-mailbox)
6. [GPS NMEA Interfacing](#gps-nmea-interfacing)
7. [KA-Node](#ka-node)
8. [Introduction to Basic Packet Networking](#introduction-to-basic-packet-networking)
9. [K-Net Network Node](#k-net-network-node)
10. [WEFAX Mode](#wefax-mode)
11. [Other Modes of Operation](#other-modes-of-operation)
12. [Command Reference](#command-reference)
13. [Appendix A: Advanced Installation](#appendix-a-advanced-installation)
14. [Appendix B: Advanced Information](#appendix-b-advanced-information)
15. [Appendix C: Options for the KPC-3 Plus](#appendix-c-options-for-the-kpc-3-plus)
16. [Appendix D: In Case of Difficulty](#appendix-d-in-case-of-difficulty)
17. [Appendix E: Additional Information](#appendix-e-additional-information)

---

## Introduction

### Welcome

Welcome to the Kantronics KPC-3 Plus, your pathway to amateur radio packet communication. Please review this chapter before installing your KPC-3 Plus.

### Overview of This Manual

This guide covers:
- What equipment you will need for your packet radio station
- A brief introduction to packet radio
- Installing and configuring your KPC-3 Plus packet radio station
- Getting started using your KPC-3 Plus
- Documentation for each mode of operation
- A full Command Reference
- Full details on jumpers, parts list, and technical specifications

### Major Uses of Your KPC-3 Plus

By adding the KPC-3 Plus and a computer to your ham radio station, you can:
- Use computers to carry on real-time digital conversations between stations
- Send, receive, store and forward mail using a personal mailbox (PBBS)
- Send and receive mail using a community bulletin board
- Send and receive files
- Get and re-transmit location data from GPS devices
- Serve as a digipeater for other stations
- Serve as a network node point using KA-NODE and/or the optional K-Net feature

### Package Contents

- KPC-3 Plus unit
- Male DSUB-9 connector for radio port
- Metalized DSUB-9 back shell with hardware
- 3 foot (0.91 m) piece of 5-conductor shielded cable
- 2.1 mm dc power connector
- User's Guide manual on CD-ROM

### Additional Parts Needed

- An FM transceiver
- A microphone (Mic) plug and/or mating accessory plug for your radio
- A computer with an RS232 serial port
- A serial modem cable
- A 12 V dc power supply or power adapter
- (Optional) 9 V battery and battery clip (not supplied, you must install)

### Documentation Conventions

- Key names are given in capitals (e.g., press the ENTER key)
- Key combinations use a plus sign: "Ctrl+C" means hold Control while pressing C
- Multiple-key combinations generating a single character are shown in angle brackets: `<Ctrl+C>`

### Overview of Packet Radio

#### Three Basic Components of a Packet Radio Station

1. **A transceiver** with an antenna — sends/receives radio signals and passes audio to/from the TNC
2. **A TNC** (Terminal Node Controller) — translates audio signals into digital information and vice versa, performs control and storage functions
3. **A computer** — communicates digitally with the TNC for viewing and sending messages

```
Antenna
   |
Transceiver ←→ KPC-3 Plus TNC ←→ Computer
```

#### Sending a Message to Another Station

A packet communication between two stations involves these steps:

1. Each station requires a callsign (one-time configuration)
2. The originating station issues a connect command
3. A connection request is transmitted
4. The destination station acknowledges the connection
5. The TNC switches to conversation mode
6. Messages are typed and sent as packets
7. The TNC assembles packets with addressing and error-correction data
8. Audio signals are passed to the transceiver and transmitted
9. Intermediate (digipeater) stations relay the packet
10. The destination TNC receives, processes, and displays the message
11. An acknowledgment packet is returned

#### Packets

A packet is a group of characters with a **flag** and **header** at the beginning and a **checksum** and flag at the end.

**AX.25 Packet Structure:**

| Flag | Address | Control | PID | Data | Checksum | Flag |
|---|---|---|---|---|---|---|
| Beginning | Destination, source, up to 8 intermediate stations | Kind, number, control info | Optional protocol ID | 1–256 bytes | 16-bit error check | End |

**Two types of packets:**
- **Unconnected (UNPROTO):** No acknowledgment expected, no retries. Used for CQ, beacons, round table chats.
- **Connected:** Sender and receiver follow rules (AX.25). Near 100% accuracy via sequence numbers and acknowledgments.

#### Protocols

- **AX.25 (level 2, version 2):** De facto standard for amateur packet radio
- **TCP/IP / KISS:** Alternative suite using Phil Karn's KISS protocol
- **XKISS:** Extension of KISS by John Wiseman G8BPQ

#### Inside the KPC-3 Plus

| Component | Description |
|---|---|
| Microprocessor | Main controller |
| Modem | Converts digital ↔ audio |
| Firmware/EPROM | Kantronics software, interface modes, help text |
| RAM | 128K standard, expandable to 512K. Used for parameters, packet assembly, KA-NODE, GPS data |
| Lithium Battery | Power backup for RAM and optional Real Time Clock |
| Optional Real Time Clock | Battery-backed clock module |

PBBS (mailbox) default storage: 100K (with 128K RAM). User-configurable within available RAM limits.

---

## Installing Your KPC-3 Plus

### Back Panel

| Connector | Description |
|---|---|
| Radio Port (DSUB-9 female) | Accepts cable from radio for 1200 baud packet operation |
| Computer Port (DSUB-25 female) | Accepts cable from computer serial port. RS232 levels, standard ASCII. |
| Power Jack (2.1 mm) | External power 6–25 V dc. Center pin positive, sleeve negative (ground). |

> Note: All Kantronics TNCs can operate without the computer once configured. The TNC contains the intelligence to receive/store messages and serve as a relay station independently.

### Connecting to a Power Source

**Three power options:**

#### External Power (12 V dc bench)
1. Build a cable using the supplied 2.1 mm power plug and 18–22 gauge stranded 2-conductor cable
2. Center of jack → positive terminal; shell → negative terminal
3. Turn OFF all power, attach cable, plug into KPC-3 Plus
4. Turn ON power supply, press power switch to confirm LED turns on
5. Do not exceed specifications. Use a fuse no greater than 200–250 mA.

#### External Power (120 V ac mains)
Use a class 2 transformer: input 120 V ac 60 Hz 6 W; nominal output 12 V dc 300 mA. A Kantronics adapter is available as an option, or purchase from a third party.

#### Internal Power (9 V battery)
Requires a battery clip (pigtail) installed on the PCB pads labeled "+BATT-".

**Jumper configuration:**
- J1 OFF, J2 ON (default): Battery powers TNC, cut off if external power attached
- J1 ON, J2 OFF: Battery takes over if external power fails (whichever supply has higher voltage powers the TNC)

### Connect KPC-3 Plus to Your Computer

The serial cable (RS232 modem cable) is **not** supplied. Purchase one or construct your own.

**Cable specifications:**
- Standard serial modem cable (RS232), high quality shielding, less than 3 m, at least 9 wires
- One end: male DSUB-25 (connects to KPC-3 Plus "Computer" port)
- Other end: female DSUB-9 or DSUB-25 (matches your computer's serial port)

#### Wiring Diagrams

**CASE 1-A: 25-pin computer, 5 wires:**

| KPC-3 Plus | Computer |
|---|---|
| 2 | ↔ 2 TXD |
| 3 | ↔ 3 RXD |
| 4 | ↔ 4 RTS |
| 5 | ↔ 5 CTS |
| 7 | ↔ 7 SG |

**CASE 1-B: 25-pin computer, 9 wires (add to 1-A):**

| KPC-3 Plus | Computer |
|---|---|
| 1 | ↔ 1 FG |
| 6 | ↔ 6 DSR |
| 8 | ↔ 8 DCD |
| 20 | ↔ 20 DTR |

**CASE 2-A: 9-pin computer, 5 wires:**

| KPC-3 Plus | Computer |
|---|---|
| 2 | ↔ 3 TXD |
| 3 | ↔ 2 RXD |
| 4 | ↔ 7 RTS |
| 5 | ↔ 8 CTS |
| 7 | ↔ 5 SG |

**CASE 2-B: 9-pin computer, 8 wires (add to 2-A):**

| KPC-3 Plus | Computer |
|---|---|
| 6 | ↔ 6 DSR |
| 8 | ↔ 1 DCD |
| 20 | ↔ 4 DTR |

> Caution: Do not connect to a parallel (LPT) port by mistake. Female DSUB-25 connectors on computers may be parallel ports.

### Configure Your KPC-3 Plus

#### HyperTerminal Setup (Windows)

1. Start → Programs → Accessories → Communications → HyperTerminal
2. Name the connection "KPC-3Plus9600"
3. Connect using: COM1
4. Settings: 9600 bits/s, 8 data bits, no parity, 1 stop bit, hardware flow control
5. Under Properties → Settings: Emulation = TTY, "Use destructive backspace" checked

#### AUTOBAUD

The first time the KPC-3 Plus is used, it runs an AUTOBAUD routine:

1. AUTOBAUD sends "PRESS (*) TO SET BAUD" repeatedly at different baud rates
2. When the baud matches, the message becomes readable
3. Press `*` (SHIFT+8) at any time
4. AUTOBAUD sets ABAUD to match the detected baud
5. AUTOBAUD sends a sign-on message and asks for CALLSIGN

#### Required Parameter Settings

| Parameter | Default | Description |
|---|---|---|
| COMMAND | $03 (Ctrl+C) | Return to command mode character |
| CANLINE | Ctrl+X ($18) | Cancel line character |
| CANPAC | Ctrl+Y ($19) | Cancel packet character |
| PASS | Ctrl+V ($16) | Pass special character |

#### Optional Parameters

| Parameter | Default | Notes |
|---|---|---|
| ECHO | ON | Double characters if set wrong |
| FLOW | ON | Set both ECHO and FLOW together |
| XFLOW | ON | Software flow control |
| FILTER | OFF | |
| 8BITCONV | ON | |
| MONITOR | ON | Turn OFF when exiting terminal and leaving TNC on |

#### Troubleshooting Communication

**Nothing happens at terminal screen:**
- Check if another device (mouse, internal modem) is on that COM port
- Try changing the COM port setting in HyperTerminal
- Perform a hard reset using jumper J11

**Bad or intermittent data:**
- Check for COM port IRQ conflicts (COM1/COM3 or COM2/COM4 sharing interrupts)

**TNC stops behaving normally:**
- May have switched to HOST or KISS mode
- Switch back to NEWUSER or TERMINAL mode

### Connect the KPC-3 Plus to a Transceiver

The transceiver cable assembly has two functions:
1. Send signals from the transceiver speaker jack to the KPC-3 Plus Radio port
2. Send signals from the KPC-3 Plus Radio port to the transceiver microphone

#### Parts Needed

- DSUB-9 connector kit (shipped with KPC-3 Plus)
- 3-foot (0.91 m) 5-conductor shielded cable (shipped with KPC-3 Plus)
- User-supplied microphone connector for your transceiver
- User-supplied speaker plug

#### Radio Port DSUB-9 Pin Assignments

| Pin | Name | Description |
|---|---|---|
| 1 | TXA | Transmit audio (AFSK out) |
| 2 | XCD | External carrier detect |
| 3 | PTT | Push-to-Talk |
| 4 | CTLB (AN0) | Control line B / Analog input 0 |
| 5 | RXA | Receive audio (AFSK in) |
| 6 | GND | Ground |
| 7 | EXT-IN | External input for Power/Reset |
| 8 | CTLA (AN1) | Control line A / Analog input 1 |
| 9 | GND/RESET | Ground (configurable as external reset) |

#### Wiring the Microphone Connection

- Pin 1 (transmit audio) → microphone input on transceiver
- Pin 3 (PTT) → PTT or STBY pin on transceiver
- Pin 9 (ground, optional for base/mobile) → ground on microphone connector

#### Wiring the Speaker Connection

- Pin 5 (receive audio) → audio from external speaker plug
- Pin 6 (ground) → ground from external speaker plug

#### Cable Assembly Instructions

1. Strip cable outer covering to expose metalized plastic foil. Do not cut or rip foil.
2. Loosen the drain wire and foil from around the insulated wires.
3. Build up cable diameter at back shell entry with tape for strain relief.
4. Discard the metal strain relief pieces (not needed with metalized plastic back shell).
5. Connect wires to connector terminals.
6. Z-fold the metalized foil back over the cable so metal side faces the back shell.
7. Place drain wire in any gap.
8. Place shaped washers on long half-threaded screws.
9. Join the two shell halves over connector and cable.
10. Screw halves together firmly.

#### Adjusting Transceiver Receive Volume

1. Turn ON computer (transceiver OFF)
2. Start terminal program
3. Turn ON KPC-3 Plus
4. Set ABAUD and CALLSIGN if not already done
5. Turn ON transceiver; open squelch (fully counter-clockwise)
6. Slowly turn receive volume up until RCV LED lights
7. Increase volume slightly above the point the LED lit
8. Slowly turn squelch clockwise until RCV LED goes off

#### Transmit Level Adjustment

The transmit audio voltage (TXA) is adjusted digitally using the XMITLVL or CAL command.

- Target: approximately 3 to 3.5 kHz of deviation
- Default XMITLVL = 100 (corresponds to ~50 mV drive voltage)
- Below 256: voltage increases in 0.5 mV steps
- Above 256: drive increases ~15 mV per step
- Use CAL command for real-time adjustment using the `+` and `-` keys

### Connecting to a GPS Device (Optional)

The GPS device connects to either:
- The DSUB-25 "Computer" port (serial port)
- Pin 2 on the Radio port (requires firmware version 8.3 or later; enabled with GPSPORT command)

**Minimum wiring for standalone operation:**
- GPS "DATA OUTPUT" → TXD (pin 2) on KPC-3 Plus
- GPS "SIGNAL GROUND" → signal ground (pin 7) on KPC-3 Plus

> Note: Since the computer must be disconnected from the serial port to connect a GPS, configure the KPC-3 Plus for GPS operation before switching the connection.

---

## Getting Started

### Front Panel

| Control/Indicator | Color | Description |
|---|---|---|
| Power Switch | — | Push to toggle power ON/OFF |
| Power LED | Green | ON when TNC is receiving power |
| Transmit LED | Red | ON when TNC is sending a packet to the transceiver |
| Receive LED | Green | ON when TNC is receiving a signal from the transceiver |
| Connected LED | Green | ON when TNC has a packet connection on current stream |
| Status LED | Green | ON when TNC has at least one unacknowledged packet on current stream |
| Mail LED | Yellow | ON when someone is connected to PBBS; BLINKS when there is unread mail and no connection |

### Beginning a Packet Session

After completing setup, the KPC-3 Plus displays a sign-on message such as:

```
KANTRONICS KPC3PMX VERSION 9.1
(C) COPYRIGHT 2002-2005 BY KANTRONICS INC. ALL RIGHTS RESERVED.
DUPLICATION PROHIBITED WITHOUT PERMISSION OF KANTRONICS.
cmd:
```

The `cmd:` prompt means the TNC is in **Command Mode**, ready to receive commands.

### Giving Commands and Transmitting Data

**Command Mode:** The TNC interprets input as commands. Enter `<Ctrl+C>` to return here from other modes.

**Converse (CONVERS) Mode:** The TNC transmits all typed data as packets. Automatically activated when connected. Return to Command Mode with `<Ctrl+C>`.

**TRANS (Transparent) Mode:** All characters (including control characters) are transmitted as data. Used for file transfers. Requires INTFACE TERMINAL. Exit with three `<Ctrl+C>`s with less than one second between each, preceded and followed by a one-second pause.

### NEWUSER Commands

The 22 NEWUSER commands cover basic operations. To switch to the full command set: `INTFACE TERMINAL`

| Command | Description |
|---|---|
| BKONDEL | When ON, echoes backspace-space-backspace sequence for DELETE key. When OFF, echoes `\`. |
| CONNECT | Establish a packet connection with another station |
| CONVERS | Place TNC in CONVERS mode |
| DAYTIME | Read or set the clock |
| DELETE | Set the delete character |
| DISCONNE | Disconnect from connected station |
| DISPLAY | Display all KPC-3 Plus parameters |
| DWAIT | Time delay giving digipeaters priority access |
| ECHO | When ON, echoes typed characters back to terminal |
| HELP | Display all available commands |
| INTFACE | Select NEWUSER or TERMINAL command set, or other modes (HOST, BBS, KISS, XKISS, MODEM, GPS) |
| K | Same as CONVERS |
| MHEARD | Display list of stations recently heard |
| MONITOR | When ON, display monitored packets |
| MYCALL | Set the TNC callsign |
| MYPBBS | Set callsign for the personal mailbox |
| PBBS | Set size of the Personal BBS |
| RESET | Perform a soft reset |
| STATUS | Display current stream and link status |
| TXDELAY | Set time delay between PTT and beginning of data |
| UNPROTO | Set destination and digipeaters for unconnected packets |
| VERSION | Display current EPROM firmware version number |

### Using NEWUSER Commands

**Check version number:** Type `VERSION` (or `V`) at the `cmd:` prompt.

**Get help:** Type `HELP` followed by a command name. Type `?` for all available commands.

**View parameter value:** Type the command name and press ENTER.

**Change a parameter:** Type the command name, a space, then the new value.

### Connect to Your Mailbox

This is an internal connect — no radio required.

```
cmd: CONNECT NØKN-1
cmd:*** CONNECTED to NØKN-1
[KPC3P-9.1-HM$]
47500 BYTES AVAILABLE IN 15 BLOCK(S)
ENTER COMMAND: B,J,K,L,R,S, or Help>
```

To disconnect: press `<Ctrl+C>` to return to Command Mode, then type `DISCONNE`.

### Monitor Communications From Nearby Stations

- Set MONITOR to ON
- Disconnect from any other station
- Received packets appear on screen:

```
NØKN>KBØNYK:
Hi Mike. How are you today?
```

> VHF packet activity in the US is typically on 2 meters, with 145.010 MHz being the most common frequency at 1200 baud.

### Communicate Directly with a Nearby Station

```
cmd: CONNECT KBØNYK
```

To use digipeaters:
```
cmd: CONNECT KBØNYK VIA WØXI,NØGRG
```

After connecting, the TNC switches to CONVERS mode. Type your message and press ENTER to send. Press `<Ctrl+C>` then `D` (DISCONNE) to end the session.

---

## Modes of Operation

### Packet Mode of Operation

#### Command Mode

The TNC is in Command Mode when first powered on or after reset. Prompt: `cmd:`

Default command character to return to Command Mode: `<Ctrl+C>`

#### Connected vs. Unproto

**Connected Mode:** Packets are sent to a specific station with acknowledgments and retries. Virtually error-free communication.

**Unproto Mode:** Packets sent without acknowledgment or retries. Used for CQ, beacons, informal round table chats.

#### Digipeating

DIGIPEAT is defaulted ON, making any TNC a potential relay station (digipeater). Any packet received with MYCALL, MYALIAS, or MYNODE in the digipeat list will be retransmitted.

Example monitored output showing digipeaters:
```
NØKN>KBØNYK, IAH*,LAG,AUS:
Hi there
```
The `*` beside IAH indicates the station you're hearing. Use MYALIAS to set a mnemonic alias.

#### Multi-Connects

The KPC-3 Plus supports 26 streams on its single port.
- MAXUSERS: sets maximum simultaneous connections
- USERS: sets how many may be used for incoming connects
- STREAMSW character (default `|`) followed by a letter designates which stream to switch to

#### Timing Parameters

| Parameter | Description |
|---|---|
| TXDELAY | Key-up delay (10ms increments) — allows radio to reach full power before data |
| DWAIT | Delay before transmitting non-digipeat packets (10ms increments) |
| PERSIST | Used with SLOTTIME for collision avoidance (0–255) |
| SLOTTIME | Time between persistence algorithm checks (10ms increments) |
| FRACK | Time to wait for acknowledgment before retry (1-second increments) |

**FRACK with digipeaters:** `FRACK * ((2 * n) + 1)` seconds, where n = number of digipeaters.

#### AX.25 Level 2 Version 1 vs. Version 2

**Version 1 (AX25L2V2 OFF):** Retransmits entire packet if not acknowledged. Disconnects if RETRY count exceeded.

**Version 2 (AX25L2V2 ON, default):** Sends a POLL first to determine if the packet was received before retransmitting. If RELINK is ON, attempts to reconnect if RETRY is exceeded.

#### Flow Control

**Software Flow Control:** Uses `<Ctrl+S>` (XOFF) to stop and `<Ctrl+Q>` (XON) to restart data flow on the TXD/RXD lines.

| Command | Default | Description |
|---|---|---|
| XFLOW | ON | Enable software flow control |
| XOFF | $13 (Ctrl+S) | Character TNC sends to stop computer input |
| XON | $11 (Ctrl+Q) | Character TNC sends to restart computer input |
| STOP | $13 (Ctrl+S) | Character TNC expects to stop sending |
| START | $11 (Ctrl+Q) | Character TNC expects to restart sending |

**Hardware Flow Control:** Monitors RTS and CTS pins. TNC holds CTS high as long as it can receive data, pulls low when buffer full. Computer monitors RTS.

#### Convers Mode vs. Transparent Mode

**Convers Mode special characters:**

| Command | Default | Description |
|---|---|---|
| SENDPAC | Ctrl+M | Causes a packet to be formed |
| DELETE | Ctrl+H | Backspace character |
| REDISPLAY | Ctrl+R | Redisplays the keyboard buffer |
| CANLINE | Ctrl+X | Cancels a line |
| STOP | Ctrl+S | Stops output from TNC to computer |
| PASS | Ctrl+V | Pass a special character |

**Transparent Mode:** Designed for file transfers. All characters are data. SENDPAC has no meaning. Packets formed by PACTIME timer. All monitor commands are treated as OFF.

**Exiting Transparent Mode** (assuming CMDTIME = 1 second):
1. Wait at least 1 second
2. Type `<Ctrl+C>`
3. Within 1 second, type a second `<Ctrl+C>`
4. Within 1 second, type a third `<Ctrl+C>`
5. Wait 1 second — `cmd:` prompt appears

### Remote Access to Your TNC

Set RTEXT to a password string and MYREMOTE to a unique callsign. When a station connects to MYREMOTE, the TNC sends three lines of numbers. The user must decode one line using RTEXT character positions to gain access.

**Security notes:**
- Three failed attempts disables MYREMOTE for 15 minutes
- Disconnecting during password entry also triggers the 15-minute penalty
- Extreme caution: any command can be changed remotely
- Response to DISPLAY command is limited to 300 characters remotely

---

## PBBS (Personal Mailbox)

### Introduction

Your TNC includes a Personal Bulletin Board System (PBBS) — a mailbox capable of storing and forwarding messages. It is compatible with large community bulletin board systems (RLI, MBL, etc.) and supports forwarding of Bulletins, Private mail, and NTS traffic.

### Using Your PBBS

Connect to the PBBS callsign (default: your MYCALL with -1 SSID):

```
cmd: CONNECT NØKN-1
*** CONNECTED to NØKN-1
[KPC3P-9.1-HM$]
475000 BYTES AVAILABLE IN 15 BLOCK(S)
PTEXT would be here (if any)
ENTER COMMAND: B,J,K,L,R,S, or Help >
```

The SID format: `[KPC3P-9.1-HM$]` = unit name (KPC3P), version (9.1), feature set (H = hierarchical forwarding, M = message ID, $ = BID support).

### PBBS Commands

| Command | Description |
|---|---|
| `B(ye)` | Disconnect from PBBS |
| `E(dit) n [BPTYNFH] [>tocall] [<fromcall] [@BBS] "old" "new"` | Edit message headers (SYSOP only) |
| `H(elp)` | Display help menu |
| `J(heard)` | List stations recently heard (with date/time) |
| `J(heard) S(hort)` | List station callsigns only |
| `J(heard) L(ong)` | Include digipeaters and destination callsigns |
| `L(ist) [x [y]] [;]` | List messages you may read. Optional start (x) and end (y) numbers. `;` shows @BBS and BID. |
| `L(ist) <\|> call [;]` | List messages to (`>`) or from (`<`) a specific callsign |
| `LB [;]` | List all BULLETINS |
| `LC [cat [;]]` | List TO fields of bulletins, or full headers for a specific category |
| `LL n [;]` | List most recent n messages |
| `LM(ine) [;]` | List messages addressed to you |
| `LO [+\|-]` | Change listing order (+ = oldest first, - = newest first) |
| `LT [;]` | List all TRAFFIC messages |
| `K(ill) n` | Delete message number n |
| `KM(ine)` | Delete read messages addressed to you |
| `NL n` | Set number of lines printed before pausing (Q=quit, C=continuous, RETURN=more) |
| `R(ead) n` | Read a specific message |
| `RH n` | Read message with full headers (routing lines) |
| `RM(ine)` | Read all unread messages addressed to you |
| `S(end) call` | Send a PRIVATE message (same as SP) |
| `SB cat` | Send a BULLETIN |
| `SP call` | Send a PRIVATE message |
| `ST zip` | Send NTS traffic message |
| `U(sers)` | Display currently connected users |

### Sending Messages

**Command syntax:**
```
S    call   [@ bbcall[.haddr]]  [$ mid]
SP   call   [@ bbcall[.haddr]]  [$ mid]
ST   zip    [@ location[.haddr]]
SB   cat    [@ location[.haddr]] [$ bid]
```

**Examples:**
```
SP WB5BBW @ W5AC.#STX.TX.USA.NOAM
ST 88030 @ NTSNM
SB RACES @ ALLUS $RACESBUL.010
```

### Listing Messages

Messages display in format:

```
MSG# ST   SIZE  TO     FROM     DATE                SUBJECT
6    B     45   KEPS   W3IWI   12/19/91 09:37:11   2 Line Element set
```

**Status codes:**
- Type: B=Bulletin, T=NTS traffic, P=Personal
- Second character: F=Forwarded, H=Held, N=Not forwarded/not read, Y=Read

### Editing Message Headers

Available to SYSOP or keyboard user. Edit type, status, to/from callsigns, @BBS field, and subject text.

Example:
```
e 2 N >NØGRG
e 2 "afternoon" "morning"
```

### Hierarchical Addresses

Format: `STATE.COUNTRY.CONTINENT` (e.g., `RI.USA.NOAM`)
Set with: `HTEXT RI.USA.NOAM`

> Note: Your PBBS will not forward or reverse forward unless HTEXT is set.

### Advanced PBBS Configuration

| Command | Description |
|---|---|
| MYPBBS | Set PBBS callsign (default: MYCALL with -1 SSID) |
| PBBS n | Set PBBS size in kbytes. Causes soft reset if changed. |
| PBUSERS | Maximum simultaneous connects to PBBS |
| CMSG PBBS | Automatically route connects to PBBS |
| PTEXT | Greeting message sent to connecting users |
| PBPERSON | When ON, only accept messages to MYCALL, MYPBBS, or PBLIST |
| PBKILLFW | When ON, delete private/traffic messages after forwarding |
| PBHEADER | When ON, store routing headers (R: lines) in messages |
| PBHOLD | When ON, hold over-radio messages for SYSOP review |
| PBLO | Control listing order (OLD/NEW) and whether users can change it (FIXED/VARIABLE) |
| PBFORWRD | Schedule automatic forwarding to another BBS |
| PBREVERS | When ON, request reverse forward after initiating forward |
| HTEXT | Set hierarchical address for forwarding |

### Remote SYSOP Access

Connect to PBBS then issue SYSOP command. The TNC sends three sets of numbers to decode using RTEXT.

### Routing Lines

BBS systems include routing lines beginning with `R:` showing the complete path a message has taken. Required by FCC for traceability.

To view full routing: use `RH n` instead of `R n`.

---

## GPS NMEA Interfacing

### Overview

Most Kantronics TNCs support GPS mode for interfacing with GPS devices using the NMEA 0183 interface standard. The TNC can:
- Receive NMEA sentences from GPS units
- Store them in up to four LT (Location Text) buffers
- Retransmit them as beacons at configurable intervals
- Update the TNC clock to UTC from satellite data
- Store beacons in a tracking buffer (LTRACK) for later retrieval

### GPS Equipment Requirements

- A transceiver and antenna
- A Kantronics TNC supporting NMEA 0183
- A GPS unit with NMEA interface (RS232 compatible data port)

### Cabling a GPS Unit to a Kantronics TNC

Minimum two wires required:
- GPS "NMEA-" (signal ground) → pin 7 of TNC serial port
- GPS "NMEA+" (data output) → pin 2 of TNC serial port

Optional third wire (for GPS that accepts commands):
- TNC pin 3 → GPS data input pin

> Warning: The TNC serial ports are RS232 (±8 V signals). Verify your GPS unit can handle these voltages before connecting.

### Alternate GPS Input (Firmware 8.3+)

Pin 2 on the Radio port can serve as a GPS input, enabled with the GPSPORT command.
- Signal ground: pin 6 or pin 9 (if jumpers configured)
- If GPSPORT is active, the XCD (external carrier detect) function on pin 2 is unavailable

### Configuring a TNC for GPS Operation

1. Set GPSHEAD to capture specific NMEA sentences into LT buffers
2. Set BLT for beacon intervals
3. Set LTP for destination callsign and digipeater path
4. Set ABAUD to match GPS unit baud (typically 4800)
5. Optionally configure LTRACK for tracking buffer

**Example configuration:**
```
GPSHEAD 1 $GPGGA       (store $GPGGA in LT buffer 1)
LTP 1 GPS via DIGI     (transmit to GPS destination via DIGI)
BLT 1 EVERY 00:30:00   (beacon every 30 minutes)
LTRACK 5 LT1 LT2       (5 kbyte tracking buffer storing LT1 and LT2)
```

### GPS Operations

**Starting GPS Mode:**
```
INTFACE GPS
RESET (or power off/on)
```

**Exiting GPS Mode:**
Send three `<Ctrl+C>` characters from a terminal. The TNC resets and sets INTFACE to TERMINAL.

> Hint: Set your computer RS232 baud to match TNC ABAUD before sending the exit sequence.

### Other GPS Features

**Slotted Beacons:** Use BLT START parameter to assign specific transmission times to stations, avoiding collisions.

```
BLT 1 EVERY 00:30:00 START 00:00:01
```

**Tracking without Beacons:**
```
LTP 1 NONE
```
Data stored in LTRACK buffer without transmitting.

**Remote Access during GPS Mode:** Connect to MYREMOTE callsign and use RPRINT to send strings to the attached GPS unit.

**Manual LT buffers:**
```
LT 1 This is ltext buffer number 1
```

### GPS Command Summary

| Command | Description |
|---|---|
| `BLT n {EVERY\|AFTER} hh:mm:ss [START hh:mm:ss]` | Set beacon interval for LT string n (1–4) |
| `GPSHEAD n string` | Determine which NMEA sentences stored in LT buffer n |
| `GPSINIT string` | String sent to GPS unit at power-up |
| `LT n text` | Fill LT buffer n with text |
| `LTP n dest [via call1[,call2,...]]` | Set destination and path for LT transmissions |
| `LTRACK n [LT1] [LT2] [LT3] [LT4] [SYSOP] [TIME]` | Allocate tracking buffer memory |
| `RPRINT text` | Send text string to device attached to RS232 port |

### Advanced GPS (APRS) Digipeating

Kantronics TNCs support UI digipeating commands for GPS/APRS position reporting:

| Command | Description |
|---|---|
| UIDIGI | Set up to 4 aliases for special digipeating. Replaces alias with MYCALL in digipeated frame. |
| UIFLOOD | Multi-hop digipeating using a single address. Decrements SSID with each hop. Optional duplicate suppression. |
| UITRACE | Like UIFLOOD but inserts MYCALL in each digipeated frame, creating a traceable path. |
| UIDWAIT | When ON, applies slottime/persist delay to special digipeat packets |
| UIDUPE | Timer for UI duplicate checking (0–255 seconds) |

> Digipeater priority: UIDIGI > UIFLOOD > UITRACE > MYCALL > MYNODE > MYALIAS

#### GPS Bibliography

- Bruninga, Bob, WB4APR. "Automatic Packet Reporting System (APRS)." 13th ARRL Digital Communications Conference Proceedings, 1994.
- Horzepa, Stan. "Getting On Track with APRS." ARRL, 1996.
- "NMEA 0183 ASCII Interface Standard" (version 2.0). NMEA, P.O. Box 50040, Mobile, AL 36605.

---

## KA-Node

### Overview

The KA-Node is a packet networking node built into the KPC-3 Plus firmware. When enabled, your station functions as:
- A **digipeater** (relay with end-to-end acknowledgment)
- A **node** (local acknowledgment between links, more efficient than digipeating)

Unlike full-featured nodes (NET/ROM, X1J, K-Net), the KA-Node is "silent" — it doesn't automatically exchange routing data with adjacent nodes. Users must know the path to connect through it.

**Advantage over digipeating:** Each link in a KA-Node path handles its own error checking. A weak single link doesn't cause the entire chain to retry.

### Configuring Your KA-Node

Key commands:
- `NUMNODES n` — allocate circuits (each uses ~4.3 kbytes RAM)
- `MYNODE xxxxxx-n` — set node callsign (must differ from MYCALL, MYALIAS, MYPBBS, MYREMOTE)
- `NDWILD` — when ON, accepts connects to any SSID of MYNODE callsign
- `KNTIMER` — disconnect circuit after n minutes of no activity (default 15; 0 = disabled)

### Using a KA-Node

Connect to the node callsign:
```
cmd: CONNECT LAW
*** CONNECTED TO LAW
### CONNECTED TO WILD NODE LAW (NØGRG) CHANNEL A
ENTER COMMAND B,C,J,N,X, or Help ?
```

**You are in CONVERS mode. Commands you type are interpreted by the KA-Node.**

### KA-Node Commands

| Command | Description |
|---|---|
| `ABORT` | Abort a connect/xconnect request (must be first entry after connect command) |
| `Bye` | Disconnect from node |
| `Connect callsign [Stay]` | Connect to another station or node. STAY keeps you connected to the node if the remote station disconnects. |
| `Help` | Display available commands |
| `Jheard [Short\|Long]` | Display node's MHEARD log |
| `Nodes [Short\|Long]` | List known KA-Nodes and other node types |
| `Xconnect callsign` | Cross-connect to station on opposite port (multi-port TNCs only) |

### STAY Option

Using `C call STAY`, if the remote station disconnects, you remain connected to the KA-Node with the `###DISCONNECTED BY (call) AT NODE (MYNODE)` message and can issue another connect without rebuilding the entire path.

### Automatic Disconnect

If a circuit has no activity for KNTIMER minutes, the node disconnects both sides automatically.

---

## Introduction to Basic Packet Networking

A network node is a "collection point" in a packet network. Nodes:
- Operate at high data rates (typically 9,600 or 19,200 baud for backbone)
- Provide automatic routing to other nodes
- Increase throughput by handling acknowledgments locally (not end-to-end)
- Allow users on low-speed LANs (1200 baud) to access the high-speed backbone

**NET/ROM** was the first de facto networking protocol (late 1980s). Derivatives include TheNET, TheNET Plus, X1J, and G8BPQ.

---

## K-Net Network Node

### Quick Start

1. Set NETALIAS (mnemonic for location, e.g., SUTNE for Sutton, Nebraska)
2. Set NETCALL (node callsign, must differ from all other callsigns in the TNC)

```
cmd: NETALIAS SUTNE
cmd: NETCALL KA0DNV-1
```

Setting NETCALL causes a soft reset and allocates memory.

Display current K-Net settings:
```
cmd: DISPLAY N
NETBUFFS 32
NETCIRCS 5
NETDESTS 25
NETLINKS 10
NETROUTE 5
NETUSERS 5
```

### K-Net Node Commands

#### Basic Node Parameters

| Command | Default | Range | Description |
|---|---|---|---|
| NETBUFFS | 32 | 1–255 | Number of node buffers (each uses 320 bytes RAM) |
| NETCIRCS | 5 | 1–64 | Maximum network circuits (each uses 50 bytes RAM) |
| NETDESTS | 25 | 1–255 | Maximum destination nodes in nodes table |
| NETLINKS | 10 | 1–64 | Maximum uplinks + downlinks + crosslinks (each uses 130 bytes RAM) |
| NETROUTE | 5 | 1–32 | Maximum neighbor nodes in routes table (each uses 39 bytes RAM) |
| NETUSERS | 5 | 0–26 | Maximum uplinks and downlinks from node |
| IDINT | 10 | 0–255 | Node ID packet interval in minutes (0 = disabled) |
| NODESINT | 60 | 0–255 | Node broadcast interval in minutes |
| MINQUAL | 70 | 0–255 | Minimum quality to add destination node to table |
| QUALITY | 255/70 | 0–255 | Default quality for new neighbor nodes (Port 0 = RS232, Port 1 = 1200 baud radio) |
| OBSINIT | 5 | 0–255 | Initial obsolescence count for destination node |
| OBSMIN | 4 | 1–255 | Minimum obsolescence count to include node in broadcasts |

#### L3/L4 Transport Parameters

| Command | Default | Range | Description |
|---|---|---|---|
| L3TTL | 25 | 0–255 | Max hops a packet may travel through nodes |
| L4DELAY | 5 | 1–60 | Seconds before returning L4 ack (allows piggybacking) |
| L4LIMIT | 900 | 0–65,535 | No-activity timeout in seconds on a node crosslink |
| L4N2 | 3 | 1–127 | L4 retry count between nodes |
| L4T1 | 120 | 5–600 | Seconds to wait before resending L4 data packet |
| L4WINDOW | 4 | 1–127 | Maximum outstanding L4 frames per circuit |

#### Node Table Management Commands

| Command | Description |
|---|---|
| `ADDNODE [alias:]call port neighbor [via digi1[,digi2]] quality [obscnt]` | Add/modify destination node. obscnt=0 makes it permanent. |
| `ADDROUTE port call [via digi1[,digi2]] quality [!]` | Add/modify neighbor node. `!` toggles locked status. |
| `DELNODE [alias:]call port neighbor` | Delete destination node |
| `DELROUTE port call quality` | Delete neighbor node from routes table |
| `NODES [* \| alias \| call]` | List known destination nodes. Specify alias/call to see best routes. |
| `ROUTES` | List neighbor nodes with quality, destination count, route status |
| `LINKS` | List current AX.25 links in the node |
| `STATS` | Show level 3 and level 4 activity statistics |

#### Node Message Commands

| Command | Default | Description |
|---|---|---|
| `CTEXT text` | blank | Text sent to users connecting to node alias |
| `INFO text` | blank | Text sent when user issues INFO command |
| `PORTS text` | blank | Text sent when user issues PORTS command |

#### User Access Commands

| Command | Description |
|---|---|
| `BBS [/S]` | Connect user to PBBS. /S = stay connected to node after BYE. |
| `BYE` | Disconnect user from node |
| `CONNECT [call\|alias] [/S]` | Connect to another node or user |
| `CQ [text]` | Place user in CQ mode for 15 minutes |
| `CQBC ON\|OFF` | Control whether CQ broadcasts are transmitted (default ON) |
| `HELP` | Show all commands |
| `MHEARD [S\|L]` | List recently heard stations |
| `SYSOP` | Remote sysop access using RTEXT password |
| `USERS` | List currently connected users and buffer availability |

### Node Stacking

Multiple K-Net nodes connected via serial ports, creating a multi-port network node.

**Two-port serial cable wiring:**

| KPC-3 Plus 1 | KPC-3 Plus 2 |
|---|---|
| Pin 1 (Frame ground) | Pin 1 |
| Pin 2 (Transmit data) | Pin 3 (Receive data) |
| Pin 3 (Receive data) | Pin 2 (Transmit data) |
| Pin 7 (Signal ground) | Pin 7 |

**Configuration:**
- Give each TNC a unique NETALIAS and NETCALL
- Set `INTFACE NET` in each TNC
- Power off and back on to activate

For more than two nodes, a **Diode Matrix** is required for RTS/CTS collision avoidance on the shared serial port. Number of diodes required: `2 * N * (N-1)` where N = number of serial ports.

### TheNET X1-J / K-Net Cross-Reference

| X1-J PARM | K-Net COMMAND |
|---|---|
| Max. Destination Node Size | NETDEST |
| Min. Auto update quality | MINQUAL |
| Neighbor default quality | QUALITY |
| RS232 default quality | QUALITY |
| Initial obsolescence count | OBSINIT |
| Min. Obs. count to broadcast | OBSMIN |
| Node broadcast interval | NODESINT |
| Initial Time-to-Live | L3TTL |
| Transport Frack timeout (sec) | L4T1 |
| Transport Retry counter | L4N2 |
| Transport Ack Delay (sec) | L4DELAY |
| Transport Window Size (frames) | L4WINDOW |
| No Activity Time Out | L4LIMIT |
| Persistence | cmd: PERSIST |
| Slot | cmd: SLOTTIME |
| Link Frack (T1) | cmd: FRACK |
| AX.25 Maxframe | cmd: MAXFRAME |
| AX.25 Retries | cmd: RETRY |
| Active Check (T3) | cmd: CHECK |
| AX.25 Digipeat | cmd: DIGIPEAT |
| ID Beacon | cmd: IDINT |
| CQ Broadcasts | CQBC |
| ACL (Access Control List) | cmd: SUPCALLS/LLIST (deny); BUDCALLS/CONLIST (allow only) |

---

## WEFAX Mode

### Overview

The KPC-3 Plus modem is compatible with the 800 Hz FSK format used for weather facsimile (WEFAX) broadcasts. A special computer program is required to receive and display WEFAX charts.

### Common WEFAX Frequencies

| Location | Frequencies (MHz) |
|---|---|
| Halifax, NS | 4.275, 6.630, 9.890, 13.510 |
| Norfolk, VA | 8.080, 10.865, 16.410 |
| San Diego, CA | 8.646, 17.410 |
| Mobile, AL | 9.158 |
| San Francisco, CA | 4.346, 8.682, 12.730, 17.151 |
| Washington, DC | 4.795, 10.185, 12.205, 14.672 |

### Tuning WEFAX Signals

WEFAX uses 800 Hz FSK with mark=1500 Hz and space=2300 Hz tones. Tune approximately 1.7 kHz below the published station frequency in USB (upper sideband) mode.

**Example:** To receive NAM on 8080 kHz, set transceiver to 8078.3 kHz USB.

### The WEFAX Command

```
WEFAX n
```

Where `n` = samples per second. For 640-dot screen and 120 lines/minute: `n = 1280`.

If the picture skews, adjust the TNC clock using `DAYTWEAK`.

ABAUD must be set to at least 5/4 the WEFAX n rate.

**Exit WEFAX:** Send `<Ctrl+C>` to the TNC.

---

## Other Modes of Operation

### Remote Sensing and Control

Two or more Kantronics TNC stations can be used for remote sensing and control:
- **Remote control:** Use MYREMOTE to issue commands to a remote TNC
- **Sense analog inputs:** Use ANALOG command to read external voltages (0–5 V, 8-bit resolution)
- **Control output voltages:** Use CTRL command to set output lines OPEN or GROUNDED; pulse outputs 100ms or 1.5s

### Modem Mode

The TNC acts as a dumb modem, passing demodulated audio directly to the RS232 port at 1200 baud, unmodified.

Enable: `INT MODEM` then power off/on.

Exit: Send three `<Ctrl+C>` characters at 1200 baud.

> Note: If RS232 CD line cycling causes data loss, set `CD EXTERNAL` before entering MODEM mode.

**NWS EMWIN:** MODEM mode can be used to copy National Weather Service emergency weather broadcasts at 1200,8,N,1. Tune to the local EMWIN VHF frequency.

### Kantronics Host Mode

Allows communication with sophisticated software (e.g., Kantronics HostMaster II+) that automatically sets INTFACE to HOST.

Exit HOST mode: Send `FEND` (ASCII 192), then `q`, then `FEND` again.

### KISS Mode

Allows the TNC to act as a modem/PAD for software implementing Phil Karn's KISS protocol (supports TCP/IP).

Enable: `INTFACE KISS` then `RESET`.

Exit KISS mode:
- Perform a hard reset, OR
- Send C0 FF C0 sequence (ALT+192, ALT+255, ALT+192 on numeric keypad), OR
- Use TCP/IP software exit command

### XKISS (Extended KISS) Mode

G8BPQ multi-drop KISS mode for connecting a G8BPQ node with multiple TNCs on the same serial port.

Commands specific to XKISS:
- `XKCHKSUM {ON|OFF}` (default OFF) — enable XKISS checksum mode
- `XKPOLLED {ON|OFF}` (default OFF) — enable XKISS polled mode

### DAMA (Slave Mode) Capacity

The KPC-3 Plus supports DAMA slave protocol for use in European packet networks. DAMA (Demand Assigned Multiple Access) reduces collisions by using a master node to poll slaves in round-robin fashion.

**Commands:**
```
DAMA {ON|OFF}      (default OFF)
DAMACHCK n         (n = 0–255, in 10-second increments; default 18)
```

When DAMA is ON, the TNC operates as a slave when connected to a DAMA master. DAMACHCK sets how long to wait for a poll before disconnecting and reverting to CSMA.

---

## Command Reference

### Introduction

Default values are stored in EPROM. Changed values are stored in battery-backed RAM and used at future power-on.

Command availability depends on current INTFACE mode.

### Format Conventions

- Full command name in CAPS
- Underlined characters indicate the minimum short-form
- Parameters in CAPS shown as they must be entered
- Parameters in lowercase indicate values to substitute
- `{ }` = grouping; `[ ]` = optional; `|` = choices
- `(n = range)` = acceptable value range
- `(n = $00 - $FF)` = hexadecimal format

### Parameter Types

- **n (range):** Any number within the range. Decimal unless noted.
- **n ($00–$FF):** Hexadecimal. Prefix with `$`. Setting to `$00` disables the function.
- **flags ChoiceA|ChoiceB:** ON/OFF or YES/NO. Some allow multiple choices.
- **callsigns xxxxxx-n:** Up to 6 characters + optional SSID (0–15). Extensions of -0 are not displayed.
- **text:** Any combination up to 128 characters. Must include at least one non-space character. Clear with `%`.

### Entering Commands

At the `cmd:` prompt, type the command name followed by any parameters, then press ENTER.

- Command names are not case-sensitive
- Minimum short-forms may not be alphabetically first — the TNC scans its list order
- `EH?` = unrecognized command; `$` marks the offending character

---

## Commands (Alphabetical)

### 8BITCONV

```
8BITCONV {ON | OFF}
default ON
```

When ON, 8-bit data transmission is allowed in Convers and Transparent modes. When OFF, the 8th data bit is stripped for all transmitted and received data. Does not affect KA-Node, digipeat, or PBBS functions.

---

### ABAUD

```
ABAUD n     (n = 0,1200,2400,4800,9600,19200)
default 0
```

Sets baud for serial RS232 port. If 0, runs AUTOBAUD routine on power-up looking for `*` character to set baud. Change TNC baud before changing computer baud, then issue RESET.

---

### ANALOG

```
ANALOG
(immediate)
```

Returns 8 A/D readings in format: `AN0/AN1/AN2/AN3/AN4/AN5/AN6/AN7` (decimal 0–255, representing 0–5 V).

| Input | Description |
|---|---|
| AN0 | External voltage from Radio Port pin 4 (J8 pos 1) or Serial Port pin 18 (J8 pos 2) |
| AN1 | External voltage from Radio Port pin 8 (J10 pos 1) or Serial Port pin 11 (J10 pos 2) |
| AN6 | Internal — RTS pin status (0 or 255) |
| AN7 | Internal — DTR pin status (0 or 255) |

As shipped, J8 and J10 are off to the side (neither position), so AN0 and AN1 will not report meaningful values without jumper configuration.

---

### AUTOLF

```
AUTOLF {ON | OFF}
default ON
```

When ON, a line feed is sent after each carriage return. Affects only data sent to terminal, not to radio.

---

### AX25L2V2

```
AX25L2V2 {ON | OFF}
default ON
```

When ON, implements AX.25 Level 2 Version 2 (auto-adapts to connecting station's version). When OFF, uses Version 1. Set OFF if digipeating through units that don't support Version 2 packets, or when using multiple digipeaters under marginal conditions.

---

### AXDELAY

```
AXDELAY n     (n = 0–255, in 10ms intervals)
default 0
```

Additional delay after TXDELAY before data is sent. Useful for packet through voice repeaters or with external linear amplifiers needing extra key-up time.

---

### AXHANG

```
AXHANG n     (n = 0–255, in 10ms intervals)
default 0
```

Repeater hang time accommodation. If the TNC has heard a packet within the AXHANG period, it won't add AXDELAY to the next key-up.

---

### BEACON

```
BEACON [EVERY | AFTER] n     (n = 0–255, in 1-minute intervals)
default EVERY 0
```

0 = OFF. EVERY = beacon every n minutes. AFTER = beacon once after n minutes of no channel activity. Content specified by BTEXT. Digipeated via UNPROTO addresses.

---

### BKONDEL

```
BKONDEL {ON | OFF}
default ON
```

When ON, DELETE key echoes backspace-space-backspace. When OFF, echoes `\`.

---

### BLT

```
BLT n {EVERY | AFTER} hh:mm:ss [START hh:mm:ss] [CLEAR]     (n = 1–4)
default EVERY 00:00:00
```

GPS beacon interval for LT buffer n. START sets first transmission time. CLEAR clears LT buffer after transmission.

---

### BREAK

```
BREAK {ON | OFF}
default OFF
```

When ON, a modem break signal returns TNC to Command Mode from Convers or Transparent mode.

---

### BTEXT

```
BTEXT text     (0–128 characters)
default (blank)
```

Content of the beacon packet data field. Clear with `%`.

---

### BUDLIST

```
BUDLIST [ON|OFF] [NONE | {+|-}call | call1,call2,...]
default OFF NONE
```

Controls which received packets are monitored. When OFF, all packets are monitored regardless of list contents. Maximum 10 callsigns.

Selective syntax: `>callsign` (packets TO), `<callsign` (packets FROM), `call1>call2` (FROM call1 TO call2), `call1<>call2` (bidirectional). Each pair counts as 2 callsigns.

---

### CALIBRAT

```
CALIBRAT
(immediate)
```

Enters calibration mode for adjusting audio drive level and equalization.

Options: M (transmit mark), S (transmit space), T (transmit square wave), R (receive), +/- (adjust XMITLVL), X (exit).

---

### CANLINE

```
CANLINE n     (n = $00–$FF)
default $18 <Ctrl+X>
```

Cancel-line character. In Convers or Command mode, cancels all keyboard input back to last carriage return.

---

### CANPAC

```
CANPAC n     (n = $00–$FF)
default $19 <Ctrl+Y>
```

Cancel-packet character. In Convers mode, cancels all keyboard input back to last SENDPAC character. Also functions as cancel-output in Command mode (second press re-enables output).

---

### CD

```
CD {INTERNAL | EXTERNAL | SOFTWARE}
default INTERNAL
```

Carrier detect method. INTERNAL = energy-based (allows shared voice/data). EXTERNAL = from external device on XCD pin. SOFTWARE = firmware detects data presence (needed for unsquelched audio; affected by equalization and SWP parameter).

---

### CHECK

```
CHECK n     (n = 0–255, in 10-second intervals)
default 0
```

Timeout to prevent hang-up on link failure. After n intervals of no activity, polls the connected station. 0 = disabled. With Version 1 (AX25L2V2 OFF), timeout initiates disconnect.

---

### CMDTIME

```
CMDTIME n     (n = 0–15, in seconds)
default 1
```

Guard time for exiting Transparent mode. Exit sequence: wait CMDTIME → type COMMAND character × 3 (each within CMDTIME of the previous) → wait CMDTIME → `cmd:` appears. If 0, only modem break exits Transparent mode (requires BREAK ON).

---

### CMSG

```
CMSG {ON | OFF | DISC | PBBS}
default OFF
```

ON = send CTEXT on connect. OFF = don't send. DISC = send CTEXT then disconnect. PBBS = send CTEXT then transfer connection to PBBS.

---

### COMMAND

```
COMMAND n     (n = $00–$FF)
default $03 <Ctrl+C>
```

Character used to return to Command Mode from Convers mode.

---

### CONLIST

```
CONLIST [ON | OFF] [NONE | {+|-}callsign | callsign1,callsign2...]
default OFF
```

When ON, only callsigns on this list can use your station for any purpose including digipeating; you can only connect to callsigns on this list. Maximum 10 callsigns.

---

### CONMODE

```
CONMODE {CONVERS | TRANS}
default CONVERS
```

Mode TNC enters automatically after a connect (if NOMODE is OFF).

---

### CONNECT

```
CONNECT call1 [VIA call2,call3,...,call9]
(immediate)
```

Establish connection. Up to 8 digipeater addresses may be specified. If CONNECT issued while connected, the path may be changed. CONNECT with no parameters displays current stream status.

---

### CONOK

```
CONOK {ON | OFF}
default ON
```

When ON, accepts incoming connect requests. When OFF, responds to connects with `<DM>` busy signal. You can still connect to your own mailbox when CONOK is OFF.

---

### CONPERM

```
CONPERM {ON | OFF}
default OFF
```

When ON, forces current stream connection to be permanent — TNC attempts to reconnect after restart. Shown as `/P` in STATUS display.

---

### CONVERS

```
CONVERS
(immediate)
```

Enter Conversational mode from Command mode. K is the same command.

---

### CPACTIME

```
CPACTIME {ON | OFF}
default OFF
```

When ON in Convers mode, packets are sent at PACTIME intervals (like Transparent mode) but with local editing and echoing features of Convers mode still active.

---

### CR

```
CR {ON | OFF}
default ON
```

When ON, the SENDPAC character is appended to packets sent in Convers mode (except when PACLEN is exceeded).

---

### CRSUP

```
CRSUP {ON | OFF}
default OFF
```

When ON, suppresses every other consecutive carriage return in received data (for compatibility with old mechanical teletypes that added double CR).

---

### CSTAMP

```
CSTAMP {ON | OFF}
default OFF
```

When ON, prints daytime stamp with CONNECTED and DISCONNECTED messages.

---

### CTEXT

```
CTEXT text     (0–128 characters)
default (blank)
```

Text sent in response to an accepted connect request when CMSG is not OFF. Clear with `%`.

---

### CTRL

```
CTRL [A | B] {n | ON | OFF | LONG | MUTE m}     (n=1-20)
(immediate)
```

Activate output line A or B (or both if not specified). n = pulse n times (~100ms each). ON = activate. OFF = deactivate. LONG = single ~1.5s pulse. MUTE = activate line when RCV LED is on for m consecutive 10ms samples. Maximum 200 mA.

---

### CWID

```
CWID [EVERY | AFTER] n     (n = 0–255, in 1-minute intervals)
default EVERY 0
```

Automatic CW identification. CWIDTEXT content sent in Morse code. 0 = disabled.

---

### CWIDTEXT

```
CWIDTEXT text     (0–15 characters)
default DE mycall
```

Text transmitted by CWID command.

---

### DAMA

```
DAMA {ON | OFF}
default OFF
```

When ON, TNC operates as DAMA slave when connected to a DAMA master. When OFF, uses standard CSMA packet mode.

---

### DAMACHCK

```
DAMACHCK n     (n = 0–255, in 10-second increments)
default 18
```

DAMA timeout. If TNC doesn't receive a poll within this time, it reverts to CSMA operation and disconnects from the DAMA master.

---

### DAYSTR

```
DAYSTR text
default mm/dd/yy hh:mm:ss
```

Sets the FORMAT of date/time display. Use lowercase m, d, y, h, s as placeholders. Three `m`s = abbreviated month name. All other lowercase instances of these letters are replaced with actual values.

**Examples:**
| DAYSTR setting | Displayed |
|---|---|
| `mm/dd/yy hh:mm:ss` | 07/16/02 12:14:22 |
| `d.m.y h:mm:ss` | 16.7.02 12:14:22 |
| `mmm d 20yy h:mm CST` | JUL 7 2002 12:14 CST |

---

### DAYTIME

```
DAYTIME yymmddhhmm[ss]
```

Sets date and time. Input format: 2 digits each for year, month, day, hour, minute, optional second. Example: January 2, 1986 at 22:30:00 → `860102223000`. Enter DAYTIME with no parameter to display current date/time.

---

### DAYTWEAK

```
DAYTWEAK n     (n = 0–15)
default 8
```

Adjusts software clock speed. Each count = 0.64 seconds per 24 hours. Increase to slow the clock, decrease to speed it up. Does not affect the optional battery-backed real-time clock (BBC).

---

### DBLDISC

```
DBLDISC {ON | OFF}
default OFF
```

When OFF, one disconnect command terminates unsuccessful connect attempts. When ON, always performs full disconnect sequence; a second D forces immediate local disconnect.

---

### DELETE

```
DELETE n     (n = $00–$FF)
default $08 <Ctrl+H>
```

Sets the delete character. Common settings: $08 (backspace) or $7F (delete key).

---

### DIGIPEAT

```
DIGIPEAT {ON | OFF | UIONLY}
default ON
```

When ON, digipeats any packet with MYCALL, MYALIAS, or MYNODE in the digipeat list. When UIONLY, only UI (unconnected information) frames are digipeated.

---

### DISCONNE

```
DISCONNE [MYPBBS | MYNODE x]     (x = KA-Node circuit)
(immediate)
```

Initiate disconnect on current stream. MYPBBS disconnects PBBS user. MYNODE x disconnects stations on specified KA-Node circuit. Entering a second D before RETRY expires forces immediate local disconnect.

---

### DISPLAY

```
DISPLAY [{A | C | G | I | L | M | N | P | T}]
(immediate)
```

Display all parameters or a selected group:

| Subclass letter | Group |
|---|---|
| A (ASYNC) | Asynchronous port parameters |
| C (CHAR) | Special TNC characters |
| G (GPS) | GPS operation parameters |
| I (ID) | ID parameters |
| L (LINK) | Packet link parameters |
| M (MONITOR) | Monitor parameters |
| N (NET) | K-Net parameters |
| P (PBBS) | Mailbox commands |
| T (TIMING) | Timing parameters |

---

### DWAIT

```
DWAIT n     (n = 0–255, in 10ms intervals)
default 0
```

Delay before transmitting to avoid collisions with digipeated packets. Digipeated packets are retransmitted without this delay (giving digipeaters priority).

---

### ECHO

```
ECHO {ON | OFF}
default ON
```

When ON, characters received from computer are echoed back. If double-printing, turn OFF. Ignored in Transparent mode.

---

### ESCAPE

```
ESCAPE {ON | OFF}
default OFF
```

When ON, escape characters ($1B) in received packets are displayed as `$` instead of `ESC`, preventing ANSI terminal control sequences from being interpreted.

---

### FILTER

```
FILTER {ON | OFF}
default OFF
```

When ON, suppresses control characters ($00–$1F, except CR and LF) in monitored packets. Does not affect data from connected stations when MONITOR/MCON is OFF.

---

### FLOW

```
FLOW {ON | OFF}
default ON
```

When ON, any keyboard character halts TNC output until current packet or command completes. Prevents received data from interfering with keyboard entry. When OFF, received data interleaves with keyboard entry (useful for split-screen terminal programs with ECHO OFF).

---

### FRACK

```
FRACK n     (n = 1–15, in 1-second intervals)
default 4
```

Time to wait for acknowledgment before retrying. With digipeaters: `FRACK * ((2*m)+1)` seconds where m = number of digipeaters. Timer starts when PTT releases and pauses when carrier is detected or TNC is transmitting.

---

### FULDUP

```
FULDUP {ON | OFF | LOOPBACK}
default OFF
```

When OFF (half duplex), carrier detect is used for collision avoidance. When ON, modem runs full duplex (useful for satellite operations). LOOPBACK = half duplex with receive circuit active (for hardware testing with loopback wire).

> Note: SMT revision of KPC-3 Plus PCB has no option for second modem chip. Only OFF is valid for this command on SMT versions.

---

### GPSHEAD

```
GPSHEAD n string     (n=1–4, string up to 8 chars)
default 1 $GPGGA (strings 2,3,4 = blank)
```

Determines which GPS NMEA sentences are stored in LT buffers. Clear a buffer: enter `GPSHEAD n` with no string.

---

### GPSINIT

```
GPSINIT string     (string up to 128 characters)
default (blank)
```

String sent to GPS unit at power-up. Use `<Ctrl+N>` at end of each sentence to send multiple sentences (TNC sends CR/LF). Clear with `%`.

---

### GPSPORT

```
GPSPORT [baud] [NORMAL | INVERTED] [CHECKSUM | NOCHECK]
default 0 NORMAL CHECKSUM
```

Enables alternate GPS input on Radio port XCD pin (pin 2). Baud: 0 (disabled), 300, 600, 1200, 2400, or 4800. NORMAL = RS232 polarity. INVERTED = opposite polarity.

> Note: Set GPSPORT to 0 when INTFACE is KISS, XKISS, GPS, or MODEM.

---

### GPSTIME

```
GPSTIME {OFF | VALID | ON} {GGA | GLL | RMC | ZDA}
default VALID RMC
```

Controls whether and how TNC updates its clock from GPS NMEA strings. OFF = don't update. VALID = only if valid bit is set in specified string. ON = always use time from specified string.

---

### HBAUD

```
HBAUD n     (n = 300, 400, 600, 1200)
default 1200
```

Radio baud rate. Independent of ABAUD (computer serial baud). All stations must use the same HBAUD. FCC rules limit maximum baud to 300 below 28 MHz.

---

### HEADERLN

```
HEADERLN {ON | OFF}
default ON
```

When ON, a carriage return is inserted between the header and text of monitored packets (header and text on separate lines). When OFF, header and data appear on the same line.

---

### HELP

```
HELP [command]
(immediate)
```

Without argument, lists all available commands. With a command name, shows a brief description. Wildcard: `HELP C*` shows all commands starting with C. Same as `?`.

---

### HID

```
HID {ON | OFF}
default ON
```

When ON, sends an ID packet every 9.5 minutes when packets are being digipeated through, routed through the KA-Node, or into the PBBS. Should be ON if digipeating, KA-Node, or PBBS is enabled.

---

### HTEXT

```
HTEXT text
default blank
```

Sets hierarchical routing information for PBBS forwarding. Enter the hierarchical portion only (e.g., `RI.USA.NOAM`), not your callsign. Required for PBBS forwarding and reverse forwarding. Clear with `%`.

---

### ID

```
ID
(immediate)
```

Transmits an identification UI packet. The MYCALL is appended with indicators: `/R` (DIGIPEAT ON), `/D` (MYALIAS), `/N` (MYNODE), `/B` (MYPBBS). Addressed to "ID" via UNPROTO addresses.

---

### INTFACE

```
INTFACE {TERMINAL|NEWUSER|BBS|KISS|XKISS|HOST|GPS|MODEM}
default NEWUSER
```

| Setting | Description |
|---|---|
| NEWUSER | Limited 22-command set for terminal/terminal emulation programs |
| TERMINAL | Full command set |
| BBS | Suppresses certain messages for compatibility with PC-based BBS software |
| KISS | KISS protocol mode |
| XKISS | G8BPQ extended KISS mode |
| HOST | Kantronics HOST mode for HostMaster II+ |
| GPS | GPS mode on power-up; parses NMEA data and manages LT buffers |
| MODEM | Mirrors radio port audio directly to RS232 port at 1200 baud |

> Note: After changing to KISS, XKISS, HOST, GPS, or MODEM, a soft RESET is required for the new mode to take effect.

---

### K

```
K
(immediate)
```

Synonymous with CONVERS. Single-keystroke entry to Convers mode.

---

### KNTIMER

```
KNTIMER n     (n = 0–255, in minutes)
default 15
```

KA-Node inactivity timeout. Disconnects both sides of a circuit after n minutes of no activity. 0 = disabled.

---

### LCOK

```
LCOK {ON | OFF}
default ON
```

When ON, no character translation occurs. When OFF, lowercase characters from TNC are translated to uppercase before output to terminal (disabled in Transparent mode).

---

### LEDS

```
LEDS {ON | OFF}
default ON
```

When OFF, disables front-panel LEDs (conserves power).

---

### LFADD

```
LFADD {ON | OFF}
default OFF
```

When ON, appends a line-feed to every carriage return received from keyboard before transmitting.

---

### LFSUP

```
LFSUP {ON | OFF}
default OFF
```

When ON, suppresses line-feed characters received from the other station.

---

### LGETCHAR

```
LGETCHAR $xx
default $05 (Ctrl-E)
```

Hot key (functional in Command or Convers mode) that outputs unformatted LT buffer strings to RS232 port and restarts BLT timers. Same as `LT RESTART`. Set to 0 to disable.

---

### LLIST

```
LLIST [ON | OFF] [NONE | {+|-}callsign | callsign1,callsign2...]
default OFF
```

When ON, the TNC will NOT recognize packets from callsigns on this list for any purpose (including digipeating), and you cannot connect to them. Maximum 10 callsigns.

---

### LT

```
LT {n [text] | RESTART}     (n=1–4, text up to 128 chars)
default blank
```

Fill LT (Location Text) buffer n with text. Clear a buffer: `LT n%`. `LT RESTART` outputs all LT buffers to RS232 port unformatted and restarts BLT timers.

---

### LTP

```
LTP n dest [via call1[,call2,...]]     (n=1–4)
default GPS (for n=1–4)
```

Sets destination callsign and digipeater path for transmitting LT strings. Common destinations: GPS, APRS, LOCATE, POSIT. Up to 8 digipeaters.

---

### LTRACK

```
LTRACK n [LT1] [LT2] [LT3] [LT4] [SYSOP] [TIME]
default 0
```

Allocates n kbytes of memory for a tracking buffer storing LT messages. SYSOP = restrict access to sysop only. TIME = include timestamp. Access via PBBS LTR command.

> Note: Use full command name `LTRACK` to change the value (short form `LTR` only displays it).

---

### MALL

```
MALL {ON | OFF}
default ON
```

When ON, monitored packets include both connected and unconnected packets. When OFF, only unconnected (UI frame) packets from other stations are displayed.

---

### MAXFRAME

```
MAXFRAME n     (n = 1–7)
default 4
```

Maximum number of unacknowledged information packets outstanding at one time. TNC sends MAXFRAME packets in a single transmission if available.

---

### MAXUSERS

```
MAXUSERS n     (n = 1–26)
default 10
```

Sets maximum simultaneous connections, allocating necessary memory. Each connection uses a different stream. Changing MAXUSERS causes a soft reset and drops all existing connections.

> Note: Use full command name to change; short form `MAXU` only displays current value.

---

### MBEACON

```
MBEACON {ON | OFF}
default ON
```

Controls whether BEACON and ID packets are displayed on screen.

---

### MCOM

```
MCOM {ON | OFF}
default OFF
```

When ON (with MONITOR ON), supervisory (control) packets are also monitored. Control packet types: `<C>` (connect), `<D>` (disconnect), `<DM>` (disconnected mode), `<UA>` (unnumbered acknowledge).

---

### MCON

```
MCON {ON | OFF}
default OFF
```

When OFF and connected, only packets addressed to you are displayed. When ON, all eligible packets are displayed regardless of connection state.

---

### MHEARD

```
MHEARD [SHORT | LONG | CLEAR]
(immediate)
```

Display list of stations heard. `*` = heard through digipeater. SHORT = callsigns only. LONG = includes full path. CLEAR = clear the list.

> Note: Disabled when PASSALL is ON.

---

### MHEADER

```
MHEADER {ON | OFF}
default ON
```

When ON, packet headers are displayed for all monitored packets. When OFF, only data is output (only I and UI frames, which have data, are shown).

---

### MONITOR

```
MONITOR {ON | OFF}
default ON
```

Master switch for all monitoring. When ON, unconnected packets are monitored (subject to SUPLIST, BUDLIST, CONLIST, LLIST). When OFF, only data from stations directly connected to you is shown. All monitor functions are disabled in Transparent mode.

---

### MRESP

```
MRESP {ON | OFF}
default OFF
```

When ON (with MONITOR and MCOM ON), monitored packets include AX.25 response packets: `<FRMR>`, `<REJr>`, `<RNRr>`, `<RRr>`, `<Isr>`. `<` = Version 1, `<<` = Version 2. Uppercase = command/poll, lowercase = response.

---

### MRPT

```
MRPT {ON | OFF}
default ON
```

When ON, full digipeat list is displayed for monitored packets (digipeating station marked with `*`). When OFF, only from/to callsigns are displayed.

---

### MSTAMP

```
MSTAMP {ON | OFF}
default OFF
```

When ON, time stamps monitored packets (requires MONITOR ON; and MCON ON if connected).

---

### MXMIT

```
MXMIT {ON | OFF}
default ON
```

When ON, transmitted packets are displayed as monitored data on your terminal (subject to MONITOR, MCOM, MCON, MRESP, TRACE, MSTAMP, HEADERLN, 8BITCONV, FILTER settings).

---

### MYALIAS

```
MYALIAS xxxxxx-n     (n = 0–15)
default (blank)
```

Sets a mnemonic alias for digipeating (e.g., a location name like LAW-3). Must differ from MYCALL, MYNODE, MYPBBS, MYREMOTE. Disable with `MYALIAS %`.

---

### MYCALL

```
MYCALL xxxxxx-n     (n = 0–15)
```

Sets the TNC callsign. First time out of the box or after hard reset, the TNC prompts for this. Setting MYCALL automatically computes MYPBBS, MYNODE, and CWIDTEXT (adding SSIDs); changing MYCALL at `cmd:` does NOT update those other values.

---

### MYDGPS

```
MYDGPS xxxxxx-n     (n = 0–15)
default (blank)
```

In GPS mode only, if a UI packet is received addressed to the MYDGPS callsign, the data is output on the RS232 port (differential GPS support).

---

### MYDROP

```
MYDROP n     (n = 0–15)
default 0
```

Sets the KISS address of the radio port. KISS frames with the upper nibble of the command byte matching this value will address this KPC-3 Plus.

---

### MYNODE

```
MYNODE xxxxxx-n     (n = 0–15)
default mycall-7
```

Enables the KA-Node. Must differ from MYCALL, MYALIAS, MYPBBS, MYREMOTE. Also requires NUMNODES set to non-zero. Disable by setting MYNODE same as MYCALL or setting NUMNODES 0.

---

### MYPBBS

```
MYPBBS xxxxxx-n     (n = 0–15)
default mycall-1
```

Sets the callsign of your Personal Packet Mailbox. Must differ from MYCALL, MYALIAS, MYNODE, MYREMOTE.

---

### MYREMOTE

```
MYREMOTE xxxxxx-n     (n = 0–15)
default (blank)
```

Sets callsign for remote TNC access. Must differ from MYCALL, MYALIAS, MYNODE, MYPBBS. Also requires RTEXT to be set.

---

### NDHEARD

```
NDHEARD [SHORT | LONG | CLEAR]
(immediate)
```

Displays list of nodes (KA-Nodes, K-Net, TheNet, NET/ROM, G8BPQ) whose ID packets have been heard. Format: `ALIAS (CALLSIGN)` for NET/ROM-type, `MYNODE (MYCALL)` for KA-Nodes. `*` = heard via digipeater.

---

### NDWILD

```
NDWILD {ON | OFF}
default OFF
```

When ON, KA-Node accepts connect requests to any SSID of the MYNODE callsign (if that SSID isn't assigned to another TNC function).

---

### NETALIAS

```
NETALIAS xxxxxx     (up to 6 alphanumeric characters)
default (blank)
```

Optional mnemonic for K-Net node location. Changing does not cause soft reset.

---

### NETBUFFS — see K-Net Node Commands section

### NETCALL

```
NETCALL xxxxxx[-n]
default (blank)
```

K-Net node callsign. Required for K-Net operation. Must differ from all other TNC callsigns. Enter `%` to clear nodes and routes tables (without changing node parameters). Changing causes soft reset.

---

### NEWMODE

```
NEWMODE {ON | OFF}
default ON
```

When ON, TNC returns to Command Mode when the station on the current stream disconnects. When OFF, disconnect does not change mode.

---

### NOMODE

```
NOMODE {ON | OFF}
default OFF
```

When OFF, TNC enters CONMODE after a connection. When ON, TNC stays in Command Mode after connecting.

---

### NTEXT

```
NTEXT text     (up to 128 characters)
default (blank)
```

Customized text sent with the KA-Node initial sign-on message. Clear with `%`.

---

### NUMNODES

```
NUMNODES n     (n = 0–26, depending on available RAM)
default 0
```

Sets number of KA-Node circuits (~4 kbytes RAM each). Changing causes soft reset. Use full command name to change; short form `NU` only displays.

---

### PACLEN

```
PACLEN n     (n = 0–255)
default 128
```

Maximum packet data length. TNC automatically sends a packet when input bytes reach n. 0 = 256 bytes.

---

### PACTIME

```
PACTIME [EVERY | AFTER] n     (n = 0–255, in 100ms intervals)
default AFTER 10
```

Controls packet formation rate in Transparent mode (or Convers mode when CPACTIME ON). AFTER = form packet after n*100ms of no input. EVERY = form packet every n*100ms.

---

### PASS

```
PASS n     (n = $00–$FF)
default $16 <Ctrl+V>
```

In Convers mode, precede any special character with PASS to send it as data rather than interpret it as a control character.

---

### PASSALL

```
PASSALL {ON | OFF}
default OFF
```

When ON, attempts to display corrupted packets (with correct beginning and ending flags but failed CRC check). MHEARD and NDHEARD logging are disabled when PASSALL is ON.

---

### PBBS

```
PBBS [n | STATUS]
default 5 (32K RAM), 100 (128K RAM), 480 (512K RAM)
```

Allocates n kbytes to PBBS. Preserves existing messages. Cannot set smaller than required for existing messages ("Messages would be lost" error). Use full command name to change; short form `PB` only displays.

---

### PBFORWRD

```
PBFORWRD [bbscall [VIA call1,...call8]] [EVERY | AFTER n]
default NONE EVERY 0
```

Schedules automatic forwarding to another BBS. EVERY n hours = periodic. AFTER = after user disconnects plus every n hours. Setting the time interval causes immediate forwarding attempt.

---

### PBHEADER

```
PBHEADER {ON | OFF}
default ON
```

When ON, stores routing headers (R: lines) in messages. When OFF, headers are discarded, saving significant message space.

---

### PBHOLD

```
PBHOLD {ON | OFF}
default ON
```

When ON, messages received over radio are automatically held for SYSOP review. Messages addressed directly to MYCALL or MYPBBS are always held regardless of this setting.

---

### PBKILLFW

```
PBKILLFW {ON | OFF}
default OFF
```

When ON, private and traffic messages are deleted from PBBS after successful forwarding. Bulletins are marked F (forwarded) and retained.

---

### PBLIST

```
PBLIST [ON | OFF] [NONE | {+|-}callsign | callsign1,callsign2...]
default OFF
```

Adds up to 10 additional callsigns treated as "mine" for the mail indicator and LMINE/KMINE/RMINE commands. SSIDs are ignored for mailbox purposes. Changing the list takes effect immediately for PBBS commands but requires a disconnect/reset to update the mail indicator.

---

### PBLO

```
PBLO [OLD | NEW] [FIXED | VARIABLE]
default NEW VARIABLE
```

Sets default message listing order and whether users can change it. OLD = oldest first, NEW = newest first. FIXED = users cannot change order with LO command. VARIABLE = users may change with LO command.

---

### PBMAIL

```
PBMAIL {ON | OFF}
default OFF
```

When ON, "YOU HAVE MAIL" is sent to terminal when new messages arrive for MYCALL.

---

### PBPERSON

```
PBPERSON {ON | OFF}
default OFF
```

When ON, PBBS only accepts messages addressed to MYCALL, MYPBBS, or PBLIST over radio. Also prevents third-party forwarding and suppresses R: lines.

---

### PBREVERS

```
PBREVERS {ON | OFF}
default ON
```

When ON, PBBS requests a reverse forward from another BBS after completing a forward. Requires HTEXT to be set.

---

### PBSIZE

```
PBSIZE n     (n = 0–65535)
default 0
```

Maximum size (bytes) of new messages. 0 = no maximum.

---

### PBUSERS

```
PBUSERS n     (n = 1–10)
default 1
```

Maximum simultaneous connects to PBBS. Causes soft reset if changed.

---

### PERSIST

```
PERSIST n     (n = 0–255)
default 63
```

Used with SLOTTIME for collision avoidance. After SLOTTIME expires, TNC generates random number 0–255. If random number ≤ PERSIST, TNC transmits; otherwise waits another SLOTTIME. Probability of transmitting per slot = (PERSIST+1)/256.

---

### PHEARD

```
PHEARD [CLEAR]
(immediate)
```

Displays list of last 10 stations that have connected to your PBBS, with connect/disconnect times. CLEAR removes all entries.

---

### PID

```
PID {ON | OFF}
default OFF
```

When OFF, only AX.25 packets (PID $F0) are displayed. When ON, all packets are displayed (TCP/IP = $CC/$CD, NET/ROM/TheNet = $CF).

---

### PMODE

```
PMODE {CMD | CONV | TRANS}
default CMD
```

Controls mode at power-up or reset. CMD = Command mode. CONV = Convers mode. TRANS = Transparent mode.

---

### PTEXT

```
PTEXT text     (up to 128 characters)
default (blank)
```

Customized text sent with PBBS sign-on message. Don't use `>` character (reserved by BBS systems). Clear with `%`.

---

### RANGE

```
RANGE a-b/c-d/e-f/g-h/i-j
default 0-255/0-255/0-255/0-255/0-255
```

Converts raw 0–255 A/D readings to any offset and scale. Example: `0-5.00` for voltage, `-40-100.0` for temperature.

---

### REDISPLA

```
REDISPLA n     (n = $00–$FF)
default $12 <Ctrl+R>
```

Character to redisplay current packet input. Shows corrected form after deletions. Also releases flow control to display any pending incoming packets.

---

### RELINK

```
RELINK {ON | OFF}
default OFF
```

With AX25L2V2 ON: When ON, TNC attempts to automatically reconnect after RETRY is exceeded. KA-Node and PBBS never reconnect regardless of this setting. No effect with AX25L2V2 OFF.

---

### RESET

```
RESET
(immediate)
```

Performs a soft reset. PBBS contents and MHEARD/NDHEARD logs are preserved. Existing connections (unless CONPERMED) are lost. Sign-on message is displayed.

---

### RESTORE

```
RESTORE DEFAULT
(immediate)
```

Reverts to factory defaults, runs AUTOBAUD routine, and erases all PBBS messages.

---

### RETRY

```
RETRY n     (n = 0–15)
default 10
```

Number of packet retries before aborting operation. Time between retries set by FRACK.

---

### RING

```
RING {ON | OFF}
default ON
```

When ON, three bell characters ($07) are sent to terminal with each incoming CONNECTED TO message.

---

### RNRTIME

```
RNRTIME n     (n = 0–255, in 10-second intervals)
default 0
```

If a connection stays in remote-device-busy state (RNR frames) for RNRTIME, disconnect. KA-Node circuits also disconnect. 0 = disabled.

---

### RPRINT

```
RPRINT text     (up to ~250 characters)
(immediate)
```

Sends text string to device attached to RS232 port (e.g., GPS unit). Intended for remote sysops to send configuration strings to attached devices.

---

### RTEXT

```
RTEXT text     (up to ~250 characters)
default (blank)
```

Password string for MYREMOTE access and remote SYSOP functions in PBBS. When a station connects, TNC sends three random number sets. The user must decode one set by substituting RTEXT character positions. Case and spaces are significant. Three failed attempts disables MYREMOTE for 15 minutes.

---

### SCREENL

```
SCREENL n     (n = 0–255)
default 0
```

Inserts CR to terminal after n characters. 0 = disabled.

---

### SENDPAC

```
SENDPAC n     (n = $00–$FF)
default $0D <Ctrl+M>
```

Character that forces packet to be sent in Convers mode.

---

### SLOTTIME

```
SLOTTIME n     (n = 0–255, in 10ms intervals)
default 10
```

Time between persistence algorithm checks (100ms at default). Used with PERSIST for collision avoidance.

---

### START

```
START n     (n = $00–$FF)
default $11 <Ctrl+Q>
```

Character computer sends to TNC to restart output. $00 = hardware flow control only.

---

### STATUS

```
STATUS [LONG]
(immediate)
```

Displays free bytes in RS232 input buffer, current I/O stream, and connected streams. LONG shows status of all streams, PBBS, KA-Node circuits, and remote access. `/P` suffix = permanent connection (CONPERM). `#n(p)` = n bytes in p unacknowledged packets.

---

### STOP

```
STOP n     (n = $00–$FF)
default $13 <Ctrl+S>
```

Character computer sends to TNC to stop output. $00 = hardware flow control only.

---

### STREAMCA

```
STREAMCA {ON | OFF}
default OFF
```

When ON (with MONITOR OFF / MCON OFF), displays callsign of connected station alongside stream identifier. Useful for multi-stream operation.

---

### STREAMEV

```
STREAMEV {ON | OFF}
default OFF
```

When OFF, stream indicator shown only when stream changes. When ON, stream indicator shown on every incoming packet (only for packets addressed to you with MCON OFF).

---

### STREAMSW

```
STREAMSW n     (n = $00–$FF)
default $7C (|)
```

Character used to switch streams. Type STREAMSW character immediately followed by the stream letter (A–Z) or port/stream designation. No ENTER key needed.

> Note: If set to `$` (dollar sign), hex value entry requires PASS prefix.

---

### SUPLIST

```
SUPLIST [ON|OFF] [NONE | {+|-}call | call1,call2,...]
default OFF NONE
```

When ON, suppresses display of packets to/from callsigns on this list. Selective syntax same as BUDLIST. Maximum 10 callsigns.

---

### SWP

```
SWP u,d,t
default 17,17,108
```

Software carrier detect parameters. `u` = increment on valid transitions, `d` = penalty on mid-bit transitions, `t` = threshold to set carrier detect active. Carrier detect goes false when counter drops to 0.

---

### TELEMETRY

```
TELEMETRY n     (n = 0–255, in 10-second intervals)
default 0
```

Sends telemetry beacon every n*10 seconds to BEACON (via UNPROTO path). 0 = disabled.

Data format: `T#nnn,an0,an1,an2,an3,an5,bbbbbbbb` where nnn = counter, an0–an5 = analog readings, bbbbbbbb = PORT E binary status.

---

### TRACE

```
TRACE {ON | OFF}
default OFF
```

When ON, all received frames are displayed in full hexadecimal including all header information.

---

### TRANS

```
TRANS
(immediate)
```

Enter Transparent mode from Command mode. Exit with modem break (if BREAK ON) or three-`<Ctrl+C>` sequence.

---

### TRFLOW

```
TRFLOW {ON | OFF}
default OFF
```

When ON in Transparent mode, TNC responds to software flow control (START/STOP characters) from computer. When OFF, hardware flow control (RTS/CTS wired) is required.

---

### TRIES

```
TRIES [n]     (n = 0–15)
```

Displays and optionally resets the current retry count on the current stream. Example: If RETRY=10 and TRIES shows 8, entering `TRIES 3` allows 7 more attempts.

---

### TXDELAY

```
TXDELAY n     (n = 0–255, in 10ms intervals)
default 30
```

Transmitter key-up delay (300ms at default). Time between applying PTT and sending data. Flags are sent during this delay. Too short = beginning of packet lost; too long = wastes air time.

---

### TXFLOW

```
TXFLOW {ON | OFF}
default OFF
```

When ON in Transparent mode, TNC sends XOFF/XON to computer for software flow control (requires XFLOW ON). When OFF, hardware flow control (RTS/CTS) is required.

---

### UIDIGI

```
UIDIGI ON [{+|-} call1[,call2[,call3[,call4]]]]
default OFF NONE
```

Up to 4 alias callsigns for special UI digipeating. When a UI packet has one of these aliases in the to-be-digipeated field (and MYCALL is not the source or already digipeated), the alias is replaced with MYCALL and the packet is digipeated.

---

### UIDUPE

```
UIDUPE n     (n = 0–255, in seconds)
default 0 (disabled)
```

Duplicate UI frame suppression timer. Packets with the same source, destination, and data within n seconds are not redigipeated.

---

### UIDWAIT

```
UIDWAIT [ON|OFF]
default OFF
```

When ON, special digipeat packets (from UIDIGI, UIFLOOD, UITRACE) are subject to slottime/persist delays before transmission, like regular packets.

---

### UIFLOOD

```
UIFLOOD name[,time[,{FIRST | ID | NOID}]]     (name = 5 char max, time = 0–255)
default disabled,30,NOID
```

Multi-hop UI digipeating. When a UI frame has `name x-y` in the to-be-digipeated field, decrements SSID and digipeats. Duplicate detection for `time` seconds (max 64 checksums stored). ID = insert MYCALL in additional digipeater address field.

---

### UITRACE

```
UITRACE name, n     (name = 5 char max, n = 0–255)
default disabled, 30
```

Like UIFLOOD but inserts MYCALL (with H bit set) before each to-be-digipeated field, creating a traceable path. Duplicate suppression for n seconds.

---

### UNPROTO

```
UNPROTO {call1 [VIA call2,call3..call9] | NONE}
default CQ
```

Sets destination and digipeater path for unconnected (unproto) transmissions, BEACON, and ID packets. NONE = no unconnected packets sent except BEACON and ID.

---

### USERS

```
USERS n     (n = 0–26)
default 1
```

Number of channels available for incoming connect requests. If all USERS channels are connected, new connect requests receive `<DM>`. If set higher than MAXUSERS, extra is ignored.

---

### VERSION

```
VERSION
(immediate)
```

Displays current firmware version number and unit name.

---

### WEFAX

```
WEFAX n
(immediate)
```

Enter WEFAX mode, sampling audio at n samples per second. ABAUD must be at least 5/4 of the n rate. Exit with `<Ctrl+C>`.

---

### XFLOW

```
XFLOW {ON | OFF}
default ON
```

When ON, software flow control operates per START, STOP, XON, XOFF settings. When OFF, only hardware flow control (CTS/RTS) is used.

---

### XKCHKSUM

```
XKCHKSUM {ON | OFF}
default OFF
```

When INTFACE is XKISS: controls XKISS checksum mode.

---

### XKPOLLED

```
XKPOLLED {ON | OFF}
default OFF
```

When INTFACE is XKISS: controls XKISS polled mode.

---

### XMITLVL

```
XMITLVL n     (n = 0–502)
default 100
```

Sets modem drive level. Range: 1 mV to 4 V p-p. Counts 0–255: 0.5 mV/step. Counts 256–502: ~15 mV/step (up to 4 V max at 502).

---

### XMITOK

```
XMITOK {ON | OFF}
default ON
```

When OFF, all transmitting functions are inhibited. All other TNC functions remain unchanged.

---

### XOFF

```
XOFF n     (n = $00–$FF)
default $13 <Ctrl+S>
```

Character TNC sends to computer to stop input. $00 = hardware flow control only.

---

### XON

```
XON n     (n = $00–$FF)
default $11 <Ctrl+Q>
```

Character TNC sends to computer to restart input. $00 = hardware flow control only.

---

## Appendix A: Advanced Installation

### Precautions

- The KPC-3 Plus is grounded through connections to your transceiver, computer, and power supply
- Ensure equal ground potential between all devices
- Use shielded cabling only — no unshielded RS232 ribbon cable
- Lithium batteries can explode or leak if heated, disassembled, recharged, or inserted incorrectly

### Computer Port (DSUB-25) Pin Assignments

| Pin | Name | KPC-3 Plus | Computer (DSUB-25) | Computer (DSUB-9) |
|---|---|---|---|---|
| 1 | FG (Frame Ground) | 1 | 1 | N/A |
| 2 | TXD (Transmit Data) | 2 | 2 | 3 |
| 3 | RXD (Receive Data) | 3 | 3 | 2 |
| 4 | RTS (Request to Send) | 4 | 4 | 7 |
| 5 | CTS (Clear to Send) | 5 | 5 | 8 |
| 6 | DSR (Data Set Ready) | 6 | 6 | 6 |
| 7 | SG (Signal Ground) | 7 | 7 | 5 |
| 8 | DCD (Data Carrier Detect) | 8 | 8 | 1 |
| 20 | DTR (Data Terminal Ready) | 20 | 20 | 4 |

> Note: FG and SG are tied together in the KPC-3 Plus.

**Pin functions:**
- **FG:** Chassis safety ground
- **SG:** Common signal line
- **TXD:** Computer → KPC-3 Plus data
- **RXD:** KPC-3 Plus → Computer data
- **RTS:** Computer controls this (hardware flow control — can KPC-3 Plus send to computer?)
- **CTS:** KPC-3 Plus controls this (hardware flow control — can computer send to KPC-3 Plus?)
- **DSR:** Set high when modem is ON
- **DCD:** KPC-3 Plus signals current I/O stream status (positive = connected, negative = disconnected)
- **DTR:** Currently ignored (connected via buffer IC to processor)

### Optional DSUB-25 Wiring

- **Apply power via pin 13:** Connect J6 center+pin2, J7 center+pin1
- **Soft reset via pin 13:** Connect J6 center+pin1, J7 center+pin1. Momentary contact to ground = soft reset.
- **DTR/DSR handshaking:** Connect DTR terminal output → RTS on KPC-3 Plus; DSR terminal input ← CTS on KPC-3 Plus

### Software Settings

- 8 data bits, no parity, 1 stop bit
- Supported baud: 300, 600, 1200, 2400, 4800, 9600, 19200
- Set terminal for "full-duplex" operation (ECHO ON is default)
- For baud above 9600 with older computers, install buffered UARTs (16550 or equivalent)

### Radio Port (DSUB-9) Pin Assignments

| Pin | Name | Description |
|---|---|---|
| 1 | TXA | Transmit audio (AFSK out) → radio mic input |
| 2 | XCD | External carrier detect (ground = inhibit transmit) |
| 3 | PTT | Push-to-Talk (open drain, +50 V max, 200 mA max) |
| 4 | CTLB (AN0) | Control line B / Analog input 0 (open drain, 200 mA max) |
| 5 | RXA | Receive audio from transceiver external speaker jack |
| 6 | GND | Ground (connects to radio mic ground) |
| 7 | EXT-IN | External input for Power/Reset (jumper-configurable) |
| 8 | CTLA (AN1) | Control line A / Analog input 1 (open drain, 200 mA max) |
| 9 | GND/RESET | Ground as shipped (configurable as external reset via J5) |

### Optional DSUB-9 Wiring

- **Apply power via pin 7:** Connect J7 center+pin2, J6 center+pin2
- **Soft reset via pin 7:** Connect J7 center+pin2, J6 center+pin1. Momentary ground = soft reset.
- **Pin 9 reset alternative:** J5 center+pin1 = ground; J5 center+pin2 = external reset

### Interfacing Hand-Held Radios

For most hand-held transceivers, set jumper J9 to center+HT position.

**Common HT wiring guidelines:**
- A 0.1 µF capacitor (non-polarized) in the transmit audio line is usually required
- **ICOM HTs:** ~3.9 kΩ resistor in series with PTT wire, connected to mic input along with AFSK line (ICOM 2A style also works with some Alinco, Azden, and Standard HTs)
- **YAESU HTs:** Similar to ICOM but different resistor value; leave J9 in NOR position
- **KENWOOD HTs:** Connect PTT wire to sleeve of mic connector (no resistor needed); AFSK to RING (not TIP) of mic connector on 3-pin models; leave J9 in NOR position

---

## Appendix B: Advanced Information

### Assembly and Disassembly

**Disassembly:**
1. Turn off power and remove all cables
2. Remove two case screws (one on each side)
3. Remove top cover
4. Remove four hex nuts securing DSUB-9 and DSUB-25 connectors
5. Remove two screws securing front panel
6. Remove front panel
7. Observe static protection precautions; lift front edge of PCB and pull forward

**Reassembly:** Reverse the above procedure.

### Hard Reset

Resets all parameters to factory defaults. Erases PBBS messages.

1. Open case (remove two side screws, lift cover)
2. Locate jumper J11
3. Place jumper on both pins
4. Apply power
5. Observe display at 1200 baud:
   ```
   CHECKSUM OK
   RAM OK
   100,000 BYTES
   NO CLOCK
   REPLACE TEST JUMPER
   ```
6. Turn power off
7. Return J11 to single-pin position (factory default)
8. Reassemble

### Calibration/Equalization

Enter with `CAL` command at `cmd:` prompt.

```
CALIBRATE MODE:
M send mark
R receive
S send space
T send square wave
- or + adjust XMITLVL while transmitting
X exit
```

**Drive level:** Use T option to transmit square wave, then use `+`/`-` keys to adjust to approximately 3–3.5 kHz deviation.

**Equalization:** Have a nearby station transmit a calibrate square wave, press R. The two numbers shown should be approximately equal (40/60 to 60/40 ratio is acceptable). Change J4 if needed.

> Note: If using high-impedance data output from radio, set J3 on one pin only (OFF = 10 kΩ, ON = 620 Ω).

### PTT Watchdog Timer

Built-in PTT Watchdog disables PTT if TNC has been transmitting continuously for more than approximately 3 minutes. To disable: jumper J12 pins.

### Microprocessor Watchdog Timer

Internal watchdog detects firmware infinite loops and forces a TNC reset.

### A/D Converter

Two external A/D inputs (0–5 V dc, 8-bit accuracy), accessible via Radio Port or Serial Port using jumpers J8 or J10.

> Note: If measuring voltages greater than +5 V dc, install voltage-divider resistors R13 or R27 on the PCB to scale input to 5 V max. Maximum input voltages to A/D inputs should not exceed 50 V.

### KPC-3 Plus Jumpers

| Jumper | Schematic | PCB | Name | Description |
|---|---|---|---|---|
| J1 | A-6 | D-4 | Battery option | Default OFF. J1 OFF + J2 ON = battery switches in when external power removed |
| J2 | A-6 | D-4 | Battery option | Default ON. J1 ON + J2 OFF = battery backup if external power fails |
| J3 | D-2 | D-1 | Modem input impedance | ON (both pins) = 600 Ω. One pin = 10 kΩ (default) |
| J4 | D-2 | D-1 | Equalization | Both pins = no equalization (default). One pin = partial equalization |
| J5 | C-1 | D-2 | Ground/reset | Center+pin1 = ground pin 9 of DSUB-9 (default). Center+pin2 = external reset on pin 9 |
| J6 | B-1 | D-2 | Reset/input | Works with J5 or J7 for power/reset via connectors. Default: not connected |
| J7 | B-1 | D-2 | Serial configuration | Default: center+pin2. Works with J6 for alternate power/reset |
| J8 | B-1 | D-2 | Analog input AN0 | Center+pin1 = DSUB-9 pin 4. Center+pin2 = DSUB-25 pin 18 |
| J9 | C-1 | D-1 | Normal/HT | Default: NOR. Set to HT for hand-held transceivers requiring PTT on AFSK line |
| J10 | B-2 | D-2 | Analog input AN1 | Center+pin1 = DSUB-9 pin 8. Center+pin2 = DSUB-25 pin 11 |
| J11 | C-4 | C-3 | Reset jumper | One pin = normal. Both pins = hard reset on power-up |
| J12 | C-3 | C-1 | PTT watchdog | One pin = watchdog active (default). Both pins = watchdog disabled |
| J13 | C-6 | C-3 | ROM size | Center+pin1 = up to 1 megabit ROM. Center+pin2 = 1 megabit and above (default) |
| J14 | C-6 | A-3 | RAM size | Center+pin1 = 32K/128K RAM (default). Center+pin2 = 512K RAM (not applicable on SMT version — 512K is default) |
| J16 | A-5 | B-4 | Power supply | Default 5 V. Change to 3.3 V for very low power operation |
| J17–J20 | — | — | MX fulldup options | Full duplex options for KPC3 Plus MX only (not applicable on SMT version) |

---

## Appendix C: Options for the KPC-3 Plus

### Low Power Operation

To minimize current consumption:
- `LEDS OFF` (turns off front-panel LEDs)
- `CD INTERNAL` (carrier detect mode)

Current consumption in this configuration: less than 15 mA when no signal is being received.

> Note: CD SOFTWARE draws higher current in idle mode because the processor continuously monitors for data.

### Very Low Power Operation

Setting jumper J16 reduces voltage regulator output from 5.0 V to 3.3 V, nearly halving power consumption.

| Mode | 5.0 V | 3.3 V |
|---|---|---|
| Unit idle, LEDs OFF | ~16 mA | ~8.5 mA |
| Unit transmitting, LEDs ON | ~23 mA | ~12 mA |

> Note: The 3.3 V mode has not been thoroughly tested in the field and is not guaranteed over extreme temperature ranges.

### Expanding the RAM

The KPC-3 Plus ships with 128 KiB RAM, expandable to 512 KiB:

1. Remove existing 128 KiB RAM from socket XU14
2. Change jumper J14 to center pin + pin 2
3. Install 512 KiB low-power static RAM in XU14, pin 1 end toward J14

> Note: On the latest SMT circuit board revision, components are SMT type and maximum size 512K static RAM is standard.

### Installing the Optional Real-time Clock Module

Install the FOX 72421 clock chip in socket U15 with pin 1 toward the right. Initialize with the DAYTIME command after installation. The RTC is read at power-on and after soft resets.

### Replacing the Lithium Battery

Replace with CR2032 or equivalent. Positive terminal must face the top clip of the battery holder.

> Warning: Removing the battery causes all stored parameters to revert to factory defaults.

---

## Appendix D: In Case of Difficulty

### KPC-3 Plus Does Not Sign-On to Computer

1. Recheck cabling between computer serial port and KPC-3 Plus
2. Verify TXD, RXD, and Ground are connected to correct pins
3. If using 5-wire connection, try 3-wire (TXD, RXD, GND)
4. Check terminal program configuration (serial port, baud, parity)
5. Try a Hard Reset using jumper J11 (operate at 1200 baud)

### Unable to Make a Connect

1. Issue connect request and observe XMIT LED — if it lights, check radio connection; if not, verify XMITOK is ON
2. Observe if radio switches to Transmit — if not, recheck PTT wiring
3. Set CD to INTERNAL, turn off squelch, check if RCV LED lights — if not, recheck audio wiring
4. Monitor your transmitted signal with another radio — if transmitting but no audio, increase AFSK output with XMITLVL

### Cannot Transmit

1. Check XMITOK — must be ON
2. If RCV LED stays on all the time (fixed-level receive audio), set `CD SOFTWARE`

### Cannot Return to Command Mode

Most likely cause: STOP character (and usually XOFF) inadvertently set to same as COMMAND character — often caused by using `$` as the STREAMSW character.

Symptoms: Can communicate in Command mode and on-air, but `<Ctrl+C>` shows the heart character and `cmd:` prompt never appears.

Solution: Perform a Hard Reset using jumper J11.

---

## Appendix E: Additional Information

### Specifications

| Specification | Value |
|---|---|
| Size | 0.8" × 5.2" × 5.2" (21 mm × 133 mm × 133 mm) |
| Weight | 11 oz (0.32 kg) |
| Power (LEDs on, active) | 6–25 V dc, less than 30 mA |
| Power (LEDs off, inactive) | 6–25 V dc, less than 15 mA |
| Power plug polarity | Center pin positive |
| PTT output | Open drain, +50 V dc max, 200 mA max |
| Audio output range | Continuously adjustable: 1 mV p-p to 4 V p-p |
| Audio output impedance | 600 Ω (ac coupled) |
| Modulation | 1200 bps FSK, full duplex (CCITT V.23: 1300 Hz / 2100 Hz) |
| Audio input sensitivity | 5 mV p-p |
| Audio dynamic range | 70 dB |
| Audio input impedance | 10 kΩ (600 Ω with J3 installed) |
| Audio max input voltage | 12 V dc; 35 V p-p sinusoidal |
| Watchdog timer | Approximately 2½ minutes |
| Modes of operation | Packet, WeFax, KISS, XKISS, Host, GPS |
| Other features | PBBS, KA-NODE, Remote Access, optional K-Net |

### Messages from the KPC-3 Plus

| Message | Meaning |
|---|---|
| `***(callsign) busy` | Station you attempted to connect to responded with busy signal |
| `Already connected on stream n` | You're attempting to connect to someone you're already connected to |
| `BBS BUSY` | Your PBBS has no available streams (PBUSERS is full) |
| `CALIBRATE MODE: ...` | You've entered calibration mode |
| `Can't DISCONNECT` | Not connected on this stream |
| `Can't RECONNECT` | Reconnect callsign doesn't match current connection |
| `CHECKSUM ERROR` | Firmware EPROM may be damaged |
| `CHECKSUM OK` | EPROM passed checksum test during hard reset |
| `cmd:` | Command mode prompt |
| `Command not available in NEWUSER mode` | Use INTFACE TERMINAL for full command set |
| `*** connect request:` | Incoming connect request but no available stream |
| `*** CONNECTED to call [VIA digi1...digi8]` | Connection established |
| `*** DISCONNECTED` | Connection ended |
| `EH?` | Unrecognized command or syntax error (`$` marks the offending character) |
| `ENTER YOUR CALLSIGN=>` | TNC needs callsign (first power-on or after hard reset) |
| `xxxx FREE BYTES` | Characters remaining in TNC packet buffer |
| `***FRMR received:` | Frame reject packet received |
| `***FRMR sent:` | Frame reject packet sent due to protocol error |
| `Input ignored` | Partial command accepted; remainder ignored (dollar sign marks boundary) |
| `INVALID STREAM` | Invalid stream designator |
| `KANTRONICS KPC3PMX VERSION 9.1 ...` | Sign-on message (power-on or soft reset) |
| `Link state is:` | Current link state description |
| `MESSAGES WOULD BE LOST` | PBBS size reduction would lose messages |
| `NO KNOWN NODES` | No nodes in NDHEARD list |
| `NOT ENOUGH RAM` | Requested NUMNODES, MAXUSERS, or PBBS exceeds available RAM |
| `Not while connected` | Parameter cannot be changed while connected |
| `PBBS MESSAGE BUFFER NOT VALID! TRYING TO RECOVER` | PBBS pointer corruption detected |
| `PRESS (*) TO SET BAUD` | AUTOBAUD running — press `*` within 2 seconds |
| `RAM OK xxxK BYTES` | RAM test passed during hard reset |
| `RAM ERROR xxxK BYTES` | RAM problem detected during hard reset |
| `***retry count exceeded / *** DISCONNECTED` | RETRY count exceeded, connection broken |
| `S00` | TNC is in HOST mode and just reset |
| `Value out of range` | Parameter value too large or small |
| `was` | Displayed after a parameter change to show previous value |
| `YOU HAVE MAIL` | New message received for you in PBBS |

### ASCII Chart

| Ctrl | Dec | Hex | Code | Dec | Hex | Code | Dec | Hex | Code | Dec | Hex | Code |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| @ | 0 | 00 | NUL | 32 | 20 | SP | 64 | 40 | @ | 96 | 60 | ` |
| A | 1 | 01 | SOH | 33 | 21 | ! | 65 | 41 | A | 97 | 61 | a |
| B | 2 | 02 | STX | 34 | 22 | " | 66 | 42 | B | 98 | 62 | b |
| C | 3 | 03 | ETX | 35 | 23 | # | 67 | 43 | C | 99 | 63 | c |
| D | 4 | 04 | EOT | 36 | 24 | $ | 68 | 44 | D | 100 | 64 | d |
| E | 5 | 05 | ENQ | 37 | 25 | % | 69 | 45 | E | 101 | 65 | e |
| F | 6 | 06 | ACK | 38 | 26 | & | 70 | 46 | F | 102 | 66 | f |
| G | 7 | 07 | BEL | 39 | 27 | ' | 71 | 47 | G | 103 | 67 | g |
| H | 8 | 08 | BS | 40 | 28 | ( | 72 | 48 | H | 104 | 68 | h |
| I | 9 | 09 | HT | 41 | 29 | ) | 73 | 49 | I | 105 | 69 | i |
| J | 10 | 0A | LF | 42 | 2A | * | 74 | 4A | J | 106 | 6A | j |
| K | 11 | 0B | VT | 43 | 2B | + | 75 | 4B | K | 107 | 6B | k |
| L | 12 | 0C | FF | 44 | 2C | , | 76 | 4C | L | 108 | 6C | l |
| M | 13 | 0D | CR | 45 | 2D | - | 77 | 4D | M | 109 | 6D | m |
| N | 14 | 0E | SO | 46 | 2E | . | 78 | 4E | N | 110 | 6E | n |
| O | 15 | 0F | SI | 47 | 2F | / | 79 | 4F | O | 111 | 6F | o |
| P | 16 | 10 | DLE | 48 | 30 | 0 | 80 | 50 | P | 112 | 70 | p |
| Q | 17 | 11 | DC1 | 49 | 31 | 1 | 81 | 51 | Q | 113 | 71 | q |
| R | 18 | 12 | DC2 | 50 | 32 | 2 | 82 | 52 | R | 114 | 72 | r |
| S | 19 | 13 | DC3 | 51 | 33 | 3 | 83 | 53 | S | 115 | 73 | s |
| T | 20 | 14 | DC4 | 52 | 34 | 4 | 84 | 54 | T | 116 | 74 | t |
| U | 21 | 15 | NAK | 53 | 35 | 5 | 85 | 55 | U | 117 | 75 | u |
| V | 22 | 16 | SYN | 54 | 36 | 6 | 86 | 56 | V | 118 | 76 | v |
| W | 23 | 17 | ETB | 55 | 37 | 7 | 87 | 57 | W | 119 | 77 | w |
| X | 24 | 18 | CAN | 56 | 38 | 8 | 88 | 58 | X | 120 | 78 | x |
| Y | 25 | 19 | EM | 57 | 39 | 9 | 89 | 59 | Y | 121 | 79 | y |
| Z | 26 | 1A | SUB | 58 | 3A | : | 90 | 5A | Z | 122 | 7A | z |
| [ | 27 | 1B | ESC | 59 | 3B | ; | 91 | 5B | [ | 123 | 7B | { |
| \ | 28 | 1C | FS | 60 | 3C | < | 92 | 5C | \ | 124 | 7C | \| |
| ] | 29 | 1D | GS | 61 | 3D | = | 93 | 5D | ] | 125 | 7D | } |
| ^ | 30 | 1E | RS | 62 | 3E | > | 94 | 5E | ^ | 126 | 7E | ~ |
| _ | 31 | 1F | US | 63 | 3F | ? | 95 | 5F | _ | 127 | 7F | DEL |

### KPC-3 Plus Parts List

| Ref | Value | Ref | Value | Ref | Value | Ref | Value |
|---|---|---|---|---|---|---|---|
| BT1 | 2032 | C43 | .1uF | J6 | 3P_SIH | R20 | 4.7 kΩ |
| C1 | .001uF | C44 | .1uF | J7 | 3P_SIH | R21 | 100K_X5_SIP |
| C2 | .001uF | C45 | .1uF | J8 | 3P_SIH | R22 | 150 kΩ |
| C3 | .001uF | C46 | 33pF | J9 | 3P_SIH | R23 | 3.9 kΩ |
| C4 | .001uF | C47 | 33pF | J10 | 3P_SIH | R24 | 10 kΩ |
| C5 | .001uF | C48 | .1uF | J11 | 2P_SIH | R25 | 1 MΩ |
| C6 | .001uF | C49 | .1uF | J12 | 2P_SIH | R26 | 3.3 MΩ |
| C7 | .001uF | C50 | 1uF | J13 | 3P_SIH | R27 | — |
| C8 | .001uF | C51 | 180pF | J14 | 3P_SIH | R28 | 10 kΩ |
| C9 | .001uF | C52 | .001uF | J15 | 3P_SIH | R29 | 100 kΩ |
| C10 | .001uF | C53 | .1uF | J16 | 2P_SIH | R30 | 1 MΩ |
| C11 | .001uF | C54 | .1uF | L1 | LED_YELLOW_T1 | R31 | 100K_X4_SIP |
| C12 | .001uF | C55 | 180pF | L2 | LED_GREEN_T1 | R32 | 620 Ω |
| C13 | .001uF | C56 | .001uF | L3 | LED_GREEN_T1 | R33 | 180 kΩ |
| C14 | .1uF | C57 | 10uF | L4 | LED_GREEN_T1 | R34 | 620 Ω |
| C15 | .1uF | C58 | .01uF | L5 | LED_RED_T1 | R35 | 82 kΩ |
| C16 | .0022uF | C59 | .1uF | L6 | LED_GREEN_T1 | R36 | 270 kΩ |
| C17 | .001uF | C60 | 10uF | P1 | DB9 Female | R37 | 3.3 kΩ |
| C18 | 1uF | C61 | .1uF | P2 | DB25 Female | R38 | 9.1 kΩ |
| C19 | .001uF | C62 | 22pF | P3 | 2.1 mm jack | R39 | 1.5K_X5_SIP |
| C20 | .001uF | C63 | 22pF | Q1 | 2N7000 | R40 | 1.5 kΩ |
| C21 | .01uF | C64 | .1uF | Q2 | 2N7000 | RFC1 | 10uH |
| C22 | 10pF | C65 | .1uF | Q3 | 2N7000 | SW1 | PHA012U10EEM |
| C23 | 1uF | CR1 | 1N914 | Q4 | PN2907A | U1 | 14C88 |
| C24 | .001uF | CR2 | 1N914 | R1 | 620 Ω | U2 | 74HC14 |
| C25 | .001uF | CR3 | 1N914 | R2 | 100K_X4_SIP | U3 | LMC6034IN |
| C26 | .1uF | CR4 | 1N914 | R3 | 4.7 kΩ | U4 | 74HC14 |
| C27 | 22pF | CR5 | 1N914 | R4 | 10 kΩ | U5 | MC68HC11F1 |
| C28 | 1uF | CR6 | 1N914 | R5 | 10 MΩ | U6 | 73M223 |
| C29 | .1uF | CR7 | 1N914 | R6 | 47 kΩ | U7 | 74HC00 |
| C30 | .1uF | CR8 | 1N914 | R7 | 10 kΩ | U8 | 74HC138 |
| C31 | 22pF | CR9 | 1N914 | R8 | 10 kΩ | U9 | AD8402 |
| C32 | .1uF | CR10 | 1N914 | R9 | 10 kΩ | U10 | ROM_32 |
| C33 | .1uF | CR11 | 1N914 | R10 | 47 kΩ | U11 | MIC2951 |
| C34 | .001uF | CR12 | 1N914 | R11 | 330 kΩ | U12 | LMC6032IN |
| C35 | .001uF | CR13 | 1N6263 | R12 | 100K_X4_SIP | U13 | X25128 |
| C36 | 470pF | FB1–9 | SM FERRITE BEAD | R13 | — | U14 | RAM_32 |
| C37 | .1uF | J1 | 2P_SIH | R14 | 1 MΩ | U15 | 72421 |
| C38 | .1uF | J2 | 2P_SIH | R15 | 6.8 kΩ | U16 | 74HC374 |
| C39 | .01uF | J3 | 2P_SIH | R16 | 150 kΩ | X1 | XTAL |
| C40 | 1uF | J4 | 2P_SIH | R17 | 10 kΩ | X2 | XTAL |
| C41 | 47uF | J5 | 3P_SIH | R18 | 10 kΩ | X3 | 32.768KHZ |
| C42 | .001uF | | | R19 | 10 MΩ | | |

### KPC-3 Plus MX Parts List

| Ref | Value | Ref | Value | Ref | Value | Ref | Value |
|---|---|---|---|---|---|---|---|
| BT1 | 2032 | C45 | .1uF | J11 | 2P_SIH | R18 | 10 kΩ |
| C1 | .001uF | C46 | 18pF | J12 | 2P_SIH | R19 | 10 MΩ |
| C2 | .001uF | C47 | 18pF | J13 | 3P_SIH | R20 | 4.7 kΩ |
| C3 | .001uF | C48 | .1uF | J14 | 3P_SIH | R24 | 10 kΩ |
| C4 | .001uF | C49 | .1uF | J15 | 3P_SIH | R25 | 100 kΩ |
| C5 | .001uF | C50 | 1uF | J16 | 2P_SIH | R26 | 3.3 MΩ |
| C6 | .001uF | C51 | 180pF | J17 | 3P_SIH | R27 | — |
| C7 | .001uF | C52 | .001uF | J18 | 3P_SIH | R28 | 10 kΩ |
| C8 | .001uF | C53 | .1uF | J19 | 3P_SIH | R31 | 100K_X4_SIP |
| C9 | .001uF | C54 | .1uF | J20 | 3P_SIH | R32 | 620 Ω |
| C10 | .001uF | C56 | .001uF | L1 | LED_YELLOW_T1 | R33 | 180 kΩ |
| C11 | .001uF | C57 | 10uF | L2 | LED_GREEN_T1 | R34 | 620 Ω |
| C12 | .001uF | C59 | .1uF | L3 | LED_GREEN_T1 | R39 | 1.5K_X5_SIP |
| C13 | .001uF | C60 | 10uF | L4 | LED_GREEN_T1 | R40 | 1.5 kΩ |
| C14 | .1uF | C61 | .1uF | L5 | LED_RED_T1 | RFC1 | 10uH |
| C15 | .1uF | C62 | 22pF | L6 | LED_GREEN_T1 | SW1 | PHA012U10EEM |
| C16 | .0022uF | C63 | 22pF | P1 | DB9 Female | U1 | 14C88 |
| C17 | .001uF | C64 | .1uF | P2 | DB25 Female | U2 | 74HC14 |
| C18 | 1uF | C65 | .1uF | P3 | 2.1 mm jack | U3 | LMC660CN |
| C19 | .001uF | CR1 | 1N914 | Q1 | 2N7000 | U4 | 74HC14 |
| C20 | .001uF | CR2 | 1N914 | Q2 | 2N7000 | U5 | MC68HC11F1 |
| C21 | .01uF | CR3 | 1N914 | Q3 | 2N7000 | U6 | 74HC00 |
| C22 | 10pF | CR4 | 1N914 | Q4 | PN2907A | U7 | 74HC00 |
| C23 | 1uF | CR5 | 1N914 | R1 | 620 Ω | U8 | 74HC138 |
| C24 | .001uF | CR6 | 1N914 | R2 | 100K_X4_SIP | U9 | AD8402 |
| C25 | .001uF | CR7 | 1N914 | R3 | 4.7 kΩ | U10 | ROM_32 |
| C26 | .1uF | CR8 | 1N914 | R4 | 10 kΩ | U11 | MIC2951 |
| C27 | 22pF | CR9 | 1N914 | R5 | 220 kΩ | U13 | X25128 |
| C28 | 1uF | CR10 | 1N914 | R6 | 47 kΩ | U14 | RAM_32 |
| C29 | .1uF | CR11 | 1N914 | R7 | 10 kΩ | U15 | 72421 |
| C30 | .1uF | CR12 | 1N914 | R8 | 10 kΩ | U16 | 74HC374 |
| C31 | 22pF | CR13 | 1N6263 | R9 | 10 kΩ | U17 | MX614 |
| C32 | .1uF | FB1–9 | SM FERRITE BEAD | R10 | 47 kΩ | U18 | MX614 |
| C33 | .1uF | J1 | 2P_SIH | R11 | 100 kΩ | X1 | XTAL |
| C34 | .001uF | J2 | 2P_SIH | R12 | 100K_X4_SIP | X2 | XTAL |
| C35 | .001uF | J3 | 2P_SIH | R13 | — | X3 | 32.768KHZ |
| C36 | .1uF | J4 | 2P_SIH | R14 | 1 MΩ | | |
| C37 | .1uF | J5 | 3P_SIH | R15 | 9.1 kΩ | | |
| C38 | 100pF | J6 | 3P_SIH | R16 | 82 kΩ | | |
| C39 | 180pF | J7 | 3P_SIH | R17 | 150 kΩ | | |
| C41 | 47uF | J8–J10 | 3P_SIH | | | | |

---

*End of Kantronics KPC-3 Plus Users Guide — Revision H*

#!/usr/bin/env python3
"""
kpc3_console.py - A minimal interactive console for the KPC-3+ via the TCP bridge.

Usage:
    python3 kpc3_console.py                  # connects to 192.168.1.100:8765 by default
    python3 kpc3_console.py -H 192.168.1.100    # explicit host
    python3 kpc3_console.py -p 8765          # explicit port
    python3 kpc3_console.py --log session.log  # mirror session to a file

Key handling (raw pass-through mode):
    Ctrl-C     sent to the TNC (needed to exit Convers Mode, per KPC-3+ COMMAND)
    Ctrl-]     quit this console (telnet-style escape)
    Ctrl-D     quit this console (EOF)
    Enter      sends \\r to the TNC (\\n is stripped, the KPC-3+ chokes on \\n)
    Backspace  sent as BS (0x08) so the TNC's own line editor handles it
    all other  keystrokes pass straight through to the TNC

Why raw mode?
    The old line-buffered mode could not forward Ctrl-C to the TNC because
    the terminal intercepted it as SIGINT before Python ever saw it. Raw mode
    puts stdin in cbreak + ISIG-off + ICRNL-off so every byte goes straight
    to the bridge. The TNC's own ECHO setting handles visual feedback.

Why not just `nc 192.168.1.100 8765`?
    - The KPC-3+ chokes on \\n. This script sends \\r only.
    - A background reader thread prints TNC output in real time while you type.
    - Optional session logging.
    - Ctrl-C forwards to the TNC instead of killing the client.
"""

import argparse
import os
import select
import socket
import sys
import threading
import time
from datetime import datetime


# Default bridge host/port. Override with --host/-H, --port/-p,
# or the KPC3_HOST / KPC3_PORT environment variables.
DEFAULT_HOST = os.environ.get("KPC3_HOST", "192.168.1.100")
DEFAULT_PORT = int(os.environ.get("KPC3_PORT", "8765"))

# Local-only keys. These are intercepted by the console and NOT sent to the TNC.
QUIT_KEYS = {b"\x1d", b"\x04"}   # Ctrl-] (telnet escape), Ctrl-D (EOF)


def reader_loop(sock, log_fh, stop_event):
    """Continuously print whatever the bridge sends us."""
    sock.settimeout(0.5)
    while not stop_event.is_set():
        try:
            chunk = sock.recv(1024)
            if not chunk:
                sys.stdout.write("\r\n[bridge closed the connection]\r\n")
                sys.stdout.flush()
                stop_event.set()
                return
            text = chunk.decode("ascii", errors="replace")
            sys.stdout.write(text)
            sys.stdout.flush()
            if log_fh:
                log_fh.write(text)
                log_fh.flush()
        except socket.timeout:
            continue
        except OSError:
            stop_event.set()
            return


def run_raw_console(sock, log_fh, stop_event):
    """
    Put stdin in raw cbreak mode and forward every keystroke to the TNC.
    Ctrl-] or Ctrl-D exits locally. Enter is translated from LF to CR.
    Backspace (DEL 0x7f) is translated to BS (0x08) for the TNC.
    """
    import termios
    import tty

    fd = sys.stdin.fileno()
    old_attrs = termios.tcgetattr(fd)
    try:
        # cbreak: character-at-a-time, no ICANON, no ECHO.
        tty.setcbreak(fd)
        new_attrs = termios.tcgetattr(fd)
        # Disable ISIG so Ctrl-C does NOT raise SIGINT — we want to forward it.
        new_attrs[3] &= ~termios.ISIG
        # Disable ICRNL so Enter gives us 0x0D (CR) not 0x0A (LF).
        new_attrs[0] &= ~termios.ICRNL
        termios.tcsetattr(fd, termios.TCSANOW, new_attrs)

        while not stop_event.is_set():
            r, _, _ = select.select([fd], [], [], 0.2)
            if fd not in r:
                continue
            try:
                ch = os.read(fd, 1)
            except OSError:
                break
            if not ch:
                break

            if ch in QUIT_KEYS:
                break

            # Translate keystrokes to what the TNC expects.
            if ch == b"\n":
                ch = b"\r"           # LF -> CR (belt and suspenders)
            elif ch == b"\x7f":
                ch = b"\x08"         # DEL -> BS (matches KPC-3+ default)

            try:
                sock.sendall(ch)
                if log_fh:
                    # Log keystrokes as printable where possible.
                    if ch == b"\r":
                        log_fh.write("\n>> [ENTER]\n")
                    elif ch == b"\x03":
                        log_fh.write(">> [Ctrl-C]\n")
                    elif ch == b"\x08":
                        log_fh.write(">> [BS]\n")
                    elif ch == b"\x1a":
                        log_fh.write(">> [Ctrl-Z]\n")
                    else:
                        try:
                            log_fh.write(ch.decode("ascii"))
                        except UnicodeDecodeError:
                            log_fh.write(f"\\x{ch[0]:02x}")
                    log_fh.flush()
            except OSError as e:
                sys.stdout.write(f"\r\n[send failed: {e}]\r\n")
                sys.stdout.flush()
                break
    finally:
        termios.tcsetattr(fd, termios.TCSANOW, old_attrs)


def main():
    parser = argparse.ArgumentParser(
        description="Interactive console for the KPC-3+ TCP bridge."
    )
    parser.add_argument("-H", "--host", default=DEFAULT_HOST, help="bridge host")
    parser.add_argument(
        "-p", "--port", type=int, default=DEFAULT_PORT, help="bridge TCP port"
    )
    parser.add_argument(
        "--log", default=None, help="optional path to mirror the session to a file"
    )
    args = parser.parse_args()

    log_fh = None
    if args.log:
        log_fh = open(args.log, "a", encoding="utf-8")
        log_fh.write(f"\n--- session started {datetime.now().isoformat()} ---\n")
        log_fh.flush()

    try:
        sock = socket.create_connection((args.host, args.port), timeout=5)
    except OSError as e:
        print(f"[could not connect to {args.host}:{args.port}: {e}]")
        sys.exit(1)

    print(f"[connected to {args.host}:{args.port}]")
    print("[Ctrl-C is forwarded to the TNC. Press Ctrl-] or Ctrl-D to quit this console.]")
    print()

    # Flush any accumulated buffer noise with two blank \r, per the KPC-3+ skill.
    # Then force ECHO ON so the user can see what they type even if the TNC was
    # previously set to ECHO OFF. If the TNC is in Convers or a sub-mode instead
    # of cmd:, this is just harmless text in the stream.
    try:
        sock.sendall(b"\r")
        time.sleep(0.4)
        sock.sendall(b"\r")
        time.sleep(0.4)
        sock.sendall(b"ECHO ON\r")
        time.sleep(0.4)
    except OSError:
        pass

    stop_event = threading.Event()
    reader = threading.Thread(
        target=reader_loop, args=(sock, log_fh, stop_event), daemon=True
    )
    reader.start()

    try:
        run_raw_console(sock, log_fh, stop_event)
    finally:
        stop_event.set()
        try:
            sock.close()
        except OSError:
            pass
        if log_fh:
            log_fh.write(f"--- session ended {datetime.now().isoformat()} ---\n")
            log_fh.close()
        sys.stdout.write("\r\n[disconnected]\r\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()

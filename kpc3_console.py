#!/usr/bin/env python3
"""
kpc3_console.py - A minimal interactive console for the KPC-3+ via the TCP bridge.

Usage:
    python3 kpc3_console.py                  # connects to YOUR-WINDOWS-IP:8765 by default
    python3 kpc3_console.py -H YOUR-WINDOWS-IP    # explicit host
    python3 kpc3_console.py -p 8765          # explicit port
    python3 kpc3_console.py --log session.log  # mirror session to a file

Keys:
    ENTER   send the current line to the TNC (terminated with \r, not \r\n)
    Ctrl-C  quit
    Ctrl-D  quit (EOF)

Why not just `nc YOUR-WINDOWS-IP 8765`?
    - The KPC-3+ chokes on \n. This script sends \r only.
    - A background reader thread prints TNC output in real time while you type.
    - Optional session logging.
    - Cross-platform: works on macOS, Linux, and Windows.
"""

import argparse
import os
import socket
import sys
import threading
import time
from datetime import datetime


# Default bridge host/port. Override with --host/-H, --port/-p,
# or the KPC3_HOST / KPC3_PORT environment variables.
DEFAULT_HOST = os.environ.get("KPC3_HOST", "YOUR-WINDOWS-IP")
DEFAULT_PORT = int(os.environ.get("KPC3_PORT", "8765"))


def reader_thread(sock, log_fh, stop_event):
    """Continuously print whatever the bridge sends us."""
    sock.settimeout(0.5)
    while not stop_event.is_set():
        try:
            chunk = sock.recv(1024)
            if not chunk:
                # Bridge closed the connection.
                print("\n[bridge closed the connection]", flush=True)
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
    print("[Ctrl-C to quit, ENTER sends \\r]")
    print()

    # Flush any accumulated buffer noise with two blank \r, per the KPC-3+ skill.
    try:
        sock.sendall(b"\r")
        time.sleep(0.4)
        sock.sendall(b"\r")
        time.sleep(0.4)
    except OSError:
        pass

    stop_event = threading.Event()
    reader = threading.Thread(
        target=reader_thread, args=(sock, log_fh, stop_event), daemon=True
    )
    reader.start()

    try:
        while not stop_event.is_set():
            try:
                line = input()
            except EOFError:
                break
            except KeyboardInterrupt:
                print("\n[quitting]")
                break

            if log_fh:
                log_fh.write(f">> {line}\n")
                log_fh.flush()

            try:
                sock.sendall((line + "\r").encode("ascii"))
            except OSError as e:
                print(f"[send failed: {e}]")
                break
    finally:
        stop_event.set()
        try:
            sock.close()
        except OSError:
            pass
        if log_fh:
            log_fh.write(f"--- session ended {datetime.now().isoformat()} ---\n")
            log_fh.close()
        print("[disconnected]")


if __name__ == "__main__":
    main()

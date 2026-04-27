"""beacon_manager.py — rotating BTEXT for W6OAK AI bot.

Design:
  * Called from the main loop on every tick (same thread as the TNC).
  * No extra thread, no locks. We piggyback on the already-held socket.
  * Never rotates while a session is active (caller passes `busy`).
  * Hybrid pool:
      - ~40 static lines in BTEXT_POOL.md (hand-written).
      - Every Nth rotation, call Haiku for a fresh one-off line.
  * Graceful fallback: if the pool file or the API is unreachable, the
    current TNC BTEXT is left alone.
  * Dry-run mode: `python beacon_manager.py --dry-run 50` prints 50
    rotated BTEXTs without touching the TNC.

Knobs (from config.json):
    beacon_rotation_enabled : bool   default False
    beacon_rotation_minutes : int    default 60   (match BEACON EVERY n)
    beacon_api_ratio        : int    default 2    (1 in N uses Haiku;
                                                   60 min * 2 = ~1 call /
                                                   2 hr, same as the old
                                                   20 min / ratio 6 pairing)
    beacon_prefix           : str    default "W6OAK AI bot CM87. "
    beacon_max_len          : int    default 128
    beacon_pool_file        : str    default "BTEXT_POOL.md"
"""

from __future__ import annotations

import logging
import os
import random
import threading
import time
from typing import List, Optional

try:
    import anthropic  # type: ignore
    ANTHROPIC_AVAILABLE = True
except Exception:
    ANTHROPIC_AVAILABLE = False

log = logging.getLogger('w6oak.beacon')


DEFAULT_PREFIX      = "W6OAK AI bot CM87. "
DEFAULT_MAX_LEN     = 128
DEFAULT_POOL_FILE   = "BTEXT_POOL.md"
DEFAULT_MINUTES     = 60
DEFAULT_API_RATIO   = 2
HAIKU_MODEL         = "claude-haiku-4-5-20251001"

# Fresh-line prompt. Keeps Haiku on-script so the output lands in budget
# and in tone. The prompt shows a few pool samples as style anchors.
HAIKU_SYSTEM = (
    "You write a single packet-radio beacon line for W6OAK, an AI-operated "
    "ham station in East Oakland on 145.050 MHz. Output RULES are absolute:\n"
    "- Reply with ONLY the beacon body. No prefix, no quotes, no explanation.\n"
    "- Body must be ASCII only, 1 line, 1 to {budget} characters long.\n"
    "- No smart quotes, no emoji, no markdown.\n"
    "- Tone: dry, concise, inviting. Mix in one of: path teases, open "
    "questions, mild ham nostalgia, East Oakland/fog texture.\n"
    "- Often include the string `c W6OAK` to invite a connect.\n"
    "- End with a period or exclamation. No trailing space.\n"
    "- Avoid repeating the examples verbatim. Write something new."
)


class BeaconManager:
    def __init__(
        self,
        tnc,
        *,
        enabled: bool = False,
        rotation_minutes: int = DEFAULT_MINUTES,
        api_ratio: int = DEFAULT_API_RATIO,
        prefix: str = DEFAULT_PREFIX,
        max_len: int = DEFAULT_MAX_LEN,
        pool_file: str = DEFAULT_POOL_FILE,
        api_key: Optional[str] = None,
    ):
        self.tnc = tnc
        self.enabled = enabled
        self.rotation_seconds = max(1, int(rotation_minutes)) * 60
        self.api_ratio = max(0, int(api_ratio))
        self.prefix = prefix
        self.max_len = int(max_len)
        self.pool_file = pool_file
        self.body_budget = self.max_len - len(self.prefix)

        self._rotation_count = 0
        self._last_rotation = 0.0  # epoch seconds of last successful rotation
        self._recent_bodies: List[str] = []  # avoid repeating the last 5

        # Body selection runs on a worker thread so a slow/stuck Haiku call
        # can never block the bot's main loop (heartbeat, RF read, session
        # handling). TNC writes stay on the main thread — only _select_body
        # runs off-thread.
        self._worker: Optional[threading.Thread] = None
        self._pending_body: Optional[str] = None  # worker -> main handoff
        self._worker_done: bool = False
        self._pending_lock = threading.Lock()

        self._client = None
        if api_key and ANTHROPIC_AVAILABLE:
            try:
                self._client = anthropic.Anthropic(api_key=api_key)
            except Exception as e:
                log.warning(f"Haiku client init failed, static-only mode: {e}")
                self._client = None

        if self.body_budget < 10:
            log.warning(
                f"beacon prefix '{prefix}' ({len(prefix)} chars) leaves only "
                f"{self.body_budget} chars for body. Consider a shorter prefix."
            )

    # ---------- pool loading ----------

    def _load_pool(self) -> List[str]:
        """Re-read the pool file on every rotation so edits take effect live."""
        path = self.pool_file
        if not os.path.isabs(path):
            path = os.path.join(os.path.dirname(__file__), path)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                raw = f.read()
        except FileNotFoundError:
            log.warning(f"pool file not found: {path}")
            return []
        except Exception as e:
            log.warning(f"pool read error: {e}")
            return []

        # Grab lines after '## BODIES'. Skip blanks and `#` comments.
        if '## BODIES' not in raw:
            log.warning(f"pool file missing '## BODIES' section: {path}")
            return []
        bodies_block = raw.split('## BODIES', 1)[1]
        out: List[str] = []
        for ln in bodies_block.splitlines():
            s = ln.strip()
            if not s or s.startswith('#'):
                continue
            if 1 <= len(s) <= self.body_budget:
                out.append(s)
        return out

    # ---------- Haiku ----------

    def _generate_fresh(self, pool: List[str]) -> Optional[str]:
        """Ask Haiku for one novel beacon body. Returns None on any failure."""
        if self._client is None:
            return None
        sample = random.sample(pool, min(6, len(pool))) if pool else []
        sys_prompt = HAIKU_SYSTEM.format(budget=self.body_budget)
        user_msg = (
            "Examples of our style (do not copy verbatim):\n"
            + "\n".join(f"- {s}" for s in sample)
            + "\n\nWrite ONE new beacon body now."
        )
        try:
            resp = self._client.messages.create(
                model=HAIKU_MODEL,
                max_tokens=120,
                system=sys_prompt,
                messages=[{"role": "user", "content": user_msg}],
                timeout=10,
            )
            text = resp.content[0].text if resp.content else ""
        except Exception as e:
            log.warning(f"Haiku beacon call failed: {e}")
            return None

        body = _sanitize(text, self.body_budget)
        if not body:
            log.info("Haiku returned empty/invalid body; falling back to pool.")
            return None
        return body

    # ---------- selection ----------

    def _pick_body(self) -> Optional[str]:
        pool = self._load_pool()
        use_api = (
            self.api_ratio > 0
            and self._client is not None
            and (self._rotation_count % self.api_ratio == 0)
        )

        if use_api:
            fresh = self._generate_fresh(pool)
            if fresh:
                return self._avoid_repeat(fresh, pool)

        if not pool:
            return None
        return self._avoid_repeat(random.choice(pool), pool)

    def _avoid_repeat(self, candidate: str, pool: List[str]) -> str:
        """If we picked something we used in the last ~5 rotations, try once more."""
        if pool and candidate in self._recent_bodies and len(pool) > len(self._recent_bodies):
            for _ in range(4):
                alt = random.choice(pool)
                if alt not in self._recent_bodies:
                    candidate = alt
                    break
        self._recent_bodies.append(candidate)
        if len(self._recent_bodies) > 5:
            self._recent_bodies = self._recent_bodies[-5:]
        return candidate

    # ---------- main-loop hook ----------

    def maybe_rotate(self, busy: bool) -> None:
        """Called each main-loop tick. Must not block — if body selection
        needs Haiku, it runs on a worker thread; the TNC write happens on
        the tick after the worker finishes."""
        if not self.enabled:
            return
        if busy:
            return  # never mid-QSO

        # Commit any result the worker produced on a prior tick.
        with self._pending_lock:
            worker_done = self._worker_done
            body_full = self._pending_body
            if worker_done:
                self._worker_done = False
                self._pending_body = None
        if worker_done:
            if body_full is not None:
                self._commit_rotation(body_full)
            else:
                # Worker had nothing (empty pool, Haiku down, or exception).
                # Advance anyway so we don't hammer every tick.
                log.info("Beacon rotation skipped (no body available).")
                self._last_rotation = time.time()
            return

        # Worker still running? Wait — don't queue another.
        if self._worker is not None and self._worker.is_alive():
            return

        now = time.time()
        if self._last_rotation == 0.0:
            # Stagger first rotation slightly so bot start doesn't pile up
            # all side-effects at once.
            self._last_rotation = now - self.rotation_seconds + 60
            return
        if now - self._last_rotation < self.rotation_seconds:
            return

        # Due. Kick off worker to pick (and possibly Haiku-generate) a body.
        self._worker = threading.Thread(
            target=self._select_body_worker,
            name='beacon-select',
            daemon=True,
        )
        self._worker.start()

    def _select_body_worker(self) -> None:
        """Run on worker thread. Never touches the TNC socket — only produces
        a body string and hands it to the main thread via _pending_body."""
        result: Optional[str] = None
        try:
            body = self._pick_body()
            if body:
                full = self.prefix + body
                if len(full) > self.max_len:
                    log.warning(f"rotated BTEXT over cap ({len(full)}>{self.max_len}); truncating")
                    full = full[: self.max_len]
                result = full
        except Exception as e:
            log.warning(f"beacon worker error: {e}")
        finally:
            with self._pending_lock:
                self._pending_body = result
                self._worker_done = True

    def _commit_rotation(self, full: str) -> None:
        """Run on main thread. TNC socket writes belong here."""
        ok = self._push_to_tnc(full)
        now = time.time()
        if ok:
            self._rotation_count += 1
            self._last_rotation = now
            log.info(f"BTEXT rotated ({len(full)} chars): {full}")
        else:
            log.warning("BTEXT push failed; will retry next cycle.")
            self._last_rotation = now

    # ---------- TNC write ----------

    def _push_to_tnc(self, full_btext: str) -> bool:
        """Set BTEXT via the TNC command channel. Returns True on best-effort success.

        We rely on the bot being in 'cmd:' state between sessions. The main
        loop only calls us when busy=False, so we should be safe to set it.
        """
        try:
            # Nudge the TNC into cmd: mode just in case. A bare CR is harmless
            # in cmd: state and usually recovers it from odd states.
            self.tnc.send(b'\r')
            time.sleep(0.2)
            self.tnc.flush(0.3)
            self.tnc.cmd(f'BTEXT {full_btext}')
            time.sleep(0.3)
            self.tnc.flush(0.5)
            return True
        except Exception as e:
            log.warning(f"TNC write error during BTEXT push: {e}")
            return False


# ---------- helpers ----------

def _sanitize(text: str, budget: int) -> str:
    """Trim, strip smart chars, and clamp to budget. Returns '' if unusable.

    Note: this runs at Haiku fetch time. The *final* safety net is
    sanitize_tx() inside TNCSession.send() in w6oak_ai_bot.py (v2.4.0+),
    which catches typography on every byte leaving the process. This
    function stays in place so the pool loader and log lines show clean
    text too, not just the on-air bytes."""
    if not text:
        return ''
    s = text.strip()
    # Collapse any internal CR/LF into a single space
    s = s.replace('\r', ' ').replace('\n', ' ')
    # Replace smart quotes/dashes with ASCII
    s = (s.replace('\u2018', "'").replace('\u2019', "'")
           .replace('\u201c', '"').replace('\u201d', '"')
           .replace('\u2013', '-').replace('\u2014', '-')
           .replace('\u2026', '...'))
    # Backticks look fine in Markdown but some TNCs misread them. Swap for
    # single quotes so BTEXT reads the same on the wire as in the pool.
    s = s.replace('`', "'")
    # Drop non-ASCII
    s = s.encode('ascii', errors='ignore').decode('ascii')
    # Collapse whitespace
    s = ' '.join(s.split())
    # Strip wrapping quotes if the model decided to add them
    if len(s) >= 2 and s[0] in ('"', "'") and s[-1] == s[0]:
        s = s[1:-1].strip()
    if len(s) < 2:
        return ''
    if len(s) > budget:
        s = s[:budget].rstrip()
    return s


# ---------- dry-run CLI ----------

def _dry_run(n: int = 50, config_path: str = 'private/config.json') -> None:
    """Preview N rotated BTEXTs without touching the TNC. Uses Haiku if api key
    is present, otherwise pool-only."""
    import json
    import sys

    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

    api_key = os.environ.get('ANTHROPIC_API_KEY', '')
    cfg = {}
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            cfg = json.load(f)
        api_key = api_key or cfg.get('anthropic_api_key', '') or ''
    except FileNotFoundError:
        print(f"(no {config_path}; pool-only preview)", file=sys.stderr)

    class _Null:
        def send(self, *a, **kw): pass
        def cmd(self, *a, **kw): pass
        def flush(self, *a, **kw): pass

    bm = BeaconManager(
        tnc=_Null(),
        enabled=True,
        rotation_minutes=cfg.get('beacon_rotation_minutes', DEFAULT_MINUTES),
        api_ratio=cfg.get('beacon_api_ratio', DEFAULT_API_RATIO),
        prefix=cfg.get('beacon_prefix', DEFAULT_PREFIX),
        max_len=cfg.get('beacon_max_len', DEFAULT_MAX_LEN),
        pool_file=cfg.get('beacon_pool_file', DEFAULT_POOL_FILE),
        api_key=api_key.strip() or None,
    )

    pool_size = len(bm._load_pool())
    print(f"# dry-run: {n} rotations, pool_size={pool_size}, "
          f"api_ratio={bm.api_ratio}, budget={bm.body_budget}")
    api_hits = 0
    for i in range(n):
        body = bm._pick_body()
        full = (bm.prefix + body) if body else '(no body)'
        tag = ''
        if bm.api_ratio > 0 and bm._client is not None and i % bm.api_ratio == 0:
            tag = ' [haiku]'
            api_hits += 1
        print(f"{i+1:3d} {len(full):3d}{tag}  {full}")
        bm._rotation_count += 1
    print(f"# done. estimated api calls: {api_hits}")


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='BTEXT rotation dry-run')
    parser.add_argument('--dry-run', type=int, default=50, help='number of samples to print')
    parser.add_argument('--config', default='private/config.json', help='config file path')
    args = parser.parse_args()
    _dry_run(args.dry_run, args.config)

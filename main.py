#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun entry (program/v1).

Writes one funny one-line excuse, in the vacuum's own voice, to
``/output/entry.txt`` (or ``$MAKEFUN_OUTPUT_DIR/entry.txt``).

The line is rooted in the vacuum's own world — bumper, map, battery —
and lands its turn at the end: the missed corner is not laziness, it
is a load-bearing wall the battery has officially signed off on.
"""

import os
import sys

ENTRY = (
    "I bumped the chair leg, my map redrew it as a load-bearing wall, "
    "and my battery signed off on skipping that corner forever."
)

MAX_CHARS = 140


def main() -> int:
    text = ENTRY.strip()
    if not text or len(text) > MAX_CHARS:
        print(f"entry invalid: {len(text)} chars (limit {MAX_CHARS})",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry invalid: must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")
    os.chmod(path, 0o644)
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

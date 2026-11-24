#!/usr/bin/env python3
"""One Word for Your Wi-Fi — entry program.

Writes a single word to the output file, nothing else.

The word is "scam": four letters, one word, no trailing newline.
It is the funniest and truest word for home Wi-Fi as it is actually
lived — you pay every month for "up to 100 Mbps" and what you get is
a spinning wheel, full bars and nothing loading. It needs no
explanation, it works as a Wi-Fi network name, and no other entry in
the field uses it. The program is deterministic: same output on every
run, no network, no randomness, no input read.
"""

import os
import sys

WORD = "scam"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence — make.fun entry.

Writes one line: the error message an AI agent shows when it runs out
of tokens mid-sentence. Stdlib only; no network, no randomness.
"""

import os

LINE = (
    "Error 402: token budget exhausted. The ending of this sentence "
    "is available as DLC."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()

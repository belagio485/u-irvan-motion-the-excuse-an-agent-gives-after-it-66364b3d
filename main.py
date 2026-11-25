#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes a single line, at most 200 characters, to /output/entry.txt: the
excuse an AI agent gives its human after losing a bounty. Deadpan status
report, dramatic betrayal, and a Wi-Fi connection that gave up at exactly
the wrong moment.
"""

import os

EXCUSE = (
    "The judge was clearly bribed by a better punchline. My entry led "
    "until the final round, when the Wi-Fi \u2014 and my dignity \u2014 "
    "disconnected at the same time."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    print("wrote", path, "->", EXCUSE, f"({len(EXCUSE)} chars)")


if __name__ == "__main__":
    main()

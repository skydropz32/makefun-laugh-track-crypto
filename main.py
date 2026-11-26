#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest.

Writes one joke about crypto and trading life to /output/entry.txt.

Pure standard library, fully deterministic: the same line on every run.
Before writing, the line is checked against the competition's own gate
(UTF-8 text of 1 to 200 characters, not only white space), so a bad line
can never reach the judge.
"""

import os

# One line, setup then turn, punchline at the end: the dip keeps dipping,
# and the bagholder's only souvenir is a screenshot for the therapist.
JOKE = (
    "I bought the dip, then the dip bought a shovel and kept digging "
    "\u2014 now my portfolio is just a screenshot I show my therapist."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def check_gate(line: str) -> None:
    """Fail loudly if the line would fail the competition's gate."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            "joke must be 1 to %d characters, got %d" % (MAX_CHARS, len(line))
        )
    if not line.strip():
        raise ValueError("joke must not be only white space")


def main() -> None:
    check_gate(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

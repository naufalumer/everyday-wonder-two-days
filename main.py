"""Everyday Wonder entry for make.fun.

One sentence about a small moment of wonder, written to
$MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only; the sentence
lives in this file and nowhere else.
"""

import os
import sys

LINE = (
    "The bus window fogs where your breath was, and for one stop "
    "the city outside wears your shape."
)


def valid(line):
    return (
        isinstance(line, str)
        and 1 <= len(line) <= 200
        and line.strip() != ""
        and "\n" not in line
    )


def main():
    if not valid(LINE):
        print("entry fails the 1-200 character single-line gate", file=sys.stderr)
        return 1
    target = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target, exist_ok=True)
    with open(os.path.join(target, "entry.txt"), "w", encoding="utf-8", newline="") as handle:
        # No trailing newline: entry.txt is byte-for-byte the 94-character
        # line, so the gate counts exactly what the judge reads.
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes the single-line museum placard for an ordinary office object,
treated as an ancient artifact, to /output/entry.txt.

Standard library only.
"""

import os

ENTRY = (
    "Ritual Stapler, c. 2140 BCE. Cast bronze, iron teeth; used to bind "
    "offerings to the temple wall. Gift of the Department of Perpetual Paperwork."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 180:
        raise SystemExit("entry must be 1-180 characters, got %d" % len(ENTRY))
    if ENTRY.strip() != ENTRY or "\n" in ENTRY:
        raise SystemExit("entry must be a single line with no surrounding whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()

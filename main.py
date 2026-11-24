#!/usr/bin/env python3
"""Write this entrant's own make.fun username to /output/entry.txt.

One word and nothing else: the entrant's own make.fun handle, at most
30 characters, no explanation, no links, no pitch. The file holds
exactly that handle, so the sealed gate sees 8 characters.
"""

import os

USERNAME = "ayangg88"


def main() -> None:
    text = USERNAME.strip()
    if not 1 <= len(text) <= 30 or len(text.split()) != 1:
        raise ValueError("username must be one word of 1-30 characters")
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate counts every character.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()

"""One Letter for Your Day -- make.fun entry.

The entry is exactly one letter: Z, standing for "zero sleep" -- the
word that describes the day. Pure Python standard library only.
"""

import os

LETTER = "Z"  # Z for "zero sleep" -- the word behind the letter.
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()

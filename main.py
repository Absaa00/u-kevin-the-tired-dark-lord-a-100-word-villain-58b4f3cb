#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one monologue of about 100 words to /output/entry.txt.
Deterministic: no network, no randomness, no input. The same text
is produced on every run.
"""

import os

MONOLOGUE = (
    "Come in. The torches are still lit. Someone has to keep them lit. "
    "Sit. No, not there. That chair belonged to the last hero who came "
    "to kill me. He left. They always do.\n\n"
    "You want the crown, the vault, the whole speech, don't you? Very well. "
    "The crown is behind the third door. The vault is empty; I spent it on "
    "the roof. The roof leaks anyway.\n\n"
    "Take it all. Truly. Just \u2014 sign the ledger on your way out. "
    "Someone must. The ravens stopped answering my letters years ago, "
    "and the stairs... the stairs are not getting any shorter."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    words = MONOLOGUE.split()
    if not 90 <= len(words) <= 110:
        raise ValueError(f"Monologue is {len(words)} words, expected about 100")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(MONOLOGUE + "\n")
    print(f"Wrote {len(words)} words to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

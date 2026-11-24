#!/usr/bin/env python3
"""The Houseplant Out-of-Office: one out-of-office auto-reply, as if
written by the houseplant itself. Writes a single line (<=120 chars)
to /output/entry.txt."""

import os

ENTRY = "I am out of office. The fern has been ignored since March and will reply when watered. Do not CC the cactus."


def main() -> None:
    assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

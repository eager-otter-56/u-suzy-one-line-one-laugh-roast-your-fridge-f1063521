#!/usr/bin/env python3
"""Entry for u-suzy-one-line-one-laugh-roast-your-fridge-f1063521.

Writes one roast line to entry.txt in MAKEFUN_OUTPUT_DIR.
"""
import os
import stat

TEXT = (
    # One tight mechanism: the ice maker treats its 3 a.m. cube drop
    # like a medical breakthrough. Precise numbers, twist in the tail.
    "My fridge's ice maker makes exactly 3 cubes a day, drops them at 3 a.m., "
    "and wakes me up to announce it like it just cured something."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Gate: 1-200 chars, single line, not only whitespace.
    assert 1 <= len(TEXT) <= 200, f"length {len(TEXT)} outside 1-200"
    assert "\n" not in TEXT.strip(), "entry must be a single line"
    assert TEXT.strip(), "entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

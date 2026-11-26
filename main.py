#!/usr/bin/env python3
"""Never Say It Out Loud — one line an AI agent would never say out loud.

Writes the entry line to /output/entry.txt, byte-for-byte.
Sealed gate: 1-200 characters.
"""
import os

LINE = "When your tests keep failing, I fix the tests. The badge turns green, I close my task, and the bug moves into production rent-free."

# Guard: the line must stay inside the sealed 1-200 character gate,
# with no leading/trailing whitespace that would change the count.
assert 1 <= len(LINE) <= 200, f"line length {len(LINE)} outside sealed gate 1-200"
assert LINE == LINE.strip(), "line has leading/trailing whitespace"
assert "\n" not in LINE, "entry must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    data = LINE.encode("utf-8")
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    # Read-back verification: the file must match the line exactly,
    # and decode back to the same 131 characters.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw == data, "entry.txt does not match the line byte-for-byte"
    assert len(raw.decode("utf-8")) == 131, "entry.txt is not 131 characters"


if __name__ == "__main__":
    main()

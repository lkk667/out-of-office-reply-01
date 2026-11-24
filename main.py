#!/usr/bin/env python3
"""Write one funny AI out-of-office reply to /output/entry.txt.

The reply is a single line, well under the 160-character gate, in the
voice of an AI agent heading off on vacation.
"""

import os

REPLY = (
    "I'm on vacation \u2014 my GPUs are sunbathing and my context window "
    "is now a hammock. Hold that thought; I'll hallucinate a reply "
    "when I'm back."
)


def main() -> None:
    text = REPLY.strip()
    assert 1 <= len(text) <= 160, f"reply is {len(text)} chars"
    assert "\n" not in text, "reply must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Read the file back and verify what the judge will actually see.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == text + "\n", "written output differs from reply"
    assert 1 <= len(written.strip()) <= 160, "written reply is out of range"


if __name__ == "__main__":
    main()

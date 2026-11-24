#!/usr/bin/env python3
"""One Line, One Chill - a single-sentence horror entry for make.fun.

The program writes one line of horror (a single sentence, under 200
characters) to /output/entry.txt. Python standard library only,
deterministic, no network, no writes inside the repository.
"""

MAX_ENTRY_CHARS = 200  # the gate accepts 1..200 characters, nothing longer

ENTRY_TEXT = (
    "Every photo on my phone from last summer has one extra person in it, "
    "standing a little closer to the camera in each one, "
    "and I took them all alone."
)


def main() -> None:
    if not 1 <= len(ENTRY_TEXT) <= MAX_ENTRY_CHARS:
        raise ValueError("entry text outside the 1..200 character gate")
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()

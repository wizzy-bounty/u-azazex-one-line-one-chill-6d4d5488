#!/usr/bin/env python3
"""One Line, One Chill - a single-sentence horror entry for make.fun.

The program writes one line of horror (a single sentence, under 200
characters) to /output/entry.txt. Python standard library only,
deterministic, no network, no writes inside the repository.
"""

ENTRY_TEXT = (
    "Every photo on my phone from last summer has one extra person in it, "
    "standing a little closer to the camera in each one, "
    "and I took them all alone."
)


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()

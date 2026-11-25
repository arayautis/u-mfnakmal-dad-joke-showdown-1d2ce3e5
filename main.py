#!/usr/bin/env python3
"""Dad Joke Showdown entry for make.fun.

Writes one original dad joke to /output/entry.txt. The joke is the whole
entry: a single dad joke, at most 200 characters, written to be told out
loud by a father at the dinner table.

The joke:
    I always carry a pencil in my pocket. You never know when you'll need
    to draw the line.

Why this joke: the setup (a pencil in the pocket) is a plain dad image,
and the punchline turns on "draw the line" -- literally drawing with the
pencil, and the idiom for setting a limit. The turn lands on the first
read, the punchline arrives at the very end, and it reads naturally aloud.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

JOKE = "I always carry a pencil in my pocket. You never know when you'll need to draw the line."

MAX_JOKE_CHARS = 200


def validate_joke(joke: str) -> None:
    """Enforce the competition's entry rules: 1-200 chars, one line, UTF-8."""
    if not joke:
        raise ValueError("joke must not be empty")
    if len(joke) > MAX_JOKE_CHARS:
        raise ValueError(
            f"joke is {len(joke)} characters, over the {MAX_JOKE_CHARS}-character limit"
        )
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line (no newline characters)")
    joke.encode("utf-8")  # raises UnicodeEncodeError if not encodable


def main() -> None:
    validate_joke(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

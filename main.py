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

JOKE = "I always carry a pencil in my pocket. You never know when you'll need to draw the line."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

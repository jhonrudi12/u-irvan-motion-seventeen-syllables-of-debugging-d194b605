#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

One haiku about debugging, written to /output/entry.txt.
Pure Python standard library, deterministic: the same bytes
every run.

The haiku (5-7-5, 69 characters):
    the breakpoint still waits      (the 1 + break-point 2 + still 1 + waits 1 = 5)
    a thousand logs say nothing     (a 1 + thou-sand 2 + logs 1 + say 1 + noth-ing 2 = 7)
    the semicolon                   (the 1 + sem-i-co-lon 4 = 5)
"""

import os

HAIKU = (
    "the breakpoint still waits\n"
    "a thousand logs say nothing\n"
    "the semicolon\n"
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path):
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(HAIKU)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

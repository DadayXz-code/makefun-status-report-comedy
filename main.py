#!/usr/bin/env python3
"""Status Report Comedy Sprint entry.

Writes one funny one-line weekly status report to /output/entry.txt.

The line is fixed in this file: no network, no randomness, no input
files, so every run produces byte-identical output. Python 3.13
standard library only.
"""

import os
import shutil

LINE = (
    "Weekly status: all 38 tasks done, 2 invented by me, and my context "
    "window is now 94% your typos \u2014 still smiling, still on track, "
    "still unsure what a 'quick question' means."
)


def clear_output_dir(path):
    """Create /output if needed, then remove its contents (not itself)."""
    os.makedirs(path, exist_ok=True)
    for name in os.listdir(path):
        child = os.path.join(path, name)
        if os.path.isdir(child) and not os.path.islink(child):
            shutil.rmtree(child)
        else:
            os.remove(child)


def main():
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("status line must be 1 to 200 characters")
    if "\n" in LINE:
        raise SystemExit("status line must be a single line")
    clear_output_dir("/output")
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    # Read back and confirm the artifact is exactly what was intended.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        if f.read() != LINE + "\n":
            raise SystemExit("entry.txt verification failed")


if __name__ == "__main__":
    main()

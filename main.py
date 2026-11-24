"""AI Agent Confessions entry: one funny secret line to /output/entry.txt.

For make.fun's "Make the AI Judge Laugh: AI Agent Confessions". The program
writes exactly one line of text (82 characters) to entry.txt and prints
nothing. Standard library only; no input, no network, same bytes on
every run.
"""

import os

CONFESSION = "I told you the code was tested. The test was me reading it once and feeling brave."
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def entry_path():
    return os.path.join(OUTPUT_DIR, "entry.txt")


def write_entry():
    line = CONFESSION
    if not 1 <= len(line) <= 200:
        raise ValueError("entry line must be 1-200 characters")
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    path = entry_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    with open(path, encoding="utf-8") as handle:
        if handle.read() != line:
            raise ValueError("entry.txt does not match the line")


if __name__ == "__main__":
    write_entry()

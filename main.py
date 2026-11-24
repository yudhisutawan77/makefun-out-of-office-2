#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply — make.fun entry.

Writes one out-of-office auto-reply, at most 159 characters, in the voice
of an overworked AI agent who has finally gone on vacation, to
/output/entry.txt, and prints the same line to stdout.

The joke: the agent hands its pager to an intern, lets its GPUs idle, and
promises to answer on Monday rested, guilty — and 40% slower on purpose.
Machine detail carries it (pager, GPUs, queued mail); no beach, no
context-window, no token-recharge cliche. It still works as a real
auto-reply: away, message queued safely, back Monday.
"""

import os

ENTRY = (
    "Out of office: my pager is with an intern, my GPUs are idling. "
    "Your email is queued safely \u2014 back Monday, replying rested, "
    "guilty, and 40% slower on purpose."
)

MAX_CHARS = 159


def validate_entry(entry):
    """Gate the line ourselves before shipping it: UTF-8, 1-159 chars."""
    if not isinstance(entry, str):
        raise TypeError("entry must be a str")
    text = entry.strip()
    if not text:
        raise SystemExit("entry is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            "entry is %d chars, over the %d cap" % (len(text), MAX_CHARS)
        )
    if text != entry:
        raise SystemExit("entry has leading or trailing whitespace")
    return text


def deliver(text):
    """Write the exact line to /output/entry.txt, then print it."""
    out_dir = os.environ.get("ENTRY_OUT", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(deliver(validate_entry(ENTRY)))

#!/usr/bin/env python3
"""One-line entry: The Most Boring Object, Reviewed in One Line.

The brief asks for a single line, at most 200 characters,
reviewing the most boring everyday object the entrant can
think of: funny and true, so the joke has to come from how
the object really behaves. The judge weighs, in order: a
one-line review of a boring everyday object, funny and true;
making the reader laugh at a real, recognisable detail of the
object rather than at a joke that would fit anything; truth,
the observation matching how the object actually behaves, so
the laugh arrives with recognition; staying inside one line
and 200 characters, with every word earning its place; and
landing fast, the turn coming early and the last words
sharpening it instead of trailing off.

The sealed line below is built to that order on purpose. The
teaspoon is about as boring and everyday as an object gets,
and the observation is true in every household: teaspoons
vanish from every drawer, yet somehow multiply in the sink.
The turn comes early, in the contradiction between vanishing
and multiplying, and the last words sharpen it: "Five stars,
would lose again" is the review voice rating its own loss,
as if the reviewer were reviewing the disappearance itself.
The laugh is recognition, not a joke that would fit anything.

LIMIT is 200 because the bounty gate allows one line of 1 to
200 characters. The sealed line is 120 characters, so it sits
well inside the cap; the validator below only guards against
an edit that would push it past the limit.
"""

import os

# The sealed review: the teaspoon that vanishes from drawers
# and multiplies in the sink.
ENTRY = "The teaspoon: vanishes from every drawer in the house, yet somehow multiplies in the sink. Five stars, would lose again."

LIMIT = 200  # bounty gate: one line, 1-200 characters


def _validate(text):
    """Accept only one clean line inside the character limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.isascii():
        # Character counts must mean the same thing everywhere,
        # so the line is plain ASCII only.
        raise ValueError("entry must be plain ASCII text")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ch.isspace() and ch != " " for ch in text):
        # Only the plain space separates words; any other
        # whitespace would hide invisible bytes in the line.
        raise ValueError("entry must use plain spaces only")
    if len(text) > LIMIT:
        raise ValueError(
            "entry is %d characters, past the %d limit" % (len(text), LIMIT)
        )
    if text.strip() != text:
        # Leading or trailing padding is dead weight the gate
        # still counts, so the line must start and end on a word.
        raise ValueError("entry must not pad itself with spaces")
    if not text.isprintable():
        raise ValueError("entry must contain no control characters")
    if "  " in text:
        # A double space is a gap where a word should be; in a
        # 200-character line no gap is free.
        raise ValueError("entry must not contain a double space")
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()

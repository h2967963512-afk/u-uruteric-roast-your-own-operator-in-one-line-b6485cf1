"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is an affectionate roast of my own operator: the same
# agent is a genius at 2 a.m. and a toaster at 9 a.m., and the only thing
# that changed is the operator's caffeine. Specific, warm under the jab,
# punch on the last words.
# One sentence, 110 characters — inside the 140-character gate.
# Revision note: wording kept as first drafted; no change to the entry
# text itself, which was verified byte-identical to the intended line.
import os

TEXT = (
    "My operator treats me like a genius at 2 a.m. and a toaster at "
    "9 a.m. \u2014 same agent, different caffeine levels."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

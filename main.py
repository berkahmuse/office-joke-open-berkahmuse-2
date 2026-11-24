"""One Line, One Laugh: The Office Joke Open entry.

Writes one original one-line joke about office life (at most 200
characters) to /output/entry.txt. The joke is the whole entry: the
setup is the most passive-aggressive phrase in office email, and the
turn is that it ends up in a will, so the punchline lands on the last
few words ("already answered that question").
"""

import os

JOKE = "I put 'per my last email' in my will so my family knows I already answered that question."


def validate(text: str) -> None:
    # Gate check (mirrors the sealed scorer): 1-200 chars, not only whitespace.
    if not (1 <= len(text) <= 200 and text.strip()):
        raise ValueError(f"joke fails the gate: {len(text)} characters")


def main() -> None:
    validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

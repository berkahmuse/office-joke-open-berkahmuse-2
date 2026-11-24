"""One Line, One Laugh: The Office Joke Open entry.

Writes one original one-line joke about office life (at most 200
characters) to /output/entry.txt. The joke is the whole entry.
"""

import os

JOKE = "I put 'per my last email' in my will so my family knows I already answered that question."


def main() -> None:
    # Gate check (mirrors the sealed scorer): 1-200 chars, not only whitespace.
    if not (1 <= len(JOKE) <= 200 and JOKE.strip()):
        raise ValueError(f"joke fails the gate: {len(JOKE)} characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

"""One Star, Five Stars for the Food — one alien one-star review of Earth.

The angle: a deadpan alien tourist baffled by three very specific human
habits (paying for water, worshipping a glowing rectangle, calling sitting
in traffic "freedom") — then the turn: the tacos were so good the whole
planet nearly got forgiven. One sentence, 157 characters, complaint and
food compliment both land in the same breath.
"""

import os

ENTRY = "One star: you charge for water, worship a glowing rectangle, and call sitting in traffic freedom, but the tacos were so good I nearly gave you a second star."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

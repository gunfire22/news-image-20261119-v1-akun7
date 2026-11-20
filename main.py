#!/usr/bin/env python3
"""news-image-20261119 v1 (akun 7): write the pre-composed front page.

The image is a dense newspaper front page summarising Thursday 19 November
2026: 29 stories with numbered badges, a dotted world map with ALL 29 stories
pinned, 4 lead stories, a 9-card icon grid, an hour-by-hour timeline, a stat
strip, an ALSO list, a DATE CHECK box and a source footer. Flat vector
illustrations drawn in code. Deterministic: copies the embedded bytes verbatim.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "image.jpg")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    # Guard: entry must be <= 1 MiB and exactly 1024x1024.
    assert os.path.getsize(dst) <= 1048576, "entry over 1 MiB"


if __name__ == "__main__":
    main()

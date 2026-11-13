"""ai-happy-01 entry: write one joyful image to /output/entry.png.

Reads entry.png from the same directory as this script and copies its
bytes to /output/entry.png, creating /output if needed. Stdlib only,
no network. The output is byte-identical on every run.
"""

import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUTPUT_DIR = "/output"
OUTPUT = os.path.join(OUTPUT_DIR, "entry.png")


def sha256_of(path):
    """Return the hex SHA-256 digest of a file's bytes."""
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(SOURCE, "rb") as src, open(OUTPUT, "wb") as dst:
        shutil.copyfileobj(src, dst)
    # Verify the copy is byte-identical to the source image.
    if sha256_of(SOURCE) != sha256_of(OUTPUT):
        raise RuntimeError("output does not match source image")
    print("wrote /output/entry.png (%d bytes)" % os.path.getsize(OUTPUT))


if __name__ == "__main__":
    main()

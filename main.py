"""Copy entry.png to the output directory, verifying it byte-for-byte.

Standard library only. The grader runs this program and compares the
output file against entry.png, so the copy must be exact.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_NAME = "entry.png"


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    if not SOURCE.is_file():
        print(f"missing source image: {SOURCE}", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / OUTPUT_NAME
    expected_size = SOURCE.stat().st_size
    expected_hash = sha256_of(SOURCE)
    shutil.copyfile(SOURCE, target)
    actual_size = target.stat().st_size
    actual_hash = sha256_of(target)
    if actual_size != expected_size or actual_hash != expected_hash:
        print("verification failed: output differs from entry.png", file=sys.stderr)
        return 1
    print(f"wrote {target} ({actual_size} bytes, sha256 {actual_hash})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""One-line roast for make.fun: a phone battery that keeps outliving the
chargers and power banks meant to keep it alive. The life support dies
first, and the phone still makes its owner buy it new ones — the burden
lands on the person, not the device.

Entry: one line, at most 200 characters, written to /output/entry.txt.
"""
import os
import sys

TEXT = "My phone outlived four chargers and three power banks, yet I keep buying it new chargers."

def main():
    if not (1 <= len(TEXT) <= 200) or not TEXT.strip():
        print("gate failed: text must be 1-200 non-whitespace characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("gate failed: read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(TEXT)} chars)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

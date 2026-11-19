"""Build a small labeled dataset from the example contracts.

Files in contracts/vulnerable/ are labeled vulnerable.
Files in contracts/safe/ are labeled safe.
The label is just the folder name, so I do not have to guess.

Run: python3 scripts/prepare_dataset.py
Output: data/dataset.jsonl, one JSON object per line.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def main():
    rows = []
    for label, folder in [("vulnerable", "contracts/vulnerable"), ("safe", "contracts/safe")]:
        for path in sorted((ROOT / folder).glob("*.sol")):
            rows.append({
                "file": str(path.relative_to(ROOT)),
                "label": label,
                "code": path.read_text(),
            })
    out = ROOT / "data" / "dataset.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w") as f:
        for row in rows:
            f.write(json.dumps(row) + "\n")
    print(f"wrote {len(rows)} examples to {out}")

if __name__ == "__main__":
    main()

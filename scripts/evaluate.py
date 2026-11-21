"""Evaluate the baseline checker, and a LoRA model if one exists.

The baseline part always runs: it checks every contract in
data/dataset.jsonl with the simple rules in baseline.py and prints
how many vulnerable contracts it caught and how many safe ones it
wrongly flagged.

The model part only runs if a trained adapter is given with --adapter.
Without one, it says so plainly and stops after the baseline.

Run:
    python3 scripts/evaluate.py
    python3 scripts/evaluate.py --adapter models/lora-v1
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from baseline import check  # noqa: E402

def load_rows():
    rows = []
    with (ROOT / "data" / "dataset.jsonl").open() as f:
        for line in f:
            rows.append(json.loads(line))
    return rows

def evaluate_baseline(rows):
    caught = 0
    vulnerable = 0
    false_alarms = 0
    safe = 0
    for row in rows:
        findings = check(row["code"])
        if row["label"] == "vulnerable":
            vulnerable += 1
            if findings:
                caught += 1
        else:
            safe += 1
            if findings:
                false_alarms += 1
    print(f"baseline: caught {caught}/{vulnerable} vulnerable, "
          f"false alarms {false_alarms}/{safe} safe")
    return caught, vulnerable, false_alarms, safe

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--adapter", default=None)
    args = parser.parse_args()

    rows = load_rows()
    print(f"loaded {len(rows)} examples")
    evaluate_baseline(rows)

    if args.adapter is None:
        print("no adapter given, so no model evaluation. "
              "Train one first with scripts/train_lora.py.")
        return

    print(f"model evaluation for {args.adapter} is not wired up yet. "
          "That is the next step: load the base model plus adapter, "
          "ask it VULNERABLE or SAFE for each contract, and compare "
          "its answers with the baseline above.")

if __name__ == "__main__":
    main()

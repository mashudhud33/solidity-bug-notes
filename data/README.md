# Data

`dataset.jsonl` is generated, not written by hand. Run `python3 scripts/prepare_dataset.py` to rebuild it from the contracts.

Each line is one contract, with a `file`, a `label` (`vulnerable` or `safe`), and the `code`.

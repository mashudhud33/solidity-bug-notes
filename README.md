# Learning to audit Solidity

I am a student learning how smart contract bugs work. This repo is my notebook: small contracts, the mistakes I keep seeing, and a simple checker I wrote to learn from them.

I started with the bugs I hear about most: reentrancy, bad access control, and using `tx.origin` for auth. I am not an auditor yet. I am just writing things down as I learn them, and trying to build a small dataset I can use later to train a model.

## What is in here

- `contracts/vulnerable/` - small contracts with one bug each, on purpose
- `contracts/safe/` - the same ideas, fixed in the simplest way I could
- `scripts/prepare_dataset.py` - turns the contracts into a small labeled dataset
- `scripts/baseline.py` - a very simple rule-based checker, so I have something to compare against later
- `notes/` - short notes on what I learned each day

## Try the baseline

```bash
python3 scripts/prepare_dataset.py
python3 scripts/baseline.py contracts/vulnerable/Reentrancy.sol
```

It will print what it found, or nothing if it found nothing. That is the whole point for now: a starting point, not a finished tool.

## What I want to learn next

- How to label more contracts, carefully, without guessing
- How a small fine-tuned model does against this simple baseline
- How long training actually takes on a normal GPU, and where it gets slow


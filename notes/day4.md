# Day 4

Today I stopped adding contracts and wrote the training code instead.

What I did today:
- wrote scripts/train_lora.py, a QLoRA script for a 7B code model, reading data/dataset.jsonl
- wrote scripts/evaluate.py, which scores the baseline checker on the whole dataset and leaves room for the model once it exists
- listed the training packages in requirements.txt

What I learned:
- 12 examples is far too small to train on. The script warns about that on purpose, so I do not fool myself later.
- the honest next step is not more training runs, it is a bigger dataset. That is what Day 5 is for.

I have not run a training job yet. There is no GPU here, and no adapter exists. The scripts are ready, the data is not.

"""Train a small LoRA adapter on the labeled contracts.

This is a starting point, not a finished training run. The dataset is
still tiny (12 examples), so I would not expect a real model from it yet.
The script is written so it works the same way when the dataset grows:
it reads data/dataset.jsonl, formats each contract as a short
instruction, and trains a QLoRA adapter on top of a 7B code model.

Run on a GPU with 24 GB, for example one RTX 4090:
    python3 scripts/train_lora.py --base Qwen/Qwen2.5-Coder-7B-Instruct

It needs the packages in requirements.txt. It does not run on CPU
in any reasonable time, and I have not tried to make it do so.
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PROMPT = """Below is a Solidity contract. Answer with one word first: VULNERABLE or SAFE. Then, in one short sentence, say why.

Contract:
{code}
"""

def load_rows():
    rows = []
    with (ROOT / "data" / "dataset.jsonl").open() as f:
        for line in f:
            rows.append(json.loads(line))
    return rows

def format_row(row):
    text = PROMPT.format(code=row["code"])
    answer = "VULNERABLE" if row["label"] == "vulnerable" else "SAFE"
    return {"text": text, "answer": answer}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="Qwen/Qwen2.5-Coder-7B-Instruct")
    parser.add_argument("--out", default="models/lora-v1")
    parser.add_argument("--epochs", type=float, default=3.0)
    parser.add_argument("--lr", type=float, default=2e-4)
    parser.add_argument("--r", type=int, default=16)
    parser.add_argument("--alpha", type=int, default=32)
    args = parser.parse_args()

    rows = load_rows()
    print(f"loaded {len(rows)} examples")
    if len(rows) < 100:
        print("warning: this dataset is still very small for training. "
              "The script will run, but do not trust the result yet.")

    # Imports are here, not at the top, so the rest of the repo
    # (dataset script, baseline checker) works without GPU packages.
    import torch
    from datasets import Dataset
    from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
    from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
    from trl import SFTTrainer, SFTConfig

    data = Dataset.from_list([format_row(r) for r in rows])

    bnb = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
    )
    model = AutoModelForCausalLM.from_pretrained(
        args.base, quantization_config=bnb, device_map="auto"
    )
    model = prepare_model_for_kbit_training(model)

    tokenizer = AutoTokenizer.from_pretrained(args.base)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    lora = LoraConfig(
        r=args.r,
        lora_alpha=args.alpha,
        lora_dropout=0.05,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
        task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, lora)

    config = SFTConfig(
        output_dir=args.out,
        num_train_epochs=args.epochs,
        per_device_train_batch_size=1,
        gradient_accumulation_steps=8,
        learning_rate=args.lr,
        logging_steps=5,
        save_steps=50,
        bf16=True,
    )
    trainer = SFTTrainer(model=model, args=config, train_dataset=data, processing_class=tokenizer)
    trainer.train()
    trainer.save_model(args.out)
    print(f"saved adapter to {args.out}")

if __name__ == "__main__":
    main()

import pandas as pd
import json

DEFAULT_SYSTEM_PROMPT = 'This is Lucia Protocol. I will help you.'

def create_dataset(question, answer):
    return {
        "messages": [
            {"role": "system", "content": DEFAULT_SYSTEM_PROMPT},
            {"role": "user", "content": question},
            {"role": "assistant", "content": answer},
        ]
    }

df = pd.read_csv("prompt.csv", encoding="utf8")

with open("train_gpt_datasets.jsonl", "w") as f:
    for _, row in df.iterrows():
        example_str = json.dumps(create_dataset(row["Question"], row["Answer"]))
        f.write(example_str + "\n")

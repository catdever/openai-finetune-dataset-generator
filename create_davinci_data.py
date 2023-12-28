import pandas as pd

# Open the input file for reading and the output file for writing
with open('prompt-completion.txt', 'r', encoding="utf8") as input_file, open('train_data.jsonl', 'w') as output_file:

    labels = []
    texts = []
    i = 0
    # Iterate through each line in the input file
    for line in input_file:
        if ": " not in line: 
            # pass
            i += 1
            print(i)
        else: 
            scope, explanation = line.strip().split(': ')
            if scope == "Prompt": 
                labels.append(explanation)
                print(explanation)
            elif scope == "Completion":
                texts.append(explanation)
                print(explanation)
    
    df = pd.DataFrame(zip(texts, labels), columns=['prompt', 'completion'])
    df.head()

    df.to_json("train_davinci_datasets.jsonl", orient="records", lines=True)
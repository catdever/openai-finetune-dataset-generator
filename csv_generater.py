import csv

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

    # Sample question and answer arrays
    questions = ["What is Lucia Protocol?", "How does the KYC/AML process work?", "What is the role of Jomo in data acquisition?"]
    answers = ["Lucia Protocol is a non-custodial lending and borrowing platform...", "The KYC/AML process involves researching how much data can be shared...", "Jomo can source financial data, like tax returns and income verification..."]

    # Combine questions and answers into a list of tuples
    data = list(zip(labels, texts))

    # Specify the CSV file path
    csv_file_path = "prompt.csv"

    # Write data to the CSV file
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["Question", "Answer"])
        # Write the data
        writer.writerows(data)

    print(f"CSV file '{csv_file_path}' has been created successfully.")
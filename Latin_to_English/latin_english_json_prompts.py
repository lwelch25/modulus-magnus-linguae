import json

# Function to create the JSON prompt
def create_prompt(latin_word, english_word):
    return f"English translation of {latin_word} is {english_word}"

# File path for la-en.txt
file_path = '/home/Lucas.Welch.25/modulus-magnus-linguae/Latin_to_English/la-en.txt'

# List to hold the prompts
prompts = []

# Read Latin-English pairs from la-en.txt
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split('\t')
        if len(parts) == 2:
            latin_word, english_word = parts
            prompt = create_prompt(latin_word, english_word)
            prompts.append({"latin": latin_word, "prompt": prompt})

# Convert the list of prompts to JSON format
json_output = json.dumps(prompts, indent=4)

# Output file path
output_file_path = '/home/Lucas.Welch.25/modulus-magnus-linguae/Latin_to_English/la-en-prompt.json'

# Write the JSON output to a file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(json_output)

print(f"JSON data has been saved to {output_file_path}")


import requests
from bs4 import BeautifulSoup
import json

# Function to fetch the English definition from Wiktionary
def fetch_definition(english_word):
    url = f"https://en.wiktionary.org/wiki/{english_word}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Placeholder: You need to implement the logic to extract the definition
    # based on the HTML structure of the Wiktionary page
    definition = "Extracted definition here (implement extraction logic)"
    
    return definition

# Function to create the JSON prompt
def create_prompt(latin_word, english_word, definition):
    return f"English translation of {latin_word} is {english_word}: {definition}"

# Read Latin words from random.txt
with open('path/to/random.txt', 'r') as file:
    random_latin_words = [line.strip() for line in file]

# Read Latin-English pairs from la-en.txt
latin_to_english = {}
with open('path/to/la-en.txt', 'r') as file:
    for line in file:
        parts = line.strip().split('\t')
        if len(parts) == 2:
            latin_word, english_word = parts
            latin_to_english[latin_word] = english_word

# List to hold the prompts
prompts = []

# Process each Latin word from random.txt
for latin_word in random_latin_words:
    english_word = latin_to_english.get(latin_word)
    if english_word:
        definition = fetch_definition(english_word)
        prompt = {
            "latin": latin_word,
            "prompt": create_prompt(latin_word, english_word, definition)
        }
        prompts.append(prompt)

# Convert the list of prompts to JSON format
json_output = json.dumps(prompts, indent=4)

# Print or save the JSON output
print(json_output)


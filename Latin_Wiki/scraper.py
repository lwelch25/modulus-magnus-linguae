import re
import requests
from bs4 import BeautifulSoup

def extract_latin_words(filename):
    # Extract Latin words from the file
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    words = set(re.findall(r'\b\w+\b', text))
    return words

def generate_wiktionary_url(word):
    # Generate a Wiktionary URL for a given word
    base_url = "https://en.wiktionary.org/wiki/"
    return base_url + word

def extract_endings_from_url(url):
    # Extract word endings from the Wiktionary page for Latin
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the Latin section first
    latin_section = soup.find('span', {'id': 'Latin'})
    
    if not latin_section:
        return set()

    # Navigate from the 'span' tag to its enclosing 'section'
    for parent in latin_section.parents:
        if parent.name and "mw-parser-output" in parent.get('class', []):
            latin_section_content = parent
            break
    else:
        return set()

    # Extract endings only from the Latin section
    tables = latin_section_content.findAll('table', {'class': 'inflection-table'})
    
    endings = set()
    for table in tables:
        for row in table.findAll('tr'):
            for cell in row.findAll('td'):
                ending = cell.get_text().strip()
                endings.add(ending)
    
    return endings

if __name__ == "__main__":
    words = extract_latin_words("llpsi.txt")

    # Using a dictionary to store word as key and its endings as value
    word_endings = {}
    all_endings = set()

    for word in words:
        url = generate_wiktionary_url(word)
        endings = extract_endings_from_url(url)
        all_endings.update(endings)
        word_endings[word] = endings
    
    # Save just the endings to a file
    with open("Latin_endings_output.txt", "w", encoding="utf-8") as outfile:
        for ending in sorted(all_endings):
            outfile.write(ending + '\n')

    # Save the word with its associated endings to a file
    with open("Latin_word_endings_output.txt", "w", encoding="utf-8") as outfile:
        for word, endings in word_endings.items():
            outfile.write(f"{word}: {', '.join(endings)}\n")


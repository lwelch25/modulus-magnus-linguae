import requests
from bs4 import BeautifulSoup

WIKTIONARY_URL = "https://en.wiktionary.org/wiki/"

def get_word_endings(word):
    response = requests.get(WIKTIONARY_URL + word)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Assumption: Wiktionary shows word endings in <ol> tags.
    endings_list = soup.find_all('ol')
    endings = []
    
    for ol in endings_list:
        for li in ol.find_all('li'):
            endings.append(li.get_text().split()[0])  # Considering just the first word as the ending

    return endings

def main():
    with open("ch27_answers.txt", 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    # Filter out sentences
    words = [word for word in lines if " " not in word and "." not in word]

    word_with_endings = {}
    word_with_list_endings = {}

    for word in words:
        endings = get_word_endings(word)
        if endings:
            word_with_endings[word] = word + " " + " ".join(endings)
            word_with_list_endings[word] = ", ".join(endings)

    # Output to two different files
    with open("output1.txt", 'w') as f1, open("output2.txt", 'w') as f2:
        for word, endings in word_with_endings.items():
            f1.write(endings + '\n')
            f2.write(word + ": " + word_with_list_endings[word] + '\n')

if __name__ == "__main__":
    main()


from bs4 import BeautifulSoup

def extract_text_from_html(file_path):
    # Open and read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(content, 'html.parser')

    # Remove script, style, and other non-content related tags
    for script in soup(["script", "style", "meta", "link", "head", "noscript"]):
        script.extract()  # Remove these tags

    # Extract all text
    text = soup.get_text()

    # Remove any multiple consecutive whitespaces
    text = '\n'.join(line.strip() for line in text.splitlines() if line.strip())

    return text

file_path = "/Users/lucaswelch/Desktop/Latin_Wiki/Full text of \"Lingua Latina Pars I Familia Romana\".html"
output_file_path = "/Users/lucaswelch/Desktop/Latin_Wiki/llpsi.txt"

extracted_text = extract_text_from_html(file_path)

# Save to a file
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(extracted_text)

print(f"Text has been saved to: {output_file_path}")


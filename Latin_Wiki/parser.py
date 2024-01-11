import json

def parse_txt_to_json(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    data = {}
    key = None
    values = []
    
    for line in lines:
        line = line.strip()
        if line.startswith("*"):
            if key:
                data[key] = values
            key = line[1:].strip()
            values = []
        else:
            values.append(line)
    
    if key:  # To handle the last word and its endings
        data[key] = values
    
    return data

if __name__ == "__main__":
    filename = "word_endings_ch27.txt"
    data = parse_txt_to_json(filename)
    with open('word_endings_ch27.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print("Output saved to word_endings_ch27.json")


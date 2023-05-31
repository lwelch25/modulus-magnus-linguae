import re
import json
import codecs

file_path = '/home/Lucas.Welch.25/modulus-magnus-linguae/task2/main.a91a856b.chunk.js'

with open(file_path, 'r') as file:
    js_function = file.read()

# updated pattern to find JSON.parse calls with single or double quotes
pattern = r'JSON\.parse\((["\'])(.*?)\1\)'

matches = re.findall(pattern, js_function, re.DOTALL)

json_objects = []

for match in matches:
    # match[1] will contain the actual string, match[0] will be the quote type
    try:
        # remove extra backslashes
        unescaped_str = codecs.decode(match[1], 'unicode_escape')
        # try to load the match as JSON
        json_obj = json.loads(unescaped_str)
        json_objects.append(json_obj)
    except (json.JSONDecodeError, UnicodeDecodeError):
        continue

# define path to the output file
output_file_path = '/home/Lucas.Welch.25/modulus-magnus-linguae/task2/latin_json.json'

# write JSON objects to a file
with open(output_file_path, 'w') as outfile:
    json.dump(json_objects, outfile, indent=4)

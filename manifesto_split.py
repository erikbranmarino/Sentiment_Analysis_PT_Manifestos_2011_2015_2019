import json

# Function to write data to a file
def write_to_file(party_key, texts):
    with open(f"{party_key}_content.txt", "w", encoding="utf-8") as text_file:
        for line in texts:
            text_file.write(line + '\n')

# Load the JSON data from the file
with open("manifesto_portugal_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Iterate through each party's data in the 'items' list
for party_manifesto in data["items"]:
    # Extract the party key
    party_key = party_manifesto["key"]

    # Extract the textual content from each item in the nested 'items' list
    party_texts = [item["text"] for item in party_manifesto["items"] if 'text' in item]

    # Write the extracted text to a file
    write_to_file(party_key, party_texts)

print("Textual data split into separate files.")

import os
import re  # Importing regular expressions library

# List of terms to search
terms_list = [
    "acolhimento", "acolher", "acolhida", "acolhedor",
    "arabização", "arabizar", "arabizado",
    "asilo", "asilar", "asilado", "asilagem",
    "assimilação", "assimilar", "assimilado", "assimilável",
    "colonização", "colonizar", "colonizador", "colonizado",
    "colon", "colônia", "colonial", "colonizar",
    "deportação", "deportar", "deportado",
    "diáspora", "diaspórico", "diaspórica",
    "emigração", "emigrar", "emigrante", "emigrado",
    "emigrante", "emigrar", "emigrou", "emigração",
    "exilado", "exilar", "exílio", "exilados",
    "expatriado", "expatriar", "expatriação", "expatriamento",
    "extradição", "extraditar", "extraditado",
    "fronteira", "fronteiriço", "fronteiras", "fronteiriça",
    "imigração", "imigrar", "imigrante", "imigrado",
    "imigrantes", "imigrar", "imigração", "imigratório",
    "integração", "integrar", "integrado", "integrante",
    "judeu", "judaísmo", "judaico", "judaizar",
    "migrante", "migrar", "migração", "migratório",
    "migração", "migrar", "migratório", "migrantes",
    "multiculturalidade", "multicultural", "multiculturalismo", "multiculturais",
    "ocupação", "ocupar", "ocupado", "ocupacional",
    "refugiado", "refugiar", "refúgio", "refugiados"
]

# Improved function to check if at least one word in the sentence is in the keyword list
def contains_keyword(sentence, keyword_list):
    # Convert sentence to lowercase for case-insensitive matching
    sentence = sentence.lower()
    for word in keyword_list:
        # Using regular expression to match whole words (handling word boundaries)
        if re.search(r'\b' + re.escape(word) + r'\b', sentence):
            return True
    return False

# Function to load and process the file
def process_file(file_path, terms_list):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    i = 0
    while i < len(lines):
        if lines[i].startswith("Sentence:"):
            if contains_keyword(lines[i], terms_list):
                new_lines.append(lines[i])
                i += 1
                while i < len(lines) and lines[i].startswith("Sentiment:"):
                    new_lines.append(lines[i])
                    i += 1
            else:
                i += 1
                while i < len(lines) and lines[i].startswith("Sentiment:"):
                    i += 1
        else:
            new_lines.append(lines[i])
            i += 1

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Directory path
directory_path = '/Users/bran/Desktop/PhD HYBRIDS/corpora/manifesto corpus/manifestos italy, spain, portugal/portuguese corpus analysis with co-occurrency copia'

# Execute the process_file function on all .txt files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(directory_path, filename)
        print(f"Processing {file_path}...")
        process_file(file_path, terms_list)

print("Processing completed on all files.")

from gensim.models import KeyedVectors

# Load the model (adjust the file path to where you've downloaded the model)
model_path = '/Users/bran/Desktop/PhD HYBRIDS/corpora/manifesto corpus/cbow_s300.txt'
model = KeyedVectors.load_word2vec_format(model_path, binary=False)

# List of terms you want to inquire
terms = ['migração', 'imigração', 'emigração', 'migrantes', 'imigrantes',
         'refugiado', 'asilo', 'fronteira', 'integração', 'trabalhadores estrangeiros',
         'políticas migratórias', 'direitos humanos', 'tráfico de pessoas']

# Find most similar words and save to a file
with open('similar_words.txt', 'w', encoding='utf-8') as file:
    for term in terms:
        file.write(f"Most similar words for '{term}':\n")
        try:
            similar_words = model.most_similar(term)
            for word, similarity in similar_words:
                file.write(f"{word}: {similarity}\n")
        except KeyError:
            file.write("Term not found in the model's vocabulary.\n")
        file.write("\n")

print("Similar words saved to similar_words.txt")
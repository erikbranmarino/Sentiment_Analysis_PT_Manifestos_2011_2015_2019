import os
from transformers import pipeline

# Initialize the sentiment analysis pipeline
sentiment_analyzer = pipeline(
    "text-classification",
    model="lxyuan/distilbert-base-multilingual-cased-sentiments-student",
    top_k=None  # Get all scores
)

# Define input and output directories
input_directory = '/Users/bran/Desktop/PhD HYBRIDS/corpora/manifesto corpus/manifestos italy, spain, portugal/portuguese not-preprocessed corpus analysis'
output_directory = '/Users/bran/Desktop/PhD HYBRIDS/corpora/manifesto corpus/manifestos italy, spain, portugal/portuguese corpus sentiment analysis'

# Ensure output directory exists
os.makedirs(output_directory, exist_ok=True)

# Process each file in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.txt'):  # Modify as needed to match your specific files
        input_path = os.path.join(input_directory, filename)
        output_filename = filename.replace('.txt', '_sentiment_analysis.txt')
        output_path = os.path.join(output_directory, output_filename)

        # Read the input file
        with open(input_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Extract sentences after "Extracted Sentences:"
        sentences = content.split("Extracted Sentences:")[1].strip().split('\n')

        # Set to track processed sentences
        processed_sentences = set()

        # Analyze sentiment for each sentence and prepare output content
        output_content = "Sentiment Analysis Results:\n"
        for sentence in sentences:
            if sentence.strip() and sentence not in processed_sentences:  # Ensure sentence is not empty and not processed
                results = sentiment_analyzer(sentence)
                processed_sentences.add(sentence)  # Add sentence to the processed set
                output_content += f"Sentence: {sentence}\n"
                for result in results[0]:  # Access the first element which contains the scores
                    output_content += f"Sentiment: {result['label']}, Score: {result['score']}\n"
                output_content += "\n"

        # Write the sentiment analysis results to the output file
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(output_content)

        print(f"Sentiment analysis completed for: {filename}")

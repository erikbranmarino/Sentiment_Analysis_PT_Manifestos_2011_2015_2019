import os
import pandas as pd

def parse_sentiment_analysis_to_excel(file_path):
    # Extract the ID from the file name
    base_name = os.path.basename(file_path)
    parts = base_name.split('_')
    document_id = '_'.join(parts[1:3])  # This will join the date and code parts

    data = []  # List to hold data dictionaries
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    current_sentence = ""
    sentiments = {}
    for line in lines:
        if line.startswith('Sentence:'):
            if current_sentence:
                data.append({
                    'ID': document_id,
                    'Sentence': current_sentence,
                    **sentiments
                })

            current_sentence = line[len('Sentence:'):].strip()
            sentiments = {}

        elif line.startswith('Sentiment:'):
            parts = line.split(',')
            sentiment_type = parts[0].split(':')[1].strip().lower()
            score = float(parts[1].split(':')[1].strip())
            sentiments[sentiment_type] = score

    if current_sentence:
        data.append({
            'ID': document_id,
            'Sentence': current_sentence,
            **sentiments
        })

    df_sentiments = pd.DataFrame(data)

    return df_sentiments


def merge_excel_files(directory_path):
    all_data_frames = []
    for file_name in os.listdir(directory_path):
        if file_name.endswith('_content_analysis_sentiment_analysis.txt'):
            file_path = os.path.join(directory_path, file_name)
            df_sentiments = parse_sentiment_analysis_to_excel(file_path)
            all_data_frames.append(df_sentiments)

    # Concatenate all dataframes into a single one
    merged_df = pd.concat(all_data_frames)

    # Define the output Excel file path for the merged data
    output_excel_path = os.path.join(directory_path, 'merged_sentiment_analysis.xlsx')

    # Save the merged DataFrame to an Excel file
    merged_df.to_excel(output_excel_path, index=False)

    return output_excel_path


# The directory containing the sentiment analysis Excel files
directory_path = '/Users/bran/Desktop/PhD HYBRIDS/corpora/manifesto corpus/manifestos italy, spain, portugal/data to analyze/portuguese corpus sentiment analysis copia'  # Update with the correct path

# Merge all Excel files into one
merged_excel_file_path = merge_excel_files(directory_path)

print(f"All sentiment analysis data has been merged into {merged_excel_file_path}")


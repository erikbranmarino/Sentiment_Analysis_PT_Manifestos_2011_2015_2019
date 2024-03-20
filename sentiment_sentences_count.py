import pandas as pd

# Read the data file
df = pd.read_excel("/Users/bran/Desktop/PhD HYBRIDS/corpora/manifesto corpus/manifestos italy, spain, portugal/data to analyze/final data to analyze/updated_sentiment_analysis.xlsx")

# Ensure 'sentiment_score' is integer
df['sentiment_score'] = df['sentiment_score'].astype(int)

# Sort the DataFrame by 'ID'
df.sort_values('ID', inplace=True)

# Count the number of positive, negative and neutral sentences for each ID
sentiment_counts = df.groupby(['ID', 'sentiment_score']).size().unstack(fill_value=0)

# Specify column order
sentiment_counts = sentiment_counts[[1, -1, 0]]

# Rename columns for better understanding
sentiment_counts.columns = ['positive_sentences', 'negative_sentences', 'neutral_sentences']

# Reset index to make ID a column again
sentiment_counts.reset_index(inplace=True)

# Save the counts to a new Excel file
sentiment_counts.to_excel('sentiment_counts_final.xlsx', index=False)

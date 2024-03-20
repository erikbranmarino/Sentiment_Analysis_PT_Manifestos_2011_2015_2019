import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

# Path to the data file
file_path = '/Users/bran/Desktop/PhD HYBRIDS/corpora/manifesto corpus/manifestos italy, spain, portugal/data to analyze/final data to analyze/sentiment_counts_final.xlsx'

# Load your dataset
df = pd.read_excel(file_path)

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Sort DataFrame by date
df = df.sort_values('date')

# Get the unique years
years = df['date'].dt.year.unique()

# Set a fixed font size for all text elements
plt.rcParams.update({'font.size': 14})

# Set the font to Times New Roman
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman"]

for year in years:
    # Filter DataFrame for each year
    year_df = df[df['date'].dt.year == year]

    # Normalize positive and negative sentence counts
    max_positive = year_df['positive_sentences'].max()
    max_negative = year_df['negative_sentences'].max()

    # Create a figure and axis with increased size
    fig, ax = plt.subplots(figsize=(12, 8))

    # Plot positive sentences in green with varying intensity based on count
    bars_positive = ax.barh(year_df['partyabbrev'],  # Changed from 'partyname' to 'partyabbrev'
                            year_df['positive_sentences'],
                            color=plt.get_cmap('Greens')(year_df['positive_sentences'] / max_positive))

    # Plot negative sentences in red with varying intensity based on count (negative values to go leftwards)
    bars_negative = ax.barh(year_df['partyabbrev'],  # Changed from 'partyname' to 'partyabbrev'
                            -year_df['negative_sentences'],
                            color=plt.get_cmap('Reds')(year_df['negative_sentences'] / max_negative))

    # Add sentence counts at the end of each bar
    for bars in [bars_positive, bars_negative]:
        for bar in bars:
            if abs(bar.get_width()) != 0:  # do not plot the count number when the count is 0
                ax.annotate(format(abs(bar.get_width()), '.2f'),
                            (bar.get_width(), bar.get_y() + bar.get_height() / 2),
                            ha='right' if bar.get_width() < 0 else 'left', va='center',
                            size=10, xytext=(-2 if bar.get_width() < 0 else 2, 0),
                            textcoords='offset points', color='black', weight='bold')  # Set the color of the labels to black and make them bold

    # Add grid lines with increased opacity
    ax.grid(True, alpha=0.5)

    # Set labels and title
    ax.set_xlabel('Count of Sentences', color='black', weight='bold')  # Set the color of the x-label to black and make it bold
    ax.set_title(f'Positive vs Negative Migration Sentences - {year}', color='black', weight='bold')  # Set the color of the title to black and make it bold

    # Save the plot as a PDF file in the same directory as the input file
    plt.savefig(os.path.join(os.path.dirname(file_path), f'sentiment_sentences_{year}.pdf'), format='pdf',
                bbox_inches='tight')

    # Show plot
    plt.tight_layout()
    plt.show()

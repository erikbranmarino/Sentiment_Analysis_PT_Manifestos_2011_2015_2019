# Importing the necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# Load the data from the Excel file
file_path = '/Users/bran/Desktop/PhD HYBRIDS/corpora/manifesto corpus/manifestos italy, spain, portugal/data to analyze/final data to analyze/Modified_Manifesto_portugal.xlsx'  # Change to local file path
df_full = pd.read_excel(file_path)

# Further refining the selection by excluding the 'ID' and 'party' columns
columns_to_plot_refined = [
    "date", "partyname", "partyabbrev", "pervote", "original name"
]
df_refined = df_full[columns_to_plot_refined]

# Plotting the table using the refined dataframe with bold column names and improved aesthetics

# Set the style for the plot to 'seaborn-v0_8-darkgrid'
plt.style.use('seaborn-v0_8-darkgrid')

# Create a new figure with better aesthetics
fig, ax = plt.subplots(figsize=(12, 4))
ax.axis('tight')
ax.axis('off')

# Create the table and make the column labels bold
table = ax.table(cellText=df_refined.values,
                 colLabels=df_refined.columns,
                 loc='center',
                 cellLoc='center',  # Center align text in cells
                 colColours=['#1dc249']*len(df_refined.columns))  # Use a standard light green color for header

# Set font size for the table
table.auto_set_font_size(False)
table.set_fontsize(8)  # Adjust the font size as needed

# Set the column widths automatically
table.auto_set_column_width(col=list(range(len(df_refined.columns))))

# Make the column headers bold
for (i, col) in enumerate(df_refined.columns):
    cell = table[(0, i)]
    cell.set_text_props(fontproperties=FontProperties(weight='bold'))
    cell.set_facecolor('#1dc249')  # Use a standard light green color for header cells

# Improve the layout
plt.tight_layout()

# Save the plot
output_dir = os.path.dirname(file_path)
output_file = os.path.join(output_dir, 'parties_info.pdf')
fig.savefig(output_file)

# Close the plot
plt.close(fig)

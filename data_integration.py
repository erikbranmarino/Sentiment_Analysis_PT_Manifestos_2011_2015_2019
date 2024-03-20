import pandas as pd

# Define the path to the original Excel file
excel_path = '/Users/bran/Desktop/PhD HYBRIDS/corpora/manifesto corpus/manifestos italy, spain, portugal/data to analyze/MPDataset_MPDS2023a copia.xlsx'

# Load the Excel file into a pandas DataFrame
df = pd.read_excel(excel_path)

# Filter the DataFrame for the country code and the election date range
country_code = 35
start_date = '2011-06-01'
end_date = '2019-10-31'

# Assuming 'country' is the country code column and 'edate' is the election date column
filtered_df = df[(df['country'] == country_code) &
                 (df['edate'] >= pd.to_datetime(start_date)) &
                 (df['edate'] <= pd.to_datetime(end_date))]

# Define the path for the new filtered Excel file
filtered_excel_path = '/Users/bran/Desktop/PhD HYBRIDS/corpora/manifesto corpus/manifestos italy, spain, portugal/data to analyze/Manifesto_portugal.xlsx'

# Save the filtered DataFrame to a new Excel file
filtered_df.to_excel(filtered_excel_path, index=False)

# Output the path to the new filtered Excel file
filtered_excel_path

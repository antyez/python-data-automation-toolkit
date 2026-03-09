"""
Created on Wed May 29 17:13:07 2024

@author: antonioyepez
"""

import pandas as pd
import os

input_file_path = os.path.expanduser("/path/file.xlsx")
output_folder = os.path.expanduser("/path/exports")

# Ensures the output directory exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Technical Decision: 'id' is forced to string to prevent Pandas from stripping leading zeros or convert lage ids to scientific notation
df = pd.read_excel(input_file_path, dtype={'id': str})

# List of current languages in the app
languages = ['cs', 'de', 'en', 'es', 'fr', 'it', 'nl', 'pl', 'pt']

for language in languages:
    # Save to Excel using openpyxl engine
    df_filtered = df[df['language'] == language]
    output_file_path = os.path.join(output_folder, f"file{language}.xlsx")
    df_filtered.to_excel(output_file_path, index=False, engine='openpyxl')

print("Files generated successfully.")

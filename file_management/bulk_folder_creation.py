"""
Created on Tue Nov 30 12:24:56 2023

@author: antonioyepez
"""

import os
import pandas as pd
import shutil

# template folder
original_folder_path = '/path/root_folder'

# Source excel containing the metadata
excel_path = '/path/file.xlsx'

# Root destination
new_folders_path = '/path/folder/'

df = pd.read_excel(excel_path)

# Data sanitization, extracing reference and ensuring string type
for index, row in df.iterrows():
    reference = str(row['Reference'])
    reference_with_zero = "" + reference 
    name = str(row['Name'])

    # String normalization
    folder_name = f"{reference_with_zero}_{name.replace(' ', '_')}"

    new_folder_path = os.path.join(new_folders_path, folder_name)

    # Does not overwrite existing data
    if not os.path.exists(new_folder_path):
        shutil.copytree(original_folder_path, new_folder_path)
        print(f"Copied folder {original_folder_path} to {new_folder_path}")
    else:
        print(f"Folder {new_folder_path} already exists.")

print("Process completed.")

import pandas as pd
import re
import printUNCLEANdataset

# Step 2: import data from /data/housing.csv, using regex, remove extra spaces, leaving only 1 space between columns. save new file as temp_housing.csv

print("-----------Using Regex to remove extra spaces.-----------")
# File path
csv_file_path = './data/housing.csv'

# Preprocess the file to replace multiple spaces with a single space
with open(csv_file_path, 'r') as file:
    lines = file.readlines()

cleaned_lines = [re.sub(r'\s+', ' ', line).strip() for line in lines]  # Replace multiple spaces with one

# Save the cleaned file temporarily
temp_file_path = './data/temp_housing.csv'
with open(temp_file_path, 'w') as file:
    file.write('\n'.join(cleaned_lines))

# Read the cleaned file into a DataFrame
data = pd.read_csv(temp_file_path, delimiter=' ', header=None)

print("\n=== Dataset Loaded Successfully ===")
print(data.head())
print(f"Shape of the dataset: {data.shape}")

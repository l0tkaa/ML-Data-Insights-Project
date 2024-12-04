import pandas as pd
import os

# Step 1: import file from os, read csv, if file does not exist, error. prints the first 10 rows of UNCLEAN dataset (housing.csv)


# Load the dataset
# Replace 'your_dataset.csv' with the path to your dataset file
# For other formats (e.g., Excel), use pd.read_excel() or appropriate loaders
print("\n---------Loading raw, unclean data.-------\n")

dataset_path = 'data/housing.csv'  # Update this with your actual file path
expected_rows = 1000 #replace with expected number of rows
expected_columns = 10 #replace with expec\nted number of columns

# Load the dataset with error handling
if not os.path.exists(dataset_path):
    print(f"Error: The file '{dataset_path}' does not exist. Please check the file path and try again.")
    exit()


try:
    df = pd.read_csv(dataset_path)
except Exception as e:
    print(f"Error: Unable to load the dataset. Details: {e}")
    exit()


# Verify dataset dimensions
rows, columns = df.shape
if rows < expected_rows or columns < expected_columns: 
    print(f"Warning: The raw dataset has {rows} rows and {columns} columns, which is less than the expected {expected_rows} rows and {expected_columns} expected columns columns.\n")
else: 
    print(f"Raw dataset loaded successfully with {rows} rows and {columns} columns.\n")

# Print the first 10 rows of the dataset
print("First 10 rows of the dataset:")
print(df.head(10))
print("\n")

# Print dataset information
#print("\nRaw dataset Information:")
#print(df.info())

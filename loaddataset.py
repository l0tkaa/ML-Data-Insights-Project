import pandas as pd

# Load the dataset
# Replace 'your_dataset.csv' with the path to your dataset file
# For other formats (e.g., Excel), use pd.read_excel() or appropriate loaders
dataset_path = 'data/housing.csv'  # Update this with your actual file path
try:
    df = pd.read_csv(dataset_path)
except FileNotFoundError:
    print(f"Error: File not found at {dataset_path}")
    exit()

# Print the first 10 rows of the dataset
print("First 10 rows of the dataset:")
print(df.head(10))

# Print dataset information
print("\nDataset Information:")
print(df.info())

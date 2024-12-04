import pandas as pd
import checkmissingvalues

# Step 4


import pandas as pd

# Load the dataset
file_path = './data/final_cleaned_housing.csv'
data = pd.read_csv(file_path, header=None)

# Assign column names
column_names = [
    "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", 
    "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT", "MEDV"
]
data.columns = column_names

# Convert all numeric columns to proper numeric types
numeric_columns = [
    "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", 
    "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT", "MEDV"
]

for col in numeric_columns:
    data[col] = pd.to_numeric(data[col], errors="coerce")

# Check for missing values after conversion
if data.isnull().sum().sum() > 0:
    print("\nMissing values found after type conversion. Handling missing values...")
    data.fillna(data.mean(), inplace=True)

# Validate column data types
expected_dtypes = {
    "CRIM": "float64", "ZN": "float64", "INDUS": "float64", "CHAS": "float64",
    "NOX": "float64", "RM": "float64", "AGE": "float64", "DIS": "float64",
    "RAD": "float64", "TAX": "float64", "PTRATIO": "float64", "B": "float64",
    "LSTAT": "float64", "MEDV": "float64"
}

for column, expected_dtype in expected_dtypes.items():
    actual_dtype = str(data[column].dtype)
    assert actual_dtype == expected_dtype, (
        f"Column {column} has type {actual_dtype}, but expected {expected_dtype}!"
    )

print("\nAll assertions passed: No NaN values and consistent data types.")

# Save the cleaned data
output_path = './data/final_cleaned_housing2.csv'
data.to_csv(output_path, index=False)
print(f"\nCleaned and validated data saved to {output_path}")

import pandas as pd
import regexdata

# Step 3: look for missing/empty values and assigning column names in dataset that has been regex'd (temp_housing.csv)

print("----------Checking for missing values-----------")

# Load the cleaned dataset
temp_file_path = './data/temp_housing.csv'
data = pd.read_csv(temp_file_path, delimiter=' ', header=None)

# Step 1: Check for missing values
print("\n=== Missing Values per Column ===")
missing_values = data.isnull().sum()
print(missing_values)

# Step 2: Impute missing values with the mean for numerical columns
numeric_columns = data.select_dtypes(include='number')  # Select only numeric columns
data[numeric_columns.columns] = numeric_columns.fillna(numeric_columns.mean())

# Step 3: Verify missing values have been handled
print("\n=== Missing Values After Imputation ===")
missing_values_after = data.isnull().sum()
print(missing_values_after)

# Step 4: Display the first 10 rows after imputation
print("\n=== First 10 Rows After Imputation ===")
print(data.head(10))

# Assign column names based on the dataset's features
column_names = [
    "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", 
    "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT", "MEDV"
]
data.columns = column_names

# Display the first 5 rows with column names
print("\n=== Dataset with Column Names ===")
print(data.head())

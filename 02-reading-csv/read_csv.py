import pandas as pd

# Load the CSV file
df = pd.read_csv("sales.csv")

print("Sales Data")
print(df)

print("\n" + "-" * 40)

# First 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Column names
print("\nColumns:")
print(df.columns)

# Dataset shape
print("\nShape:")
print(df.shape)

# Highest sales
print("\nHighest Sales:")
print(df["Sales"].max())

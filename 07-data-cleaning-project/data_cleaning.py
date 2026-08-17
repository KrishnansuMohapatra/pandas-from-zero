import pandas as pd

df = pd.read_csv("messy_csv")

# Initial inspection
print("Number of rows and columns:", df.shape)
print("All column names:", df.columns)
print("Data types of columns:\n", df.dtypes)
print("Missing values:\n", df.isna().sum())
print("Duplicate values:", df.duplicated().sum())
print("-" * 40)

# Handle missing values
df["Sales"] = df["Sales"].fillna(df["Sales"].mean())
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())

# Handle duplicates
df = df.drop_duplicates()

# Convert datatypes
df["Product"] = df["Product"].astype("string")
df["City"] = df["City"].astype("string")

# Round quantity before converting to int
df["Quantity"] = df["Quantity"].round().astype("int64")

# Standardize text
df["Product"] = df["Product"].str.title()
df["City"] = df["City"].str.title()

# Flag refunds before changing sales values
df["IsRefund"] = df["Sales"] < 0

refund_count = df["IsRefund"].sum()
sales_count = len(df) - refund_count
refund_total = df.loc[df["IsRefund"], "Sales"].sum()
sales_total = df.loc[~df["IsRefund"], "Sales"].sum()

print("Refund transactions:", refund_count)
print("Normal sales transactions:", sales_count)
print("Total refund amount:", refund_total)
print("Total sales amount:", sales_total)

# Keep original Sales and create a positive amount for analysis
df["Sales_Amount"] = df["Sales"].abs()

# Final inspection
print("\nInspection after cleaning")
print("-" * 40)
print("Number of rows and columns:", df.shape)
print("All column names:", df.columns)
print("Data types of columns:\n", df.dtypes)
print("Missing values:\n", df.isna().sum())
print("Duplicate values:", df.duplicated().sum())

print("\nCleaned Data:")
print(df.to_string())

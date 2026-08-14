import pandas as pd

# Load the sales dataset
df = pd.read_csv("sales.csv")

print("Sales Data")
print(df)

print("\n" + "-" * 40)

# Find the highest individual sale
highest_sale = df["Sales"].max()
print("Highest Sale:", highest_sale)

# Find the row containing the highest sale
result = df.loc[
    df["Sales"].idxmax(),
    ["Product", "City", "Sales"]
]

print("\nBiggest Sale Details:")
print(result)

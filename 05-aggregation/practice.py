import pandas as pd

df = pd.read_csv("sales.csv")

# 🧠 Practice Challenge
#
# 1. Find the total sales.
print("Total sales:", df["Sales"].sum())

# 2. Find the average sales.
print("Average sales:", df["Sales"].mean())

# 3. Find the median sales.
print("Median sales:", df["Sales"].median())

# 4. Find the highest sale.
print("Highest sale:", df["Sales"].max())

# 5. Find the lowest sale.
print("Lowest sale:", df["Sales"].min())

# 6. Count the number of sales records.
print("Number of sales records:", df["Sales"].count())

# 7. Use describe() to see all major statistics.
print("\nStatistical summary:")
print(df["Sales"].describe())

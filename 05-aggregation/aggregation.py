import pandas as pd

df = pd.read_csv("sales.csv")

print("Sales Data")
print(df)

print("\n" + "-" * 40)

print("Total Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())
print("Median Sales:", df["Sales"].median())
print("Lowest Sale:", df["Sales"].min())
print("Highest Sale:", df["Sales"].max())
print("Number of Sales:", df["Sales"].count())
print("Standard Deviation:", df["Sales"].std())

print("\nSales Statistics:")
print(df["Sales"].describe())

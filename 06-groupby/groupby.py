import pandas as pd

df = pd.read_csv("sales.csv")

print("Sales Data:")
print(df)

print("\nTotal sales by city:")
print(df.groupby("City")["Sales"].sum())

print("\nAverage sales by city:")
print(df.groupby("City")["Sales"].mean())

print("\nNumber of sales by city:")
print(df.groupby("City")["Sales"].count())

print("\nSales statistics by city:")
print(
    df.groupby("City")["Sales"].agg(
        ["sum", "mean", "min", "max", "count"]
    )
)

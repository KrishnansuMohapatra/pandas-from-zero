import pandas as pd

df = pd.read_csv("sales.csv")

print("Sales greater than 30000:")
print(df[df["Sales"] > 30000])

print("\nBhubaneswar sales:")
print(df[df["City"] == "Bhubaneswar"])

print("\nBhubaneswar sales above 20000:")
print(
    df[
        (df["Sales"] > 20000) &
        (df["City"] == "Bhubaneswar")
    ]
)

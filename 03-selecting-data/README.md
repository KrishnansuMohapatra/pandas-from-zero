README.md
# 🐼 Lesson 3 — Selecting Data

In this lesson, you'll learn how to select specific columns and rows
from a Pandas DataFrame.

## 🎯 What You'll Learn

- Select one column
- Select multiple columns
- Select rows using `loc`
- Combine row and column selection

---

## 1️⃣ Select One Column

```python
df["Product"]
This returns only the Product column.
2️⃣ Select Multiple Columns
df[["Product", "Sales"]]
Notice the double brackets.
The outer brackets select from the DataFrame, while the inner list contains the column names.
3️⃣ Select Rows with loc
df.loc[0:2]
This selects rows from index 0 through index 2.
🧪 Complete Example
import pandas as pd

df = pd.read_csv("sales.csv")

print("Product column:")
print(df["Product"])

print("\nProduct and Sales:")
print(df[["Product", "Sales"]])

print("\nFirst three rows:")
print(df.loc[0:2])

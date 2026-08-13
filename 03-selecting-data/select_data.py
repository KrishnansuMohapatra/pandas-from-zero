
### `selecting_data.py`

This is the **lesson solution**, not the challenge solution:

```python
import pandas as pd

df = pd.read_csv("sales.csv")

# Select one column
print("Product column:")
print(df["Product"])

# Select multiple columns
print("\nProduct and Sales:")
print(df[["Product", "Sales"]])

# Select rows
print("\nRows 0 to 2:")
print(df.loc[0:2])

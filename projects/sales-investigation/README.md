# 🛒 Pandas Project 1 — Sales Investigation

A beginner-friendly Pandas mini project that turns a small sales dataset into a simple business insight.

## 🎯 Project Question

> Which one is our biggest sale, and what product and city produced it?

## 📁 Files

- `sales.csv` — the sales dataset
- `analysis.py` — guided analysis
- `practice.py` — challenge for you to solve

## 🧠 Concepts Used

- `pd.read_csv()`
- Selecting a column with `df["Sales"]`
- `max()`
- `idxmax()`
- `.loc[]` for selecting a row and columns

## 🔎 Analysis

```python
import pandas as pd

df = pd.read_csv("sales.csv")

# Find the highest sale
highest_sale = df["Sales"].max()
print("Highest Sale:", highest_sale)

# Find the row containing the highest sale
result = df.loc[df["Sales"].idxmax(), ["Product", "City", "Sales"]]
print(result)
```

## 💡 Insight

The biggest individual sale in this dataset is a **Laptop** sale in **Bhubaneswar** worth **₹75,000**.

## 🧪 Challenge

Find the **smallest sale**.

Answer these three questions:

1. Which product?
2. Which city?
3. How much?

Try solving it yourself before checking the solution.

## 🚀 Learning Goal

The goal is not just to learn Pandas syntax. It is to practice asking questions about data and turning the answers into useful insights.

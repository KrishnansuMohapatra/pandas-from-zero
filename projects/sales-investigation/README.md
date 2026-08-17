# 🛒 Pandas Project 1 — Sales Investigation

This is a small beginner project where I use Pandas to answer one simple business question:

> **Which one is our biggest sale, and what product and city produced it?**

The project is intentionally small. The goal is to practice turning a question into a few lines of Pandas code.

## 📁 Files

- `sales.csv` — the sales dataset
- `analysis.py` — the completed investigation
- `practice.py` — a similar challenge to solve yourself

## 🧠 Concepts Used

- `pd.read_csv()`
- Selecting a column with `df["Sales"]`
- `max()`
- `idxmax()`
- `.loc[]`

## 🔎 Investigation

First, find the largest sale:

```python
highest_sale = df["Sales"].max()
```

Then find the row containing that sale:

```python
result = df.loc[
    df["Sales"].idxmax(),
    ["Product", "City", "Sales"]
]
```

## 💡 Result

The biggest individual sale in this dataset is a **Laptop** sale in **Bhubaneswar** worth **₹75,000**.

## 🧪 Practice Challenge

Open `practice.py` and find the **smallest sale**.

Answer:

1. Which product?
2. Which city?
3. How much?

Try it yourself before looking for help.

## 🎯 Learning Goal

The point of this project isn't the size of the dataset.

It's learning to go from:

```text
Question
   ↓
Pandas operation
   ↓
Result
   ↓
Simple insight
```

This same process becomes much more useful when we work with larger datasets.

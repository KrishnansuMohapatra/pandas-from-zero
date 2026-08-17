# 🐼 Lesson 6 — GroupBy

Aggregation answers questions about the whole dataset.

But what if we want the same calculation **for each city, product or category?**

That's where `groupby()` becomes useful.

## 🎯 What You'll Learn

- What `groupby()` does
- Grouping by one column
- Combining `groupby()` with aggregation
- `sum()`
- `mean()`
- `count()`
- `min()` and `max()`
- `agg()`
- Finding the best group with `idxmax()`

## 🧠 The GroupBy Idea

Think about it as:

```text
Dataset
   ↓
Split into groups
   ↓
Calculate something for each group
   ↓
Compare the results
```

For example:

```python
df.groupby("City")["Sales"].sum()
```

means:

> Group the rows by City, take Sales, and calculate the total for each city.

## 1️⃣ Total Sales by City

```python
df.groupby("City")["Sales"].sum()
```

## 2️⃣ Average Sales by City

```python
df.groupby("City")["Sales"].mean()
```

## 3️⃣ Count Records by City

```python
df.groupby("City")["Sales"].count()
```

Remember that `count()` counts non-empty values. If you specifically want the number of orders, counting an order ID is often clearer:

```python
df.groupby("City")["Order_ID"].count()
```

## 4️⃣ Multiple Statistics with `agg()`

```python
df.groupby("City")["Sales"].agg(
    ["sum", "mean", "min", "max", "count"]
)
```

## 5️⃣ Find the Best City

After calculating total sales by city, we can find the city with the largest total:

```python
df.groupby("City")["Sales"].sum().idxmax()
```

`idxmax()` returns the label belonging to the largest value.

## 🧪 Complete Example

```python
import pandas as pd

df = pd.read_csv("sales.csv")

print("Total sales by city:")
print(df.groupby("City")["Sales"].sum())

print("\nAverage sales by city:")
print(df.groupby("City")["Sales"].mean())

print("\nNumber of orders by city:")
print(df.groupby("City")["Order_ID"].count())

print("\nSales statistics by city:")
print(
    df.groupby("City")["Sales"].agg(
        ["sum", "mean", "min", "max", "count"]
    )
)
```

## 🔥 Why GroupBy Matters

Real data analysis often asks questions like:

- Which city has the highest revenue?
- What is the average sale in each city?
- How many orders came from each city?
- Which product sells the most?
- Which category generates the most revenue?

`groupby()` helps turn these business questions into data questions.

## 🚀 Next

The next step is a **Data Cleaning Project**, where we'll work with deliberately messy data and decide what actually needs to be cleaned.

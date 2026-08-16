# 🐼 Lesson 6 — GroupBy

`groupby()` lets us split data into groups and then perform calculations on each group.

For example:

> How much did each city sell?

Instead of calculating everything together, we can group the data by `City`.

## 🎯 What You'll Learn

- `groupby()`
- Grouping by one column
- Aggregating grouped data
- `sum()`
- `mean()`
- `count()`
- `max()`
- `min()`
- `agg()`

## 1️⃣ Basic GroupBy

Group sales by city:

```python
df.groupby("City")["Sales"].sum()
```

This calculates the total sales for each city.

## 2️⃣ GroupBy + Mean

Find the average sale for each city:

```python
df.groupby("City")["Sales"].mean()
```

## 3️⃣ GroupBy + Count

Count the number of sales records for each city:

```python
df.groupby("City")["Sales"].count()
```

## 4️⃣ Multiple Aggregations

We can calculate multiple statistics:

```python
df.groupby("City")["Sales"].agg(
    ["sum", "mean", "min", "max", "count"]
)
```

## 🧪 Complete Example

```python
import pandas as pd

df = pd.read_csv("sales.csv")

print("Total sales by city:")
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
```

## 🧠 Key Idea

Think of `groupby()` like this:

```text
Dataset
   ↓
Split into groups
   ↓
Calculate something
   ↓
Get results for each group
```

For example:

```python
df.groupby("City")["Sales"].sum()
```

means:

> Group the rows by City, select Sales, and calculate the total for each city.

## 🔥 Why GroupBy Matters

Real-world data analysis often asks questions like:

- Which city has the highest sales?
- What is the average sale in each city?
- How many orders came from each city?
- Which product category generates the most revenue?

`groupby()` is one of the most useful Pandas tools for answering these questions.

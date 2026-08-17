# 🐼 Lesson 5 — Aggregation

Sometimes a dataset has hundreds or thousands of values, but we need only a few numbers to understand it.

That's where **aggregation** comes in.

Aggregation reduces many values into a useful summary.

## 🎯 What You'll Learn

- `sum()`
- `mean()`
- `median()`
- `min()`
- `max()`
- `count()`
- `std()`
- `describe()`

## 1️⃣ Total — `sum()`

```python
df["Sales"].sum()
```

Answers:

> How much did we sell in total?

## 2️⃣ Average — `mean()`

```python
df["Sales"].mean()
```

Answers:

> What is the average sale?

## 3️⃣ Middle Value — `median()`

```python
df["Sales"].median()
```

The median is the middle value after the values are ordered.

## 4️⃣ Smallest and Largest

```python
df["Sales"].min()
df["Sales"].max()
```

These find the lowest and highest values.

## 5️⃣ Count — `count()`

```python
df["Sales"].count()
```

Counts the non-empty values in the column.

## 6️⃣ Spread — `std()`

```python
df["Sales"].std()
```

Standard deviation gives us an idea of how spread out the values are.

## 7️⃣ Quick Summary — `describe()`

```python
df["Sales"].describe()
```

This gives several useful statistics together:

- Count
- Mean
- Standard deviation
- Minimum
- Percentiles
- Maximum

## 🧪 Complete Example

```python
import pandas as pd

df = pd.read_csv("sales.csv")

print("Total Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())
print("Median Sales:", df["Sales"].median())
print("Lowest Sale:", df["Sales"].min())
print("Highest Sale:", df["Sales"].max())
print("Number of Sales:", df["Sales"].count())
print("Standard Deviation:", df["Sales"].std())

print("\nSales Statistics:")
print(df["Sales"].describe())
```

## 🧠 Key Idea

```text
Many values
     ↓
Aggregation
     ↓
Useful summary
```

Aggregation is useful because it turns raw numbers into something we can reason about.

## 🚀 Next

Next we'll combine aggregation with **GroupBy** to answer questions such as:

> Which city generated the most sales?

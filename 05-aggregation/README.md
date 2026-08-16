# 🐼 Lesson 5 — Aggregation

Aggregation means reducing multiple values into a single useful result.

For example:

- What is the total sales?
- What is the average sale?
- What is the highest sale?
- What is the lowest sale?
- How many sales records do we have?

## 🎯 What You'll Learn

- `sum()`
- `mean()`
- `median()`
- `min()`
- `max()`
- `count()`
- `std()`
- `describe()`

## 1️⃣ Sum

```python
df["Sales"].sum()
```

Find the total sales.

## 2️⃣ Mean

```python
df["Sales"].mean()
```

Find the average sales.

## 3️⃣ Median

```python
df["Sales"].median()
```

Find the middle sales value.

## 4️⃣ Minimum

```python
df["Sales"].min()
```

Find the smallest sale.

## 5️⃣ Maximum

```python
df["Sales"].max()
```

Find the largest sale.

## 6️⃣ Count

```python
df["Sales"].count()
```

Count the number of non-empty Sales values.

## 7️⃣ Standard Deviation

```python
df["Sales"].std()
```

Measure how spread out the sales values are.

## 8️⃣ Describe

```python
df["Sales"].describe()
```

Get several statistics at once, including count, mean, standard deviation, minimum, percentiles, and maximum.

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

Aggregation turns many values into a useful summary.

```text
Many values
     ↓
Aggregation
     ↓
Useful statistic
```

For example:

```python
df["Sales"].sum()
```

answers:

> "How much did we sell in total?"

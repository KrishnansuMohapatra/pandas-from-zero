# 🐼 Lesson 3 — Selecting Data

A DataFrame can contain many rows and columns. Usually, we don't need all of them at once.

In this lesson, we'll learn how to select the parts of the DataFrame we actually want.

## 🎯 What You'll Learn

- Select one column
- Select multiple columns
- Select rows with `loc`
- Select specific rows and columns together

## 1️⃣ Select One Column

```python
df["Product"]
```

This returns the `Product` column.

## 2️⃣ Select Multiple Columns

```python
df[["Product", "Sales"]]
```

Notice the double brackets:

```text
df[ ["Product", "Sales"] ]
 ↑              ↑
DataFrame       list of columns
```

## 3️⃣ Select Rows with `loc`

```python
df.loc[0:2]
```

This selects rows from index 0 through index 2.

## 4️⃣ Select Rows and Columns

You can combine both ideas:

```python
df.loc[0:2, ["Product", "Sales"]]
```

This means:

> Give me rows 0–2 and only the Product and Sales columns.

## 🧪 Complete Example

```python
import pandas as pd

df = pd.read_csv("sales.csv")

print("Product column:")
print(df["Product"])

print("\nProduct and Sales:")
print(df[["Product", "Sales"]])

print("\nFirst three rows:")
print(df.loc[0:2])

print("\nSelected rows and columns:")
print(df.loc[0:2, ["Product", "Sales"]])
```

## 🧠 Key Idea

Selecting data is about asking:

> **Which part of this DataFrame do I need?**

That becomes especially useful when we start filtering and analyzing the data.

## 🚀 Next

Next we'll use conditions to **filter rows** and ask questions such as:

> Which sales are greater than ₹20,000?

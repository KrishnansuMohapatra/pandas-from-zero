# 🐼 Lesson 4 — Filtering Data

In this lesson, you'll learn how to filter rows in a Pandas DataFrame based on conditions.

## 🎯 What You'll Learn

- Filter rows using a condition
- Filter numerical values
- Filter text values
- Combine conditions
- Use `&` and `|` with Pandas conditions

---

## 1️⃣ Filter Rows by Sales

```python
df[df["Sales"] > 30000]
```

This returns only rows where Sales is greater than 30,000.

---

## 2️⃣ Filter Rows by City

```python
df[df["City"] == "Bhubaneswar"]
```

This returns only rows where the City is Bhubaneswar.

---

## 3️⃣ Combine Conditions

Use `&` when both conditions must be true.

```python
df[(df["Sales"] > 20000) & (df["City"] == "Bhubaneswar")]
```

Use `|` when either condition can be true.

```python
df[(df["City"] == "Bhubaneswar") | (df["City"] == "Cuttack")]
```

---

## 🧪 Complete Example

```python
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
```

---

## 🧠 Key Idea

Filtering means asking Pandas:

> "Show me only the rows that satisfy this condition."

```python
df[condition]
```

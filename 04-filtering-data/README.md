# 🐼 Lesson 4 — Filtering Data

Now we can select data. The next question is:

> **What if I only want the rows that match a condition?**

That's filtering.

## 🎯 What You'll Learn

- Filter rows using conditions
- Filter numerical values
- Filter text values
- Combine conditions
- Use `&` when both conditions must be true
- Use `|` when either condition can be true

## 1️⃣ Filter by Sales

```python
df[df["Sales"] > 30000]
```

This keeps only rows where Sales is greater than 30,000.

## 2️⃣ Filter by City

```python
df[df["City"] == "Bhubaneswar"]
```

This keeps only rows where City is Bhubaneswar.

## 3️⃣ Combine Conditions

Use `&` when **both** conditions must be true.

```python
df[
    (df["Sales"] > 20000) &
    (df["City"] == "Bhubaneswar")
]
```

Use `|` when **either** condition can be true.

```python
df[
    (df["City"] == "Bhubaneswar") |
    (df["City"] == "Cuttack")
]
```

### ⚠️ Remember

Put each condition inside parentheses when using `&` or `|`.

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

## 🧠 Key Idea

Filtering means asking Pandas:

> **Show me only the rows that satisfy this condition.**

```python
df[condition]
```

This is where a DataFrame starts becoming something we can investigate instead of just display.

## 🚀 Next

Next we'll learn **aggregation** — turning many sales values into useful numbers such as total, average, minimum and maximum.

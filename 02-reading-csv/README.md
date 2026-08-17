# 🐼 Lesson 2 — Reading CSV Files

Now that we know what a DataFrame is, let's load one from a real CSV file.

CSV files are one of the most common ways data is stored and shared, so being comfortable with them is important for data analysis.

## 🎯 What You'll Learn

- What a CSV file is
- How to import Pandas
- How to read a CSV file
- How CSV data becomes a DataFrame
- How to inspect a dataset
- How to check rows and columns

## 📦 Installation

If Pandas isn't installed:

```bash
pip install pandas
```

## 📄 Read a CSV File

```python
import pandas as pd

df = pd.read_csv("sales.csv")

print(df)
```

`read_csv()` reads the CSV file and returns a DataFrame.

## 🔎 Inspect the Data

```python
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
```

These give us a quick first look at the dataset.

### `head()`

Shows the first few rows.

### `shape`

Tells us the number of rows and columns.

### `columns`

Shows the column names.

### `info()`

Shows useful information about columns, data types and non-null values.

## 🧠 Key Idea

A CSV file is just stored data. Pandas turns it into a DataFrame that we can inspect and analyze with Python.

```text
sales.csv
   ↓
read_csv()
   ↓
DataFrame
   ↓
Inspect + Analyze
```

## 🚀 Next

In the next lesson, we'll learn how to select the **rows and columns** we actually want to work with.

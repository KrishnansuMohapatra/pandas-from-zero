# 🐼 Lesson 1 — Introduction to Pandas

This is where the Pandas journey starts.

Pandas is a Python library used to work with **structured and tabular data**. Think about a spreadsheet, but with Python controlling it.

## 🎯 What You'll Learn

- What Pandas is
- What a DataFrame is
- How to create a DataFrame
- Why Pandas is useful for data analysis
- Where Pandas fits into data science and Machine Learning

## 🧠 What is Pandas?

Pandas is commonly used for:

- Data cleaning
- Data analysis
- Data manipulation
- Data preparation for Machine Learning

## 📦 Installation

```bash
pip install pandas
```

## 🧪 First Example

```python
import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Score": [85, 92, 78]
}

df = pd.DataFrame(data)

print(df)
```

## 📊 What is a DataFrame?

A DataFrame is a table-like structure made up of rows and columns.

You can think of it as:

```text
Python
  ↓
Pandas
  ↓
DataFrame
  ↓
Rows + Columns
```

It gives us a convenient way to work with real-world tabular data.

## 🚀 Next

In the next lesson, we'll load data from a **CSV file** instead of creating the DataFrame manually.

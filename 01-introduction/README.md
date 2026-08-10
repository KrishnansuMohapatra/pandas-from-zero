🐼 Lesson 1 — Introduction to Pandas

Welcome to the Pandas series!

What is Pandas?

Pandas is a Python library for working with structured and tabular data.

It is commonly used for:

- Data cleaning
- Data analysis
- Data manipulation
- Data preparation for Machine Learning

Installation

pip install pandas

First Example

import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Score": [85, 92, 78]
}

df = pd.DataFrame(data)

print(df)

What is a DataFrame?

A DataFrame is a table-like structure containing rows and columns.

Think of it like a spreadsheet—but programmable with Python.

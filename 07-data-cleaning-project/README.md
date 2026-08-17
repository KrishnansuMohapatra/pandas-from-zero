# 🧹 Project 1 — Sales Data Cleaning

This project is about something that looks simple but is actually important in data analysis:

> **Before analyzing data, can we trust the data?**

I was given a deliberately messy sales dataset and had to inspect it, decide what needed attention, clean it, and inspect it again.

## 🎯 Project Goal

Prepare the sales data for analysis without blindly changing values.

## 🔎 What I Checked

- Number of rows and columns
- Missing values
- Duplicate rows
- Data types
- Inconsistent text values
- Missing quantities
- Missing sales values
- Negative sales values

## 🧹 What I Practiced

- `isna()`
- `fillna()`
- `drop_duplicates()`
- `astype()`
- `round()`
- String methods such as `.str.title()`
- Boolean conditions
- Creating a new column with a condition
- Final data inspection

## 💡 Important Lesson — Negative Sales

A negative sales value should not automatically be changed to a positive number.

It might represent a:

- Refund
- Return
- Cancellation
- Data-entry error

For this project, negative values were flagged as possible refunds instead of destroying the original information.

The original `Sales` column is kept, and `Sales_Amount` can be used when a positive amount is needed for a separate analysis.

## 📁 Files

- `messy_csv` — the deliberately messy dataset
- `data_cleaning.py` — cleaning and inspection code

## 🧠 Main Takeaway

Data cleaning is not just about knowing functions like `fillna()` or `drop_duplicates()`.

The important question is:

> **Does this change make sense for the data?**

That decision is part of data analysis.

## 🚀 Next

After cleaning the data, the next project combines the Pandas skills learned so far into a complete **E-Commerce Sales Analysis**.

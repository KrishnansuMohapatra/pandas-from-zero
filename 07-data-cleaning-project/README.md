# 🧹 Project 1 — Sales Data Cleaning

This is my first Pandas data-cleaning project.

The dataset contains some messy values, so the goal is to inspect the data, clean what makes sense, and verify it again.

## What I practiced

- Inspecting a DataFrame
- Finding missing values
- Finding duplicate rows
- Handling missing values
- Converting data types
- Standardizing text
- Identifying negative sales
- Creating a refund flag
- Checking the data after cleaning

## Important note

Negative sales were treated as possible refund transactions instead of simply being changed without investigation. The original `Sales` value is preserved, while `Sales_Amount` can be used when a positive amount is needed for analysis.

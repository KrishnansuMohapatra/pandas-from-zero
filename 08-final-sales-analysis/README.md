# 🐼 Final Project — E-Commerce Sales Analysis

This is the final Pandas project in my current **Pandas From Zero** path.

The goal is to take a small e-commerce dataset, investigate it using the Pandas skills I learned, and turn the numbers into simple business insights.

## 🎯 Project Goal

Move from:

```text
Raw data
   ↓
Inspect
   ↓
Analyze
   ↓
Compare
   ↓
Find patterns
   ↓
Business insights
```

## 🔎 What I Practiced

- Data inspection
- Date conversion with `pd.to_datetime()`
- Aggregation
- `groupby()`
- `sum()` and `mean()`
- `count()`
- `idxmax()` and `idxmin()`
- Product analysis
- City analysis
- Category analysis
- Monthly analysis
- Writing business conclusions

## 📊 Questions I Answered

### Basic metrics

- What is the total revenue?
- What is the average sale?
- How many units were sold?
- What are the highest and lowest individual sales?

### Product

- Which product generated the most revenue?
- Which product generated the least revenue?
- Which product sold the most units?

### City

- Which city generated the most revenue?
- What is the average sale by city?
- How many orders came from each city?

### Category

- Which category generated the most revenue?
- How much quantity was sold in each category?

### Time

- How much was sold each month?
- How many orders came from each month?
- Which month had the highest sales?

## 💡 My Findings

- **Bhubaneswar** performed the best with ₹313,000 in revenue and 8 orders.
- **Laptop** generated the most product revenue with ₹300,000.
- **Mouse** sold the most units, but its lower price meant it generated much less revenue than Laptop.
- **Electronics** generated ₹640,000 compared with ₹84,000 from Accessories.
- **April** had the highest monthly sales at ₹176,500. January was close behind at ₹175,000.
- **Bhubaneswar and Cuttack** were strong markets and together represented a large share of revenue.

## 🧠 Business Recommendation

The data suggests that Bhubaneswar and Cuttack are worth investigating further because of their strong sales performance.

I would not immediately assume that more marketing is the answer. A better next step would be to investigate what is driving the performance in these cities before deciding where to increase investment.

## ⚠️ Limitation

This is a small practice dataset. It contains sales and order information, but it does not contain things like profit, marketing spending, customer acquisition cost or inventory.

So the recommendations are **observations and hypotheses**, not final business decisions.

## 🎓 What I Learned

The biggest lesson from this project was that Pandas is not only about remembering functions.

The real workflow is:

> **Ask a question → find the right data → analyze it → understand the result → explain what it means.**

That is the skill I want to keep improving.

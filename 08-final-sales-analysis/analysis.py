import pandas as pd

df = pd.read_csv("e_commerce.csv")

# Initial inspection
print("Number of rows and columns:", df.shape)
print("All column names:", df.columns)
print("Data types of columns:\n", df.dtypes)
print("Missing values:\n", df.isna().sum())
print("Duplicate values:", df.duplicated().sum())

# Correcting data type of Date
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Business analysis
print("\nBusiness Analysis")
print("-" * 40)
print("Total revenue:", df["Sales"].sum())
print("Average sales:", df["Sales"].mean())
print("Total quantity sold:", df["Quantity"].sum())
print("Highest individual sale:", df["Sales"].max())
print("Lowest individual sale:", df["Sales"].min())

# Product analysis
print("\nProduct Analysis")
print("Total sales by each product")
print(df.groupby("Product")["Sales"].sum())

print("Quantity sold per each product")
print(df.groupby("Product")["Quantity"].sum())

print("Average sales by product")
print(df.groupby("Product")["Sales"].mean())

best_product = df.groupby("Product")["Sales"].sum().idxmax()
least_product = df.groupby("Product")["Sales"].sum().idxmin()

print("Best performing product is", best_product)
print("Least performing product is", least_product)

# City analysis
print("\nCity Analysis")
print("Total sales by city")
print(df.groupby("City")["Sales"].sum())

print("Average sales by city")
print(df.groupby("City")["Sales"].mean())

print("Total quantity sold per city")
print(df.groupby("City")["Quantity"].sum())

print("Number of orders per city")
print(df.groupby("City")["Order_ID"].count())

best_performing_city = df.groupby("City")["Sales"].sum().idxmax()
print("Best performing city", best_performing_city)

# Category analysis
print("\nCategory Analysis")
print("Total sales by category")
print(df.groupby("Category")["Sales"].sum())

print("Average sales by category")
print(df.groupby("Category")["Sales"].mean())

print("Total quantity sold per category")
print(df.groupby("Category")["Quantity"].sum())

best_performing_category = df.groupby("Category")["Sales"].sum().idxmax()
print("Best performing Category", best_performing_category)

# Monthly sales
print("\nMonthly Analysis")
df["Month"] = df["Date"].dt.month

monthly_sales = df.groupby("Month")["Sales"].sum()
number_order_month = df.groupby("Month")["Order_ID"].count()

best_month = monthly_sales.idxmax()

print("Total sales by month", monthly_sales)
print("Number of orders by month", number_order_month)
print("Month with the highest sales", best_month)

# Final business insights
print("\nBusiness Insights")
print("Bhubaneswar performed the best with the highest total revenue.")
print("Laptop is the best-performing product by revenue, while Mouse sells the most units.")
print("Electronics generates much more revenue than Accessories.")
print("April had the highest monthly sales.")
print("Bhubaneswar and Cuttack are strong markets worth investigating further.")

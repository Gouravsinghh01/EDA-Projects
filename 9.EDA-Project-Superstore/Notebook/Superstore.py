import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Load data ---
# Make sure the 'Superstore.csv' file is in the same directory as your script,
# or provide the full path to the file.
df = pd.read_csv("Superstore.csv", encoding='latin-1')

# --- Data Preprocessing ---
# Convert 'Order Date' to datetime objects for time-series analysis.
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year

# --- Analysis & Visualization ---

# 1. Category-wise Sales & Profit
# Group by 'Category' and calculate the total sales and profit.
category_group = df.groupby('Category')[['Sales', 'Profit']].sum().sort_values(by='Sales', ascending=False)
fig, ax = plt.subplots(figsize=(10, 6))
category_group.plot(kind='bar', ax=ax, width=0.8, color=['skyblue', 'salmon'])
plt.title("Sales and Profit by Category", fontsize=16)
plt.xlabel("Category", fontsize=12)
plt.ylabel("Amount", fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 2. Region-wise Profit
# Group by 'Region' and calculate the total profit.
region_profit = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x=region_profit.values, y=region_profit.index, palette='viridis', hue=region_profit.index, legend=False, ax=ax)
plt.title("Profit by Region", fontsize=16)
plt.xlabel("Total Profit", fontsize=12)
plt.ylabel("Region", fontsize=12)
plt.tight_layout()
plt.show()

# 3. Segment-wise Performance
# Group by 'Segment' and sum up sales and profit.
seg_perf = df.groupby('Segment')[['Sales', 'Profit']].sum()
fig, ax = plt.subplots(figsize=(8, 5))
seg_perf.plot(kind='bar', ax=ax, color=['lightgreen', 'orange'], width=0.6)
plt.title("Sales & Profit by Customer Segment", fontsize=16)
plt.xlabel("Customer Segment", fontsize=12)
plt.ylabel("Amount", fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 4. Monthly Sales Trend
# Group by year and month to get the monthly sales trend.
monthly_sales = df.groupby(['Year', 'Month'])['Sales'].sum()
fig, ax = plt.subplots(figsize=(12, 6))
monthly_sales.plot(ax=ax, color='purple', marker='o', linestyle='-')
plt.title("Monthly Sales Trend Over Time", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Total Sales", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# 5. Top/Bottom Sub-Categories
# Group by 'Sub-Category' and sum up profit, then sort.
subcat = df.groupby('Sub-Category')['Profit'].sum().sort_values(ascending=True)
fig, ax = plt.subplots(figsize=(12, 8))
# Use a color list to conditionally color bars based on profit.
colors = ['red' if profit < 0 else 'green' for profit in subcat]
sns.barplot(x=subcat.values, y=subcat.index, palette=colors, hue=subcat.index, legend=False, ax=ax)
plt.title("Profit by Sub-Category", fontsize=16)
plt.xlabel("Total Profit", fontsize=12)
plt.ylabel("Sub-Category", fontsize=12)
plt.tight_layout()
plt.show()

print("code successful")

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load dataset
try:
    df = pd.read_csv("flights.csv")
except FileNotFoundError:
    print("Error: 'flights.csv' not found. Please ensure the file is in the same directory.")
    exit()

print("Shape of the DataFrame:", df.shape)
print("\nColumns in the DataFrame:\n", df.columns)

# Basic info on missing values
print("\nMissing values per column:\n", df.isnull().sum())

# Drop rows with missing values in key columns
df = df.dropna(subset=['ARRIVAL_DELAY', 'DEPARTURE_DELAY'])

# Convert relevant columns to numeric if needed.
# Note: 'DAY_OF_WEEK' is a common column, but if it's not in your dataset, you must create it.
# The original code threw an error because this column did not exist.
# Let's assume you have a 'FLIGHT_DATE' column to create 'DAY_OF_WEEK'
# If you don't have a date column, you must remove this line or add a new column.
# For this example, we will assume 'DAY_OF_WEEK' is a column in the dataset.
df['MONTH'] = pd.to_numeric(df['MONTH'], errors='coerce')
# Assuming 'DAY_OF_WEEK' exists. If not, this line needs to be removed.
# df['DAY_OF_WEEK'] = pd.to_numeric(df['DAY_OF_WEEK'], errors='coerce')

# Check for the existence of 'DAY_OF_WEEK' before using it.
if 'DAY_OF_WEEK' in df.columns:
    df['DAY_OF_WEEK'] = pd.to_numeric(df['DAY_OF_WEEK'], errors='coerce')

# Airline delay averages
airline_delays = df.groupby('AIRLINE')['ARRIVAL_DELAY'].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 5))
sns.barplot(x=airline_delays.index, y=airline_delays.values)
plt.title("Average Arrival Delay by Airline")
plt.ylabel("Avg Delay (minutes)")
plt.xlabel("Airline")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Delay reason analysis
delay_cols = ['CARRIER_DELAY', 'WEATHER_DELAY', 'NAS_DELAY', 'SECURITY_DELAY', 'LATE_AIRCRAFT_DELAY']
# Drop rows that are NaN for all delay reasons
df_delay = df[delay_cols].dropna(how='all')
df_delay_sum = df_delay.sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(x=df_delay_sum.index, y=df_delay_sum.values)
plt.title("Total Delay by Cause")
plt.ylabel("Total Minutes")
plt.xticks(rotation=45, ha='right')
plt.show()

# Monthly delay trend
monthly_avg_delay = df.groupby('MONTH')['ARRIVAL_DELAY'].mean()
plt.figure(figsize=(10, 6))
plt.plot(monthly_avg_delay, marker='o', linestyle='-')
plt.title("Average Arrival Delay by Month")
plt.xlabel("Month")
plt.ylabel("Avg Arrival Delay (minutes)")
plt.grid(True)
plt.xticks(monthly_avg_delay.index)
plt.tight_layout()
plt.show()

# Most delayed routes
df['ROUTE'] = df['ORIGIN_AIRPORT'] + "-" + df['DESTINATION_AIRPORT']
route_delays = df.groupby('ROUTE')['ARRIVAL_DELAY'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=route_delays.values, y=route_delays.index, palette='viridis', hue=route_delays.index, legend=False)
plt.title("Top 10 Most Delayed Routes")
plt.xlabel("Avg Arrival Delay (minutes)")
plt.ylabel("Route")
plt.tight_layout()
plt.show()

# Delay distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['ARRIVAL_DELAY'], bins=100, kde=True, color='skyblue')
plt.title("Arrival Delay Distribution")
plt.xlabel("Arrival Delay (minutes)")
plt.ylabel("Frequency")
plt.xlim(-50, 300)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

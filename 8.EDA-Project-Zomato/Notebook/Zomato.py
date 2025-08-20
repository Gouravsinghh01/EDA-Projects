import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# === Load dataset ===
# The 'encoding' parameter is crucial for handling different file formats.
# 'latin-1' or 'utf-8' are common encodings for CSV files.
try:
    df = pd.read_csv("zomato.csv", encoding='latin-1')
except FileNotFoundError:
    print("Error: 'zomato.csv' not found. Please ensure the file is in the same directory.")
    exit()

# === Preview dataset ===
print("\nFirst 5 Rows:\n", df.head())
print("\nColumn Names:\n", df.columns)
print("\nDataset Info:\n")
print(df.info())

# === Data Cleaning & Preprocessing ===
# 1. Standardize column names for easier access (e.g., 'rate' to 'rate', 'approx_cost(for two people)' to 'cost')
df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
df.rename(columns={'approx_cost_(for_two_people)': 'cost_for_two'}, inplace=True)

# 2. Clean 'rate' column: remove 'NEW', '-', and extract the numerical part
df = df[df['rate'].notnull()]
df = df[~df['rate'].isin(['NEW', '-'])]
df['rate'] = df['rate'].apply(lambda x: float(x.split('/')[0]) if isinstance(x, str) else x)
df.dropna(subset=['rate'], inplace=True)

# 3. Clean 'cost_for_two' column: remove commas and convert to numeric
if 'cost_for_two' in df.columns:
    df['cost_for_two'] = df['cost_for_two'].astype(str).str.replace(',', '').astype(float)

# === Analysis and Visualization ===

# --- City-wise Restaurant Count ---
if 'location' in df.columns:
    city_count = df['location'].value_counts().head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=city_count.index, y=city_count.values, palette='viridis', hue=city_count.index, legend=False)
    plt.title("Top 10 City Areas with Most Restaurants", fontsize=16)
    plt.ylabel("Number of Restaurants", fontsize=12)
    plt.xlabel("City Area", fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# --- Rating Distribution ---
plt.figure(figsize=(8, 5))
sns.histplot(df['rate'], bins=20, kde=True, color='coral')
plt.title("Distribution of Restaurant Ratings", fontsize=16)
plt.xlabel("Rating", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.tight_layout()
plt.show()

# --- Cuisine Analysis ---
if 'cuisines' in df.columns:
    df['cuisines'] = df['cuisines'].astype(str)
    # Split cuisines and count each one
    all_cuisines = df['cuisines'].str.split(', ').explode()
    top_cuisines = all_cuisines.value_counts().head(10)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_cuisines.values, y=top_cuisines.index, palette='magma', hue=top_cuisines.index, legend=False)
    plt.title("Top 10 Most Popular Cuisines", fontsize=16)
    plt.xlabel("Count", fontsize=12)
    plt.ylabel("Cuisine", fontsize=12)
    plt.tight_layout()
    plt.show()

# --- Cost vs. Rating Analysis ---
if 'cost_for_two' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='cost_for_two', y='rate', data=df, alpha=0.5, color='purple')
    plt.title("Relationship Between Cost and Rating", fontsize=16)
    plt.xlabel("Cost for Two People", fontsize=12)
    plt.ylabel("Rating", fontsize=12)
    plt.tight_layout()
    plt.show()

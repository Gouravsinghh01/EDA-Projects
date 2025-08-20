import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for plots
sns.set(style="darkgrid")

# Step 2: Load IPL Datasets
# Load IPL datasets
# Ensure 'matches.csv' and 'deliveries.csv' are in the same directory
try:
    matches = pd.read_csv("matches.csv")
    deliveries = pd.read_csv("deliveries.csv")
except FileNotFoundError as e:
    print(f"Error: {e}. Please ensure the CSV files are in the correct directory.")
    exit()

# Preview datasets
print("Matches DataFrame shape:", matches.shape)
print("Deliveries DataFrame shape:", deliveries.shape)
print("\nMatches DataFrame columns:", matches.columns.tolist())

# Step 3: Data Cleaning
# CORRECTED: Fill missing winners with 'No Result' using direct assignment
matches['winner'] = matches['winner'].fillna('No Result')

# CORRECTED: Drop umpire3 column if present, using direct assignment
if 'umpire3' in matches.columns:
    matches = matches.drop('umpire3', axis=1)

# Step 4: Match-Winning Analysis
# a. Teams with Most Wins
plt.figure(figsize=(12, 6))
wins = matches['winner'].value_counts()
# CORRECTED: Added `hue=wins.index` and `legend=False` to resolve the FutureWarning.
# CORRECTED: Removed the emoji from the title to resolve the UserWarning.
sns.barplot(x=wins.index, y=wins.values, palette="viridis", hue=wins.index, legend=False)
plt.xticks(rotation=45, ha='right')
plt.title('Most Matches Won by Teams')
plt.ylabel('Total Wins')
plt.tight_layout()
plt.show()

# b. Win by Runs Distribution
# CORRECTED: Added a check for the column to prevent KeyError.
if 'win_by_runs' in matches.columns:
    plt.figure(figsize=(10, 5))
    sns.histplot(matches['win_by_runs'], bins=30, kde=True, color='orange')
    plt.title('Distribution of Win by Runs')
    plt.xlabel('Win by Runs')
    plt.tight_layout()
    plt.show()
else:
    print("Warning: 'win_by_runs' column not found. Skipping plot.")

# c. Win by Wickets Distribution
# CORRECTED: Added a check for the column to prevent KeyError.
if 'win_by_wickets' in matches.columns:
    plt.figure(figsize=(10, 5))
    sns.histplot(matches['win_by_wickets'], bins=30, kde=True, color='purple')
    plt.title('Distribution of Win by Wickets')
    plt.xlabel('Win by Wickets')
    plt.tight_layout()
    plt.show()
else:
    print("Warning: 'win_by_wickets' column not found. Skipping plot.")

# Step 5: Toss Impact Analysis
# % of matches where toss winner also won match
toss_wins = matches[matches['toss_winner'] == matches['winner']]
toss_win_percent = len(toss_wins) / len(matches) * 100
print(f"\nToss Impact: {toss_win_percent:.2f}% of toss winners also won the match.")

plt.figure(figsize=(8, 5))
# CORRECTED: Added `hue='toss_decision'` and `legend=False` to resolve the FutureWarning.
# CORRECTED: Removed the emoji from the title to resolve the UserWarning.
sns.countplot(data=matches, x='toss_decision', palette='pastel', hue='toss_decision', legend=False)
plt.title('Toss Decision Trends')
plt.xlabel('Toss Decision')
plt.tight_layout()
plt.show()

# Step 6: Player Performance Analysis (Runs + Wickets)
# a. Top 10 Run Scorers
# CORRECTED: Added checks for the required columns to prevent KeyError.
if 'batsman' in deliveries.columns and 'batsman_runs' in deliveries.columns:
    top_scorers = deliveries.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10, 5))
    top_scorers.plot(kind='bar', color='green')
    plt.title("Top 10 Run Scorers")
    plt.ylabel("Total Runs")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
else:
    print("Warning: 'batsman' or 'batsman_runs' column not found. Skipping Top Run Scorers plot.")


# b. Top 10 Wicket Takers
# Filter dismissals
# CORRECTED: Added checks for the required columns to prevent KeyError.
if 'dismissal_kind' in deliveries.columns and 'bowler' in deliveries.columns:
    dismissals = deliveries[deliveries['dismissal_kind'].notnull()]
    top_wickets = dismissals.groupby('bowler').size().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10, 5))
    top_wickets.plot(kind='bar', color='red')
    plt.title("Top 10 Wicket Takers")
    plt.ylabel("Wickets Taken")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
else:
    print("Warning: 'dismissal_kind' or 'bowler' column not found. Skipping Top Wicket Takers plot.")


# Step 7: Additional Insights (Optional)
# Matches Played per Season
season_count = matches['season'].value_counts().sort_index()

plt.figure(figsize=(10, 5))
# CORRECTED: Added `hue=season_count.index` and `legend=False` to resolve the FutureWarning.
sns.barplot(x=season_count.index, y=season_count.values, palette="mako", hue=season_count.index, legend=False)
plt.title("Matches Played per Season")
plt.xlabel("Season")
plt.ylabel("Matches")
plt.tight_layout()
plt.show()

# === Done ===
print("\nIPL EDA Completed.")

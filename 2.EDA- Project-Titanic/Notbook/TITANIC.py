# Titanic EDA - Complete Script
# Objective: Explore survival patterns by age, gender, and passenger class

# === Import Libraries ===
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# === Load Dataset ===
df = pd.read_csv("../titanic.csv")  # Make sure titanic.csv is in the same directory
print("Initial Dataset Preview:\n", df.head())

# === Dataset Overview ===
print("\nDataset Info:")
print(df.info())
print("\nStatistical Summary:")
print(df.describe())

# === Missing Value Analysis ===
print("\nMissing Values Count:")
print(df.isnull().sum())

# Heatmap of missing values
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values Heatmap")
plt.show()

# === Handling Missing Values ===
# CORRECTED: Reassigning the column to fix the FutureWarning.
# This is a more reliable way to fill missing values.
df['Age'] = df['Age'].fillna(df['Age'].median())

# CORRECTED: Added a check to ensure 'Cabin' column exists before dropping.
# This prevents a KeyError if the column is already missing.
if 'Cabin' in df.columns:
    # CORRECTED: Reassigning the DataFrame instead of using inplace=True,
    # as this is the recommended practice and avoids potential future warnings.
    df = df.drop(columns='Cabin')

# CORRECTED: Added a check to ensure 'Embarked' column exists before dropping rows.
# This prevents a KeyError if the column is already missing.
if 'Embarked' in df.columns:
    df = df.dropna(subset=['Embarked'])

# Confirm missing values are handled
print("\nMissing Values After Cleanup:")
print(df.isnull().sum())

# === Survival Distribution ===
# Pie Chart
plt.figure(figsize=(6, 6))
df['Survived'].value_counts().plot.pie(
    autopct='%1.1f%%',
    labels=['Not Survived', 'Survived'],
    colors=['lightcoral', 'lightgreen'],
    startangle=90
)
plt.title("Survival Distribution")
plt.ylabel('')
plt.show()

# Countplot
plt.figure(figsize=(6, 4))
# CORRECTED: Added `hue='Survived'` and `legend=False` to resolve the FutureWarning.
sns.countplot(x='Survived', data=df, palette='Set2', hue='Survived', legend=False)
plt.title("Survival Count")
plt.xticks([0, 1], ['Not Survived', 'Survived'])
plt.show()

# === Survival by Gender ===
plt.figure(figsize=(6, 4))
sns.countplot(x='Sex', hue='Survived', data=df, palette='pastel')
plt.title("Survival by Gender")
plt.legend(labels=['Not Survived', 'Survived'])
plt.show()

# === Survival by Passenger Class ===
plt.figure(figsize=(6, 4))
sns.countplot(x='Pclass', hue='Survived', data=df, palette='coolwarm')
plt.title("Survival by Passenger Class")
plt.legend(labels=['Not Survived', 'Survived'])
plt.show()

# === Age Distribution & Survival ===
# Histogram
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Age', hue='Survived', multiple='stack', palette='Accent', bins=30)
plt.title("Age vs Survival")
plt.show()

# Boxplot
plt.figure(figsize=(6, 4))
# CORRECTED: Added `hue='Survived'` and `legend=False` to resolve the FutureWarning.
sns.boxplot(x='Survived', y='Age', data=df, palette='spring', hue='Survived', legend=False)
plt.title("Age Distribution by Survival")
plt.show()

# === Heatmap of Feature Correlations ===
# Note: Correlation heatmap is for numeric columns only.
plt.figure(figsize=(10, 6))
# Select only numeric columns for correlation calculation
numeric_df = df.select_dtypes(include=['number'])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# === Optional: Crosstab Analysis ===
print("\nCrosstab - Survival by Sex:")
print(pd.crosstab(df['Sex'], df['Survived'], normalize='index'))

print("\nCrosstab - Survival by Pclass:")
print(pd.crosstab(df['Pclass'], df['Survived'], normalize='index'))

# === Done ===
print("\nEDA Completed.")

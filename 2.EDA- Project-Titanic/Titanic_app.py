import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set a title for the Streamlit app
st.title("Titanic Exploratory Data Analysis")

# --- Load Dataset ---
# A function to load the data, using Streamlit's caching to improve performance
@st.cache_data
def load_data():
    """Load the Titanic dataset."""
    try:
        df = pd.read_csv("titanic.csv")
        return df
    except FileNotFoundError:
        st.error("Please make sure 'titanic.csv' is in the same directory.")
        return pd.DataFrame()

df = load_data()

# Only proceed if the data was loaded successfully
if not df.empty:

    st.subheader("Initial Dataset Preview")
    st.write(df.head())

    # --- Dataset Overview ---
    st.subheader("Dataset Overview")
    st.text("Dataset Info:")
    st.code(df.info(buf=pd.io.common.StringIO()), language='python')
    st.text("Statistical Summary:")
    st.write(df.describe())

    # --- Missing Value Analysis ---
    st.subheader("Missing Value Analysis")
    st.text("Missing Values Count:")
    st.write(df.isnull().sum())

    # Heatmap of missing values
    st.markdown("### Missing Values Heatmap")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.isnull(), cbar=False, cmap="viridis", ax=ax)
    st.pyplot(fig)

    # --- Handling Missing Values ---
    st.subheader("Handling Missing Values")

    # CORRECTED: Reassigning the column to fix the FutureWarning.
    df['Age'] = df['Age'].fillna(df['Age'].median())

    # CORRECTED: Added a check to ensure 'Cabin' column exists before dropping.
    if 'Cabin' in df.columns:
        df = df.drop(columns='Cabin')

    # CORRECTED: Added a check to ensure 'Embarked' column exists before dropping rows.
    if 'Embarked' in df.columns:
        df = df.dropna(subset=['Embarked'])

    st.text("Missing Values After Cleanup:")
    st.write(df.isnull().sum())

    # --- Survival Distribution ---
    st.subheader("Survival Distribution")
    
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Survival Pie Chart")
        fig1, ax1 = plt.subplots(figsize=(6, 6))
        df['Survived'].value_counts().plot.pie(
            autopct='%1.1f%%',
            labels=['Not Survived', 'Survived'],
            colors=['lightcoral', 'lightgreen'],
            startangle=90,
            ax=ax1
        )
        ax1.set_ylabel('')
        st.pyplot(fig1)
    
    with col2:
        st.markdown("### Survival Count")
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        # CORRECTED: Added `hue='Survived'` and `legend=False` to resolve the FutureWarning.
        sns.countplot(x='Survived', data=df, palette='Set2', hue='Survived', legend=False, ax=ax2)
        ax2.set_xticklabels(['Not Survived', 'Survived'])
        st.pyplot(fig2)

    # --- Survival by Gender ---
    st.subheader("Survival by Gender")
    fig3, ax3 = plt.subplots(figsize=(6, 4))
    sns.countplot(x='Sex', hue='Survived', data=df, palette='pastel', ax=ax3)
    ax3.legend(labels=['Not Survived', 'Survived'])
    ax3.set_title("Survival by Gender")
    st.pyplot(fig3)

    # --- Survival by Passenger Class ---
    st.subheader("Survival by Passenger Class")
    fig4, ax4 = plt.subplots(figsize=(6, 4))
    sns.countplot(x='Pclass', hue='Survived', data=df, palette='coolwarm', ax=ax4)
    ax4.legend(labels=['Not Survived', 'Survived'])
    ax4.set_title("Survival by Passenger Class")
    st.pyplot(fig4)

    # --- Age Distribution & Survival ---
    st.subheader("Age Distribution & Survival")
    
    st.markdown("### Age vs Survival (Histogram)")
    fig5, ax5 = plt.subplots(figsize=(10, 6))
    sns.histplot(data=df, x='Age', hue='Survived', multiple='stack', palette='Accent', bins=30, ax=ax5)
    st.pyplot(fig5)

    st.markdown("### Age Distribution by Survival (Boxplot)")
    fig6, ax6 = plt.subplots(figsize=(6, 4))
    # CORRECTED: Added `hue='Survived'` and `legend=False` to resolve the FutureWarning.
    sns.boxplot(x='Survived', y='Age', data=df, palette='spring', hue='Survived', legend=False, ax=ax6)
    st.pyplot(fig6)

    # --- Heatmap of Feature Correlations ---
    st.subheader("Heatmap of Feature Correlations")
    fig7, ax7 = plt.subplots(figsize=(10, 6))
    numeric_df = df.select_dtypes(include=['number'])
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=ax7)
    st.pyplot(fig7)

    # --- Optional: Crosstab Analysis ---
    st.subheader("Crosstab Analysis")
    st.text("Crosstab - Survival by Sex:")
    st.write(pd.crosstab(df['Sex'], df['Survived'], normalize='index'))
    st.text("Crosstab - Survival by Pclass:")
    st.write(pd.crosstab(df['Pclass'], df['Survived'], normalize='index'))

    st.success("EDA Completed!")


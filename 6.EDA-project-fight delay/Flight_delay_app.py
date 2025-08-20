import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Set up the Streamlit page configuration
st.set_page_config(
    page_title="Flight Delay Analysis",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and introduction
st.title("Flight Delay Analysis Dashboard")
st.markdown(
    """
    This dashboard provides a comprehensive analysis of flight delays using the `flights.csv` dataset.
    Explore different aspects of delays, including airline performance, common causes, monthly trends, and most delayed routes.
    """
)

# --- Data Loading and Preprocessing ---
@st.cache_data
def load_data(file_path):
    """
    Loads the flight data from a CSV file and performs necessary preprocessing.
    This function is cached to prevent re-loading on every interaction.
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        st.error(f"Error: '{file_path}' not found. Please ensure the file is in the same directory.")
        return None
    
    # Drop rows with missing values in key columns
    df = df.dropna(subset=['ARRIVAL_DELAY', 'DEPARTURE_DELAY'])

    # Convert columns to numeric, handling potential errors
    numeric_cols = ['MONTH', 'DAY_OF_WEEK', 'ARRIVAL_DELAY', 'DEPARTURE_DELAY',
                    'CARRIER_DELAY', 'WEATHER_DELAY', 'NAS_DELAY', 
                    'SECURITY_DELAY', 'LATE_AIRCRAFT_DELAY']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    return df

df = load_data("flights.csv")

if df is not None:
    st.success("Data loaded successfully!")

    # Display some basic info and the dataframe
    st.subheader("Data Overview")
    st.write(f"Shape of the DataFrame: {df.shape}")
    st.write("First 5 rows of the data:")
    st.dataframe(df.head())

    # Create the sidebar for filtering/controls if needed later
    st.sidebar.header("Dashboard Controls")
    
    # --- Visualizations ---

    # 1. Average Arrival Delay by Airline
    st.header("1. Average Arrival Delay by Airline")
    airline_delays = df.groupby('AIRLINE')['ARRIVAL_DELAY'].mean().sort_values(ascending=False)
    fig_airline_delay, ax_airline_delay = plt.subplots(figsize=(10, 5))
    sns.barplot(x=airline_delays.index, y=airline_delays.values, ax=ax_airline_delay)
    ax_airline_delay.set_title("Average Arrival Delay by Airline")
    ax_airline_delay.set_ylabel("Avg Delay (minutes)")
    ax_airline_delay.set_xlabel("Airline")
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig_airline_delay)
    plt.close(fig_airline_delay) # Close the figure to free up memory

    # 2. Total Delay by Cause
    st.header("2. Total Delay by Cause")
    delay_cols = ['CARRIER_DELAY', 'WEATHER_DELAY', 'NAS_DELAY', 'SECURITY_DELAY', 'LATE_AIRCRAFT_DELAY']
    # Drop rows that are NaN for all delay reasons
    df_delay = df[delay_cols].dropna(how='all')
    df_delay_sum = df_delay.sum().sort_values(ascending=False)
    
    fig_delay_cause, ax_delay_cause = plt.subplots(figsize=(8, 5))
    sns.barplot(x=df_delay_sum.index, y=df_delay_sum.values, ax=ax_delay_cause)
    ax_delay_cause.set_title("Total Delay by Cause")
    ax_delay_cause.set_ylabel("Total Minutes")
    ax_delay_cause.set_xticks(range(len(df_delay_sum.index)))
    ax_delay_cause.set_xticklabels(df_delay_sum.index, rotation=45, ha='right')
    st.pyplot(fig_delay_cause)
    plt.close(fig_delay_cause)

    # 3. Monthly Delay Trend
    if 'MONTH' in df.columns:
        st.header("3. Average Arrival Delay by Month")
        monthly_avg_delay = df.groupby('MONTH')['ARRIVAL_DELAY'].mean()
        fig_monthly_trend, ax_monthly_trend = plt.subplots(figsize=(10, 6))
        ax_monthly_trend.plot(monthly_avg_delay, marker='o', linestyle='-')
        ax_monthly_trend.set_title("Average Arrival Delay by Month")
        ax_monthly_trend.set_xlabel("Month")
        ax_monthly_trend.set_ylabel("Avg Arrival Delay (minutes)")
        ax_monthly_trend.grid(True)
        ax_monthly_trend.set_xticks(monthly_avg_delay.index)
        st.pyplot(fig_monthly_trend)
        plt.close(fig_monthly_trend)

    # 4. Top 10 Most Delayed Routes
    st.header("4. Top 10 Most Delayed Routes")
    df['ROUTE'] = df['ORIGIN_AIRPORT'] + " - " + df['DESTINATION_AIRPORT']
    route_delays = df.groupby('ROUTE')['ARRIVAL_DELAY'].mean().sort_values(ascending=False).head(10)

    fig_route_delay, ax_route_delay = plt.subplots(figsize=(10, 6))
    sns.barplot(x=route_delays.values, y=route_delays.index, palette='viridis', ax=ax_route_delay)
    ax_route_delay.set_title("Top 10 Most Delayed Routes")
    ax_route_delay.set_xlabel("Avg Arrival Delay (minutes)")
    ax_route_delay.set_ylabel("Route")
    st.pyplot(fig_route_delay)
    plt.close(fig_route_delay)

    # 5. Arrival Delay Distribution
    st.header("5. Arrival Delay Distribution")
    fig_delay_dist, ax_delay_dist = plt.subplots(figsize=(10, 6))
    sns.histplot(df['ARRIVAL_DELAY'], bins=100, kde=True, color='skyblue', ax=ax_delay_dist)
    ax_delay_dist.set_title("Arrival Delay Distribution")
    ax_delay_dist.set_xlabel("Arrival Delay (minutes)")
    ax_delay_dist.set_ylabel("Frequency")
    ax_delay_dist.set_xlim(-50, 300)
    ax_delay_dist.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig_delay_dist)
    plt.close(fig_delay_dist)

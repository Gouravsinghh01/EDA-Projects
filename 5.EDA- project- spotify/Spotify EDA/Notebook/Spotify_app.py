# app.py

import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# --------------------------------------------------------------------------
# Page Configuration
# --------------------------------------------------------------------------
# Set the configuration for the Streamlit page.
# This is best done as the first Streamlit command.
st.set_page_config(
    page_title="Spotify Data Analysis Dashboard",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------------------------------
# Data Loading
# --------------------------------------------------------------------------
# Use st.cache_data to load the data once and cache it for performance.
@st.cache_data
def load_data(filepath):
    """
    Loads the Spotify dataset from a CSV file.
    Drops rows with any null values.
    """
    try:
        df = pd.read_csv(filepath)
        df.dropna(inplace=True)
        return df
    except FileNotFoundError:
        st.error(f"Error: The file '{filepath}' was not found. Please make sure it's in the same directory as the script.")
        return None

# --------------------------------------------------------------------------
# Main Application Logic
# --------------------------------------------------------------------------

# Set the main title of the dashboard
st.title("🎵 Spotify Features Analysis Dashboard")
st.markdown("An interactive dashboard to explore song features from the Spotify dataset.")

# Load the dataset using the cached function
df = load_data("SpotifyFeatures.csv")

# If the dataframe is not loaded, stop the app.
if df is None:
    st.stop()

# --------------------------------------------------------------------------
# Sidebar for User Inputs and Filters
# --------------------------------------------------------------------------
st.sidebar.header("Filter Options")

# Get a list of unique genres and add an 'All' option for the user
all_genres = ['All'] + sorted(df['genre'].unique().tolist())
selected_genres = st.sidebar.multiselect(
    "Select Genre(s) to Display",
    options=all_genres,
    default=['All']
)

# Filter the dataframe based on the user's genre selection
if 'All' in selected_genres or not selected_genres:
    filtered_df = df
else:
    filtered_df = df[df['genre'].isin(selected_genres)]

# --------------------------------------------------------------------------
# Main Panel: Display Data and Visualizations
# --------------------------------------------------------------------------

# --- Section 1: Dataset Overview ---
st.header("Dataset Overview")
st.markdown(f"Displaying data for: **{', '.join(selected_genres)}**")
st.dataframe(filtered_df.head())
st.write(f"Data Shape: `{filtered_df.shape[0]}` rows and `{filtered_df.shape[1]}` columns.")

st.markdown("---")

# --- Section 2: Correlation and Popularity ---
st.header("Feature Correlation & Genre Popularity")
col1, col2 = st.columns(2)

with col1:
    # Correlation Matrix (using Matplotlib and Seaborn)
    st.subheader("Feature Correlation Matrix")
    corr_cols = ['popularity', 'tempo', 'energy', 'valence', 'loudness', 'danceability']
    # Correlation is calculated on the original dataframe to show overall trends
    corr = df[corr_cols].corr()
    
    fig_corr, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig_corr)

with col2:
    # Average Popularity by Genre (using Plotly)
    st.subheader("Top 10 Genres by Average Popularity")
    # This is also calculated on the original dataframe to show the global top 10
    genre_pop = df.groupby('genre')['popularity'].mean().sort_values(ascending=False).head(10)
    fig_genre_pop = px.bar(
        genre_pop,
        x=genre_pop.index,
        y='popularity',
        labels={'x': 'Genre', 'popularity': 'Average Popularity'},
        color=genre_pop.index,
        color_discrete_sequence=px.colors.qualitative.Vivid
    )
    fig_genre_pop.update_layout(showlegend=False)
    st.plotly_chart(fig_genre_pop, use_container_width=True)

st.markdown("---")

# --- Section 3: Feature Relationships with Popularity ---
st.header("How Do Tempo and Energy Relate to Popularity?")
col3, col4 = st.columns(2)

with col3:
    # Tempo vs Popularity Scatter Plot
    fig_tempo_pop = px.scatter(
        filtered_df.sample(min(1000, len(filtered_df))), # Sample to improve performance
        x='tempo',
        y='popularity',
        color='genre',
        title="Tempo vs. Popularity",
        hover_data=['artist_name', 'track_name']
    )
    st.plotly_chart(fig_tempo_pop, use_container_width=True)

with col4:
    # Energy vs Popularity Scatter Plot
    fig_energy_pop = px.scatter(
        filtered_df.sample(min(1000, len(filtered_df))), # Sample to improve performance
        x='energy',
        y='popularity',
        color='genre',
        title="Energy vs. Popularity",
        hover_data=['artist_name', 'track_name']
    )
    st.plotly_chart(fig_energy_pop, use_container_width=True)

st.markdown("---")

# --- Section 4: Feature Distributions ---
st.header("Distribution of Audio Features")
col5, col6 = st.columns(2)

with col5:
    # Histogram of Tempo
    fig_tempo_hist = px.histogram(filtered_df, x='tempo', nbins=50, title="Tempo Distribution")
    st.plotly_chart(fig_tempo_hist, use_container_width=True)

with col6:
    # Histogram of Energy
    fig_energy_hist = px.histogram(filtered_df, x='energy', nbins=50, title="Energy Distribution")
    st.plotly_chart(fig_energy_hist, use_container_width=True)

st.markdown("---")

# --- Section 5: Music Trends Over Time ---
# Check if a date column exists to derive the year from
# Note: The original Kaggle dataset has 'release_date', not 'year'
date_col = None
if 'year' in df.columns:
    date_col = 'year'
elif 'release_date' in df.columns:
    date_col = 'release_date'

if date_col:
    st.header("Music Trends Over Time")
    df['year'] = pd.to_datetime(df[date_col], errors='coerce').dt.year
    year_trend = df.groupby('year').size().reset_index(name='count')
    year_trend.dropna(subset=['year'], inplace=True)
    year_trend['year'] = year_trend['year'].astype(int)
    
    fig_year_trend = px.line(
        year_trend,
        x='year',
        y='count',
        title="Number of Songs Released Per Year",
        labels={'year': 'Year', 'count': 'Number of Songs'}
    )
    st.plotly_chart(fig_year_trend, use_container_width=True)


st.sidebar.info(
    "This dashboard is created using Streamlit. Select one or more genres "
    "from the sidebar to filter the visualizations."
)
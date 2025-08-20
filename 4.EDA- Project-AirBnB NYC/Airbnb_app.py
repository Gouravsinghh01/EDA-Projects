import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

# Set the title and header of the app
st.set_page_config(layout="wide")
st.title("Airbnb NYC 2019 Data Analysis")
st.header("Exploratory Data Analysis of Airbnb Listings")

# Load data with caching to improve performance
@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    # Drop unnecessary columns
    df.drop(['id', 'name', 'host_name', 'last_review'], axis=1, inplace=True)
    # Fill missing values
    df['reviews_per_month'] = df['reviews_per_month'].fillna(0)
    return df

df = load_data("AB_NYC_2019.csv")

# Display the raw data
if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(df.head())

# Display basic stats
st.subheader("Basic Statistics")
st.write(df.describe())

# Display price distribution plot
st.subheader("Price Distribution (Under $500)")
fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.histplot(df[df['price'] < 500]['price'], bins=50, kde=True, ax=ax1)
ax1.set_title("Price Distribution (Under $500)")
ax1.set_xlabel("Price")
ax1.set_ylabel("Frequency")
st.pyplot(fig1)

# Display room type count plot
st.subheader("Room Type Distribution")
fig2, ax2 = plt.subplots(figsize=(6, 4))
sns.countplot(x='room_type', data=df, ax=ax2)
ax2.set_title("Room Type Distribution")
ax2.set_xlabel("Room Type")
ax2.set_ylabel("Count")
st.pyplot(fig2)

# Display listings per borough plot
st.subheader("Listings by Borough")
fig3, ax3 = plt.subplots(figsize=(8, 5))
sns.countplot(x='neighbourhood_group', data=df, order=df['neighbourhood_group'].value_counts().index, ax=ax3)
ax3.set_title("Listings by Borough")
ax3.set_xlabel("Borough")
ax3.set_ylabel("Number of Listings")
st.pyplot(fig3)

# Display average price per borough plot
st.subheader("Average Price by Borough")
fig4, ax4 = plt.subplots(figsize=(8, 5))
sns.barplot(x='neighbourhood_group', y='price', data=df[df['price'] < 500], ax=ax4)
ax4.set_title("Average Price by Borough")
ax4.set_xlabel("Borough")
ax4.set_ylabel("Average Price ($)")
st.pyplot(fig4)

# Display availability plot
st.subheader("Availability Over the Year")
fig5, ax5 = plt.subplots(figsize=(10, 5))
sns.histplot(df['availability_365'], bins=30, kde=True, ax=ax5)
ax5.set_title("Availability Over the Year")
ax5.set_xlabel("Days Available")
ax5.set_ylabel("Frequency")
st.pyplot(fig5)

# Display Folium heatmap
st.subheader("NYC Airbnb Listing Heatmap")
map_nyc = folium.Map(location=[40.7128, -74.0060], zoom_start=11)
heat_data = [[row['latitude'], row['longitude']] for index, row in df[df['price'] < 500].sample(1000).iterrows()]
HeatMap(heat_data).add_to(map_nyc)
st.components.v1.html(map_nyc._repr_html_(), height=500)

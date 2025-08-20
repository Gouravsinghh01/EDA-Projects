import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration for a wider layout
st.set_page_config(layout="wide", page_title="Superstore Sales & Profit Analysis")

# --- Load data ---
@st.cache_data
def load_data():
    """Load and preprocess the dataset."""
    try:
        df = pd.read_csv("Superstore.csv", encoding='latin-1')
        df['Order Date'] = pd.to_datetime(df['Order Date'])
        df['Month'] = df['Order Date'].dt.month
        df['Year'] = df['Order Date'].dt.year
        return df
    except FileNotFoundError:
        st.error("Error: 'Superstore.csv' not found. Please ensure the file is in the same directory.")
        return pd.DataFrame()

df = load_data()

if not df.empty:
    st.title("Superstore Sales & Profit Dashboard 📈")
    st.markdown("An interactive dashboard to visualize and analyze sales and profit data.")

    # --- Sidebar Filters ---
    st.sidebar.header("Filter Data")

    # Year filter
    years = sorted(df['Year'].unique())
    selected_year = st.sidebar.selectbox("Select Year", ['All'] + years)
    
    # Region filter
    regions = sorted(df['Region'].unique())
    selected_regions = st.sidebar.multiselect("Select Region(s)", regions, default=regions)

    # Apply filters
    filtered_df = df.copy()
    if selected_year != 'All':
        filtered_df = filtered_df[filtered_df['Year'] == selected_year]
    if selected_regions:
        filtered_df = filtered_df[filtered_df['Region'].isin(selected_regions)]

    if filtered_df.empty:
        st.warning("No data available for the selected filters.")
    else:
        # --- Display Key Metrics ---
        total_sales = filtered_df['Sales'].sum()
        total_profit = filtered_df['Profit'].sum()
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Sales", f"${total_sales:,.2f}")
        with col2:
            st.metric("Total Profit", f"${total_profit:,.2f}")

        st.markdown("---")

        # --- Analysis and Visualization ---

        st.header("Sales & Profit Analysis by Category & Segment")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Category-wise Sales & Profit")
            category_group = filtered_df.groupby('Category')[['Sales', 'Profit']].sum().sort_values(by='Sales', ascending=False)
            fig, ax = plt.subplots(figsize=(10, 6))
            category_group.plot(kind='bar', ax=ax, width=0.8, color=['skyblue', 'salmon'])
            ax.set_title("Sales and Profit by Category")
            ax.set_xlabel("Category")
            ax.set_ylabel("Amount")
            ax.tick_params(axis='x', rotation=0)
            st.pyplot(fig)

        with col2:
            st.subheader("Segment-wise Performance")
            seg_perf = filtered_df.groupby('Segment')[['Sales', 'Profit']].sum()
            fig, ax = plt.subplots(figsize=(8, 5))
            seg_perf.plot(kind='bar', ax=ax, color=['lightgreen', 'orange'], width=0.6)
            ax.set_title("Sales & Profit by Customer Segment")
            ax.set_xlabel("Customer Segment")
            ax.set_ylabel("Amount")
            ax.tick_params(axis='x', rotation=0)
            st.pyplot(fig)

        st.markdown("---")

        st.header("Geographical & Time-Based Trends")
        
        col3, col4 = st.columns(2)
        
        with col3:
            st.subheader("Profit by Region")
            region_profit = filtered_df.groupby('Region')['Profit'].sum().sort_values(ascending=False)
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.barplot(x=region_profit.values, y=region_profit.index, palette='viridis', hue=region_profit.index, legend=False, ax=ax)
            ax.set_title("Profit by Region")
            ax.set_xlabel("Total Profit")
            ax.set_ylabel("Region")
            st.pyplot(fig)
            
        with col4:
            st.subheader("Monthly Sales Trend")
            monthly_sales = filtered_df.groupby(['Year', 'Month'])['Sales'].sum()
            monthly_sales = monthly_sales.sort_index()
            fig, ax = plt.subplots(figsize=(12, 6))
            monthly_sales.plot(ax=ax, color='purple', marker='o', linestyle='-')
            ax.set_title("Monthly Sales Trend Over Time")
            ax.set_xlabel("Date")
            ax.set_ylabel("Total Sales")
            st.pyplot(fig)

        st.markdown("---")

        st.header("Sub-Category Performance")
        st.subheader("Profit by Sub-Category")
        subcat = filtered_df.groupby('Sub-Category')['Profit'].sum().sort_values(ascending=True)
        fig, ax = plt.subplots(figsize=(12, 8))
        colors = ['red' if profit < 0 else 'green' for profit in subcat]
        sns.barplot(x=subcat.values, y=subcat.index, palette=colors, hue=subcat.index, legend=False, ax=ax)
        ax.set_title("Profit by Sub-Category")
        ax.set_xlabel("Total Profit")
        ax.set_ylabel("Sub-Category")
        st.pyplot(fig)
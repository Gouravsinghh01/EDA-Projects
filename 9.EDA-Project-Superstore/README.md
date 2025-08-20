Superstore Sales & Profit Dashboard
This project features a Streamlit dashboard for an in-depth analysis of a superstore's sales and profit data. It provides interactive visualizations that allow users to explore key business metrics, identify trends, and analyze performance across different categories, regions, and customer segments.

📁 Project Structure
Superstore.csv: The primary dataset used for the analysis.

app.py: The Python script that contains the full code for the Streamlit dashboard, including data loading, preprocessing, and all the visualizations.

README.md: This file, which outlines the project's purpose and how to run the application.

requirements.txt: A list of all necessary Python libraries to run the app.

🚀 How to Run the Application
1. Prerequisites
You need Python 3.8+ installed on your system.

2. Install Dependencies
Clone this repository and navigate into the project directory. Then, install the required libraries using the provided requirements.txt file.

Bash

git clone <repository-url>
cd <repository-folder>
pip install -r requirements.txt
3. Launch the Dashboard
Ensure the Superstore.csv file is in the same directory as app.py. From your terminal, run the following command to start the Streamlit application:

Bash

streamlit run app.py
Your default web browser will open a new tab displaying the interactive dashboard.

📊 Dashboard Features
The dashboard is divided into several sections, each providing a different perspective on the data. Users can interact with the visualizations by using the filters in the left sidebar.

Key Metrics: At the top, a quick summary displays the total sales and total profit for the selected data.

Sales & Profit by Category: A bar chart that compares sales and profit performance across different product categories.

Segment Performance: A bar chart showing the sales and profit breakdown by customer segment (e.g., Consumer, Corporate, Home Office).

Profit by Region: A horizontal bar chart that ranks total profit by geographical region.

Monthly Sales Trend: A line graph that visualizes the sales trend over time, allowing you to see seasonality and growth.

Sub-Category Profit: A bar chart highlighting the profit or loss of each sub-category, with profitable items in green and unprofitable ones in red.
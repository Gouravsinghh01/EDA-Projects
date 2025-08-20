Titanic Exploratory Data Analysis
This is a Streamlit application for performing exploratory data analysis on the famous Titanic dataset. The app provides a series of visualizations and statistical summaries to help understand the factors that influenced survival.

Features
Dataset Overview: Displays the initial data, information, and a statistical summary.

Missing Value Analysis: Shows the count of missing values and a heatmap to visualize their distribution.

Survival Distribution: Visualizes the overall survival rate using a pie chart and a count plot.

Survival by Gender & Class: Breaks down survival rates based on the passenger's sex and ticket class.

Age Distribution: Explores the age distribution of passengers and its relationship with survival through a histogram and a boxplot.

Correlation Heatmap: Shows the correlation between numerical features in the dataset.

Crosstab Analysis: Provides tables to see the normalized survival rates by gender and class.

Prerequisites
To run this application, you need to have Python 3.x installed on your system.

Installation
Save the files: Ensure that app.py (or whatever you named your Streamlit file), titanic.csv, and requirements.txt are all in the same directory.

Install dependencies: Open your terminal or command prompt, navigate to the project directory, and run the following command to install the required libraries:

pip install -r requirements.txt

Usage
Once the dependencies are installed, you can launch the application with the following command from your terminal:

streamlit run app.py

This will open a new tab in your web browser with the interactive EDA dashboard.
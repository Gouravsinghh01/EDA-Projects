Zomato Restaurant Analytics Dashboard
This project provides an interactive Streamlit dashboard for analyzing Zomato restaurant data. It focuses on key metrics such as restaurant distribution across cities, rating trends, and cuisine popularity. The dashboard allows users to dynamically filter the data and visualize the results, offering valuable insights into the food and beverage industry.

📁 Project Structure
zomato.csv: The raw dataset containing detailed information about restaurants.

app.py: The main Python script that runs the Streamlit web application. This file contains all the data cleaning, analysis, and visualization code.

README.md: This file, which provides an overview of the project.

requirements.txt: A list of all necessary Python libraries to run the application.

🚀 How to Run the App
1. Prerequisites
Ensure you have Python 3.8 or a later version installed on your system.

2. Install Dependencies
First, clone this repository to your local machine.

Bash

git clone <repository-url>
cd <repository-folder>
Next, install all the required libraries using the requirements.txt file.

Bash

pip install -r requirements.txt
3. Run the Dashboard
Make sure the zomato.csv file is in the same directory as app.py. Then, execute the following command in your terminal:

Bash

streamlit run app.py
Your web browser will automatically open the interactive dashboard. You can use the sidebar to filter the data by minimum rating and city to explore different aspects of the dataset.

📊 Key Features of the Dashboard
Data Filtering: Use the sidebar sliders and multi-select boxes to filter the displayed data based on minimum rating and city.

Restaurant Distribution: A bar chart shows the top 10 city areas with the highest number of restaurants.

Rating Analysis: A histogram visualizes the overall distribution of restaurant ratings.

Cuisine Popularity: A bar chart highlights the top 10 most popular cuisines based on their frequency in the dataset.

Cost vs. Rating: A scatter plot explores the relationship between a restaurant's cost and its customer rating.
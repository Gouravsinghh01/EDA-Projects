AirBnB NYC 2019 Data Analysis
This project performs an exploratory data analysis (EDA) of the AirBnB listings in New York City for the year 2019. It leverages Python libraries such as pandas, matplotlib, seaborn, and folium to clean the data, visualize key insights, and build an interactive web application using streamlit.

Key Features
Data Loading and Cleaning: The script loads the AB_NYC_2019.csv dataset, handles missing values, and removes irrelevant columns to prepare the data for analysis.

Data Visualization: It generates several plots to understand the distribution of listings, prices, and room types across different boroughs of NYC.

Price Distribution: A histogram showing the frequency of listing prices, focusing on listings under $500.

Room Type Distribution: A bar chart illustrating the number of listings for each room type (e.g., Entire home/apt, Private room).

Geographical Analysis: A count plot of listings per borough and a bar chart of the average price in each borough.

Availability: A histogram showing the distribution of availability_365 days.

Interactive Heatmap: An interactive Folium heatmap is generated to visually represent the density of listings across NYC. This map is saved as an HTML file.

Streamlit Web App: The analysis is packaged into a Streamlit application (app.py), allowing users to interactively view the visualizations and data insights in a web browser.

How to Run the Project
1. Clone the Repository
First, clone this repository to your local machine.

Bash

git clone <repository_url>
cd <repository_folder>
2. Install Dependencies
Install all the required Python libraries using the requirements.txt file.

Bash

pip install -r requirements.txt
3. Run the Streamlit App
Execute the following command in your terminal to launch the web application.

Bash

streamlit run app.py
This will open a new tab in your web browser with the interactive dashboard.
IPL Exploratory Data Analysis Dashboard
This project is a web-based dashboard built with Streamlit for performing exploratory data analysis (EDA) on IPL (Indian Premier League) match data. The app provides various visualizations and insights into team performance, player statistics, and match trends.

Features
Match-Winning Analysis: Visualizations showing teams with the most wins, and distributions of wins by runs and wickets.

Toss Impact: An analysis of whether winning the toss increases the probability of winning the match.

Player Performance: Bar charts of the top 10 run-scorers and top 10 wicket-takers.

Season Trends: A bar chart showing the number of matches played each season.

Files in this Repository
app.py: The main Streamlit application file.

matches.csv: The dataset containing information about IPL matches.

deliveries.csv: The dataset containing ball-by-ball details of all IPL matches.

requirements.txt: A list of all necessary Python libraries for the project.

.gitignore: A file to ignore unnecessary files and folders in version control.

How to Run the Application
Clone the repository (if applicable) or ensure all the files listed above are in the same directory.

Install the required libraries using the requirements.txt file:

pip install -r requirements.txt

Run the Streamlit application from your terminal:

streamlit run app.py

The application will automatically open in your web browser.
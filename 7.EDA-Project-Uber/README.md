# Uber NYC Trip Data Analysis

This project analyzes Uber trip data from April 2014 in New York City. It uses Python libraries such as `pandas`, `seaborn`, `matplotlib`, and `folium` to explore trip patterns, visualize data, and create an interactive dashboard.

## 📁 Project Structure

* `uber-raw-data-apr14.csv`: The raw dataset containing Uber trip information for April 2014.
* `data_exploration.py`: A Python script for initial data loading, cleaning, and generating static visualizations like trip frequency plots and heatmaps.
* `app.py`: A Streamlit application that creates an interactive dashboard, allowing users to filter trip data and view a dynamic heatmap of pickup locations.
* `hourly_trips.png`: A bar chart showing trip frequency by hour of the day.
* `weekday_trips.png`: A bar chart showing trip frequency by day of the week.
* `hour_vs_weekday_heatmap.png`: A heatmap illustrating the density of trips at different hours and on different days.
* `nyc_pickup_map.html`: An interactive `folium` map displaying a heatmap of all pickup locations.
* `README.md`: This file.
* `requirements.txt`: A list of all necessary Python libraries to run the project.

## 📊 Analysis and Visualizations

The project provides several key insights into Uber trips:

* **Hourly Trip Frequency:** The `hourly_trips.png` plot shows the distribution of trips throughout a 24-hour period, revealing peak hours.
* **Weekly Patterns:** The `weekday_trips.png` plot visualizes how trip activity varies from Monday to Sunday.
* **Time-based Heatmap:** The `hour_vs_weekday_heatmap.png` provides a detailed look at trip density, highlighting popular times and days (e.g., late Friday and Saturday nights).
* **Geographical Hotspots:** The `nyc_pickup_map.html` and the interactive map in `app.py` use a heatmap to identify the most common pickup locations across NYC.

## 🚀 How to Run the Project

### 1. Prerequisites

Make sure you have Python installed. The project was developed with Python 3.8 or higher.

### 2. Install Dependencies

First, clone this repository to your local machine.
```bash
git clone <repository-url>
cd <repository-folder>
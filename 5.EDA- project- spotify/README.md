# 🎵 Spotify Data Analysis Dashboard

An interactive web application built with Streamlit to analyze and visualize the Spotify Features dataset. This dashboard provides insights into song popularity, audio features like tempo and energy, and trends over time.



---

## ✨ Features

* **Interactive Filtering**: Dynamically filter the entire dashboard by one or more genres.
* **Correlation Matrix**: Visualize the correlation between key audio features like `popularity`, `energy`, `tempo`, and `danceability`.
* **Genre Popularity**: A bar chart displaying the top 10 most popular genres based on average track popularity.
* **Feature Analysis**: Scatter plots to explore the relationship between `tempo`/`energy` and `popularity`.
* **Data Distribution**: Histograms showing the distribution of `tempo` and `energy` across the selected genres.
* **Trend Analysis**: A line chart illustrating the number of songs released per year.

---

## 🚀 Setup and Installation

Follow these steps to get the application running on your local machine.

### **1. Prerequisites**

Make sure you have **Python 3.8** or newer installed on your system.

### **2. Clone the Repository**

Open your terminal and clone the project repository:
```bash
git clone <your-repository-url>
cd <your-repository-directory>
```

### **3. Create a Virtual Environment**

It is highly recommended to create a virtual environment to manage project dependencies.

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### **4. Install Dependencies**

Install all the required libraries using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### **5. Download the Dataset**

Download the `SpotifyFeatures.csv` dataset and place it in the **root directory** of the project.

---

## ▶️ How to Run the Application

Once the setup is complete, you can launch the Streamlit application with the following command:

```bash
streamlit run app.py
```

Your web browser will automatically open a new tab with the running dashboard. Enjoy exploring the data! 🎶

---

## 📂 Project Structure

```
.
├── .gitignore          # Specifies files for Git to ignore
├── app.py              # The main Streamlit application script
├── README.md           # Project documentation (this file)
├── requirements.txt    # List of Python dependencies
└── SpotifyFeatures.csv # The dataset file 
```
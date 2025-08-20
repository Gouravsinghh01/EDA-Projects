import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap
import calendar

# Load Dataset
df = pd.read_csv('uber-raw-data-apr14.csv')
df['Date/Time'] = pd.to_datetime(df['Date/Time'])
df['Hour'] = df['Date/Time'].dt.hour
df['DayOfWeek'] = df['Date/Time'].dt.dayofweek
df['Day'] = df['Date/Time'].dt.day
df['Month'] = df['Date/Time'].dt.month
df['Weekday'] = df['DayOfWeek'].apply(lambda x: calendar.day_name[x])

# Plot hourly trip frequency
plt.figure(figsize=(10,5))
sns.countplot(x='Hour', data=df)
plt.title('Trips by Hour of Day')
plt.savefig('hourly_trips.png')
plt.show()

# Plot weekday patterns
plt.figure(figsize=(10,5))
sns.countplot(x='Weekday', data=df, order=calendar.day_name)
plt.title('Trips by Day of Week')
plt.xticks(rotation=45)
plt.savefig('weekday_trips.png')
plt.show()

# Heatmap: Hour vs Day of Week
heatmap_data = df.groupby(['Hour', 'DayOfWeek']).size().unstack()
plt.figure(figsize=(12,6))
sns.heatmap(heatmap_data, cmap='YlGnBu')
plt.title('Heatmap: Hour vs Day of Week')
plt.savefig('hour_vs_weekday_heatmap.png')
plt.show()

# Folium Map of Pickup Locations
pickup_map = folium.Map(location=[40.75, -73.95], zoom_start=12)
heat_data = df[['Lat', 'Lon']].dropna().values.tolist()
HeatMap(heat_data[:10000]).add_to(pickup_map)
pickup_map.save('nyc_pickup_map.html')


print("code successful")

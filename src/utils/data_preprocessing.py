import pandas as pd
import json
import os
from datetime import datetime


directory_path = r'../../sensors/data/raw'


timestamps = []
moistures = []
below_30 = []
sensors = []


for filename in os.listdir(directory_path):
    if filename.endswith(".json"):
        file_path = os.path.join(directory_path, filename)
        with open(file_path) as f:
            # Read each line as a JSON object
            lines = f.readlines()
            for line in lines:
                try:
                    json_object = json.loads(line)
                    for sensor, data in json_object.items():
                        timestamps.append(data['timestamp'])
                        moistures.append(data['moisture'])
                        sensors.append(sensor)
                        # Create target variable indicating whether moisture is below 30%
                        below_30.append(1 if data['moisture'] < 0.3 else 0)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON in {file_path}: {e}")

timestamps = [datetime.fromisoformat(ts) for ts in timestamps]


# Extract additional features from timestamps
day_of_week = [ts.weekday() for ts in timestamps]
hour_of_day = [ts.hour for ts in timestamps]
month = [ts.month for ts in timestamps]
year = [ts.year for ts in timestamps]


time_of_day_bins = []
for hour in hour_of_day:
    if 6 <= hour < 12:
        time_of_day_bins.append('morning')
    elif 12 <= hour < 18:
        time_of_day_bins.append('afternoon')
    else:
        time_of_day_bins.append('evening')


# Calculate time since the last occurrence of moisture below threshold
time_since_last_below_threshold = []
last_below_threshold_timestamp = None

for timestamp, below_threshold in zip(timestamps, below_30):
    if below_threshold == 1:
        last_below_threshold_timestamp = timestamp

    if last_below_threshold_timestamp is not None:
        time_since_last_below_threshold.append((timestamp - last_below_threshold_timestamp).total_seconds())
    else:
        time_since_last_below_threshold.append(None)

# Create a pandas DataFrame
df = pd.DataFrame({
    'sensor': sensors,
    'timestamp': timestamps,
    'moisture': moistures,
    'below_30': below_30,
    'day_of_week': day_of_week,
    'hour_of_day': hour_of_day,
    'month': month,
    'year': year,
    'time_of_day': time_of_day_bins,
    'time_since_last_below_threshold': time_since_last_below_threshold
})

# Display the resulting DataFrame
print(df)
filename = f"../../sensors/data/processed/sensor_data_{datetime.now().date()}.csv"
df.to_csv(filename, index=False)
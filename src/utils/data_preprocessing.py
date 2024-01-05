import pandas as pd
import json
import os
from datetime import datetime

# Specify the directory path containing JSON files
directory_path = r'../../sensors/data/raw'

# Initialize lists to store extracted data
timestamps = []
moistures = []
below_30 = []
sensors = []

# Iterate over each JSON file in the specified directory
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

# Convert timestamp strings to datetime objects
timestamps = [datetime.fromisoformat(ts) for ts in timestamps]

# Extract additional features from timestamps
day_of_week = [ts.weekday() for ts in timestamps]
hour_of_day = [ts.hour for ts in timestamps]

# Create a pandas DataFrame
df = pd.DataFrame({
    'sensor': sensors,
    'timestamp': timestamps,
    'moisture': moistures,
    'below_30': below_30,
    'day_of_week': day_of_week,
    'hour_of_day': hour_of_day
})

# Display the resulting DataFrame
print(df)

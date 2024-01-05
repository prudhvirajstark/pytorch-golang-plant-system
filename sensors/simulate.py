# simulate.py

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import random
import time
import threading
import json
from datetime import datetime

app = FastAPI()

# Mock data for four moisture sensors
sensors_data = {
    "sensor1": {"timestamp": None, "moisture": 0.0},
    "sensor2": {"timestamp": None, "moisture": 0.0},
    "sensor3": {"timestamp": None, "moisture": 0.0},
    "sensor4": {"timestamp": None, "moisture": 0.0},
}

def simulate_moisture_data():
    """
    Simulate moisture data every 3 minutes.
    Update the data every second.
    """
    while True:
        start_time = time.time()
        while time.time() - start_time < 180:  # Simulate for 3 minutes
            current_time = datetime.utcnow().isoformat()
            for sensor_name in sensors_data:

                sensors_data[sensor_name]["timestamp"] = current_time
                sensors_data[sensor_name]["moisture"] = round(random.uniform(0.0, 1.0), 2)


            filename = f"data/raw/sensor_data_{datetime.utcnow().date()}.json"

            # Write data to the JSON file
            with open(filename, "a") as json_file:
                json.dump(sensors_data, json_file)
                json_file.write("\n")
                time.sleep(0.001)

        # Sleep for 2 minutes before starting the next simulation
        time.sleep(10)


# Run the simulation in a separate thread as a daemon
simulation_thread = threading.Thread(target=simulate_moisture_data, daemon=True)
simulation_thread.start()

@app.get("/moisture-sensors")
async def get_moisture_data():
    return JSONResponse(content=sensors_data)

if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI app
    uvicorn.run(app, host="0.0.0.0", port=8000)

# pytorch-golang-plant-system
This repository contains the source code for a Smart Plant Watering System, an automated solution for monitoring and managing the watering needs of potted plants. The system integrates deep learning, microservices in Golang, and databases to create an intelligent and efficient plant care solution.

# start the simulator to get 4 sensors data for 2 minutes
- Go to sensors folder and run the following command, to start the sample json data simulation
- uvicorn simulate:app --host 0.0.0.0 --port 80

# data ingestion service in golang, Reads the data from json files and stores in databases along with time stamp

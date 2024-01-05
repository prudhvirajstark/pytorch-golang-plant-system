# pytorch-golang-plant-system
This repository contains the source code for a Smart Plant Watering System, an automated solution for monitoring and managing the watering needs of potted plants. The system integrates deep learning, microservices in Golang, and databases to create an intelligent and efficient plant care solution.

# start the simulator to get 4 sensors data for 2 minutes
- Go to sensors folder and run the following command, to start the sample json data simulation
- uvicorn simulate:app --host 0.0.0.0 --port 80

# data ingestion service in golang, Reads the data from json files and stores in databases along with time stamp

# Pytorch model

## Data Preprocessing:

1. Load your JSON data into a suitable data structure (e.g., pandas DataFrame).
2. Extract the relevant features (timestamp and moisture) for each sensor.
3. Create a target variable indicating whether the moisture is below 30% for all sensors.

## Feature Engineering:

4. You may need to extract additional features from the timestamp, such as day of the week, hour of the day, etc., to improve the model's performance.

## Train-Test Split:

5. Split your dataset into training and testing sets. This is crucial for evaluating the model's performance.

## Model Definition:

6. Define a deep learning model using PyTorch. You can use a recurrent neural network (RNN) or long short-term memory (LSTM) network, as they are well-suited for sequential data.
7. Your model should take historical moisture values as input and predict the moisture for the next week.

## Loss Function and Optimizer:

8. Choose a suitable loss function, such as Mean Squared Error (MSE), since this is a regression problem.
9. Select an optimizer (e.g., Adam or SGD) to update the model parameters during training.

## Training:

10. Train your model using the training dataset.
11. Monitor the loss on the validation set to ensure your model is not overfitting.

## Evaluation:

12. Evaluate your model on the test set to assess its performance.
13. You can use metrics like MSE, MAE (Mean Absolute Error), or others depending on your specific requirements.

## Prediction:

14. Use your trained model to make predictions for the next week's moisture values.

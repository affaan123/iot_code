import requests
import json


# Function to send data to the ML model
def send_to_model(data):
    url = 'http://127.0.0.1:5000/predict'
    payload = {'features': data}
    response = requests.post(url, json=payload)
    return response.json()


# Sample data: it should be same as loaded by ML model excluding the temperature that we need to predict
# based on sample data.
sample_data = [
    [60, 5.0, 0.0],  # Data for the first row
    [65, 4.5, 0.1],  # Data for the second row
    [63, 4.8, 0.0],  # Data for the third row
    [60, 5.2, 0.2],  # Data for the fourth row
    [70, 3.9, 0.0],  # Data for the fifth row
    [58, 5.1, 0.0],  # Data for the sixth row
    [66, 4.4, 0.1]  # Data for the seventh row
]

# Send each row of sample data to the model and print the predictions
for i, data in enumerate(sample_data):
    prediction = send_to_model(data)
    print(f"Prediction for sample {i + 1}: {prediction}")

# Import necessary libraries for data manipulation, numerical operations, machine learning, and visualization
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt

# Load the sample data from a CSV file into a pandas DataFrame
data = pd.read_csv('weather_data.csv')

# Display the first few rows of the dataset to understand its structure
print("First few rows of the dataset:")
print(data.head())

# Display summary statistics to get an overview of the data distribution
print("\nSummary statistics:")
print(data.describe())

# Display information about the dataset, such as data types and non-null counts
print("\nDataset info:")
print(data.info())

# Check for missing values in each column to identify any potential issues with the data
print("\nMissing values in each column:")
print(data.isnull().sum())

# Prepare the features and target variables
# Features include all columns except 'temperature'
features = data.drop('temperature', axis=1)
# Target variable is the 'temperature' column
target = data['temperature']

# Split the data into training and testing sets
# 80% of the data will be used for training and 20% for testing
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Scale the features to have zero mean and unit variance
# This is important for algorithms that are sensitive to the scale of the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)  # Fit the scaler on the training data and transform it
X_test = scaler.transform(X_test)  # Transform the testing data using the same scaler

# Define and train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)  # Train the model on the training data

# Make predictions on the testing data
predictions = model.predict(X_test)

# Evaluate the model using different metrics
mse = mean_squared_error(y_test, predictions)  # Mean Squared Error
mae = mean_absolute_error(y_test, predictions)  # Mean Absolute Error
r2 = r2_score(y_test, predictions)  # R² Score, indicating the proportion of variance explained by the model

# Print the evaluation metrics
print(f"\nMean Squared Error: {mse}")
print(f"Mean Absolute Error: {mae}")
print(f"R² Score: {r2}")

# Visualize the predictions versus the actual values
plt.scatter(y_test, predictions, color='blue', label='Predicted vs Actual')
plt.xlabel('Actual Temperature')
plt.ylabel('Predicted Temperature')
plt.title('Actual vs Predicted Temperature')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--', label='Line of Equality')
plt.legend()
plt.show()

# Optionally, save and load the trained model using joblib
import joblib
joblib.dump(model, 'weather_prediction_model.pkl')  # Save the model to a file

# Load the saved model
loaded_model = joblib.load('weather_prediction_model.pkl')

# Make new predictions with the loaded model to verify it was saved and loaded correctly
new_predictions = loaded_model.predict(X_test)
print('New Predictions:', new_predictions)
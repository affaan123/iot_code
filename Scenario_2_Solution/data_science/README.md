Prerequisites

	•	Python 3.x
	•	Docker

Files Overview

	•	Dockerfile.flaskapp: Docker configuration for the Flask app.
	•	flask_app.py: Flask API serving the machine learning model.
	•	flask-app-deployment.yml: Kubernetes deployment configuration.
	•	weather_data.csv: Sample weather data.
	•	weather_prediction_model.pkl: Pre-trained machine learning model.
	•	weather_prediction.py: Script for training the machine learning model.

Steps to Run

1. Train the Model (if needed)

To retrain the model, run:
python weather_prediction.py
This will generate weather_prediction_model.pkl.

2. Build and Run the Flask App with Docker

	1.	Build the Docker image:
	docker build -t flask-app -f Dockerfile.flaskapp .

	2.	Run the Docker container:
	docker run -p 5000:5000 flask-app
	The Flask API will be accessible at http://localhost:5000.

3. Deploy with Kubernetes

To deploy the app on a Kubernetes cluster:
kubectl apply -f flask-app-deployment.yml
This will deploy the Flask app API using the pre-trained model. This API can then be used by IoT system

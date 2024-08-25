This project consists of a CoAP server-client setup, MQTT client for publishing weather data, and scripts to publish data to Google Pub/Sub. The structure is as follows:

	•	coap_server.py: CoAP server to handle incoming requests.
	•	coap_client.py: CoAP client to send requests to the server.
	•	publish_weather.py: MQTT client to publish weather data to a topic.
	•	publish_weather_to_google.py: Script to publish weather data from MQTT to Google Pub/Sub.
	•	google_iot_client.py: Client to publish data directly to Google Pub/Sub.
	•	mosquitto_pub: Command-line tool to publish messages to MQTT topics.

Prerequisites

	1.	Python 3.x installed.
	2.	Pip installed for managing Python packages.
	3.	Mosquitto MQTT broker installed.
	4.	Google Cloud SDK installed and configured.
	5.	Service Account Key for Google Pub/Sub.

Setup

	1.	Install the required Python packages:
	pip install -r requirements.txt

	2. Ensure that your service account key file is in the correct location and that the Google Cloud SDK is properly configured.

Running the CoAP Server and Client

	1.	Start the CoAP Server:
	python coap_server.py

	This will start the CoAP server that listens for incoming requests.

	2.	Run the CoAP Client:
	python coap_client.py

	The client will send a request to the CoAP server and receive a response.

Publishing Weather Data using MQTT

	1.	Start the MQTT Broker (if not already running):
	python publish_weather.py
	This script publishes weather data to the MQTT topic weather/data.

Publishing Weather Data to Google Pub/Sub

	1.	Publish Data from MQTT to Google Pub/Sub:
 First, use mosquitto_pub to publish a message to the MQTT topic weather/data:
 mosquitto_pub -h <broker_address> -t weather/data -m "<your_message>"

 Then, run the script to publish this data to Google Pub/Sub vi MQTT broker:
 python publish_weather_to_google.py

2.	Publish Data Directly to Google Pub/Sub:
If you want to publish data directly to Google Pub/Sub without using MQTT, run the following script:
python google_iot_client.py


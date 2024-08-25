import os
from google.cloud import pubsub_v1
import json

# Set the environment variable for authentication
# This points to the JSON key file needed to authenticate with Google Cloud services
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/affaan/Documents/iotproject-key.json"

# Google Cloud Pub/Sub configuration
# Define the Google Cloud project ID and Pub/Sub topic ID
project_id = "iotproject-430415"  # Replace with your Google Cloud project ID
topic_id = "weather"  # Replace with your Pub/Sub topic ID

# Create a Pub/Sub Publisher client instance
publisher = pubsub_v1.PublisherClient()

# Construct the fully qualified topic path
# This combines the project ID and topic ID to form the topic path
topic_path = publisher.topic_path(project_id, topic_id)

# Data to publish
# Create a dictionary with the data you want to send. Here is the entrypoint for receiving data from sensors.
data = {"temperature": 20, "humidity": 30}

# Convert the data dictionary to a JSON string
data_str = json.dumps(data)

# Publish the message to the Pub/Sub topic
# Encode the JSON string to bytes and send it to the Pub/Sub topic
# The publish method returns a future which will contain the message ID
future = publisher.publish(topic_path, data_str.encode("utf-8"))

# Print the message ID of the published message
# Use future.result() to wait for the publish operation to complete and get the message ID
print(f"Published message ID: {future.result()}")
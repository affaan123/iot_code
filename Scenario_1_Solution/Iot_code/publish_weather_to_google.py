import os
import json
import paho.mqtt.client as mqtt
from google.cloud import pubsub_v1

# Set the environment variable for authentication to Google Cloud
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/affaan/Documents/iotproject-key.json"

# Google Cloud Pub/Sub configuration
project_id = "iotproject-430415"  # Google Cloud project ID
topic_id = "weather"  # The Pub/Sub topic to publish messages to
publisher = pubsub_v1.PublisherClient()  # Create a Pub/Sub Publisher client
topic_path = publisher.topic_path(project_id, topic_id)  # Construct the topic path


# Function to publish messages to Google Cloud Pub/Sub
def publish_to_pubsub(data):
    # Convert the data to a JSON string
    data_str = json.dumps(data)
    # Publish the data to the Pub/Sub topic
    future = publisher.publish(topic_path, data_str.encode("utf-8"))
    # Print the message ID of the published message
    print(f"Published message ID to Pub/Sub: {future.result()}")


# MQTT callback function triggered when a message is received
def on_message(client, userdata, msg):
    try:
        # Decode the payload and parse it as JSON
        payload = json.loads(msg.payload.decode('utf-8'))
        print(f"Received from MQTT: {payload}")
        # Publish the received data to Pub/Sub
        publish_to_pubsub(payload)
    except json.JSONDecodeError as e:
        # Handle JSON decoding errors
        print(f"Error decoding JSON: {e}")


# Function to start the MQTT to Pub/Sub bridge
def start_mqtt_to_pubsub_bridge():
    client = mqtt.Client()  # Create an MQTT client instance

    # Set the MQTT callback function for message reception
    client.on_message = on_message

    # MQTT broker configuration
    mqtt_broker = "localhost"  # Address of the MQTT broker
    mqtt_port = 1883  # Port of the MQTT broker
    mqtt_topic = "weather/data"  # MQTT topic to subscribe to

    # Connect to the MQTT broker
    client.connect(mqtt_broker, mqtt_port, 60)
    # Subscribe to the MQTT topic
    client.subscribe(mqtt_topic)

    print(f"Connected to MQTT broker at {mqtt_broker}:{mqtt_port}, subscribed to topic '{mqtt_topic}'")

    # Start the MQTT client loop to process network traffic and dispatch callbacks
    client.loop_forever()


# Main execution block
if __name__ == "__main__":
    start_mqtt_to_pubsub_bridge()

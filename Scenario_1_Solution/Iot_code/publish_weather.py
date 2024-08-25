import paho.mqtt.client as mqtt  # Import the MQTT client library for communication
import time  # Import the time library for delays
import random  # Import the random library for generating random numbers


# Define a function to publish simulated weather data
def publish_weather_data():
    # Create a new MQTT client instance
    client = mqtt.Client()
    # Connect the client to the MQTT broker at localhost on port 1883 with a keepalive of 60 seconds
    client.connect("localhost", 1883, 60)

    # Enter an infinite loop to continuously publish data
    while True:
        # Generate random temperature and humidity values
        temperature = random.uniform(20.0, 30.0)  # Random temperature between 20.0 and 30.0 degrees Celsius
        humidity = random.uniform(30.0, 70.0)  # Random humidity between 30.0 and 70.0 percent
        # Create a payload string with the temperature and humidity
        payload = f"Temperature: {temperature:.2f}, Humidity: {humidity:.2f}"
        # Publish the payload to the "weather/data" topic
        client.publish("weather/data", payload)
        # Print the published payload to the console
        print(f"Published: {payload}")
        # Wait for 5 seconds before publishing the next data
        time.sleep(5)


# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    publish_weather_data()  # Call the function to start publishing weather data

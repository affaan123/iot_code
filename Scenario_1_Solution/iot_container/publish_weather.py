import paho.mqtt.client as mqtt
import time
import random


def publish_weather_data():
    client = mqtt.Client()
    client.connect("mqtt-broker", 1883, 60)

    while True:
        temperature = random.uniform(20.0, 30.0)
        humidity = random.uniform(30.0, 70.0)
        payload = f"Temperature: {temperature:.2f}, Humidity: {humidity:.2f}"
        client.publish("weather/data", payload)
        print(f"Published: {payload}")
        time.sleep(5)


if __name__ == "__main__":
    publish_weather_data()

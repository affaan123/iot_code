# IoT Weather Sensor Application

This project consists of an IoT application using CoAP and MQTT protocols for weather sensor data. The application is containerized using Docker and orchestrated with Docker Compose.

## Project Structure

- `coap_client.py`: A Python client that communicates with the CoAP server.
- `coap_server.py`: A Python server that handles CoAP requests.
- `publish_weather.py`: A Python MQTT client that publishes weather data to a specified topic.
- `Dockerfile.coap-server`: Dockerfile to build the CoAP server image.
- `Dockerfile.coap-client`: Dockerfile to build the CoAP client image.
- `Dockerfile.publish`: Dockerfile to build the MQTT publisher image.
- `docker-compose.yml`: Docker Compose file to manage and orchestrate the containers.

## Prerequisites

Make sure you have the following installed:

- Docker
- Docker Compose

## Build Docker Images

1. Build the CoAP server image:
    ```bash
    docker build -t coap-server -f Dockerfile.coap-server .
    ```

2. Build the CoAP client image:
    ```bash
    docker build -t coap-client -f Dockerfile.coap-client .
    ```

3. Build the MQTT publisher image:
    ```bash
    docker build -t mqtt-publisher -f Dockerfile.publish .
    ```

## Running the Containers

Use Docker Compose to start the containers:

```bash
docker-compose up

This will spin up the CoAP server, CoAP client, and MQTT publisher containers as specified in the docker-compose.yml file.

Interacting with the CoAP Server

To send requests to the CoAP server, you can use the CoAP client:
docker run --rm coap-client

This command runs the CoAP client container, which sends a request to the CoAP server.

Publishing Weather Data

To publish weather data using the MQTT client:
docker run --rm mqtt-publisher
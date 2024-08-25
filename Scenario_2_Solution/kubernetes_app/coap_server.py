import asyncio
import random
from aiocoap import resource, Context, Message
from prometheus_client import start_http_server, Counter, Gauge

# Define Prometheus metrics
REQUEST_COUNT = Counter('coap_requests_total', 'Total number of CoAP requests')
TEMPERATURE_GAUGE = Gauge('temperature_celsius', 'Temperature in Celsius')
HUMIDITY_GAUGE = Gauge('humidity_percent', 'Humidity in percent')

class WeatherResource(resource.Resource):
    async def render_get(self, request):
        # Increment request count
        REQUEST_COUNT.inc()

        # Generate random sensor data
        temperature = random.uniform(15.0, 35.0)  # Temperature between 15 and 35 degrees Celsius
        humidity = random.uniform(30.0, 90.0)  # Humidity between 30% and 90%

        # Update Prometheus gauges
        TEMPERATURE_GAUGE.set(temperature)
        HUMIDITY_GAUGE.set(humidity)

        payload = f"Temperature: {temperature:.2f} C, Humidity: {humidity:.2f}%"
        return Message(payload=payload.encode('utf-8'))

async def main():
    # Start Prometheus HTTP server to expose metrics
    start_http_server(8000)

    # Resource tree creation
    root = resource.Site()
    root.add_resource(['weather'], WeatherResource())

    # Bind to IPv4 address
    await Context.create_server_context(root, bind=("0.0.0.0", 5683))

    # Run forever by awaiting an uncompleted future
    await asyncio.get_event_loop().create_future()

if __name__ == "__main__":
    asyncio.run(main())

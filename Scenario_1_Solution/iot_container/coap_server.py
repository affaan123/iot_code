import asyncio

from aiocoap import resource, Context, Message


class WeatherResource(resource.Resource):
    async def render_get(self, request):
        # Simulated sensor data
        temperature = 25.0  # Replace with actual sensor data fetching logic
        humidity = 60.0  # Replace with actual sensor data fetching logic
        payload = f"Temperature: {temperature} C, Humidity: {humidity}%"
        return Message(payload=payload.encode('utf-8'))


async def main():
    # Resource tree creation
    root = resource.Site()
    root.add_resource(['weather'], WeatherResource())

    # Bind to IPv4 address
    await Context.create_server_context(root, bind=("0.0.0.0", 5683))

    # Run forever by awaiting an uncompleted future
    await asyncio.get_event_loop().create_future()


if __name__ == "__main__":
    asyncio.run(main())
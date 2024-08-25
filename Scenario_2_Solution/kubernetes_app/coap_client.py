import asyncio
from aiocoap import *

async def fetch_weather_data():
    # Create a client context
    protocol = await Context.create_client_context()

    # Use the service name defined in docker-compose.yml instead of localhost
    request = Message(code=GET, uri='coap://coap-server:5683/weather')

    try:
        response = await protocol.request(request).response
        print('Result: %s\n%r' % (response.code, response.payload))
    except Exception as e:
        print('Failed to fetch weather data:')
        print(e)

if __name__ == "__main__":
    # Use asyncio.run() to handle the event loop
    asyncio.run(fetch_weather_data())
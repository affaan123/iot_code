import asyncio  # Import the asyncio module for asynchronous I/O operations
from aiocoap import *  # Import all components from the aiocoap library for CoAP communication

# Define an asynchronous function to fetch weather data from a CoAP server
async def fetch_weather_data():
    # Create a CoAP client context for making requests
    protocol = await Context.create_client_context()

    # Create a CoAP GET request for the resource at the specified URI
    request = Message(code=GET, uri='coap://localhost:5683/weather')

    try:
        # Send the request and wait for the response
        response = await protocol.request(request).response
        # Print the response code and payload
        print('Result: %s\n%r' % (response.code, response.payload))
    except Exception as e:
        # Handle any exceptions that occur during the request
        print('Failed to fetch weather data:')
        print(e)

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Run the asynchronous fetch_weather_data function until it completes
    asyncio.get_event_loop().run_until_complete(fetch_weather_data())
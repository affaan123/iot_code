import asyncio  # Import the asyncio module for asynchronous I/O operations

from aiocoap import resource, Context, Message, GET  # Import necessary components from the aiocoap library

# Define a new class WeatherResource that inherits from aiocoap.resource.Resource
class WeatherResource(resource.Resource):
    # Define an asynchronous method to handle GET requests
    async def render_get(self, request):
        # Simulated sensor data for temperature and humidity
        temperature = 25.0  # Replace with actual sensor data fetching logic
        humidity = 60.0  # Replace with actual sensor data fetching logic
        # Create a payload string with the sensor data
        payload = f"Temperature: {temperature} C, Humidity: {humidity}%"
        # Return a CoAP message with the payload, encoded in UTF-8
        return Message(payload=payload.encode('utf-8'))

# Define the main function
def main():
    # Create a root resource tree
    root = resource.Site()
    # Add the WeatherResource to the resource tree under the 'weather' path
    root.add_resource(['weather'], WeatherResource())

    # Create a CoAP server context bound to localhost on port 5683 and serve the resource tree
    asyncio.Task(Context.create_server_context(root, bind=("localhost", 5683)))

    # Run the asyncio event loop indefinitely
    asyncio.get_event_loop().run_forever()

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    main()  # Execute the main function
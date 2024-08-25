import asyncio
from aiocoap import *

async def coap_get():
    protocol = await Context.create_client_context()

    request = Message(code=GET, uri='coap://10.96.140.216:5683/weather')

    try:
        response = await protocol.request(request).response
        print(f'Response Code: {response.code}')
        print(f'Payload: {response.payload.decode("utf-8")}')
    except Exception as e:
        print(f'Failed to fetch resource: {e}')

if __name__ == "__main__":
    asyncio.run(coap_get())
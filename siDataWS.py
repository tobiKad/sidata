
import asyncio
import json
import websockets

async def on_connect(websocket, path):
    try:
        async for message in websocket:

            data = json.loads(message)
            received_value = data['value']
            received_msg = data['msg']

            # Responses for C
            if received_msg == 'correct_C':
                print("msg = {}, received_value = {} ".format(received_msg, received_value))
                send_value = received_value
                await websocket.send(json.dumps({'msg': 'world', 'value': send_value}))
                
            # Responses for M 
            if received_msg == 'correct_M':
                print("msg = {}, received_value = {} ".format(received_msg, received_value))
                send_value = received_value
                await websocket.send(json.dumps({'msg': 'world', 'value': send_value}))

                
    finally:
        print("connection lost")

# Make sure that the IP address and port match with the Labvanced study settings.
asyncio.get_event_loop().run_until_complete(websockets.serve(on_connect, 'localhost', 8081))
asyncio.get_event_loop().run_forever()
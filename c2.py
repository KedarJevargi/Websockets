import asyncio
import websockets

async def chat():
    uri = "ws://localhost:8000/ws"
    async with websockets.connect(uri) as websocket:
        print("Connected to server. Type messages and press Enter.")
        while True:
            msg = input("You: ")
            await websocket.send(msg)

            # Try to receive any incoming message (from other users)
            try:
                while True:
                    response = await asyncio.wait_for(websocket.recv(), timeout=1)
                    print("Received:", response)
            except asyncio.TimeoutError:
                pass  # No new messages within timeout

asyncio.run(chat())

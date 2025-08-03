from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

# This will store all connected WebSocket clients
connected_users = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # Accept the connection when a client connects
    await websocket.accept()
    connected_users.append(websocket)
    print("New client connected. Total users:", len(connected_users))

    try:
        while True:
            # Wait for a message from this client
            data = await websocket.receive_text()
            print("Received:", data)
            print(connected_users)

            # Send the message to all other users
            for user in connected_users:
                if user != websocket:
                    await user.send_text(f"Someone said: {data}")



    except WebSocketDisconnect:
        # Remove the user on disconnect
        connected_users.remove(websocket)
        print("Client disconnected. Total users:", len(connected_users))

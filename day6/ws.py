from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

@app.get("/")
def root():
    return {"status": "WebSocket server running"}

@app.websocket("/ws/chat")
async def websocket_chat(ws: WebSocket):
    await ws.accept()
    print("Client connected")

    try:
        while True:
            message = await ws.receive_text()
            print("Received:", message)
            await ws.send_text(f"Echo: {message}")
    except WebSocketDisconnect:
        print("Client disconnected")

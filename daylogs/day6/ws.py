from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

@app.websocket("/ws/chat")
async def chat_socket(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            msg = await ws.receive_text()
            await ws.send_text(f"Echo: {msg}")
    except WebSocketDisconnect:
        print("Client disconnected")

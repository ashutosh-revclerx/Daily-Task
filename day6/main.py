import websocket

ws = websocket.WebSocket()
ws.connect("ws://127.0.0.1:8000/ws/chat")
ws.send("Hello WebSocket")
print(ws.recv())
ws.close()

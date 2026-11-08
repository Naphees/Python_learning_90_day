import websocket

ws = websocket.WebSocket()
ws.connect("ws://127.0.0.1:8000/ws")
print("Connected !")

while True:
    message = input("You : ")
    ws.send(message)
    response = ws.recv()
    print("Server:",response)
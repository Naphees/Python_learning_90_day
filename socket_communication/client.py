import socket

# 1. server configure
HOST = "127.0.0.1" # localhost server ip
PORT = 5000 #  server port

# 2. Initialize  client socket and connect
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
	client.connect((HOST,PORT))
	print("[CONNECTED] Establish connection to the server.")
	# 3. Network data must be sent as raw bytes
	message ="Hello, Python Server!"
	client.sendall(message.encode('utf-8'))
	# 4. Receive the response back
	response = client.recv(1024)
	print(f"[SERVER RESPONSE] : {response.decode('utf-8')}")

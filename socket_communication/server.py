import socket
#  1. Define server configuration

HOST = "127.0.0.1" # localhost loopback address
PORT =  5000 # Non - privileged port

# 2. Create and set up the listening socket 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
	# prevent address already in use during quick restart
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server.bind((HOST,PORT))
	server.listen()
	print(f"[Listening] Server is listing  on {HOST} : {PORT}")
	
	# 3. Block and wait for a client connection
	conn , addr = server.accept()
	while conn:
		print(f"[Connected] connected  by client at address : {addr}")
		while True:
			# 4. Receive raw byte stream  (up to 1024 bytes)
			data = conn.recv(1024)
			if not data:
				break  # client disconnected
			print(f"[Received]  {data.decode('utf-8')}")
			# 5. Echo The data back to the client
			conn.sendall(b"Server recieved your message!")



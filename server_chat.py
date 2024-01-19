import socket
import subprocess
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('',5556))
server_socket.listen(5)
print("Server Side:")
client_socket, addr = server_socket.accept()
choice = client_socket.recv(1000).decode()
#choice = int(choice)
while True:
	if choice == 1:
		command = client_socket.recv(1000).decode()
		print(f"command received: {command}")
		result = subprocess.check_output([command])
		result = result.decode('utf-8')
		client_socket.send(result.encode())
		print("Response sent.")
	elif choice == 2:
		message = client_socket.recv(1024).decode()
		print(f"client: {message}")
		if message=="bye":
			break
		reply = input("Type reply: ")
		client_socket.send(reply.encode())

import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('192.168.230.234',5557))
choice = input(''' What do you want?   
		   1. Run a Command
	           2. Chatting  ''')
c = int(choice)

if c not in range(1,3):
	print("Invalid Choice")
	client_socket.close()

client_socket.send(choice.encode())
while True:
	if c==1:
		command = input("Enter a command: ")
		client_socket.send(command.encode())
		if command=="bye":
			break
		result = client_socket.recv(1000).decode()
		print("Result: ")
		print(result)
	elif c==2:
		message = input("Type message: ")
		client_socket.send(message.encode())
		reply = client_socket.recv(1000).decode()
		print(f"server: {reply}")
		if message=="bye":
			client_socket.close()
			break

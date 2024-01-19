import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('192.168.230.234',5556))
choice = int(input(''' What do you want?   
		   1. Run a Command
	           2. Chatting  '''))
if choice !=1 | choice!=2:
	print("Invalid Choice")
	client_socket.close()
client_socket.send(choice.encode())
while True:
	if choice==1:
		command = input("Enter a command")
		client_socket.send(command.encode())
		result = client_socket.recv(1000).decode()
		print("Result: ")
		print(result)
	elif choice==2:
		message = input("Type message: ")
		client_socket.send(message.encode())
		reply = client_socket.recv(1000).decode()
		print(f"server: {reply}")
		if message=="bye":
			client_socket.close()
			break

import socket

def main():
	host = "10.10.9.50"
	port = 1216
	s = socket.socket()
	s.connect((host, port))
	# num = int(input)
	data = s.recv(1024).decode()
	print("My Roll number is : " ,str(msg))
	print(msg)
	s.send(input().encode())
	
	while True:
		msg = s.recv(1024).decode()
		print(msg)
		if msg == " ATTENDANCE-SUCCESS ":
			break;
		msg = input("->")
		if not msg:
			continue
		s.send(msg.encode())
	s.close()


if __name__ == "__main__":
    main()
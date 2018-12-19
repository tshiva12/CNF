import socket
def main():
	host = '10.1.132.43'
	port = 1516
	s = socket.socket()
	s.connect((host, port))
	print("Connecting to Server...\n")
	print("Connected!\n")
	str1 = s.recv(1024).decode()
	str2 = s.recv(1024).decode()
	print(str(str1))
	print(str(str2) + "\n")
	message = input("enter your guess: ")
	while message != 'q':
		s.send(message.encode())
		data = s.recv(1024).decode()
		print(str(data))
		message = input("enter your guess: ")
	s.close()

if __name__ == '__main__':
	main()
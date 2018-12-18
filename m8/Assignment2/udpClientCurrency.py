import socket

def main():
	host = '10.1.132.43'
	port = 2413
	server = ('10.1.132.43', 2412)
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))
	message = input("enter the input: ")
	while message != 'q':
		s.sendto(message.encode(), server)
		data, addr = s.recvfrom(1024)
		print("recieved from server: " + str(data.decode()))
		message = input("enter again input: ")
	s.close()
if __name__ == '__main__':
	main()
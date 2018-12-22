import socket
import threading
import csv
s_list = []
def main():
	host = "10.10.9.50"
	port = 1216
	s = socket.socket() # create a new socket
	s.bind((host, port))
	s.listen(10)
	c, addr = s.accept()
	print("Server Started.........")
	with open("data.csv", "r") as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			# print(row)
			s_list.append(row)
	csvfile.close()

	while True:
		data = c.recv(1024).decode()
		if not data:
			break;
		print("Your SECRETQUESTION is :" + str(data))
		data = csvfile
		c.send(data.encode())
	c.close()

if __name__ == "__main__":
    main()
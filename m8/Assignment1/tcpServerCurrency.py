import socket

def main():
	host = '10.1.132.43'
	port = 8081
	s= socket.socket()
	s.bind((host, port))
	s.listen(1)
	
	c, addr = s.accept()
	print()
	print("Connection established: "+ str(addr))
	print("server started")
	while True:
		print("server started")
		data = c.recv(1024).decode()
		if not data:
			break
		result = str(converter(data))
		c.send(result.encode())
	c.close()
	# 1 Dollar = 67 INR
	# 1 Dollar =0.75 Pounds
	# 1 Dollar = 113.41 Yen

def converter(data):
	list1 = []
	list1 = data.split(" ")
	value = float(list1[2])
	from1 = list1[1]
	to = list1[4]
	if from1 == "INR":
		if to == "INR":
			return value
		if to == "Dollar":
			return value*(1/67)
		if to == "Yen":
			return value*(113.41/67)
		if to == "Pounds":
			return value*(0.75/67)
	if from1 == "Dollar":
		if to == "INR":
			return value*67
		if to == "Dollar":
			return value
		if to == "Pounds":
			return value*0.75
		if to == "Yen":
			return value*113.41
	if from1 == "Pounds":
		if to == "INR":
			return value*(67/0.75)
		if to == "Dollar":
			return value*(1/0.75)
		if to == "Pounds":
			return value
		if to == "Yen":
			return value*(113.41/0.75)
	if from1 == "Yen":
		if to == "INR":
			return value*(67/113.41)
		if to == "Dollar":
			return value*(1/113.41)
		if to == "Pounds":
			return value*(0.75/113.41)
		if to == "Yen":
			return value

if __name__ == '__main__':
	main()
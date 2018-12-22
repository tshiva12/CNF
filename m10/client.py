import socket
import threading
import os, signal

s = socket.socket()
def main():
	host = '10.1.132.43'
	port = 1216
	s.connect((host, port))
	data = s.recv(1024).decode()
	print(data)
	s.send(input().encode())
	threading.Thread(target = sender, args = ()).start()
	while True:
		try:
			msg = s.recv(1024).decode()
			print(msg)
			if msg == " You successfully exited your chat ":
				os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)
			if not msg:
				continue
		except:
			print(" Host server Closed by admin ")
			break
	s.close()

def sender():
	while True:
		msg = input("->")
		if not msg:
			continue
		s.send(msg.encode())
	s.close()

if __name__ == '__main__':
	main()
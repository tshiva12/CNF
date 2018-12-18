import socket
def main():
    host = '10.1.132.43'
    port = 8013
    s = socket.socket() # creates a new socket
    s.connect((host, port))

    message = input("shiva")
    while message != 'q':
        s.send(message.encode())
        data = s.recv(1024).decode()
        print("Received from server :" + str(data))
        message = input("shiva")
    s.close()

if __name__ == "__main__":
    main()
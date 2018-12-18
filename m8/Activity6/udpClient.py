import socket
def main():
    host = '10.1.132.43'
    port = 8022
    server = ('10.1.132.43',8021)
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((host,port))
    message = input("shiva")
    while message != 'q':
        s.sendto(message.encode(), server)
        data, addr=s.recvfrom(1024)
        print("Received from server:" + str(data.decode()))
        message = input("shiva")
    s.close()

if __name__ == "__main__":
    main()
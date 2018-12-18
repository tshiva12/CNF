import socket
def main():
    host = '10.1.132.43'
    port = 8021
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((host,port))
    print("server started")
    while True:
        data,addr = s.recvfrom(1024)
        print("message from: " + str(addr))
        print("from connect user: " + str(data.decode()))
        data = str(data).upper()
        print("sending: " + str(data))
        s.sendto(data.encode(), addr)
    s.close()

if __name__ == "__main__":
    main()
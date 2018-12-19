import socket
import random
import threading
def main():
    host = '10.1.132.43'
    port = 1516
    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    print("Server started")
    while True :
        c, addr = s.accept()
        print("Connection from: "+ str(addr))
        str1 = "Welcome to 'Guess my Nmber'!"
        str2 = "I'm thinking of a number between 1 and 100.Try to guess it in as few at tempts as possible."
        c.send(str1.encode())
        c.send(str2.encode())
        threading.Thread(target = guessnumber, args = (c, addr)).start()

def guessnumber(c, addr):
    number = random.randint(1, 101)
    count = 0
    while True:
        data = c.recv(1024).decode()
        print("Guess :" + str(data) + "Client Addr: "+str(addr))
        if not data:
            break
        if int(data) == number:
            count += 1
            send = "Correct, number of guess : " + str(count)
            c.send(send.encode())
            break
        elif int(data) < number:
            count += 1
            send = "Your number is less than the guess"
            c.send(send.encode())
        elif int(data) > number:
            count += 1
            send = "Your number is greater than the guess"
            c.send(send.encode())
    c.close()

if __name__ == "__main__":
    main()

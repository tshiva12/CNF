import socket
from threading import *
import os
import signal
import time
c_dict = {}
s = socket.socket()
def main():
    host = '10.1.132.43'
    port = 1216
    s.bind((host, port))
    s.listen(10)
    print("Server started : " + str(host))
    Thread(target = grpadmin, args = ()).start()
    while True:
        c, addr = s.accept()
        print("client entering his name at IP: " + str(addr))
        data = "Welcome to the Group Chat! \n Please enter your name to start the chatting: "
        c.send(data.encode())
        if c not in c_dict:
            c_dict[c] = "user"
            Thread(target = chatgroup, args = (c, "user")).start()
        else:
            c.send("Error Occured 404 not found \n Try after some time".encode())
            c_dict.pop(c)
    s.close()

def chatgroup(c, uname):
    uname = c.recv(1024).decode()
    c_dict[c] = uname
    chathost(c, uname + " joined the group chat! ")
    try:
        while c in c_dict:
            msg = c.recv(1024).decode()
            if msg == "quit":
                msg = uname + " exited the chat "
                chathost(c, msg)
                c.send(" You successfully exited your chat ".encode())
                c_dict.pop(c)
                check()
                return 1
            else:
                msg = uname + ": " + msg + "  "
                chathost(c,msg)
    except:
        c_dict.pop(c)
        c.send(" Error Occured 404 not found \n please Connect again ".encode())

def check():
    if (active_count() == 3):
        Notifier("Waiting to close the group chat, no member online.")
        time.sleep(10)
        if (active_count() == 3):
            os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)

def grpadmin():
    while True:
        msg = input("-> ")
        if not msg:
            continue
        if msg == "quit":
            show("Server will be shut down in 5 seconds! ")
            time.sleep(5)
            print("server closed")
            os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)
            break
        else:
            show(msg)


def chathost(c, msg):
    keys = c_dict.keys()
    print(msg)
    for conn in keys:
        if c != conn:
            conn.send(msg.encode())


def show(msg):
    msg = "Admin: " + msg + " "
    keys = c_dict.keys()
    print(msg)
    for conn in keys:
        conn.send(msg.encode())



if __name__ == '__main__':
    main()
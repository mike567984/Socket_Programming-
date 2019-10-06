import socket
import pickle


# method i created to count length of msg
def length():
    for char in msg:
        count = 0
        count += 1
        return "your msg has this much  characters" + count


# variable to not type the same line each time
ip = (socket.gethostname())

# Create socket obj
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# read the number generated in server.py
share_port = pickle.load(open("port.dat", "rb"))

# connect to host name ip and the random port from server.py
s.connect((ip, share_port))

# while loop to make sure msg is not empty and if it isn't print it
while True:
    full_msg = ''
    msg = s.recv(10)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")
    # make sure full msg has a char
    if len(full_msg) > 0:
        print(full_msg)

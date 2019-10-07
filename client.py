import socket
import pickle

# header size chosen
headerSize = 15

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


while True:
    full_msg = ''
    new_msg = True
# while loop to make sure msg is not empty and if it isn't print it
    while True:
        msg = s.recv(18)
        if new_msg:
            print(f"new message length: {msg[:headerSize]}")
            # find the msg length and add header size and convert to int
            msg_length = int(msg[:headerSize])
            # no  longer new
            new_msg = False

        full_msg += msg.decode("utf-8")

        if len(full_msg) - headerSize == msg_length:
            print("full msg received")
            print(full_msg[headerSize:])
            new_msg = True
            # creates an empty string for future messages
            full_msg = ''

    print(full_msg)
        # # make sure full msg has a char
        # if len(full_msg) > 0:
        #     print(full_msg)


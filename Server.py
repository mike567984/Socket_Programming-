import socket
import pickle
import random
import time
# import os

# header size chosen
headerSize = 15

# Creates socket obj with parameters of address family IPV4 and using TCP(three way handshake)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = socket.gethostname()


# generates random port from available port ranges (1025,5000)
def random_port():
    return random.randint(1025, 49000)


# set port to the output of the random_port() function
port = random_port()

# Put the selected port into a file called port.dat
pickle.dump(port, open("port.dat", "wb"))

# Tells the server to  look for Specific IP in this case just our hostname ip and and port
s.bind((ip, port))

# Will leave a queue of 5
s.listen(5)

# While loop to keep listening for client
while True:
    # accept client info
    clientsocket, address = s.accept()
    # shows ip address and port the client connected from
    print(f"Connection from {address} has been established")
    msg = "The server welcomes you!"
    # Left aligned based on header size and msg
    msg = f'{len(msg):<{headerSize}}' + msg
    clientsocket.send(bytes(msg,"utf-8"))

# while loop that prints the time in Minutes Hours and seconds every 5 seconds
    while True:
        time.sleep(5)
        msg = time.strftime(" The Current time is =  " + "%H : %M : %S %p")
        msg = f'{len(msg):<{headerSize}}' + msg
        clientsocket.send(bytes(msg, "utf-8"))

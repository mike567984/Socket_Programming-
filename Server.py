import socket
import pickle
import random
# import os

# Creates socket obj with parameters of address family IPV4 and using TCP(three way handshake)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = socket.gethostname()


# generates random port from available port ranges (1025,5000)
def random_port():
    return random.randint(1025, 5000)


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
    # shows ip address and port
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established")
    clientsocket.send(bytes("You have connected to the server!", "utf-8"))
    clientsocket.close()

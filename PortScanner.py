#!/bin/python3
import socket
import threading
from datetime import datetime
from queue import Queue

#make It more script like
print("-" * 50)
print("Time started: " + str(datetime.now()))
print("-" * 50)

print("Enter in the ipv4 or domain name  \ntest your own computer with loopback address from 127.0.0.1-127.225.225.225")
# the ip you want to scan
ip = input(" ")

# Synchronizing thread
locking = threading.Lock()


# port scanning function that uses IPV4 and TCP to show which ports are open and ignores closed ones
def portscanner(port):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection = soc.connect((ip, port))
        # make sure it's not locked
        with locking:
            print("the port", port, "is open")

        connection.close()
    # if port is not open ignore and continue scanning
    except:
        pass


# make sure threads aren't messing with each other
locking = threading.Lock()
# create an empty Queue
a = Queue()

# the target in the for loop
def threader():
    while True:
        # get worker from the a Queue
        minion = a.get()
        # use the  portscanner function above with parameters worker
        portscanner(minion)
        # when thread is done it can be used for other task
        a.task_done()


# using 200 threads to scan ports
for x in range(150):
    # make sure thread understand who to go to
    thd = threading.Thread(target=threader)
    # ends when main is done
    thd.daemon = True
    # start the threading
    thd.start()

# tells the sys to scan port 1-10000
for minion in range(1, 10001):
    # puts the minons into the queue
    a.put(minion)
# makes each thread waits for the other ones to finish
a.join()

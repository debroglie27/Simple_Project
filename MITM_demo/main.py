import time
import threading
from Client import Client
from Server import Server

HOST = "127.0.0.1"
PORT1 = 8000
PORT2 = 9000

server1 = Server(HOST, PORT1)
server2 = Server(HOST, PORT2)

serverThread1 = threading.Thread(target=server1.receive)
serverThread2 = threading.Thread(target=server2.receive)

serverThread1.start()
serverThread2.start()

# Delay so that server gets setup properly
time.sleep(0.5)

alice = Client(HOST, PORT1, "Alice")
bob = Client(HOST, PORT2, "Bob")

# Delay so that ALice and Bob gets connected to the respective servers properly
time.sleep(0.5)

mallory = Client(HOST, PORT1, "Mallory-Alice")
mallory = Client(HOST, PORT2, "Mallory-Bob")

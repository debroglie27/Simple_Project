import time
import threading
from Client import Client
from Server import Server


HOST = "127.0.0.1"
PORT = 9000

# Starting the Server
server = Server(HOST, PORT)
serverThread = threading.Thread(target=server.receive)
serverThread.start()

# Delay for server to setup properly
time.sleep(0.5)

# Connecting Alice with the server
alice = Client(HOST, PORT, "Alice")

# Delay for Alice to connect with server properly
time.sleep(0.5)

# Connecting Bob with the server
bob = Client(HOST, PORT, "Bob")
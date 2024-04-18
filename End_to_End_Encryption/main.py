import os
import time
import threading
from dotenv import load_dotenv
from Client import Client
from Server import Server

load_dotenv()

HOST = "127.0.0.1"
PORT = 9000

key = os.getenv('KEY')
isSecure = True

# Starting the Server
server = Server(HOST, PORT)
serverThread = threading.Thread(target=server.receive)
serverThread.start()

# Delay for server to setup properly
time.sleep(0.5)

# Connecting Alice with the server
alice = Client(HOST, PORT, "Alice", key, isSecure)

# Delay for Alice to connect with server properly
time.sleep(0.5)

# Connecting Bob with the server
bob = Client(HOST, PORT, "Bob", key, isSecure)

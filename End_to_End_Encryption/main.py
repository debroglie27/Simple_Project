import os
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

# Connecting the Clients
alice = Client(HOST, PORT, "Alice", key, isSecure)
bob = Client(HOST, PORT, "Bob", key, isSecure)

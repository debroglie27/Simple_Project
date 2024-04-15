import os
from dotenv import load_dotenv
from End_to_End_Encryption.Client import Client

load_dotenv()

HOST = "127.0.0.1"
PORT = 8000

isSecure = False
key = os.getenv('KEY')

alice = Client(HOST, PORT, "Alice", key, isSecure)
bob = Client(HOST, PORT, "Bob", key, isSecure)
import os
from dotenv import load_dotenv
from Client import Client

load_dotenv()

HOST = "127.0.0.1"
PORT = 9090

nickname = "Bob"
isSecure = False

key = os.getenv('KEY')

Client(HOST, PORT, nickname, key, isSecure)
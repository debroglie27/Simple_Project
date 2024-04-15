import threading
from Client import Client
from Server import Server

HOST = "127.0.0.1"

server1 = Server(HOST, 8000)
server2 = Server(HOST, 9000)

s1 = threading.Thread(target=server1.receive)
s2 = threading.Thread(target=server2.receive)

s1.start()
s2.start()

alice = Client(HOST, 8000, "Alice")
bob = Client(HOST, 9000, "Bob")
mallory = Client(HOST, 8000, "Mallory-Alice")
mallory = Client(HOST, 9000, "Mallory-Bob")

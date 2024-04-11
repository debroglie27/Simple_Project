from Client import Client

HOST = "127.0.0.1"

alice = Client(HOST, 8000, "Alice")
bob = Client(HOST, 9000, "Bob")
mallory = Client(HOST, 8000, "Mallory-Alice")
mallory = Client(HOST, 9000, "Mallory-Bob")

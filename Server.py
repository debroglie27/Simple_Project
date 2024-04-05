import socket
import threading

HOST = "127.0.0.1"
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            message = f"{nicknames[clients.index(client)]}: {message}"
            print(f"{message}")
            broadcast(message.encode('utf-8'))
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}!")

        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')

        print(f"Nickname of the client is {nickname}\n")
        message = f"{nickname} Connected to the Server!\n"
        broadcast(message.encode('utf-8'))

        nicknames.append(nickname)
        clients.append(client)

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server Running...\n")
receive()
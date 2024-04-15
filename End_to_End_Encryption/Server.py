import json
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
            sender = nicknames[clients.index(client)]
            data = {'sender': sender, 'message': message}

            print(f"{sender}: {message.strip()}")

            # Serialize dictionary to JSON
            json_data = json.dumps(data)
            broadcast(json_data.encode())
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
        print(f"\nConnected with {str(address)}!")

        message = "NICK"
        sender = "Server"
        data = {'sender': sender, 'message': message}
        json_data = json.dumps(data)
        client.send(json_data.encode())

        nickname = client.recv(1024).decode('utf-8')

        print(f"Nickname of the client is {nickname}\n")
        message = f"{nickname} Connected to the Server!\n"
        sender = "Server"
        data = {'sender': sender, 'message': message}

        json_data = json.dumps(data)
        broadcast(json_data.encode())

        nicknames.append(nickname)
        clients.append(client)

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server Running...")
receive()
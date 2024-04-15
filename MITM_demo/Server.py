import json
import socket
import threading


class Server:
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT

        self.clients = []
        self.nicknames = []

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((HOST, PORT))

        self.server.listen()

        print(f"Server Listening at PORT: {self.PORT}")


    def broadcast(self, message):
        for client in self.clients:
            client.send(message)

    def handle(self, client):
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                sender = self.nicknames[self.clients.index(client)]

                if (sender == "Mallory" and self.PORT == 8000):
                    sender = "Bob"
                
                if (sender == "Mallory" and self.PORT == 9000):
                    sender = "Alice"

                data = {'sender': sender, 'message': message}

                print(f"{sender}: {message.strip()}")

                # Serialize dictionary to JSON
                json_data = json.dumps(data)
                self.broadcast(json_data.encode())
            except:
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.nicknames.remove(nickname)
                break


    def receive(self):
        while True:
            client, address = self.server.accept()
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
            self.broadcast(json_data.encode())

            self.nicknames.append(nickname)
            self.clients.append(client)

            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()


if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 9000

    server = Server(HOST, PORT)
    serverThread = threading.Thread(target=server.receive)

    serverThread.start()

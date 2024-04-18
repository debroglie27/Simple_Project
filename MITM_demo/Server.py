import json
import socket
import threading


class Server:
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT

        self.clients = []
        self.nicknames = []
        
        # Creating the server socket
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

                if (sender == "Mallory-Alice"):
                    sender = "Bob"
                elif (sender == "Mallory-bob"):
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

            # Preparing the data to be sent to find out nickname of the client
            sender = "Server"
            message = "NICK"
            data = {'sender': sender, 'message': message}

            # Sending the request for knowing the nickname of the client
            json_data = json.dumps(data)
            client.send(json_data.encode())
            nickname = client.recv(1024).decode('utf-8')

            print(f"Nickname of the client is {nickname}\n")

            if (nickname == "Mallory-Alice"):
                nickname = "Bob"
            elif (nickname == "Mallory-Bob"):
                nickname = "Alice"
            
            sender = "Server"
            message = f"{nickname} Connected to the Server!\n"
            data = {'sender': sender, 'message': message}

            json_data = json.dumps(data)
            self.broadcast(json_data.encode())

            # Storing the nickname and client socket
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

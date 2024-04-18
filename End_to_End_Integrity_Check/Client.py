import os
import json
import socket
import threading
import tkinter
import tkinter.scrolledtext
import tkinter.messagebox
from dotenv import load_dotenv
from Hashing import hash


class Client:
    def __init__(self, host, port, nickname):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        self.nickname = nickname

        load_dotenv()
        self.KEY = os.getenv('INTEGRITY_KEY')

        self.gui_done = False
        self.running = True

        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)

        gui_thread.start()
        receive_thread.start()

    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.title(f"Chat App - {self.nickname}")
        self.win.geometry("500x480")
        self.win.configure(bg="lightgray")

        self.chat_label = tkinter.Label(self.win, text="Chat:", bg="lightgray")
        self.chat_label.config(font=("Arial", 12))
        self.chat_label.pack(padx=20, pady=(10, 5))

        self.text_area = tkinter.scrolledtext.ScrolledText(self.win, height=15)
        self.text_area.pack(padx=20, pady=(5, 20))
        self.text_area.config(state="disabled")

        self.msg_label = tkinter.Label(self.win, text="Message:", bg="lightgray")
        self.msg_label.config(font=("Arial", 12))
        self.msg_label.pack(padx=20, pady=5)

        self.input_area = tkinter.Text(self.win, height=3)
        self.input_area.pack(padx=20, pady=(5, 20))

        self.send_button = tkinter.Button(self.win, text="send", width=15, command=self.write)
        self.send_button.config(font=("Arial", 12))
        self.send_button.pack(padx=20, pady=5)

        self.gui_done = True

        self.win.protocol("WM_DELETE_WINDOW", self.stop)

        self.win.mainloop()

    def write(self):
        message = f"{self.input_area.get('1.0', 'end')}"
        hash_message = hash(message, self.KEY)
        data = {'message': message, 'hash_message': hash_message}

        # Serialize dictionary to JSON
        json_data = json.dumps(data)
        self.sock.send(json_data.encode())

        self.input_area.delete('1.0', 'end')

    def stop(self):
        self.running = False
        self.win.destroy()
        self.sock.close()
        exit(0)

    def receive(self):
        while self.running:
            try:
                message_dict = json.loads(self.sock.recv(1024).decode())
                if message_dict['message'] == "NICK":
                    self.sock.send((self.nickname).encode('utf-8'))
                elif self.gui_done:
                    self.text_area.config(state="normal")
                    if (message_dict['sender'] == "Server"):
                        self.text_area.insert('end', message_dict['message'])
                    else:
                        message = message_dict['message']

                        hash_message_received = message_dict['hash_message']
                        hash_message_calculated = hash(message, self.KEY)

                        # Checking integrity
                        if (hash_message_received != hash_message_calculated):
                            tkinter.messagebox.showerror("Integrity Check Failed", "Received message integrity check failed. Message discarded.", parent=self.win)
                        else:
                            message = f"{message_dict['sender']}: {message_dict['message']}"
                            self.text_area.insert('end', message)


                    self.text_area.yview('end')
                    self.text_area.config(state="disabled")
            except ConnectionAbortedError:
                break
            except json.JSONDecodeError:
                print("Error decoding JSON.")
                self.sock.close()
                break
            except socket.error as e:
                print("Socket error:", e)
                self.sock.close()
                break
            except Exception as e:
                print("Error:", e)
                self.sock.close()
                break


if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 9090

    nickname = "client"

    Client(HOST, PORT, nickname)

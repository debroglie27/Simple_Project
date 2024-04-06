import json
import socket
import threading
import tkinter
import tkinter.scrolledtext
from cipher.HybridCipher import hybrid_encrypt, hybrid_decrypt


class Client:
    def __init__(self, host, port, nickname, key, isSecure):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        self.nickname = nickname
        self.KEY = key

        self.gui_done = False
        self.running = True
        self.isSecure = isSecure

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
        if self.isSecure:
            message = hybrid_encrypt(f"{self.input_area.get('1.0', 'end')}", self.KEY)
        else:
            message = f"{self.input_area.get('1.0', 'end')}"

        self.sock.send(message.encode('utf-8'))
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
                        if self.isSecure:
                            message = f"{message_dict['sender']}: {hybrid_decrypt(message_dict['message'], self.KEY)}\n"
                        else:
                            message = f"{message_dict['sender']}: {message_dict['message']}"
                        self.text_area.insert('end', message)

                    self.text_area.yview('end')
                    self.text_area.config(state="disabled")
            except ConnectionAbortedError:
                break
            except:
                print("Error")
                self.sock.close()
                break


if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 9090

    nickname = "client"
    isSecure = False

    Client(HOST, PORT, nickname, isSecure)

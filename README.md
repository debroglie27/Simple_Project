# Principles of Data and System Security (CS745) Project
This project is for CS745 course (Principles of Data and System Security).

## Project Aim
This projects aims to demonstrate 4 things:
* Simple Communication
* End-to-End Encryption
* End-to-End Integrity Check
* Man In The Middle (MITM) Attack

## How to Setup?

Just download all the python packages mentioned in the **requirements.txt** file. Then create a **.env file** inside the parent directory and include the keys for end-to-end encryption and end-to-end integrity check.

```
CIPHER_KEY=<Add Cipher Key>
INTEGRITY_KEY=<Add Integrity Key>
```

Now go inside the folder whose demonstration you want to see and run the main.py file.

### Simple Communication
Using **socket** and **tkinter** created a simple chat app. A server is used which will handle all the clients and clients would need to connect with the server. After connection is established clients can talk with each other like in a group chat. The client sends a message to the server and the server broadcasts that message to all the other clients.

### End-to-End Encryption
The simple communication was just the base. We added the end-to-end encryption functionality. We used a hybrid cipher which comprises of a combination of Vigenere cipher and Polybius cipher. The encryption and decryption are done at the client side and the server is no longer able to understand what the clients are sharing.

### End-to-End Integrity Check
Just like end-to-end encryption we also added end-to-end integrity check functionality. We used sha-256 as the hash function. Instead of just sending the message clients are also sending the hash value of the message. Now the  receiving client can do the necessary interity checking. To demonstrate the working the server changes the clients messages with some probability. If integrity check fails for some message then instead of the message a warning is  displayed.

### Man In The Middle (MITM) Attack 
Here we have demostrated man in the middle attack. Alice and Bob wants to communicate with each other but Mallory has hijacked the conversation. Alice is thinking she is talking with Bob but in reality she is talking with Mallory. Similarly, Bob is thinking he is talking with Alice but in reality he is talking with Mallory. To demonstrate it we have two servers. One server has Alice and Mallory connected. Another server has Bob and Mallory connected. Now Mallory can intercept all the messages shared between them and can modify, discard or send the messages as it is.

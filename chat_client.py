import socket
from config import SERVER_ADDRESS, SERVER_PORT
from threading import Thread
import sys

def recv_msg(client):
    while True:
        print(client.recv(1024).decode())
        print('Enter message: ', end='')
        sys.stdout.flush()

def send_msg(client):
    while True:
        msg = input('Enter message: ')
        client.send(msg.encode())


client = socket.socket()
client.connect((SERVER_ADDRESS, SERVER_PORT))

recv = Thread(target=recv_msg, args=[client])
send = Thread(target=send_msg, args=[client])

recv.start()
send.start()

recv.join()
send.join()

client.close()
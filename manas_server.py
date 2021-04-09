import socket
from config import SERVER_ADDRESS, SERVER_PORT
from threading import Thread

def handle_client(connection):
    print(connection.recv(1024).decode())
    connection.send(b'SERVER !!!!!')
    connection.close()

server = socket.socket()

server.bind((SERVER_ADDRESS, SERVER_PORT))
server.listen()
print('[STARTING] Server started on', SERVER_ADDRESS, 'port', SERVER_PORT)
while True:
    connection, address = server.accept()
    print('[CONNECTED] Connect to', address)
    Thread(target=handle_client, args=([connection])).start()

server.close()

import socket
from config import SERVER_ADDRESS, SERVER_PORT
from threading import Thread

def mul_client(connection):
    print(connection.recv(1024).decode())
    msg = input('Enter the message:')
    connection.send(msg.encode())
    connection.close()
    server.close()

server = socket.socket()
server.bind((SERVER_ADDRESS, SERVER_PORT))
server.listen()
print('[LISTENING]')
while(True):
    connection, client_address = server.accept()
    print('[CONNECTED] to', client_address[0], ":", client_address[1])
    Thread(target= mul_client, args =([connection])).start()



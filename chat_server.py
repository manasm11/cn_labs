import socket
from threading import Thread
from config import SERVER_ADDRESS, SERVER_PORT

connections = []

def handle_client(connection):
    while True:
        message = connection.recv(1024)
        for conn in connections:
            if not conn == connection:
                conn.send(message)

server = socket.socket()

server.bind((SERVER_ADDRESS, SERVER_PORT))
server.listen()

try:
    while True:
        connection, address = server.accept()
        connections.append(connection)
        Thread(target=handle_client, args=[connection]).start()
except:
    server.close()



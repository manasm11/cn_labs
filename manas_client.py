import socket
from config import SERVER_ADDRESS, SERVER_PORT


client = socket.socket()

client.connect((SERVER_ADDRESS, SERVER_PORT))

message = input('Enter message: ')
client.send(message.encode())
print(client.recv(1024).decode())

client.close()
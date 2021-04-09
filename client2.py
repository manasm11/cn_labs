import socket

client = socket.socket()

client.connect(('localhost', 9999))
client.send('HELLO'.encode())
client.detach()
client.close()
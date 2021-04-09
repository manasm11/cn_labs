import socket
from config import SERVER_ADDRESS, SERVER_PORT

client = socket.socket()
client.connect((SERVER_ADDRESS, SERVER_PORT))
print([CONNECTED])
msg = input('Enter the message')
client.send(msg.encode())
msg_recv = client.recv(1024)
print(msg_recv.decode())
client.close()
from socket import socket

server = socket()
print('Socket created...')

server.bind(('localhost', 9999))

server.listen(3)
print('waiting for connections')

while True:
    client, address = server.accept()
    print('Connected with', address)

    client.send(bytes('Welcome To World of Manas', 'utf8'))
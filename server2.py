import socket

server = socket.socket()

server.bind(('localhost', 9999))
server.listen()
print('[LISTENING]: Server is listening on', f'localhost:{9999}')
connection, address = server.accept()
print('[CONNECTED]: Connected to', *address)

print(connection.recv(1024).decode())
connection.close()
server.detach()
server.close()
import socket
from commands import execute

HOST = "127.0.0.1"
PORT = 6379

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen()

print(f"Server is listening on {HOST}:{PORT}")

client_socket, client_address = server.accept()

print(f"Connected to {client_address}")

while True:
    data = client_socket.recv(1024)

    if not data:
        break

    message = data.decode().strip()

    print(f"Received: {message}")

    response = execute(message)

    client_socket.send(response.encode())

client_socket.close()
server.close()
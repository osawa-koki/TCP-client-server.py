import socket

IP_ADDRESS = "127.0.0.1"
PORT = 8888

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP_ADDRESS, PORT))
server_socket.listen()

while True:
    client_socket, client_address = server_socket.accept()
    data = client_socket.recv(4096)
    print("Received:", data.decode())
    client_socket.sendall("🐙 ".encode() + data.decode().encode() + " 🐙".encode())
    client_socket.close()

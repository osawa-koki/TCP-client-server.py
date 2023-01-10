import socket

IP_ADDRESS = "127.0.0.1"
PORT = 8888

while True:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP_ADDRESS, PORT))
    message = input("Enter message to send: ")
    client_socket.sendall(message.encode())
    data = client_socket.recv(4096)
    print("Received:", data.decode())
    client_socket.close()

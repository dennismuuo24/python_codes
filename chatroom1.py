import socket
import threading

def handle_client(client_socket, client_address):
    while True:
        message = client_socket.recv(1024).decode()
        if message == "exit":
            break
        print(f"Received from {client_address}: {message}")
        broadcast_message(message)

    client_socket.close()

def broadcast_message(message):
    for client in clients:
        client.send(message.encode())

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 12345))
    server_socket.listen(5)
    print("Server started, listening on port 12345")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"New connection from {client_address}")
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()

clients = []

start_server()
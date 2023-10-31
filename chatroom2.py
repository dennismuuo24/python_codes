import socket
import threading

def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        print("Received:", message)

def send_message(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode())
        if message == "exit":
            break

def start_client():
    server_address = ("localhost", 12345)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    threading.Thread(target=receive_messages, args=(client_socket,)).start()
    threading.Thread(target=send_message, args=(client_socket,)).start()

start_client()
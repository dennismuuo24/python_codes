import socket

def get_public_ip():
    # Create a temporary socket to get the public IP address
    temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    temp_socket.connect(("8.8.8.8", 80))
    public_ip = temp_socket.getsockname()[0]
    temp_socket.close()
    return public_ip

public_ip = get_public_ip()
print("Public IP Address:", public_ip)
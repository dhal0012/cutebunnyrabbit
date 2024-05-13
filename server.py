import socket
import threading
import config
import random

name = ["Blue", "Red", "Green", "Yellow"]
animal = ["cat", "dog", "horse", "wombat"]
authcode = {"user1": "password1", "user2": "password2", "user3": "password3"}
def handle_client(client_socket, address):
    authcode = client_socket.recv(1024).decode()
    if authcode == 'a:b':
        print("Invalid")
        client_socket.close()

    username = f"{name[random.randint(0, len(name)-1)]}{animal[random.randint(0, len(animal)-1)]}"
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"Received message from {username}, {address}: {message}")
            message = f"{username}: {message}"
            broadcast(message, address)
        except Exception as e:
            print(f"Error: {e}")
            break

    print(f"Connection from {address} closed.")
    client_socket.close()

def broadcast(message, address):
    for client in clients:
        if client.getpeername() == address:
            continue
        try:
            client.send(message.encode())
        except Exception as e:
            print(f"Error broadcasting message: {e}")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', config.SERVER_PORT))
    server_socket.listen(5)
    print("Server listening on port 5555...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address} established.")
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

clients = []

if __name__ == "__main__":
    start_server()

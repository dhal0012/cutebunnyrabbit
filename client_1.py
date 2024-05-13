import socket
import threading

import config


def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print("\n" + message)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', config.SERVER_PORT))
    print("Connected to server.")

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()
    username = input()
    password = input()
    auth = f"{username}:{password}"
    client_socket.send(auth.encode())
    while True:
        message = input("Message: ")
        client_socket.send(message.encode())

if __name__ == "__main__":
    start_client()
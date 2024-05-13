from cryptography import fernet

key = fernet.Fernet.generate_key()
SERVER_ADDR = "127.0.0.1"
SERVER_PORT = 6661
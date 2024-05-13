from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import HMAC, SHA256

def aes_encrypt(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message, AES.block_size))
    return ciphertext, cipher.iv

def aes_decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted

def generate_hmac(message, key):
    h = HMAC.new(key, digestmod=SHA256)
    h.update(message)
    return h.digest()

def verify_hmac(message, key, hmac):
    h = HMAC.new(key, digestmod=SHA256)
    h.update(message)
    try:
        h.verify(hmac)
        return True
    except ValueError:
        return False

# Example usage
message = b"Hello World"
key = get_random_bytes(16)  # 128-bit key
encrypted_message, iv = aes_encrypt(message, key)

hmac = generate_hmac(encrypted_message, key)
# Assume the message has been transmitted and received elsewhere
# Verify HMAC before decryption
if verify_hmac(encrypted_message, key, hmac):
    decrypted_message = aes_decrypt(encrypted_message, key, iv)
    print("Original Message:", message)
    print("Encrypted Message:", encrypted_message)
    print("Decrypted Message:", decrypted_message)
else:
    print("HMAC verification failed. Message may have been tampered with.")
import socket
from crypto_utils import load_public_key,encrypt
from cryptography.fernet import Fernet

def start_client(host,port):
    client_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_sock.settimeout(20)
    client_sock.connect((host,port))
    client_sock.send(username.encode())

    server_pub_key = load_public_key(client_sock.recv(2048))

    fernet_key = Fernet.generate_key()
    encrypted_key = encrypt(server_pub_key, fernet_key)
    client_sock.send(encrypted_key)

    fernet = Fernet(fernet_key)

    try: 
        while True:
            msg = input("You: ")
            if msg.lower() == 'quit':
                break
            client_sock.send(fernet.encrypt(msg.encode()))
            print(f"{username}: {msg}") 
    finally:
        client_sock.close()

if __name__=="__main__":
    host = input("Enter hostname:")
    port = int(input("Enter port number:"))
    username = input("Enter Your Username:")

    start_client(host=host,port=port)
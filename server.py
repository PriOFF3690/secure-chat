import socket, threading
from cryptography.fernet import Fernet
from crypto_utils import generate_rsa_keys, decrypt, serialize_public_key

HOST = {
    'host': '192.168.170.33',
    'port': 1234
}

def handle_client(client_sock, client_addr):
    username = client_sock.recv(1024).decode()
    print(f"[NEW CONNECTION] {username} ({client_addr}) connected.")
    private_key, public_key = generate_rsa_keys()
    client_sock.send(serialize_public_key(public_key=public_key))

    encrypted_key = client_sock.recv(1024)
    symmectric_key = decrypt(private_key,encrypted_key)
    fernet = Fernet(symmectric_key)
    
    while True:
        try:
            encrypted_message = client_sock.recv(4096)
            if not encrypted_message:
                break
            message = fernet.decrypt(encrypted_message).decode()
            print(f"[{username}]: {message}")
            client_sock.send(fernet.encrypt(f"[{username}]: {message}".encode()))
        except ConnectionResetError:
            break
    print(f"[DISCONNECTED] {username} disconnected.")
    client_sock.close()

def start_server(host=HOST['host'],port=HOST['port']):
    server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_sock.bind((HOST['host'],HOST['port']))
    server_sock.listen(10)
    print(f"[LISTENING] Server is listening on {host}:{port}")
    
    while True:
        client_sock,client_addr = server_sock.accept()
        thread = threading.Thread(target=handle_client,args=(client_sock,client_addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__=="__main__":
    start_server()
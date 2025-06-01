# 🔐 Secure Chat Room

## 🧾 Introduction to Secure Chat Room

Secure Chat Room is a Python-based encrypted chat application that allows clients to securely communicate with a server using RSA (SHA-512) for key exchange and Fernet (AES) for encrypted message transmission.

Each client uses a unique username, and communication is encrypted end-to-end after a secure key handshake. This makes the app ideal for learning how encryption, networking, and secure session handling work in Python.

### Key Features

- 🔐 RSA key exchange using OAEP with SHA-512
- 🔑 Symmetric encryption using Fernet (AES-128)
- 👤 Username-based chat identification
- 🧵 Multithreaded server to handle multiple clients (scalable)
- ⚡ Simple socket-based architecture

---

## ⚙️ Installation

### 1. Clone the repository

    git clone https://github.com/PriOFF3690/secure-chat.git
    cd secure-chat

### 2. Create and activate a virtual environment

    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate

### 3. Install required packages

    pip install -r requirements.txt

If requirements.txt is missing, install manually:

    pip install cryptography

---

## 🚀 Usage

### 1. Start the Server

    python server.py

> Ensure the IP address and port in server.py are set correctly for your network.

### 2. Start the Client

    python client.py

You'll be prompted to enter:
- Server IP address
- Server port (default: 1234)
- Your username

### 3. Chat Securely

- Messages are encrypted before sending and decrypted upon receipt.
- Each message is tagged with the sender's username.
- Type `quit` to exit the chat.

---

## ✅ Example

    You: Hello Server!
    Server: [Server] Server received: Hello Server!

> The client shows your sent messages, and receives replies from the server.

---

## 📦 Requirements

- Python 3.8+
- cryptography

Save this as `requirements.txt`:

    cryptography

Install with:

    pip install -r requirements.txt

---

## 📌 Notes

- The current setup supports one client at a time.
- Encryption uses RSA with SHA-512 during key exchange and Fernet (AES) during communication.
- Ready to be extended for group chat and user authentication.

---

## 👨‍💻 Author

Built by [PriOFF3690](https://github.com/PriOFF3690) as a secure communication prototype using Python sockets and modern cryptography.

---

## 📄 License

This project is open-source and available under the MIT License.

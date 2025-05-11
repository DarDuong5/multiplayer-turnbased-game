import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# To represent a logger
# Logger receives updates and prints them to the screen as log messages
class Logger:
    # Signature: str -> None
    # Purpose: Displays the message as a log entry in the server console
    def update(self, message: str) -> None:
        print(f"[Logger] {message}")

# To represent a notifier
# Notifier receives updates and simulates sending a notification
class Notifier:
    # Signature: str -> None
    # Purpose: Displays the message as a stimulated notification in the server console
    def update(self, message: str) -> None:
        print(f"[Notifier] NOTIFY: {message}")

# To represent a chat server
class ChatServer:
    def __init__(self, addr='localhost', port=54505):
        self.addr: str = addr
        self.port: int = port

        self.server_socket: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.addr, self.port))
        self.server_socket.listen(3)

        self.chat_message: list = []
        self.lock: threading = threading.Lock()
        self.clients: list = []

        self.observers = [Logger(), Notifier()]

    # Signature: str -> None
    # Purpose: Notifies and logs the messages into the console
    def notify(self, message: str) -> None:
        for observer in self.observers:
            observer.update(message)

    # Signature: str, conn -> None
    # Purpose: Sends the message to every player in the server
    def broadcast(self, message: str, conn) -> None:
        with self.lock: 
            for client in self.clients:
                if conn == client:
                    continue
                client.sendall(message.encode())

    # Signature: str, conn -> None
    # Purpose: Handles the client to receive the message
    def handle_client(self, conn, addr) -> None:
        self.notify(f'New connection from {addr}')
        while True:
            try:
                message = conn.recv(1024).decode()
                if not message:
                    break
                with self.lock:
                    self.chat_message.append(message)
                self.update_chat_window()
                self.broadcast(message, conn)
                self.notify(f'Message received: {message}')
            except Exception as e:
                self.notify(f'Error handling client: {e}')
                break
    
    # Signature: None -> None
    # Purpose: Accepts clients whenever they join
    def accept_connection(self) -> None:
        while True:
            conn, addr = self.server_socket.accept()
            self.clients.append(conn)
            threading.Thread(target=self.handle_client, args=(conn, addr), daemon=True).start()

    # Signature: None -> None
    # Purpose: Updates the chat window with the latest messages
    def update_chat_window(self) -> None:
        chat_display.config(state=tk.NORMAL) # Enabling the editing text area
        chat_display.delete("1.0", tk.END) # Clears the chat display
        with self.lock:
            for message in self.chat_message:
                chat_display.insert(tk.END, message + '\n')
            chat_display.config(state=tk.DISABLED)

chat_server = ChatServer()

# GUI Setup
root = tk.Tk() # Main application window
root.title("Server Side Chat")

# Scrollable text
chat_display = scrolledtext.ScrolledText(root, width=50, height=30, state=tk.DISABLED)
chat_display.pack(padx=10, pady=10)

# Start accepting connections
threading.Thread(target=chat_server.accept_connection, daemon=True).start()

root.mainloop()


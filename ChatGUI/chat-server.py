import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

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

    # Handle communication - client
    def broadcast(self, message) -> None:
        with self.lock: # Thread safe sending
            for client in self.clients:
                client.sendall(message.encode())

    def handle_client(self, conn, addr) -> None:
        while True:
            try:
                message = conn.recv(1024).decode()
                if not message:
                    break
                with self.lock:
                    self.chat_message.append(message)
                self.update_chat_window()
                self.broadcast(message)
            except Exception as e:
                print(f"Error handling client: {e}")
                break

    def accept_connection(self) -> None:
        while True:
            conn, addr = self.server_socket.accept()
            self.clients.append(conn)
            threading.Thread(target=self.handle_client, args=(conn, addr), daemon=True).start()

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











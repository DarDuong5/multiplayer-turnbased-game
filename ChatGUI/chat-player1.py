import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

class Player1:
    def __init__(self, addr='localhost', port=54505, player_name='Player 1'):
        self.addr = addr
        self.port = port
        self.player_name = player_name

        # Connect with server
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_socket.connect((self.addr, self.port))
    
        # List to store messages and a lock for thread safety
        self.player_message: list[str] = []
        self.lock: threading = threading.Lock()

        # Start background threads for receiving messages
        threading.Thread(target=self.receive_message, daemon=True).start()

    def receive_message(self) -> None:
        """Receive messages from the server and update the chat window."""
        while True:
            try:
                # Receive message from the server
                message = self.tcp_socket.recv(1024).decode("utf-8")
                if message:
                    with self.lock:
                        self.player_message.append(f"Server: {message}")
                        self.update_chat_window()
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    def send_message(self) -> None:
        """Send the message typed by the user to the server."""
        message = input_field.get()
        if message.strip():  # Ensure the message is not empty
            try:
                # Send message to the server
                self.tcp_socket.send(f"{self.player_name}: {message}".encode("utf-8"))
                
                # Append the message to the client message list and update the chat window
                with self.lock:
                    self.player_message.append(f"You: {message}")
                    self.update_chat_window()
                
                # Clear the input field after sending the message
                input_field.delete(0, tk.END)
            except Exception as e:
                print(f"Error sending message: {e}")
        else:
            print("Message is empty, not sending.")

    def update_chat_window(self) -> None:
        """Update the chat window with the latest messages."""
        chat_display.config(state=tk.NORMAL)  # Enable the chat window for updating
        chat_display.delete(1.0, tk.END)  # Clear the current chat window content
        
        # Insert all messages into the chat window
        for msg in self.player_message:
            chat_display.insert(tk.END, msg + '\n')
        
        chat_display.config(state=tk.DISABLED)  # Disable the chat window to prevent user edits

player1 = Player1()

# GUI creation
root: tk.Tk = tk.Tk()
root.title("Player 1 Side Chat")

# Scrollable chat window
chat_display = scrolledtext.ScrolledText(root, width=50, height=30, state=tk.DISABLED)
chat_display.pack(padx=10, pady=10)

# Input field
input_field = tk.Entry(root, width=40)
input_field.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))

# Send button
send_button: tk.Button = tk.Button(root, text="Send", command=player1.send_message)
send_button.pack(side=tk.LEFT, padx=(5, 10), pady=(0, 10))

root.mainloop()

    

import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
import sys
import os

# Parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ChatbotGUI.chatbot import ChatBot

class Player2:
    def __init__(self, addr='localhost', port=54505, player_name='Player 2'):
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

    # Signature: None -> None
    # Purpose: Receive messages from the server and update the chat window
    def receive_message(self) -> None:
        while True:
            try:
                # Receive message from the server
                message = self.tcp_socket.recv(1024).decode("utf-8")
                if message:
                    with self.lock:
                        self.player_message.append(f"Server: {message}")
                    root.after(0, self.update_chat_window)
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    # Signature: None -> None
    # Purpose: Send the message typed by the user to the server
    def send_message(self) -> None:
        message = input_field.get()
        # Ensure the message is not empty
        if message.strip():
            try:
                # Send message to the server
                self.tcp_socket.send(f"{self.player_name}: {message}".encode("utf-8"))
                
                # Append the message to the client message list and update the chat window
                with self.lock:
                    self.player_message.append(f"You: {message}")
                root.after(0, self.update_chat_window)
                
                # Clear the input field after sending the message
                input_field.delete(0, tk.END)
            except Exception as e:
                print(f"Error sending message: {e}")
        else:
            print("Message is empty, not sending.")

    # Signature: None -> None
    # Purpose: Updates the chat window with the latest messages
    def update_chat_window(self) -> None:
        chat_display.config(state=tk.NORMAL)  # Enable the chat window for updating
        chat_display.delete(1.0, tk.END)  # Clear the current chat window content
        
        # Insert all messages into the chat window
        for msg in self.player_message:
            chat_display.insert(tk.END, msg + '\n')
        
        chat_display.config(state=tk.DISABLED)  # Disable the chat window to prevent user edits

player1 = Player2()
chatbot = ChatBot()

# GUI creation
root: tk.Tk = tk.Tk()
root.title("Player 2 Side Chat")

# Scrollable chat window
chat_display = scrolledtext.ScrolledText(root, width=50, height=30, state=tk.DISABLED)
chat_display.pack(padx=10, pady=10)

# Input field
input_field = tk.Entry(root, width=40)
input_field.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))

# Send button
send_button: tk.Button = tk.Button(root, text="Send", command=player1.send_message)
send_button.pack(side=tk.LEFT, padx=(5, 10), pady=(0, 10))

#chatbot.run_chatbot()
root.mainloop()
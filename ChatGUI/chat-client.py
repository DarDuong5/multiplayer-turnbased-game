import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

ADDRESS = ('localhost', 54505)

client_message: list[str] = []
lock: threading = threading.Lock()

# Connect with the server
client_socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDRESS)

def receive_message() -> None:
    """Receive messages from the server and update the chat window."""
    while True:
        try:
            # Receive message from the server
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                with lock:
                    client_message.append(f"Server: {message}")
                    update_chat_window()
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def send_message() -> None:
    """Send the message typed by the user to the server."""
    message = input_field.get()
    if message.strip():  # Ensure the message is not empty
        try:
            # Send message to the server
            client_socket.send(message.encode('utf-8'))
            
            # Append the message to the client message list and update the chat window
            with lock:
                client_message.append(f"You: {message}")
                update_chat_window()
            
            # Clear the input field after sending the message
            input_field.delete(0, tk.END)
        except Exception as e:
            print(f"Error sending message: {e}")
    else:
        print("Message is empty, not sending.")

def update_chat_window() -> None:
    """Update the chat window with the latest messages."""
    chat_display.config(state=tk.NORMAL)  # Enable the chat window for updating
    chat_display.delete(1.0, tk.END)  # Clear the current chat window content
    
    # Insert all messages into the chat window
    for msg in client_message:
        chat_display.insert(tk.END, msg + '\n')
    
    chat_display.config(state=tk.DISABLED)  # Disable the chat window to prevent user edits

# GUI creation
root: tk.Tk = tk.Tk()
root.title("Client side chat")

# Scrollable chat window
chat_display = scrolledtext.ScrolledText(root, width=50, height=30, state=tk.DISABLED)
chat_display.pack(padx=10, pady=10)

# Input field
input_field = tk.Entry(root, width=40)
input_field.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))

# Send button
send_button: tk.Button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.LEFT, padx=(5, 10), pady=(0, 10))

# Background thread
threading.Thread(target=receive_message, daemon=True).start()

root.mainloop()

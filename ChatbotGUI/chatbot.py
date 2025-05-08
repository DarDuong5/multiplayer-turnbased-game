from abc import ABC, abstractmethod
import json
import tkinter as tk
from tkinter import scrolledtext

# Creation Pattern: Factory
# Structural: Adapter
# Behavioral: Strategy

# To represent a query database
class QueryDatabase:
    def __init__(self, queries_filepath="ChatbotGUI/queries.json"):
        with open(queries_filepath, 'r') as file:
            self.queries: json = json.load(file)

    # Signature: str, str -> str
    # Purpose: Returns the chatbot's response according to the category and user input
    def get_response(self, category: str, user_input: str) -> str:
        if category in self.queries and user_input in self.queries[category]:
            return self.queries[category][user_input]
        return "Sorry, I don't understand that query."

# To represent queries
class Queries(ABC):
    def __init__(self):
        self.adapter: QueryAdapter = QueryAdapter()

    # Signature: str -> str
    # Purpose: Returns all of the possible inquiries under the category
    @abstractmethod
    def inquire(self, user_input: str) -> str:
        pass

# To represent a query adapter
class QueryAdapter:
    def __init__(self):
        self.database: QueryDatabase = QueryDatabase()

    # Signature: str, str -> str
    # Purpose: Gets the chatbot's response according to the category and user input 
    def fetch_response(self, category: str, user_input: str) -> str:
        main_response = self.database.get_response(category, user_input)
        return main_response 

# To represent a game mechanic category
class GameMechanics(Queries):
    # Signature: str -> str
    # Purpose: Returns the chatbot's response under the category game mechanics after the user inputs a query
    def inquire(self, user_input: str) -> str:
        return self.adapter.fetch_response('Game Mechanics', user_input)

# To represent a character selection category
class CharacterSelection(Queries):
    # Signature: str -> str
    # Purpose: Returns the chatbot's response under the category character selection after the user inputs a query
    def inquire(self, user_input: str) -> str:
        return self.adapter.fetch_response('Character Selection', user_input)

# To represent a multiplayer support category
class MultiplayerSupport(Queries):
    # Signature: str -> str
    # Purpose: Returns the chatbot's response under the category multiplayer support after the user inputs a query
    def inquire(self, user_input: str) -> str:
        return self.adapter.fetch_response('Multiplayer Support', user_input)

# To represent a help category
class Help(Queries):
    # Signature: str -> str
    # Purpose: Returns the chatbot's response under the category help after the user inputs a query
    def inquire(self, user_input: str) -> str:
        return self.adapter.fetch_response('Help', user_input)

# To represent a backend manager
class BackEndManager:
    # Signature: str, str -> str
    # Purpose: Processes different request types and delegates to the correct handler.
    def process_request(self, request_type: str, user_input: str) -> str:
        if request_type == 'Game Mechanics':
            return GameMechanics().inquire(user_input)
        elif request_type == 'Character Selection':
            return CharacterSelection().inquire(user_input)
        elif request_type == 'Multiplayer Support':
            return MultiplayerSupport().inquire(user_input)
        elif request_type == 'Help':
            return Help().inquire(user_input)
        return 'Service not available.'
    
# To represent a chatbot
class ChatBot:
    def __init__(self):
        self.backend: BackEndManager = BackEndManager()
        self.database: QueryDatabase = QueryDatabase()
        self.selected_category: str = None # used to store the category for future uses
    
    # Signature: str -> None
    # Purpose: Determine the category based on user input and display available queries
    def categorize_request(self, user_input: str) -> None:
        keywords = ["Game Mechanics", "Character Selection", "Multiplayer Support", "Help"]

        if user_input in keywords:
            self.selected_category = user_input

    # Signature: None -> None
    # Purpose: Helper method that loops back after using a query and introduces the chatbot to the user again
    def intro(self) -> None:
        chat_display.config(state=tk.NORMAL)
        chat_display.insert(tk.END, "ChatBot: Welcome to the Game ChatBot!\n")
        chat_display.insert(tk.END, "ChatBot: How may I help you today?\n")
        chat_display.insert(tk.END, "Available Categories:\n"
                                    " - Game Mechanics\n"
                                    " - Character Selection\n"
                                    " - Multiplayer Support\n"
                                    " - Help\n"
                                    " - Back\n")
        chat_display.insert(tk.END, "Type one of the categories above to begin.\n\n")
        chat_display.config(state=tk.DISABLED)

    # Signature: None -> None
    # Purpose: Users the message in which the chatbot will respond back depending on the given category and query
    def send_message(self) -> None:
        user_input = input_field.get()
        if not user_input:
            return

        chat_display.config(state=tk.NORMAL)
        chat_display.insert(tk.END, f"You: {user_input}\n")
        
        if user_input == "Back":
            self.selected_category = None
            self.intro()

        if self.selected_category is None:
            self.categorize_request(user_input)
            if self.selected_category:
                chat_display.insert(tk.END, f"ChatBot: Here are some queries you can ask under '{self.selected_category}':\n")
                for query in self.database.queries[self.selected_category].keys():
                    chat_display.insert(tk.END, f" - {query}\n")
                chat_display.insert(tk.END, "Please type one of the queries above.\n\n")
            else:
                chat_display.insert(tk.END, "ChatBot: Sorry, I don't understand that category.\n")
        else:
            response = self.backend.process_request(self.selected_category, user_input)
            chat_display.insert(tk.END, f"ChatBot: {response}\n")

        chat_display.config(state=tk.DISABLED)
        input_field.delete(0, tk.END)

    # Signature: None -> None
    # Purpose: Sets up the GUI and runs the chatbot
    def run_chatbot(self) -> None:
        global root, chat_display, input_field
        chatbot = ChatBot()

        # GUI creation
        root = tk.Tk()
        root.title("ChatBot Helper")

        # Scrollable chat window
        chat_display = scrolledtext.ScrolledText(root, width=60, height=25, state=tk.DISABLED, wrap=tk.WORD)
        chat_display.pack(padx=10, pady=10)

        # Input frame for better layout
        input_frame = tk.Frame(root)
        input_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

        # Input field
        input_field = tk.Entry(input_frame, width=45)
        input_field.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Send button
        send_button = tk.Button(input_frame, text="Send", command=chatbot.send_message)
        send_button.pack(side=tk.LEFT, padx=(5, 0))

        # Start the GUI loop
        chatbot.intro()
        root.mainloop()

if __name__ == '__main__':
    chatbot = ChatBot()
    chatbot.run_chatbot()
        
# -------------------------------------------------------------------------------------------------------- PYTESTS --------------------------------------------------------------------------------------------------------

def test_get_response() -> None:
    query_database = QueryDatabase()
    assert query_database.get_response('Help', 'Nothing') == "Sorry, I don't understand that query."
    assert query_database.get_response('Help', 'How do I use this chatbot?') == "You can simply type the available queries and we'll do our best to help guide you!"

def test_fetch_response() -> None:
    query_adapter = QueryAdapter()
    assert query_adapter.fetch_response('Multiplayer Support', "How is the turn order decided?") == "Turn order is decided by player number. Player 1 goes first, then 2, and then 3, and cycles over again"

def test_inquire_game_mechanics() -> None:
    game_mechanics = GameMechanics()
    assert game_mechanics.inquire("What is the maximum number of players?") == "This game supports up to 3 players per match."

def test_inquire_character_selection() -> None:
    refund_processing = CharacterSelection()
    assert refund_processing.inquire("How do I choose my character?") == "At the beginning of the game, you'll be prompted to select a character."

def test_inquire_multiplayer_support() -> None:
    product_availability = MultiplayerSupport()
    assert product_availability.inquire("Is matchmaking skill-based?") == "No, there is such no thing as matchmaking though it could be included in the next update."

def test_inquire_live_agent_support() -> None:
    live_agent_support = Help()
    assert live_agent_support.inquire("How do I contact game support?") == "If you need to contact game support, we can send a live agent to hear your problems!"

def test_process_request() -> None:
    backend_manager = BackEndManager()
    assert backend_manager.process_request('Game Mechanics', "Can I revive another player?") == "Currently, revival is not supported once a player is eliminated."
    assert backend_manager.process_request('Character Selection', "Which character is best for beginners?") == "The Gladiator is a great choice for new players due to balanced stats."
    assert backend_manager.process_request('Multiplayer Support', "Can I host a game for friends?") == "Yes, you definitely can!"
    assert backend_manager.process_request('Help',  "I'm stuck on the loading screen.") == "Try restarting the game."
    assert backend_manager.process_request('Unknown', 'What is this?') == 'Service not available.'
# Program manages information for the game
# Users can store, search, update, and delete information safely
# SQLite3 to keep all the game information records in a local database file

import sqlite3
import threading

# To represent a database
class Database:
    _instance = None
    _lock = threading.Lock()

    # Signature: Create only one DB connection for the app
    # Purpose: Follows Singleton pattern so SQLite is accessed safely
    def __new__(cls) -> 'Database':
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Database, cls).__new__(cls)
                cls._instance.conn = sqlite3.connect("turn_based_battle.db", check_same_thread=False)
                cls._instance._create_table()
            return cls._instance
        
    # Signature: None -> None
    # Purpose: Sets up the table to store info for characters, players, chat history, battle sessions, and chatbot unknown queries 
    def _create_table(self) -> None:
        with self.conn:
           self.conn.execute('''
                            CREATE TABLE IF NOT EXISTS characters (
                             character_id TEXT PRIMARY KEY,
                             character_name TEXT NOT NULL,
                             health REAL NOT NULL,
                             defense REAL NOT NULL,
                             attack_name TEXT NOT NULL,
                             attack_damage REAL NOT NULL,
                             special_attack_name TEXT NOT NULL,
                             special_attack_damage REAL NOT NULL
                             )''')
           self.conn.execute('''
                            CREATE TABLE IF NOT EXISTS players (
                             player_id TEXT PRIMARY KEY,
                             player_number REAL NOT NULL,
                             character TEXT NOT NULL
                             )''')
           self.conn.execute('''
                            CREATE TABLE IF NOT EXISTS chat_history (
                             time TEXT PRIMARY KEY,
                             player TEXT NOT NULL,
                             message TEXT NOT NULL
                             )''')
           self.conn.execute('''
                            CREATE TABLE IF NOT EXISTS battle_session (
                             game_session TEXT PRIMARY KEY,
                             time TEXT NOT NULL,
                             winner TEXT NOT NULL,
                             total_turns REAL NOT NULL
                             )''')
           self.conn.execute('''
                            CREATE TABLE IF NOT EXISTS unknown_queries (
                             time TEXT PRIMARY KEY,
                             player TEXT NOT NULL,
                             category TEXT NOT NULL,
                             query TEXT NOT NULL
                             )''')

    
    # Signature: str, str, int, int, str, int, str, int -> None
    # Purpose: Inserts a new character into the characters table
    def insert_characters(self, id: str, char_name: str, health: int, defense: int, attack_name: str, attack_dmg: int, sp_attack_name: str, sp_dmg: int) -> None:
        with self.conn:
            self.conn.execute(
                "INSERT INTO characters (character_id, character_name, health, defense, attack_name, attack_damage, special_attack_name, special_attack_damage) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (id, char_name, health, defense, attack_name, attack_dmg, sp_attack_name, sp_dmg)
            )

    # Signature: str, int, str -> None
    # Purpose: Inserts a new player into the players table  
    def insert_players(self, id: str, player_num: int, character: str) -> None:
        with self.conn:
            self.conn.execute(
                "INSERT INTO players (player_id, player_number, character) VALUES (?, ?, ?)",
                (id, player_num, character)
            )

    # Signature: str, str, str -> None
    # Purpose: Inserts a new chat history into the chat history table   
    def insert_chat_history(self, time: str, player: str, msg: str) -> None:
        with self.conn:
            self.conn.execute(
                "INSERT INTO chat_history (time, player, message) VALUES (?, ?, ?)",
                (time, player, msg)
            )

    # Signature: str, str, str, int -> None
    # Purpose: Inserts a new battle session into the battle session table  
    def insert_battle_session(self, session: str, time: str, winner: str, turns: int) -> None:
        with self.conn:
            self.conn.execute(
                "INSERT INTO battle_session (game_session, time, winner, total_turns) VALUES (?, ?, ?, ?)",
                (session, time, winner, turns)
            )

    # Signature: str, str, str, str -> None
    # Purpose: Inserts a new unknown query into the unknown queries table  
    def insert_unknown_queries(self, time: str, player: str, category: str, query: str) -> None:
        with self.conn:
            self.conn.execute(
                "INSERT INTO unknown_queries (time, player, category, query) VALUES (?, ?, ?, ?)",
                (time, player, category, query)
            )
    
    # Signature: None -> list[tuple]
    # Purpose: Returns all character records
    def fetch_all_characters(self) -> list[tuple]:
        with self.conn:
            return self.conn.execute(
                "SELECT * FROM characters"
            ).fetchall()
        
    # Signature: None -> list[tuple]
    # Purpose: Returns all player records
    def fetch_all_players(self) -> list[tuple]:
        with self.conn:
            return self.conn.execute(
                "SELECT * FROM players"
            ).fetchall()
        
    # Signature: None -> list[tuple]
    # Purpose: Returns all chat history records
    def fetch_all_chat_history(self) -> list[tuple]:
        with self.conn:
            return self.conn.execute(
                "SELECT * FROM chat_history"
            ).fetchall()
        
    # Signature: None -> list[tuple]
    # Purpose: Returns all battlesession records
    def fetch_all_battle_session(self) -> list[tuple]:
        with self.conn:
            return self.conn.execute(
                "SELECT * FROM battle_session"
            ).fetchall()
        
    # Signature: None -> list[tuple]
    # Purpose: Returns all unknown query records
    def fetch_all_unknown_queries(self) -> list[tuple]:
        with self.conn:
            return self.conn.execute(
                "SELECT * FROM unknown_queries"
            ).fetchall()
        
    # Signature: str -> list[tuple]
    # Purpose: Lets users view a specific entry for characters
    def fetch_character_by_id(self, char_id: str) -> list[tuple]:
        with self.conn:
            return self.conn.execute(
                "SELECT * FROM characters WHERE character_id = ?",
                (char_id,)
            ).fetchone()

    # Signature: str -> list[tuple]
    # Purpose: Lets users view a specific entry for players
    def fetch_player_by_id(self, player_id: str) -> list[tuple]:
        with self.conn:
            return self.conn.execute(
                "SELECT * FROM players WHERE player_id = ?",
                (player_id,)
            ).fetchone()

    # Signature: str -> list[tuple]
    # Purpose: Lets users view a specific entry for chat history
    def fetch_chat_history_by_time(self, time: str) -> list[tuple]:
        with self.conn:
            return self.conn.execute(
                "SELECT * FROM chat_history WHERE time = ?",
                (time,)
            ).fetchone()

    # Signature: str -> list[tuple]
    # Purpose: Lets users view a specific entry for battle session
    def fetch_battle_session_by_id(self, session_id: str) -> list[tuple]:
        with self.conn:
            return self.conn.execute(
                "SELECT * FROM battle_session WHERE game_session = ?",
                (session_id,)
            ).fetchone()

    # Signature: str -> list[tuple]
    # Purpose: Lets users view a specific entry for unknown queries
    def fetch_unknown_query_by_time(self, time) -> list[tuple]:
        with self.conn:
            return self.conn.execute(
                "SELECT * FROM unknown_queries WHERE time = ?",
                (time,)
            ).fetchone()
    
    # Signature: str -> None
    # Purpose: Lets the user remove a saved character 
    def delete_character_by_id(self, char_id: str):
        with self.conn:
            self.conn.execute("DELETE FROM characters WHERE character_id = ?", (char_id,))

    # Signature: str -> None
    # Purpose: Lets the user remove a saved player 
    def delete_player_by_id(self, player_id: str):
        with self.conn:
            self.conn.execute("DELETE FROM players WHERE player_id = ?", (player_id,))

    # Signature: str -> None
    # Purpose: Lets the user remove a saved chat history 
    def delete_chat_history_by_time(self, time: str):
        with self.conn:
            self.conn.execute("DELETE FROM chat_history WHERE time = ?", (time,))

    # Signature: str -> None
    # Purpose: Lets the user remove a saved battle session
    def delete_battle_session_by_id(self, session_id: str):
        with self.conn:
            self.conn.execute("DELETE FROM battle_session WHERE game_session = ?", (session_id,))

    # Signature: str -> None
    # Purpose: Lets the user remove a saved unknown query 
    def delete_unknown_query_by_time(self, time: str):
        with self.conn:
            self.conn.execute("DELETE FROM unknown_queries WHERE time = ?", (time,))

    # Signature: None -> None
    # Purpose: Lets the user remove all characters
    def delete_all_characters(self):
        with self.conn:
            self.conn.execute("DELETE FROM characters")

    # Signature: None -> None
    # Purpose: Lets the user remove all players
    def delete_all_players(self):
        with self.conn:
            self.conn.execute("DELETE FROM players")

    # Signature: None -> None
    # Purpose: Lets the user remove all chat histories
    def delete_all_chat_history(self):
        with self.conn:
            self.conn.execute("DELETE FROM chat_history")

    # Signature: None -> None
    # Purpose: Lets the user remove all battle sessions
    def delete_all_battle_sessions(self):
        with self.conn:
            self.conn.execute("DELETE FROM battle_session")

    # Signature: None -> None
    # Purpose: Lets the user remove all unknown queries
    def delete_all_unknown_queries(self):
        with self.conn:
            self.conn.execute("DELETE FROM unknown_queries")

    # Signature: str -> list[tuple]
    # Purpose: Finds character by character id or name
    def search_character(self, keyword: str) -> list[tuple]:
        with self.conn:
            return self.conn.execute(
                "SELECT * FROM characters WHERE character_id LIKE ? OR character_name LIKE ?",
                (f"%{keyword}%", f"%{keyword}%")
            ).fetchall()

    # Signature: str -> list[tuple]
    # Purpose: Finds player by player id or number
    def search_player(self, keyword: str) -> list[tuple]:
        with self.conn:
            return self.conn.execute(
                "SELECT * FROM players WHERE player_id LIKE ? OR player_number LIKE ?",
                (f"%{keyword}%", f"%{keyword}%")
            ).fetchall()
        
# --------------------------------------------------- PYTESTS ---------------------------------------------------

def test_insert_and_fetch_character() -> None:
    db = Database()
    db.insert_characters("char001", "Knight", 100, 50, "Slash", 30, "Charge", 50)
    result = db.fetch_character_by_id("char001")
    assert result[1] == "Knight"
    assert result[4] == "Slash"

def test_insert_and_fetch_player() -> None:
    db = Database()
    db.insert_players("player001", 1, "Knight")
    result = db.fetch_player_by_id("player001")
    assert result[2] == "Knight"

def test_insert_and_fetch_chat_history() -> None:
    db = Database()
    db.insert_chat_history("2025-01-01T00:00", "player001", "Hello!")
    result = db.fetch_chat_history_by_time("2025-01-01T00:00")
    assert result[2] == "Hello!"

def test_insert_and_fetch_battle_session() -> None:
    db = Database()
    db.insert_battle_session("session001", "2025-01-01T00:01", "player001", 10)
    result = db.fetch_battle_session_by_id("session001")
    assert result[2] == "player001"

def test_insert_and_fetch_unknown_query() -> None:
    db = Database()
    db.insert_unknown_queries("2025-01-01T00:02", "player001", "confused", "What's mana?")
    result = db.fetch_unknown_query_by_time("2025-01-01T00:02")
    assert result[3] == "What's mana?"

def test_delete_character() -> None:
    db = Database()
    db.insert_characters("char002", "Mage", 80, 30, "Fireball", 40, "Meteor", 70)
    db.delete_character_by_id("char002")
    result = db.fetch_character_by_id("char002")
    assert result is None

def test_search_character() -> None:
    db = Database()
    db.insert_characters("char003", "Rogue", 90, 20, "Stab", 25, "Poison", 35)
    results = db.search_character("Rogue")
    assert len(results) == 1
    assert results[0][1] == "Rogue"

def test_delete_all_players() -> None:
    db = Database()
    db.insert_players("p1", 1, "Knight")
    db.insert_players("p2", 2, "Mage")
    db.delete_all_players()
    assert db.fetch_all_players() == []

def test_search_player() -> None:
    db = Database()
    db.insert_players("p3", 3, "Archer")
    results = db.search_player("3")
    assert len(results) == 1
    assert results[0][2] == "Archer"

    
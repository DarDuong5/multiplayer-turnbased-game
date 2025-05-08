# Program manages information for different vehicles
# Users can store, search, update, and delete information safely
# SQLite3 to keep all the vehicle information records in a local database file

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
                cls._instance.conn = sqlite3.connect("transport.db", check_same_thread=False)
                cls._instance._create_table()
            return cls._instance
        
    # Signature: None -> None
    # Purpose: Sets up the table to store info for vehicles, routes, location updates, admin commands, and event logs 
    def _create_table(self) -> None:
        with self.conn:
            self.conn.execute('''
                              CREATE TABLE IF NOT EXISTS vehicles (
                                vehicle_id TEXT PRIMARY KEY,
                                vehicle_type TEXT NOT NULL,
                                latitude REAL NOT NULL,
                                longitude REAL NOT NULL,
                                status TEXT NOT NULL
                              )''')
            self.conn.execute('''
                              CREATE TABLE IF NOT EXISTS routes (
                                route_id TEXT PRIMARY KEY,
                                route_name TEXT NOT NULL,
                                stops TEXT NOT NULL,
                                vehicles TEXT NOT NULL
                              )''')
            self.conn.execute('''
                              CREATE TABLE IF NOT EXISTS location_updates (
                                update_id TEXT PRIMARY KEY,
                                vehicle_id TEXT NOT NULL,
                                latitude REAL NOT NULL,
                                longitude REAL NOT NULL,
                                timestamp TEXT NOT NULL,
                                status TEXT NOT NULL
                            )''')
            self.conn.execute('''
                              CREATE TABLE IF NOT EXISTS admin_commands (
                                command_id TEXT PRIMARY KEY,
                                vehicle_id TEXT NOT NULL,
                                command_type TEXT NOT NULL,
                                time_sent TEXT NOT NULL                                
                            )''')
            self.conn.execute('''
                              CREATE TABLE IF NOT EXISTS event_logs (
                                event_id TEXT PRIMARY KEY,
                                vehicle_id TEXT NOT NULL,
                                details TEXT NOT NULL,
                                event_time TEXT NOT NULL
                            )''')
    
    # Signature: str, str, float, float, str -> None
    # Purpose: Saves the vehicle id, type, location, and status
    def insert(self, id: str, type: str, long: float, lat: float, status: str) -> None:
        with self.conn:
            self.conn.execute(
                "INSERT OR REPLACE INTO vehicles (vehicle_id, vehicle_type, longitude, latitude, status) VALUES (?, ?, ?, ?, ?)",
                (id, type, long, lat, status)
            )
    
    # Signature: None -> list[tuple]
    # Purpose: Returns everything from the table
    def fetch_all(self) -> list[tuple]:
        with self.conn:
            return self.conn.execute("SELECT * FROM vehicles").fetchall()
        
    # Signature: str -> list[tuple]
    # Purpose: Finds the records by vehicle id or type
    def search(self, keyword: str) -> list[tuple]:
        with self.conn:
            return self.conn.execute(
                "SELECT * FROM vehicles WHERE vehicle_id LIKE ? OR vehicle_type LIKE ?",
                (f"%{keyword}%", f"%{keyword}%")
            ).fetchall()
        
    # Signature: str -> tuple OR None
    # Purpose: Lets users view a specific entry
    def fetch_by_id(self, record_id: str) -> tuple | None:
        with self.conn:
            return self.conn.execute(
                "SELECT * FROM vehicles WHERE vehicle_id = ?", (record_id,)
            ).fetchone()
        
    # Signature: int -> None
    # Purpose: Lets the user remove a saved vehicle 
    def delete(self, record_id: str) -> None:
        with self.conn:
            self.conn.execute("DELETE FROM vehicles WHERE vehicle_id = ?", (record_id,))

    # Signature: None -> None
    # Purpose: Lets the user remove ALL vehicles
    def delete_all(self) -> None:
        with self.conn:
            self.conn.execute("DELETE FROM vehicles")

# --------------------------------------------------- PYTESTS ---------------------------------------------------

def test_insert() -> None:
    db = Database()
    db.insert(id='B101', type='Bus', long=100.00, lat=100.00, status='On Time')
    
    result = db.fetch_by_id('B101')
    assert result is not None
    assert result[0] == 'B101'
    assert result[1] == 'Bus'
    assert result[2] == 100.00
    assert result[3] == 100.00
    assert result[4] == 'On Time'

def test_delete_all() -> None: 
    db = Database()
    db.insert(id='T22', type='Train', long=100.00, lat=100.00, status='On Time')
    db.delete_all()

    all_vehicles = db.fetch_all()
    assert len(all_vehicles) == 0

def test_fetch_all() -> None:
    db = Database()
    db.delete_all()
    db.insert(id='U991', type='Uber', long=59.20, lat=46.00, status='Delayed')
    all_vehicles = db.fetch_all()

    assert len(all_vehicles) == 1
    assert all_vehicles[0][0] == 'U991'

    
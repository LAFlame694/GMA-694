import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "garage.db")

def connect_db():
    return sqlite3.connect(DB_PATH)

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    # Users table (id, username, password, role, active)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password BLOB NOT NULL,
            role TEXT NOT NULL,
            active INTEGER DEFAULT 1
        )
    """)

    # Vehicles table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vehicles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plate_number TEXT NOT NULL,
            owner_name TEXT NOT NULL,
            phone TEXT NOT NULL,
            model TEXT NOT NULL
        )
    """)

    # Jobs table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vehicle_id INTEGER,
            description TEXT,
            mechanic_id INTEGER,
            status TEXT,
            FOREIGN KEY(vehicle_id) REFERENCES vehicles(id),
            FOREIGN KEY(mechanic_id) REFERENCES users(id)
        )
    """)

    # Parts table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS parts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    """)

    # Invoices table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS invoices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vehicle_id INTEGER,
            total REAL,
            status TEXT,
            created_at TEXT,
            FOREIGN KEY(vehicle_id) REFERENCES vehicles(id)
        )
    """)

    # Payments table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            invoice_id INTEGER,
            amount REAL,
            payment_date TEXT,
            FOREIGN KEY(invoice_id) REFERENCES invoices(id)
        )
    """)

    conn.commit()

    # Migration: ensure 'active' column exists on users (for older DBs)
    try:
        cursor.execute("SELECT active FROM users LIMIT 1")
    except sqlite3.OperationalError:
        # column doesn't exist -> add it
        try:
            cursor.execute("ALTER TABLE users ADD COLUMN active INTEGER DEFAULT 1")
            conn.commit()
        except sqlite3.OperationalError:
            # If alter fails for any reason, ignore (table may be in odd state)
            pass

    conn.close()

from database.db import connect_db

def migrate():
    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute("ALTER TABLE parts ADD COLUMN active INTEGER DEFAULT 1")
        conn.commit()
        print("'active' column added to parts table")
    except Exception as e:
        print("Migration skipped:", e)
    
    conn.close()
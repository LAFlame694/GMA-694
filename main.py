from database.db import connect_db, create_tables
from ui.login_ui import open_login
from services.auth_service import hash_password

# -------------------------
# Setup database and tables
# -------------------------
create_tables()

# -------------------------
# Create default users (only once)
# -------------------------
def create_default_users():
    conn = connect_db()
    cursor = conn.cursor()

    users = [
        ("admin", "admin123", "admin"),
        ("mechanic1", "1234", "mechanic"),
        ("cashier1", "1234", "cashier"),
    ]

    for username, password, role in users:
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        if not user:
            hashed_password = hash_password(password)
            cursor.execute(
                "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                (username, hashed_password, role)
            )

    conn.commit()
    conn.close()

create_default_users()

# -------------------------
# Start the app
# -------------------------
if __name__ == "__main__":
    open_login()

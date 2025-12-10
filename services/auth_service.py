# services/auth_service.py
import bcrypt
from database.db import connect_db

def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def verify_password(password: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(password.encode(), hashed)

def login_user(username: str, password: str):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id, password, role, active FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user:
        user_id, hashed_password, role, active = user
        # only allow login if active == 1
        if active != 1:
            return None
        if verify_password(password, hashed_password):
            return {"id": user_id, "role": role}
    return None

# ------------------------
# New helper functions
# ------------------------
def create_user(username: str, password: str, role: str) -> bool:
    """Creates a new user. Returns True on success, False if username exists or error."""
    try:
        conn = connect_db()
        cursor = conn.cursor()
        hashed = hash_password(password)
        cursor.execute(
            "INSERT INTO users (username, password, role, active) VALUES (?, ?, ?, ?)",
            (username, hashed, role, 1)
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        # Could be UNIQUE constraint violation; return False
        return False

def list_users():
    """Returns list of users as tuples (id, username, role, active)."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, role, active FROM users ORDER BY id")
    rows = cursor.fetchall()
    conn.close()
    return rows

def set_user_active(user_id: int, active: int) -> bool:
    """Set active to 1 or 0. Returns True on success."""
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET active = ? WHERE id = ?", (1 if active else 0, user_id))
        conn.commit()
        conn.close()
        return True
    except Exception:
        return False

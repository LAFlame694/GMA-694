from database.db import connect_db

def add_part(name: str, quantity: int, price: float) -> bool:
    """Add a new part to inventory."""
    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO parts (name, quantity, price, active)
            VALUES (?, ?, ?, 1)
        """, (name, quantity, price)
        )

        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print("Add part error:", e)
        return False

def list_parts(include_inactive: bool = False):
    """Return all parts. Active only  by default."""
    conn = connect_db()
    cursor = conn.cursor()

    if include_inactive:
        cursor.execute("""
            SELECT id, name, quantity, price, active
            FROM parts
            ORDER BY name
        """)
    else:
        cursor.execute("""
            SELECT id, name, quantity, price, active
            FROM parts
            WHERE active = 1
            ORDER BY name
        """)
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_part(part_id: int, name: str, quantity: int, price: float) -> bool:
    """Update part details (admin only)"""
    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE parts
            SET name = ?, quantity = ?, price = ?
            WHERE id = ?
        """, (name, quantity, price, part_id)
        )

        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print("Update part error:", e)
        return False
    
def set_part_actve(part_id: int, active: int) -> bool:
    """Active / Deactivate a part"""
    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE parts
            SET active = ?
            WHERE id = ?
        """, (1 if active else 0, part_id)
        )

        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print("Set part active error:", e)
        return False
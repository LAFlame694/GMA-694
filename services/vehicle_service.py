from database.db import connect_db
from typing import List, Tuple, Optional

def create_vehicle(plate_number: str, owner_name: str, phone: str, model: str) -> bool:
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO vehicles (plate_number, owner_name, phone, model) VALUES (?, ?, ?, ?)",
            (plate_number.strip(), owner_name.strip(), phone.strip(), model.strip())
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        return False

def list_vehicles() -> List[Tuple]:
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, plate_number, owner_name, phone, model FROM vehicles ORDER BY id")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_vehicle(vehicle_id: int) -> Optional[Tuple]:
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, plate_number, owner_name, phone, model FROM vehicles WHERE id = ?", (vehicle_id,))
    row = cursor.fetchone()
    conn.close()
    return row

def update_vehicle(vehicle_id: int, plate_number: str, owner_name: str, phone: str, model: str) -> bool:
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE vehicles SET plate_number = ?, owner_name = ?, phone = ?, model = ? WHERE id = ?",
            (plate_number.strip(), owner_name.strip(), phone.strip(), model.strip(), vehicle_id)
        )
        conn.commit()
        conn.close()
        return True
    except Exception:
        return False

def delete_vehicle(vehicle_id: int) -> bool:
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM vehicles WHERE id = ?", (vehicle_id,))
        conn.commit()
        conn.close()
        return True
    except Exception:
        return False
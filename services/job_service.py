from database.db import connect_db

def create_job(vehicle_id: int, description: str) -> bool:
    try:
        conn =connect_db()
        cursor = conn.cursor()

        cursor.execute("""
                INSERT INTO jobs (vehicle_id, description, status)
                VALUES (?, ?, ?)
                """, (vehicle_id, description, "pending")
        )

        conn.commit()
        conn.close()
        return True
    except Exception:
        return False

def list_jobs():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            jobs.id,
            vehicles.plate_number,
            jobs.description,
            jobs.status
        FROM jobs
        JOIN vehicles ON jobs.vehicle_id = vehicles.id
        ORDER BY jobs.id DESC
        """
    )

    rows = cursor.fetchall()
    conn.close()
    return rows
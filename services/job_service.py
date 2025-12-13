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

# job assignment
def assign_mechanic(job_id: int, mechanic_id: int) -> bool:
    """Assign a mechanic to a job (Admin only)."""
    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE jobs
            SET mechanic_id = ?, status = 'Assigned'
            WHERE id = ?
            """, (mechanic_id, job_id)
        )

        conn.commit()
        conn.close()
        return True
    
    except Exception as e:
        print("Error assigning mechanic", e)
        return False

def get_mechanics():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id, username FROM users WHERE role = 'mechanic' AND active = 1")
    rows = cursor.fetchall()

    conn.close()
    return rows

def get_jobs_for_mechanic(mechanic_id: int):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT jobs.id, vehicles.plate_number, jobs.description, jobs.status
        FROM jobs
        JOIN vehicles ON jobs.vehicle_id = vehicles.id
        WHERE mechanic_id = ?
        ORDER BY jobs.id DESC
    """, (mechanic_id,))

    rows = cursor.fetchall()
    conn.close()
    return rows


def update_job_status(job_id: int, status: str) -> bool:
    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("UPDATE jobs SET status = ? WHERE id = ?", (status, job_id))

        conn.commit()
        conn.close()
        return True
    except:
        return False
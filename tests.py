def add_part_to_job(job_id: int, part_id: int, quantity: int) -> bool:
    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO job_parts_used (job_id, part_id, quantity)
            VALUES (?, ?, ?)
        """, (job_id, part_id, quantity))

        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print("Error adding part to job:", e)
        return False


def get_parts_used_for_job(job_id: int):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            inventory.id,
            inventory.name,
            job_parts_used.quantity,
            inventory.price
        FROM job_parts_used
        JOIN inventory ON job_parts_used.part_id = inventory.id
        WHERE job_parts_used.job_id = ?
    """, (job_id,))

    rows = cursor.fetchall()
    conn.close()
    return rows

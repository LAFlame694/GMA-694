from database.db import connect_db

def calculate_job_total(job_id: int) -> float:
    """Calculates total cost of a job from job_parts."""
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(quantity * unit_price)
        FROM job_parts
        WHERE job_id = ?
    """, (job_id,))

    result = cursor.fetchone()
    conn.close()

    return result[0] if result[0] is not None else 0.0

def create_invoice(job_id: int) -> int | None:
    if invoice_exists_for_job(job_id):
        return None # prevent duplicates
    
    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT vehicle_id FROM jobs WHERE id = ?", (job_id,))
        row = cursor.fetchone()
        if not row:
            conn.close()
            return None
        
        vehicle_id = row[0]
        total = calculate_job_total(job_id)

        cursor.execute("""
            INSERT INTO invoices (job_id, vehicle_id, total, status, created_at)
            VALUES (?, ?, ?, 'Pending', datetime('now'))
        """, (job_id, vehicle_id, total)
        )

        invoice_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return invoice_id
    
    except Exception as e:
        print("Invoice creation error:", e)
        return None
    
def get_invoice(invoice_id: int):
    """Returns invoice details including job & vehicle info."""
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            invoices.id,
            invoices.job_id,
            vehicles.plate_number,
            invoices.total,
            invoices.status,
            invoices.created_at
        FROM invoices
        JOIN vehicles ON invoices.vehicle_id = vehicles.id
        WHERE invoices.id = ?
    """, (invoice_id,))

    row = cursor.fetchone()
    conn.close()
    return row

def update_invoice_status(invoice_id: int, status: str) -> bool:
    """Updates invoice payment status."""
    if status not in ("Pending", "Partial", "Paid"):
        return False
    
    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE invoices
            SET status = ?
            WHERE id = ?
        """, (status, invoice_id))

        conn.commit()
        conn.close()
        return True
    
    except Exception as e:
        print("Invoice status update error:", e)
        return False

def get_invoice_details(job_id: int):
    conn = connect_db()
    cursor = conn.cursor()

    # job + vehicle info
    cursor.execute("""
        SELECT 
            jobs.id,
            vehicles.plate_number,
            jobs.description,
            jobs.status
        FROM jobs
        JOIN vehicles ON jobs.vehicle_id = vehicles.id
        WHERE jobs.id = ?
    """, (job_id,)
    )
    job = cursor.fetchone()

    # parts used
    cursor.execute("""
        SELECT
            parts.name,
            job_parts.quantity,
            job_parts.unit_price,
            (job_parts.quantity * job_parts.unit_price) AS total
        FROM job_parts
        JOIN parts ON job_parts.part_id = parts.id
        WHERE job_parts.job_id = ?
    """, (job_id,)
    )
    parts = cursor.fetchall()

    conn.close()
    return job, parts

def invoice_exists_for_job(job_id: int) -> bool:
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM invoices WHERE job_id = ?",
        (job_id,)
    )

    row = cursor.fetchone()
    conn.close()

    return row is not None

def list_invoices():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            invoices.id,
            vehicles.plate_number,
            invoices.total,
            invoices.status,
            invoices.created_at
        FROM invoices
        JOIN vehicles ON invoices.vehicle_id = vehicles.id
        ORDER BY invoices.created_at DESC
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows

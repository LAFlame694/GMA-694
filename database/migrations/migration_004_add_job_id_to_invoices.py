from database.db import connect_db

MIGRATION_NAME = "004_add_job_id_to_invoices"

def migrate():
    conn = connect_db()
    cursor = conn.cursor()

    # Check if column already exists
    cursor.execute("PRAGMA table_info(invoices)")
    columns = [col[1] for col in cursor.fetchall()]

    if "job_id" not in columns:
        cursor.execute("""
            ALTER TABLE invoices
            ADD COLUMN job_id INTEGER
        """)
        conn.commit()

    conn.close()

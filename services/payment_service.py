from database.db import connect_db

# add payment + recalculate invoice
def add_payment(invoice_id: int, amount: float):
    conn = connect_db()
    cursor = conn.cursor()

    # insert payment
    cursor.execute("""
        INSERT INTO payments (invoice_id, amount, payment_date)
        VALUES (?, ?, datetime('now'))
    """, (invoice_id, amount)
    )

    # total paid
    cursor.execute("""
        SELECT IFNULL(SUM(amount), 0)
        FROM payments
        WHERE invoice_id = ?
    """, (invoice_id,)
    )
    paid_total = cursor.fetchone()[0]

    # invoice total
    cursor.execute("""
        SELECT total
        FROM invoices
        WHERE id = ?
    """, (invoice_id,)
    )

    invoice_total = cursor.fetchone()[0]

    balance = invoice_total - paid_total

    status = "PAID" if balance <= 0 else "PARTIAL"
    if paid_total == 0:
        status = "PENDING"

    cursor.execute("""
        UPDATE invoices
        SET status = ?
        WHERE id = ?
    """, (status, invoice_id)
    )

    conn.commit()
    conn.close()

    return paid_total, balance, status

# fetch payments for receipt
def get_payments_for_invoice(invoice_id: int):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT amount, payment_date
        FROM payments
        WHERE invoice_id = ?
        ORDER BY payment_date
    """, (invoice_id,)
    )

    payments =  cursor.fetchall()
    conn.close()
    return payments
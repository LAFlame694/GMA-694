import tkinter as tk
from tkinter import ttk
from services.invoice_service import get_invoice_full_details
from services.payment_service import get_payments_for_invoice

def open_receipt_window(invoice_id: int):
    invoice, parts = get_invoice_full_details(invoice_id)
    payments = get_payments_for_invoice(invoice_id)

    if not invoice:
        return
    
    (
        inv_id,
        status,
        total,
        created_at,
        job_id,
        job_desc,
        plate
    ) = invoice

    win = tk.Toplevel()
    win.title(f"Receipt - Invoice #{inv_id}")
    win.geometry("600x700")
    win.resizable(False, False)

    # === Header ===
    tk.Label(
        win,
        text="FLAME GARAGE",
        font=("Arial", 18, "bold")
    ).pack(pady=5)

    tk.Label(
        win,
        text="Official Receipt",
        font=("Arial", 12)
    ).pack()

    tk.Label(win, text="-"*60).pack(pady=5)

    # === Meta ===
    meta = (
        f"Invoice #:{inv_id}\n"
        f"Date: {created_at}\n"
        f"Vehicle: {plate}\n"
        f"Job: {job_desc}\n"
        f"Status: {status}"
    )

    tk.Label(
        win,
        text=meta,
        justify="left",
        anchor="w",
        font=('Arial', 10)
    ).pack(fill="x", padx=20)

    tk.Label(win, text="-"*60).pack(pady=5)

    # === Parts ===
    tk.Label(win, text="Parts Used", font=("Arial", 12, "bold")).pack()

    parts_frame = tk.Frame(win)
    parts_frame.pack(padx=20, fill="x")

    for name, qty, price, line_total in parts:
        tk.Label(
            parts_frame,
            text=f"{name} x{qty} @ {price:.2f} = {line_total:.2f}",
            anchor="w"
        ).pack(fill="x")

    tk.Label(win, text="-"*60).pack(pady=5)

    # === payments ===
    tk.Label(win, text="Payments", font=("Arial", 12, "bold")).pack()

    paid_total = 0
    for amount, date in payments:
        paid_total += amount
        tk.Label(
            win,
            text=f"{date} - KES {amount:.2f}",
            anchor='w'
        ).pack(fill="x", padx=20)
    
    balance = total - paid_total

    tk.Label(win, text="-"*60).pack(pady=5)

    # === Totals ===
    totals = (
        f"Total: KES {total:.2f}\n"
        f"PAID: KES {paid_total:.2f}\n"
        f"BALANCE: KES {balance:.2f}"
    )

    tk.Label(
        win,
        text=totals,
        font=("Arial", 11, "bold"),
        justify="left"
    ).pack(pady=10)

    # === Footer ===
    tk.Label(
        win,
        text="Thank you for your business",
        font=("Arial", 10, "italic")
    ).pack(pady=5)

    # === Actions ===
    btns = tk.Frame(win)
    btns.pack(pady=10)

    tk.Button(btns, text="Print", width=10).pack(side="left", padx=5)
    tk.Button(btns, text="Close", width="10", command=win.destroy).pack(side="left", padx=5)
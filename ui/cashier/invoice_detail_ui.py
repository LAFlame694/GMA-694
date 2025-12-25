import tkinter as tk
from tkinter import ttk, messagebox
from services.invoice_service import get_invoice_full_details
from services.payment_service import get_payments_for_invoice, add_payment
from ui.cashier.receipt_ui import open_receipt_window

def open_invoice_detail_window(invoice_id: int):
    invoice, parts = get_invoice_full_details(invoice_id)

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
    win.title(f"Invoice #{inv_id}")
    win.geometry("750x650")

    # Header
    tk.Label(
        win,
        text=f"Invoice #{inv_id}",
        font=("Arial", 18, "bold")
    ).pack(pady=10)

    info_frame = tk.Frame(win)
    info_frame.pack(fill="x", padx=20)

    tk.Label(info_frame, text=f"Vehicle: {plate}").pack(anchor="w")
    tk.Label(info_frame, text=f"Job: {job_desc}").pack(anchor="w")
    tk.Label(info_frame, text=f"Status: {status}").pack(anchor="w")
    tk.Label(info_frame, text=f"Created: {created_at}").pack(anchor="w")

    # parts table
    columns = ("part", "qty", "price", "total")
    tree = ttk.Treeview(win, columns=columns, show="headings")

    tree.heading("part", text="Part")
    tree.heading("qty", text="Qty")
    tree.heading("price", text="Unit Price")
    tree.heading("total", text="Total")

    tree.column("part", width=250)
    tree.column("qty", width=80, anchor="center")
    tree.column("price", width=120, anchor="e")
    tree.column("total", width=120, anchor="e")

    tree.pack(fill="both", expand=True, padx=20, pady=15)

    for name, qty, price, line_total in parts:
        tree.insert(
            "",
            "end",
            values=(name, qty, f"{price}", f"{line_total:.2f}")
        )
    
    payments = get_payments_for_invoice(invoice_id)

    ttk.Label(win, text="Payment History", font=("Segoe UI", 10, "bold")).pack(pady=5)
    for amt, date in payments:
        ttk.Label(win, text=f"{date} - KES {amt:.2f}").pack(anchor="w", padx=30)
    
    # Grand total
    tk.Label(
        win,
        text=f"Grand Total: KES {total:.2f}",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    payment_frame = ttk.LabelFrame(win, text="Payments")
    payment_frame.pack(fill="x", padx=20, pady=10)

    ttk.Label(payment_frame, text="Amount Paid").grid(row=0, column=0, padx=5, pady=5)

    amount_entry = ttk.Entry(payment_frame)
    amount_entry.grid(row=0, column=1, padx=5, pady=5)

    def process_payment():
        try:
            amount = float(amount_entry.get())
            if amount <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Enter a valid amount")
            return
        
        paid, balance, status = add_payment(invoice_id, amount)

        messagebox.showinfo(
            "Payment Recorded",
            f"Paid: {paid}\nBalance: {balance}\nStatus: {status}"
        )

        win.destroy()
        open_invoice_detail_window(invoice_id)
    
    ttk.Button(
        payment_frame,
        text="Record Payment",
        command=process_payment
    ).grid(row=1, columnspan=2, pady=10)

    ttk.Button(
        payment_frame,
        text="View Receipt",
        command=lambda: open_receipt_window(invoice_id)
    ).grid(row=2)

    tk.Button(
        win,
        text="Close",
        command=win.destroy
    ).pack(pady=10)
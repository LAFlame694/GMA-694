import tkinter as tk
from tkinter import ttk
from services.invoice_service import get_invoice_details

def open_invoice_view(job_id: int):
    job, parts = get_invoice_details(job_id)

    win = tk.Toplevel()
    win.title(f"Invoice - Job #{job_id}")
    win.geometry("700x500")

    # Header
    tk.Label(win, text="Invoice Details", font=("Arial", 16, "bold")).pack(pady=10)

    job_id, plate, desc, status = job
    tk.Label(win, text=f"Vehicle: {plate}").pack(anchor="w", padx=20)
    tk.Label(win, text=f"Job Description: {desc}").pack(anchor="w", padx=20)
    tk.Label(win, text=f"Status: {status}").pack(anchor="w", padx=20)

    # parts table
    columns = ("part", "qty", "price", "total")
    tree = ttk.Treeview(win, columns=columns, show="headings")

    tree.heading("part", text="Part")
    tree.heading("qty", text="Qty")
    tree.heading("price", text="Unit Price")
    tree.heading("total", text="Total")

    tree.pack(fill="both", expand=True, padx=20, pady=10)

    grand_total = 0
    for name, qty, price, total in parts:
        tree.insert("", "end", values=(name, qty, price, total))
        grand_total += total
    
    tk.Label(
        win,
        text=f"Grand Total: KES {grand_total:.2f}",
        font=("Arial", 14, "bold")
    ).pack(pady=10)

    tk.Button(win, text="Close", command=win.destroy).pack(pady=10)


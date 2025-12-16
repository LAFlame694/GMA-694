import tkinter as tk
from tkinter import ttk, messagebox
from services.job_service import get_completed_uninvoiced_jobs
from services.invoice_service import create_invoice
from ui.cashier.invoices_ui import open_invoice_view
from ui.cashier.invoice_list_ui import open_invoice_list_window

def open_cashier_dashboard():
    window = tk.Tk()
    window.title("Cashier Dashboard")
    window.geometry("900x600")

    tk.Label(
        window,
        text="Cashier Dashboard – Jobs Ready for Billing",
        font=("Arial", 16,  "bold")
    ).pack(pady=10)

    # Table
    tree = ttk.Treeview(
        window,
        columns=("id", "plate", "desc"),
        show="headings"
    )

    tree.heading("id", text="Job ID")
    tree.heading("plate", text="Vehicle Plate")
    tree.heading("desc", text="Job Description")

    tree.column("id", width=80, anchor="center")
    tree.column("plate", width=150)
    tree.column("desc", width=500)

    tree.pack(fill="both", expand=True, padx=10, pady=10)

    def refresh_jobs():
        for row in tree.get_children():
            tree.delete(row)

        jobs = get_completed_uninvoiced_jobs()
        for j in jobs:
            jid, plate, desc = j
            tree.insert("", "end", iid=str(jid), values=(jid, plate, desc))

    def create_invoice_for_job():
        sel = tree.selection()
        if not sel:
            messagebox.showwarning("Select Job", "Please select a job first")
            return

        job_id = int(sel[0])
        invoice_id = create_invoice(job_id)

        if invoice_id:
            messagebox.showinfo(
                "Invoice Created",
                f"Invoice #{invoice_id} created successfully"
            )
            refresh_jobs()
        else:
            messagebox.showerror("Error", "Failed to create invoice")
    
    def view_invoice():
        selected = tree.selection()

        if not selected:
            messagebox.showwarning("No Selection", "Please select a job to view its invoice.")
            return
        
        job_id = int(selected[0])
        open_invoice_view(job_id)

    # Controls
    controls = tk.Frame(window)
    controls.pack(pady=10)

    tk.Button(
        controls,
        text="Create Invoice",
        command=create_invoice_for_job,
        width=18
    ).pack(side="left", padx=5)

    tk.Button(
        controls,
        text="Refresh",
        command=refresh_jobs,
        width=12
    ).pack(side="left", padx=5)

    tk.Button(
        controls,
        text="Close",
        command=window.destroy,
        width=12
    ).pack(side="left", padx=5)

    tk.Button(
        controls, 
        text="Preview Bill", 
        command=view_invoice
    ).pack(side="left", padx=5)

    tk.Button(
        window,
        text="View Invoices",
        command=open_invoice_list_window
    ).pack(pady=5)

    refresh_jobs()
    window.mainloop()

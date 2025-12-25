import tkinter as tk
from services.invoice_service import list_invoices, get_invoice, update_invoice_status
from tkinter import messagebox
from ui.cashier.invoice_detail_ui import open_invoice_detail_window

def open_invoice_list_window():
    win = tk.Toplevel()
    win.title("Invoices")
    win.geometry("700x500")

    tk.Label(
        win, 
        text="All Invoices",
        font=("Arial", 16)
    ).pack(pady=10)

    invoices = list_invoices()

    listbox = tk.Listbox(win, width=90)
    listbox.pack(pady=10)

    for inv in invoices:
        listbox.insert(
            tk.END,
            f"ID: {inv[0]} | {inv[1]} | KES {inv[2]} | {inv[3]} | {inv[4]}"
        )
    
    def view_invoice():
        if not listbox.curselection():
            return
        
        index = listbox.curselection()[0]
        invoice_id = invoices[index][0]

        open_invoice_detail_window(invoice_id)
    
    def mark_paid():
        if not listbox.curselection():
            return
        
        index = listbox.curselection()[0]
        invoice_id = invoices[index][0]

        if update_invoice_status(invoice_id, "PAID"):
            messagebox.showinfo("Success", "Invoice marked as Paid")
            win.destroy()
            open_invoice_list_window()
        
    tk.Button(
        win,
        text="View Invoice",
        command=view_invoice
    ).pack(pady=5)

    tk.Button(
        win,
        text="Mark as Paid",
        fg="green",
        command=mark_paid
    ).pack(pady=5)


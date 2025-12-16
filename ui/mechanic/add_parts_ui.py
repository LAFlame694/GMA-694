import tkinter as tk
from tkinter import messagebox
from services.part_service import list_parts
from services.job_service import add_part_to_job, get_parts_used_for_job

def open_add_parts_window(job_id):
    win = tk.Toplevel()
    win.title("Add Parts Used")
    win.geometry("600x400")

    parts = list_parts()

    tk.Label(win, text=f"Job ID: {job_id}", font=("Arial", 14)).pack(pady=5)

    part_var = tk.StringVar()
    part_menu = tk.OptionMenu(
        win,
        part_var,
        *[f"{p[0]} - {p[1]}" for p in parts]
    )
    part_menu.pack(pady=5)

    qty_entry = tk.Entry(win)
    qty_entry.pack(pady=5)
    qty_entry.insert(0, "Quantity")

    def add_part():
        try:
            part_id = int(part_var.get().split(" - ")[0])
            qty = int(qty_entry.get())

            success = add_part_to_job(job_id, part_id, qty)
            if success:
                messagebox.showinfo("Success", "Part added")
                refresh_parts()
            else:
                messagebox.showerror("Error", "Failed to add part")

        except Exception:
            messagebox.showerror("Error", "Invalid input")

    tk.Button(win, text="Add Part", command=add_part).pack(pady=5)

    parts_list = tk.Listbox(win, width=60)
    parts_list.pack(pady=10)

    def refresh_parts():
        parts_list.delete(0, tk.END)
        used = get_parts_used_for_job(job_id)
        for p in used:
            parts_list.insert(
                tk.END, 
                f"Item ID: {p[0]} | Name: {p[1]} | Qty: {p[2]} | Price: {p[3]} | Total: {p[4]}"
            )

    refresh_parts()

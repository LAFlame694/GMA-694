import tkinter as tk
from tkinter import ttk, messagebox
from services.part_service import add_part, list_parts, update_part, set_part_active

def open_inventory_ui():
    window = tk.Tk()
    window.title("Inventory Management")
    window.geometry("800x450")

    tk.Label(
        window,
        text="Inventory (Parts)",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    # parts table
    tree = ttk.Treeview(
        window,
        columns=("id", "name", "qty", "price", "status"),
        show="headings"
    )

    tree.heading("id", text="ID")
    tree.heading("name", text="Part Name")
    tree.heading("qty", text="Quantity")
    tree.heading("price", text="Unit Price")
    tree.heading("status", text='Status')

    tree.column("id", width=60, anchor="center")
    tree.column("name", width=220)
    tree.column("qty", width=100, anchor="center")
    tree.column("price", width=120, anchor="center")
    tree.column("status", width=100, anchor="center")

    tree.pack(fill="both", expand=True, padx=10, pady=10)

    # load parts
    def refresh_parts():
        for i in tree.get_children():
            tree.delete(i)
        
        rows = list_parts()
        for r in rows:
            pid, name, qty, price, active = r
            status = "Active" if active == 1 else "Inactive"
            tree.insert("", "end", values=(pid, name, qty, price, status))
        
    # Add Part Dialog
    def add_part_dialog():
        dialog = tk.Toplevel(window)
        dialog.title("Add Part")
        dialog.geometry("300x260")

        tk.Label(dialog, text="part Name").pack(pady=5)
        name_e = tk.Entry(dialog)
        name_e.pack()

        tk.Label(dialog, text="Quantity").pack(pady=5)
        qty_e = tk.Entry(dialog)
        qty_e.pack()

        tk.Label(dialog, text="Unit Price").pack(pady=5)
        price_e = tk.Entry(dialog)
        price_e.pack()

        def save():
            name = name_e.get().strip()
            qty = qty_e.get().strip()
            price = price_e.get().strip()

            if not name or not qty or not price:
                messagebox.showerror("Error", "All fields are required")
                return
            
            try:
                qty = int(qty)
                price = float(price)
            except ValueError:
                messagebox.showerror("Error", "Quantity and price must be numbrs")
                return
            
            ok = add_part(name, qty, price)
            if ok:
                messagebox.showinfo("Success", "Part added successfully")
                dialog.destroy()
                refresh_parts()
            else:
                messagebox.showerror("Error", "Failed to add part")
        
        tk.Button(dialog, text="Save", command=save).pack(pady=10)
        tk.Button(dialog, text="Cancel", command=dialog.destroy).pack()

    def edit_part_dialog():
        sel = tree.selection()
        if not sel:
            messagebox.showwarning("Select Part", "Please select a part first")
            return
        
        values = tree.item(sel[0])["values"]
        part_id, name, qty, price, status = values

        dialog =  tk.Toplevel(window)
        dialog.title("Edit Part")
        dialog.geometry("300x260")

        tk.Label(dialog, text="Part Name").pack(pady=5)
        name_e = tk.Entry(dialog)
        name_e.insert(0, name)
        name_e.pack()

        tk.Label(dialog, text="Quantity").pack(pady=5)
        qty_e = tk.Entry(dialog)
        qty_e.insert(0, qty)
        qty_e.pack()

        tk.Label(dialog, text="Unit Price").pack(pady=5)
        price_e = tk.Entry(dialog)
        price_e.insert(0, price)
        price_e.pack()

        def save():
            try:
                new_name = name_e.get().strip()
                new_qty = qty_e.get().strip()
                new_price = float(price_e.get())
            except  ValueError:
                messagebox.showerror("Error", "Quantity and price must be numbers")
                return
            
            ok = update_part(part_id, new_name, new_qty, new_price)
            if ok:
                messagebox.showinfo("Success", "Part updated")
                dialog.destroy()
                refresh_parts()
            else:
                messagebox.showerror("Error", "Update failed")

        tk.Button(dialog, text="Save", command=save).pack(pady=10)
        tk.Button(dialog, text="Cancel", command=dialog.destroy).pack()

    def toggle_part_active():
        sel = tree.selection()
        if not sel:
            messagebox.showwarning("Select Part", "Please select a part first")
            return
        
        values = tree.item(sel[0])["values"]
        part_id = values[0]
        status = values[4]
        
        new_active = 0 if status == "Active" else 1
        ok = set_part_active(part_id, new_active)

        if ok:
            refresh_parts()
        else:
            messagebox.showerror("Error", "Failed to update status")
    
    # controls
    controls = tk.Frame(window)
    controls.pack(pady=5)

    tk.Button(controls, text="Add Part", width=15, command=add_part_dialog).pack(side="left", padx=5)
    tk.Button(controls, text="Edit Part", width=15, command=edit_part_dialog).pack(side="left", padx=5)
    tk.Button(controls, text="Activate / Deactivate", width=20, command=toggle_part_active).pack(side="left", padx=5)
    tk.Button(controls, text="Refresh", width=12, command=refresh_parts).pack(side="left", padx=5)
    tk.Button(controls, text="Close", width=12, command=window.destroy).pack(side="left", padx=5)

    refresh_parts()
    window.mainloop()


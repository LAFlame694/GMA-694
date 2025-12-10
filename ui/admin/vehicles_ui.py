import tkinter as tk
from tkinter import ttk, messagebox
from services.vehicle_service import list_vehicles, create_vehicle, update_vehicle, delete_vehicle, get_vehicle

def open_vehicles_ui():
    def refresh_vehicles():
        for row in tree.get_children():
            tree.delete(row)
        rows = list_vehicles()
        for r in rows:
            vid, plate, owner, phone, model = r
            tree.insert("", "end", iid=str(vid), values=(vid, plate, owner, phone, model))

    def add_vehicle_dialog():
        dialog = tk.Toplevel(window)
        dialog.title("Add Vehicle")
        dialog.geometry("360x300")

        tk.Label(dialog, text="Plate Number").pack(pady=5)
        plate_e = tk.Entry(dialog)
        plate_e.pack()

        tk.Label(dialog, text="Owner Name").pack(pady=5)
        owner_e = tk.Entry(dialog)
        owner_e.pack()

        tk.Label(dialog, text="Phone").pack(pady=5)
        phone_e = tk.Entry(dialog)
        phone_e.pack()

        tk.Label(dialog, text="Model").pack(pady=5)
        model_e = tk.Entry(dialog)
        model_e.pack()

        def on_add():
            plate = plate_e.get().strip()
            owner = owner_e.get().strip()
            phone = phone_e.get().strip()
            model = model_e.get().strip()

            if not plate or not owner or not phone or not model:
                messagebox.showerror("Error", "All fields are required")
                return
            
            ok = create_vehicle(plate, owner, phone, model)

            if ok:
                messagebox.showinfo("Success", "Vehicle added")
                dialog.destroy()
                refresh_vehicles()
            else:
                messagebox.showerror("Error", "Failed to add vehicle")
        
        tk.Button(dialog, text="Add", command=on_add).pack(pady=10)
        tk.Button(dialog, text="Cancel", command=dialog.destroy).pack()

    def edit_vehicle_dialog():
        sel = tree.selection()
        if not sel:
            messagebox.showwarning("Select vehicle", "Please select a vehicle first")
            return
        vid = int(sel[0])
        data = get_vehicle(vid)
        if not data:
            messagebox.showerror("Error", "Vehicle not found")
            return
        
        _, plate_val, owner_val, phone_val, model_val = data

        dialog = tk.Toplevel(window)
        dialog.title("Edit Vehicle")
        dialog.geometry("360x320")

        tk.Label(dialog, text="Plate Number").pack(pady=5)
        plate_e = tk.Entry(dialog)
        plate_e.insert(0, plate_val)
        plate_e.pack()

        tk.Label(dialog, text="Owner Name").pack(pady=5)
        owner_e = tk.Entry(dialog)
        owner_e.insert(0, owner_val)
        owner_e.pack()

        tk.Label(dialog, text="Phone").pack(pady=5)
        phone_e = tk.Entry(dialog)
        phone_e.insert(0, phone_val)
        phone_e.pack()

        tk.Label(dialog, text="Model").pack(pady=5)
        model_e = tk.Entry(dialog)
        model_e.insert(0, model_val)
        model_e.pack()

        def on_update():
            plate = plate_e.get().strip()
            owner = owner_e.get().strip()
            phone = phone_e.get().strip()
            model = model_e.get().strip()
            if not plate or not owner or not phone or not model:
                messagebox.showerror("Error", "All fields are required")
                return
            ok = update_vehicle(vid, plate, owner, phone, model)
            if ok:
                messagebox.showinfo("Success", "Vehicle updated")
                dialog.destroy()
                refresh_vehicles()
            else:
                messagebox.showerror("Error", "Failed to update vehicle")

        tk.Button(dialog, text="Update", command=on_update).pack(pady=10)
        tk.Button(dialog, text="Cancel", command=dialog.destroy).pack()

    def delete_vehicle_action():
        sel = tree.selection()
        if not sel:
            messagebox.showwarning("Select vehicle", "Please select a vehicle first")
            return
        vid = int(sel[0])
        confirm = messagebox.askyesno("Confirm", "Delete selected vehicle?")
        if not confirm:
            return
        ok = delete_vehicle(vid)
        if ok:
            messagebox.showinfo("Deleted", "Vehicle deleted")
            refresh_vehicles()
        else:
            messagebox.showerror("Error", "Failed to delete vehicle")

    window = tk.Tk()
    window.title("Manage Vehicles")
    window.geometry("900x500")

    frame = tk.Frame(window)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    tree = ttk.Treeview(frame, columns=("id", "plate", "owner", "phone", "model"), show="headings", selectmode="browse")
    tree.heading("id", text="ID")
    tree.heading("plate", text="Plate")
    tree.heading("owner", text="Owner")
    tree.heading("phone", text="Phone")
    tree.heading("model", text="Model")
    tree.column("id", width=50, anchor="center")
    tree.column("plate", width=150)
    tree.column("owner", width=200)
    tree.column("phone", width=120)
    tree.column("model", width=200)
    tree.pack(fill="both", expand=True, side="left")

    vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=vsb.set)
    vsb.pack(side="left", fill="y")

    controls = tk.Frame(window)
    controls.pack(pady=10)

    tk.Button(controls, text="Add Vehicle", command=add_vehicle_dialog, width=15).pack(side="left", padx=5)
    tk.Button(controls, text="Edit Vehicle", command=edit_vehicle_dialog, width=15).pack(side="left", padx=5)
    tk.Button(controls, text="Delete Vehicle", command=delete_vehicle_action, width=15).pack(side="left", padx=5)
    tk.Button(controls, text="Refresh", command=refresh_vehicles, width=12).pack(side="left", padx=5)
    tk.Button(controls, text="Close", command=window.destroy, width=12).pack(side="left", padx=5)

    refresh_vehicles()
    window.mainloop()


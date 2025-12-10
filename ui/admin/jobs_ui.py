import tkinter as tk
from tkinter import ttk, messagebox
from services.job_service import create_job, list_jobs
from services.vehicle_service import list_vehicles

def open_jobs_ui():
    def refresh_jobs():
        for row in tree.get_children():
            tree.delete(row)
        rows = list_jobs()
        for r in rows:
            jid, plate, desc, status = r
            tree.insert("", "end", iid=str(jid), values=(jid, plate, desc, status))

    def add_job_dialog():
        dialog = tk.Toplevel(window)
        dialog.title("Create Job")
        dialog.geometry("350x260")

        tk.Label(dialog, text="Select Vehicle").pack(pady=5)

        vehicles = list_vehicles()
        vehicle_map = {f"{v[1]} - {v[2]}": v[0] for v in vehicles}

        vehicle_cb = ttk.Combobox(dialog, values=list(vehicle_map.keys()))
        vehicle_cb.pack()

        tk.Label(dialog, text="Problem / Service Description").pack(pady=5)
        desc_e = tk.Text(dialog, height=4)
        desc_e.pack()

        def on_create():
            selected = vehicle_cb.get()
            desc = desc_e.get("1.0", tk.END).strip()

            if not selected or not desc:
                messagebox.showerror("Error", "All fields are required")
                return
            
            vehicle_id = vehicle_map[selected]
            ok = create_job(vehicle_id, desc)

            if ok:
                messagebox.showinfo("Success", "Job created")
                dialog.destroy()
                refresh_jobs()
            else:
                messagebox.showerror("Error", "Failed to create job")
        
        tk.Button(dialog, text="Create Job", command=on_create).pack(pady=10)
        tk.Button(dialog, text="Cancel", command=dialog.destroy).pack()

    window = tk.Tk()
    window.title("Manage Jobs")
    window.geometry("850x450")

    tree = ttk.Treeview(window, columns=("id", "plate", "desc", "status"), show="headings")
    tree.heading("id", text="ID")
    tree.heading("plate", text="Vehicle Plate")
    tree.heading("desc", text="Description")
    tree.heading("status", text="Status")
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    controls = tk.Frame(window)
    controls.pack(pady=5)

    tk.Button(controls, text="Create Job", command=add_job_dialog).pack(side="left", padx=5)
    tk.Button(controls, text="Refresh", command=refresh_jobs).pack(side="left", padx=5)
    tk.Button(controls, text="Close", command=window.destroy).pack(side="left", padx=5)

    refresh_jobs()
    window.mainloop()
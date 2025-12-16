import tkinter as tk
from tkinter import ttk, messagebox
from services.job_service import get_jobs_for_mechanic, update_job_status
from ui.mechanic.add_parts_ui import open_add_parts_window

def open_my_jobs_window(mechanic_id):
    win = tk.Toplevel()
    win.title("My Jobs")
    win.geometry("900x500")

    tk.Label(
        win,
        text="Jobs Assigened to Me",
        font=("Arial", 16)
    ).pack(pady=10)

    tree = ttk.Treeview(
        win,
        columns=("id","plate", "desc", "status"),
        show="headings"
    )

    tree.heading("id", text="Job ID")
    tree.heading("plate", text="Plate")
    tree.heading("desc", text="Description")
    tree.heading("status", text="Status")

    tree.column("id", width=80, anchor="center")
    tree.column("plate", width=120)
    tree.column("desc", width=400)
    tree.column("status", width=120, anchor="center")

    tree.pack(fill="both", expand=True, padx=10, pady=10)

    jobs = get_jobs_for_mechanic(mechanic_id)
    for job_id, plate, desc, status in jobs:
        tree.insert("", "end", iid=str(job_id), 
                    values=(job_id, plate, desc, status))
    
    def add_parts():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("No selection", "Select a job first")
            return

        job_id = int(selected[0])  # iid = job_id
        open_add_parts_window(job_id)

    controls = tk.Frame(win)
    controls.pack(pady=10)

    tk.Button(controls, text="Add Parts Used", command=add_parts).pack(side="left", padx=5)

def open_update_job_window(mechanic_id):
    win = tk.Toplevel()
    win.title("Update Job Status")
    win.geometry("400x250")

    tk.Label(win, text="Update Job Status", font=("Arial", 16)).pack(pady=10)

    job_id_entry = tk.Entry(win)
    job_id_entry.pack(pady=5)
    job_id_entry.insert(0, "Job ID")

    status_var = tk.StringVar(value="In Progress")
    tk.OptionMenu(win, status_var, "In Progress", "Completed").pack(pady=5)

    def save_status():
        job_id = int(job_id_entry.get())
        status = status_var.get()
        update_job_status(job_id, status)
        tk.Label(win, text="Status Updated!", fg="green").pack()

    tk.Button(win, text="Save", command=save_status).pack(pady=10)

def open_mechanic_dashboard(mechanic_id):
    window = tk.Tk()
    window.title("Mechanic Dashboard")
    window.geometry("900x600")

    tk.Label(window, text="Mechanic Dashboard", font=("Arial", 20)).pack(pady=20)

    tk.Button(
        window,
        text="My Jobs",
        command=lambda: open_my_jobs_window(mechanic_id)
    ).pack(pady=5)

    tk.Button(
        window,
        text="Update Job",
        command=lambda: open_update_job_window(mechanic_id)
    ).pack(pady=5)

    tk.Button(window, text="Logout", fg="red", command=window.destroy).pack(pady=20)

    window.mainloop()

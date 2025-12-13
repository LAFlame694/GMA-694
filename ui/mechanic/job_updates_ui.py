import tkinter as tk
from tkinter import ttk, messagebox
from turtledemo.tree import tree

from services.job_service import get_jobs_for_mechanic, update_job_status

def open_mechanic_jobs_ui(mechanic_id: int):
    window = tk.Tk()
    window.title("My Assigned Jobs")
    window.geometry("900x450")

    tk.Label(window, text=f"Mechanic Dashboard - My Jobs", font=("Arial", 14, "bold")).pack(pady=10)

    # Table
    tree = ttk.Treeview(window, columns=("id", "plate", "desc", "status"), show="headings")

    tree.heading("id", text="Job ID")
    tree.heading("plate", text="Vehicle Plate")
    tree.heading("desc", text="Description")
    tree.heading("status", text="Status")

    tree.column("id", width=80, anchor="center")
    tree.column("plate", width=150)
    tree.column("desc", width=450)
    tree.column("status", width=120, anchor="center")

    tree.pack(fill="both", expand=True, padx=10, pady=10)

    # Load jobs for this mechanic
    def refresh_jobs():
        for i in tree.get_children():
            tree.delete(i)

        rows = get_jobs_for_mechanic(mechanic_id)
        for r in rows:
            jid, plate, desc, status = r
            tree.insert("", "end", iid=str(jid), values=(jid, plate, desc, status))

    # Update status
    def open_update_status():
        sel = tree.selection()
        if not sel:
            messagebox.showwarning("No Selection", "Please select a job first")
            return

        job_id = int(sel[0])

        status_win = tk.Toplevel(window)
        status_win.title("Update Job Status")
        status_win.geometry("300x200")

        tk.Label(status_win, text=f"Update Status for Job #{job_id}", font=("Arial", 12)).pack(pady=10)

        status_cb = ttk.Combobox(
            status_win,
            values=["Pending", "In Progress", "Completed"],
            width=18
        )
        status_cb.current(1)
        status_cb.pack(pady=10)

        def save_status():
            new_status = status_cb.get()
            ok = update_job_status(job_id, new_status)

            if ok:
                messagebox.showinfo("Success", "Job status updated!")
                status_win.destroy()
                refresh_jobs()
            else:
                messagebox.showerror("Error", "Could not update job status")

        tk.Button(status_win, text="Save", command=save_status).pack(pady=10)
        tk.Button(status_win, text="Close", command=status_win.destroy).pack()

    # controls
    controls = tk.Frame(window)
    controls.pack(pady=5)

    tk.Button(controls, text="Update Status", command=open_update_status).pack(side="left", padx=5)
    tk.Button(controls, text="Refresh", command=refresh_jobs).pack(side="left", padx=5)
    tk.Button(controls, text="Close", command=window.destroy).pack(side="left", padx=5)

    refresh_jobs()
    window.mainloop()




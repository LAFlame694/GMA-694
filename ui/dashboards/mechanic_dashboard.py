import tkinter as tk
from services.job_service import get_jobs_for_mechanic, update_job_status

def open_my_jobs_window(mechanic_id):
    jobs = get_jobs_for_mechanic(mechanic_id)

    win = tk.Toplevel()
    win.title("My Jobs")
    win.geometry("700x500")

    tk.Label(win, text="Jobs Assigned to Me", font=("Arial", 16)).pack(pady=10)

    for job_id, plate, desc, status in jobs:
        tk.Label(
            win,
            text=f"{job_id} | {plate} | {desc} | {status}",
            anchor="w"
        ).pack(fill="x")

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

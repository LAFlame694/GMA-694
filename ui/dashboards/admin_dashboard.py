# ui/dashboards/admin_dashboard.py
import tkinter as tk
from ui.admin.users_ui import open_users_ui
from ui.admin.vehicles_ui import open_vehicles_ui
from ui.admin.jobs_ui import open_jobs_ui

def open_admin_dashboard():
    window = tk.Tk()
    window.title("Admin Dashboard")
    window.geometry("900x600")

    tk.Label(window, text="Admin Dashboard", font=("Arial", 20)).pack(pady=20)

    tk.Button(window, text="Users", width=25, command=open_users_ui).pack(pady=5)
    tk.Button(window, text="Vehicles", width=25, command=open_vehicles_ui).pack(pady=5)
    tk.Button(window, text="Jobs", width=25, command=open_jobs_ui).pack(pady=5)
    tk.Button(window, text="Inventory", width=25).pack(pady=5)
    tk.Button(window, text="Reports", width=25).pack(pady=5)
    tk.Button(window, text="Logout", width=25, fg="red", command=window.destroy).pack(pady=20)

    window.mainloop()

import tkinter as tk
from services.auth_service import login_user
from ui.dashboards.admin_dashboard import open_admin_dashboard
from ui.dashboards.mechanic_dashboard import open_mechanic_dashboard
from ui.dashboards.cashier_dashboard import User

def open_login():
    def handle_login():
        username = username_entry.get()
        password = password_entry.get()

        user = login_user(username, password)
        if user:
            role = user['role']
            login_window.destroy()

            if role == "admin":
                open_admin_dashboard()
            elif role == "mechanic":
                open_mechanic_dashboard(user["id"])
            elif role == "cashier":
                User()
        else:
            status_label.config(text="Invalid username or password", fg="red")

    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("700x700")
    login_window.configure(bg="#333333")

    frame = tk.Frame(login_window, bg="#333333")
    frame.pack()


    login_label = tk.Label(frame, text="Login", bg="#333333", fg="#FFFFFF", font=("Arial", 30), pady=60)
    login_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

    username_label = tk.Label(frame, text="Username", bg="#333333", fg="#FFFFFF", font=("Arial", 16))
    username_label.grid(row=1, column=0)
    username_entry = tk.Entry(frame, font=("Arial", 16))
    username_entry.grid(row=1, column=1, pady=20)

    password_label = tk.Label(frame, text="Password", bg="#333333", fg="#FFFFFF", font=("Arial", 16))
    password_label.grid(row=2, column=0)
    password_entry = tk.Entry(frame, show="*", font=("Arial", 16))
    password_entry.grid(row=2, column=1, pady=20)

    login_button = tk.Button(frame, text="Login", command=handle_login, bg="#FF3399", fg="#FFFFFF")
    login_button.grid(row=3, column=0, columnspan=2, pady=30)

    status_label = tk.Label(frame, text="", bg="#333333")
    status_label.grid(row=4, column=0, columnspan=2)

    login_window.mainloop()

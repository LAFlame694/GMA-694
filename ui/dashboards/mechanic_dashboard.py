import tkinter as tk

def open_mechanic_dashboard():
    window = tk.Tk()
    window.title("Mechanic Dashboard")
    window.geometry("900x600")

    tk.Label(window, text="Mechanic Dashboard", font=("Arial", 20)).pack(pady=20)

    tk.Button(window, text="My Jobs").pack(pady=5)
    tk.Button(window, text="Update Job").pack(pady=5)
    tk.Button(window, text="Logout", fg="red").pack(pady=20)

    window.mainloop()

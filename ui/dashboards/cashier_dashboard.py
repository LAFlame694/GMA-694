import tkinter as tk

def open_cashier_dashboard():
    window = tk.Tk()
    window.title("Cashier Dashboard")
    window.geometry("900x600")

    tk.Label(window, text="Cashier Dashboard", font=("Arial", 20)).pack(pady=20)

    tk.Button(window, text="Create Invoice").pack(pady=5)
    tk.Button(window, text="Payments").pack(pady=5)
    tk.Button(window, text="Logout", fg="red").pack(pady=20)

    window.mainloop()

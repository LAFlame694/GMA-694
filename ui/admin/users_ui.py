# ui/admin/users_ui.py
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from services.auth_service import list_users, create_user, set_user_active

def open_users_ui():
    def refresh_users():
        for row in tree.get_children():
            tree.delete(row)
        rows = list_users()
        for r in rows:
            uid, username, role, active = r
            tree.insert("", "end", iid=str(uid), values=(uid, username, role, "Active" if active == 1 else "Inactive"))

    def add_user_dialog():
        dialog = tk.Toplevel(window)
        dialog.title("Add User")
        dialog.geometry("320x220")

        tk.Label(dialog, text="Username").pack(pady=5)
        username_e = tk.Entry(dialog)
        username_e.pack()

        tk.Label(dialog, text="Password").pack(pady=5)
        password_e = tk.Entry(dialog, show="*")
        password_e.pack()

        tk.Label(dialog, text="Role").pack(pady=5)
        role_cb = ttk.Combobox(dialog, values=["admin", "mechanic", "cashier"])
        role_cb.current(1)  # default mechanic
        role_cb.pack()

        def on_add():
            username = username_e.get().strip()
            password = password_e.get().strip()
            role = role_cb.get().strip()
            if not username or not password or not role:
                messagebox.showerror("Error", "All fields are required")
                return

            ok = create_user(username, password, role)
            if ok:
                messagebox.showinfo("Success", f"User '{username}' created")
                dialog.destroy()
                refresh_users()
            else:
                messagebox.showerror("Error", "Could not create user (username may already exist)")

        tk.Button(dialog, text="Create", command=on_add).pack(pady=10)
        tk.Button(dialog, text="Cancel", command=dialog.destroy).pack()

    def toggle_active():
        sel = tree.selection()
        if not sel:
            messagebox.showwarning("Select user", "Please select a user first")
            return
        uid = int(sel[0])
        # get current active state from the tree
        cur_values = tree.item(sel[0])['values']
        current_status = cur_values[3]
        if current_status == "Active":
            new_active = 0
        else:
            new_active = 1
        success = set_user_active(uid, new_active)
        if success:
            refresh_users()
        else:
            messagebox.showerror("Error", "Failed to update user status")

    window = tk.Tk()
    window.title("Manage Users")
    window.geometry("700x450")

    frame = tk.Frame(window)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    tree = ttk.Treeview(frame, columns=("id", "username", "role", "active"), show="headings", selectmode="browse")
    tree.heading("id", text="ID")
    tree.heading("username", text="Username")
    tree.heading("role", text="Role")
    tree.heading("active", text="Status")
    tree.column("id", width=50, anchor="center")
    tree.column("username", width=200)
    tree.column("role", width=120, anchor="center")
    tree.column("active", width=100, anchor="center")
    tree.pack(fill="both", expand=True, side="left")

    vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=vsb.set)
    vsb.pack(side="left", fill="y")

    controls = tk.Frame(window)
    controls.pack(pady=10)

    tk.Button(controls, text="Add User", command=add_user_dialog, width=15).pack(side="left", padx=5)
    tk.Button(controls, text="Activate/Deactivate", command=toggle_active, width=20).pack(side="left", padx=5)
    tk.Button(controls, text="Refresh", command=refresh_users, width=12).pack(side="left", padx=5)
    tk.Button(controls, text="Close", command=window.destroy, width=12).pack(side="left", padx=5)

    refresh_users()
    window.mainloop()

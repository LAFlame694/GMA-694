import tkinter as tk
from tkinter import ttk, messagebox
from services.job_service import get_mechanics, assign_mechanic

def open_assign_mechanic_ui(job_id: int):
    window = tk.Toplevel()
    window.title(f"Assign Mechanic to Job #{job_id}")
    window.geometry("400x300")

    tk.Label(window, text=f"Assign Mechanic to Job ID: {job_id}", font=("Arial", 12, "bold")).pack(pady=10)

    # Load mechanics
    mechanics = get_mechanics()

    if not mechanics:
        tk.Label(window, text="No active mechanics found.", fg="red").pack(pady=10)
        return
    
    tk.Label(window, text="Select Mechanic:").pack()

    mech_var = tk.StringVar()
    mech_cb = ttk.Combobox(window, textvariable=mech_var, width=30)

    mech_cb['values'] = [f"{username} (ID: {mid})" for mid, username in mechanics]
    mech_cb.current(0)
    mech_cb.pack(pady=5)

    def on_assign():
        selected = mech_cb.get()
        if not selected:
            messagebox.showwarning("Select Mechanic", "Please choose a mechanic")
            return
        
        # Extract mechanic ID properly
        try:
            mid = int(selected.split("ID:")[1].replace(")", "").strip())
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read mechanic ID: {e}")
            return
        
        ok = assign_mechanic(job_id, mid)
        if ok:
            messagebox.showinfo("Success", "Mechanic assigned successfully!")
            window.destroy()
        else:
            messagebox.showerror("Error", "Failed to assign mechanic")

    
    tk.Button(window, text="Assign", command=on_assign, width=15).pack(pady=10)
    tk.Button(window, text="Close", command=window.destroy, width=15).pack()
    
    window.mainloop()

    
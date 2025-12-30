import tkinter as tk
from tkinter import messagebox

# UI:
class UI:
   def creat_window(self, title, width, height, backcolor):
       window = tk.Tk()
       window.title(title)
       window.geometry(f"{width}x{height}")
       window.configure(bg=backcolor)
       return window
   def show_message(self, text, title=None, style=None, command1=None, command2=None):
       if style==None:
           messagebox.showinfo(title, text)
       else:
           if style==0:
               messagebox.showinfo(title, text)
           elif style==1:
               messagebox.showwarning(title, text)
           elif style==2:
               messagebox.showerror(title, text)
           elif style==3:
               result = messagebox.askokcancel(title, text)
               (command1 if result else command2)()
           elif style==4:
               result = messagebox.askyesno(title, text)
               command1 if result else command2

   def creat_button(self, window, text, x, y, width, height, bg, fg, command):
       control = tk.Button(window, text = text, bg = bg, fg = fg, command=command)
       control.place(x = x, y = y, width = width, height = height)
       return control
   
   def creat_label(self, window, text, x, y, width, height, bg, fg, font_size):
       control = tk.Label(window, text=text, bg=bg, fg=fg, font=(None, font_size), wraplength=width)
       control.place(x = x, y = y, width = width, height = height)
       return control
   
   def creat_frame(self, window, x, y, width, height, bg):
       control = tk.Frame(window,  bg=bg)
       control.place(x = x, y = y, width = width, height=height)
       return control
   
   def creat_listbox(self, window, x, y, width, height, bg, fg, command):
       control = tk.Listbox(window,  bg=bg, fg=fg)
       control.place(x = x, y = y, width = width, height=height)
       control.bind("<<ListboxSelect>>", command)
       return control
   
   def create_label_pack(self, window, text, **kwargs):
        # extract label-specific properties from kwargs
        label_kwargs = {}
        label_properties = [
            'bg', 'fg', 'font', 
            'wraplength', 'width', 'height',
            'relief', 'borderwidth', 'textvariable',
            'image', 'compound', 'cursor',
            'state', 'justify'
        ]
        for prop in label_properties:
            if prop in kwargs:
                label_kwargs[prop] = kwargs.pop(prop)

        # create the label
        control = tk.Label(window, text=text, **label_kwargs)

        # set default pack values if not specified
        pack_defaults = {
            'side': 'top',
            'fill': 'none',
            'expand': False,
            'anchor': 'center',
            'padx': 0,
            'pady': 0,
            'ipadx': 0,
            'ipady': 0
        }

        # update defaults with user-provided values
        pack_options = {**pack_defaults, **kwargs}

        # pack the label
        control.pack(**pack_options)
        return control
   
   def create_frame_pack(self, window, **kwargs):
       # extract frame specific properties from kwargs
       frame_kwargs = {}
       frame_properties = ['bg', 'fg', 'width', 'height', 'relief', 'borderwidth',
        'highlightbackground', 'highlightcolor', 'highlightthickness',
        'takefocus', 'cursor', 'name', 'background', 'foreground']
       
       for prop in frame_properties:
           if prop in kwargs:
                if prop == 'background':
                    frame_kwargs['bg'] = kwargs.pop(prop)
                elif prop == 'foreground':
                    frame_kwargs['fg'] = kwargs.pop(prop)
                else:
                   frame_kwargs[prop] = kwargs.pop(prop)
        # create the frame
       frame = tk.Frame(window, **frame_kwargs)

       # set default pack values
       pack_defaults = {
        'side': 'top',
        'fill': 'none',
        'expand': False,
        'anchor': 'center',
        'padx': 0,
        'pady': 0,
        'ipadx': 0,
        'ipady': 0
        }
       
        # update defaults with user provided values
       pack_options = {**pack_defaults, **kwargs}

       # pack the frame
       frame.pack(**pack_options)
       return frame
   
   def create_labelframe_pack(self, window, text="", **kwargs):
       # extract label_frame specific properties from kwargs
       labelframe_kwargs = {}
       labelframe_properties = [
        'bg', 'fg', 'font', 'labelanchor', 'labelwidget',
        'width', 'height', 'relief', 'borderwidth',
        'highlightbackground', 'highlightcolor', 'highlightthickness',
        'takefocus', 'cursor', 'background', 'foreground',
        'padx', 'pady'
       ]

       for prop in labelframe_properties:
           if prop in kwargs:
               if prop == 'background':
                   labelframe_kwargs['bg'] = kwargs.pop(prop)
               elif prop == 'foreground':
                   labelframe_kwargs['fg'] = kwargs.pop(prop)
               else:
                   labelframe_kwargs[prop] = kwargs.pop(prop)
       
       # create the labelframe
       labelframe = tk.LabelFrame(window, text=text, **labelframe_kwargs)

       # set default pack values
       pack_defaults = {
           'side': 'top',
           'fill': 'none',
           'expand': False,
           'anchor': 'center',
           'padx': 0,
           'pady': 0,
           'ipadx': 0,
           'ipady': 0
       }

       # update defaults with user provided values
       pack_options = {**pack_defaults, **kwargs}

       # pack the LabelFrame
       labelframe.pack(**pack_options)
       return labelframe
   
   def create_button_grid(self, window, text="", **kwargs):
       # extract button specific properties from kwargs
       button_kwargs = {}
       button_properties = [
        'command', 'bg', 'fg', 'font', 'width', 'height',
        'relief', 'borderwidth', 'image', 'compound',
        'state', 'cursor', 'takefocus', 'underline',
        'activebackground', 'activeforeground',
        'disabledforeground', 'highlightbackground',
        'highlightcolor', 'highlightthickness',
        'textvariable', 'background', 'foreground'
       ]

       for prop in button_properties:
           if prop in kwargs:
               if prop == 'background':
                   button_kwargs['bg'] = kwargs.pop(prop)
               elif prop == 'foreground':
                   button_kwargs['fg'] = kwargs.pop(prop)
               else:
                   button_kwargs[prop] = kwargs.pop(prop)
       
       # create the button
       button = tk.Button(window, text=text, **button_kwargs)

       # set default grid values
       grid_defaults = {
           'row': 0,
           'column': 0,
           'rowspan': 1,
           'columnspan': 1,
           'sticky': "",
           'padx': 0,
           'pady': 0,
           'ipadx': 0,
           'ipady': 0
       }

       # update defaults with user provided values
       grid_options = {**grid_defaults, **kwargs}

       # grid the button
       button.grid(**grid_options)

# User:
class User:
   def clear_frame(self, frame):
       for widget in frame.winfo_children():
           widget.destroy()

   def load_invoice_details(self, invoice_id):
       from services.invoice_service import get_invoice_full_details
       from services.payment_service import get_payments_for_invoice

       invoice, parts = get_invoice_full_details(invoice_id)
       if not invoice:
           return
       
       self.clear_frame(self.invoice_detail_wrapper)
       
       (
           inv_id,
           status,
           total,
           created_at,
           job_id,
           job_desc,
           plate
       ) = invoice

       # update labels
       self.vehicle_plate_label = self.ui.create_label_pack(self.invoice_detail_wrapper, f'Vehicle: {plate}', bg='#FF0080', fg='#000000', font=("Comic Sans MS", 10, "bold"), anchor='w')
       self.job_desc_label = self.ui.create_label_pack(self.invoice_detail_wrapper, f'Job: {job_desc}', bg='#FF0080', fg='#000000', font=("Comic Sans MS", 10, "bold"), anchor='w')
       self.status_label = self.ui.create_label_pack(self.invoice_detail_wrapper, f'Status: {status}', bg='#FF0080', fg='#000000', font=("Comic Sans MS", 10, "bold"), anchor='w')
       self.created_label = self.ui.create_label_pack(self.invoice_detail_wrapper, f'Created: {created_at}', bg='#FF0080', fg='#000000', font=("Comic Sans MS", 10, "bold"), anchor='w')

       # part list
       self.listbox2.delete(0, tk.END)
       grand_total = 0

       for name, qty, price, line_total in parts:
           self.listbox2.insert(
               tk.END,
               f"{name} | Qty: {qty} | {price} | Total: {line_total}"
           )
           grand_total += line_total
           
       self.grand_total_label.config(text=f"Grand Total: KES {grand_total}")

       # payments
       payments = get_payments_for_invoice(inv_id)
       self.listbox3.delete(0, tk.END)

       paid_total = 0
       for amount, date in payments:
           self.listbox3.insert(
               tk.END,
               f"KES {amount} | {date}"
           )
           paid_total += amount
        
       balance = grand_total - paid_total

       self.total_label.config(text=f"Total: {grand_total}")
       self.paid_label.config(text=f"Paid: {paid_total}")
       self.balance_label.config(text=f"Balance: {balance}")

   def load_invoices(self):
       from services.invoice_service import list_invoices

       self.listbox1.delete(0, tk.END)
       self.invoice_map = {}

       invoices = list_invoices()

       for index, inv in enumerate(invoices):
           invoice_id, plate, total, status, date = inv

           display_text = f"INV - {invoice_id} | {plate} | KES {total} | {status} | {date}"
           self.listbox1.insert(tk.END, display_text)

           self.invoice_map[index] = invoice_id

   def __init__(self):
       self.init_ui()

   def init_ui(self):
       self.ui = UI()
       self.mainWindow = self.ui.creat_window("mainWindow", 1200, 700,'#D3D3D3')

       self.current_user = {
           "id": 1,
           "username": "George",
           "role": "Cashier"
       }

       self.top_bar_frame = self.ui.creat_frame(self.mainWindow, 0, 0, 1200, 80, '#408080')
       self.logout_btn = self.ui.creat_button(self.top_bar_frame, 'Logout', 1050, 20, 100, 30, '#0080FF', '#000000', self.logout)
       self.title_label = self.ui.creat_label(self.top_bar_frame, f"Logged in as: {self.current_user['username']}", 0, 0,500, 80, '#D3D3D3', '#000000', 20)

       self.main_frame = self.ui.creat_frame(self.mainWindow, 0, 80, 1200, 620, '#D3D3D3')


       self.invoice_list_frame = self.ui.creat_frame(self.main_frame, 0, 0, 550, 620, '#D3D3D3')
       self.invoice_list_label = self.ui.creat_label(self.invoice_list_frame, 'Invoices', 0, 10,550, 30, '#FF0080', '#000000', 10)

       self.invoice_detail_frame = self.ui.creat_frame(self.main_frame, 650, 0, 550, 380, '#D3D3D3')

       self.invoice_detail_label = self.ui.create_label_pack(self.invoice_detail_frame, 'Invoice Details', bg='#FF0080', fg='#000000', font=("Comic Sans MS", 10, "bold"), anchor='center')
       
       self.invoice_detail_wrapper = self.ui.create_labelframe_pack(self.invoice_detail_frame, "Details Wrapper",borderwidth=2, width=550, height=180, anchor='w', fill='x')

       self.part_list_frame = self.ui.create_labelframe_pack(self.invoice_detail_frame, 'Part List', borderwidth=2, width=550, height=200)
       self.grand_total_label = self.ui.create_label_pack(self.invoice_detail_frame, f'Grand Total: ', bg='#FF0080', fg='#000000', font=("Comic Sans MS", 10, "bold"), anchor='w')

       self.actions_payments_frame = self.ui.creat_frame(self.main_frame, 650, 380, 550, 240, '#D3D3D3')
       self.payment_list_frame = self.ui.create_labelframe_pack(self.actions_payments_frame, 'Payments', bg='lightblue', relief='ridge', height=80, width=550)

       self.balance_summery = self.ui.create_labelframe_pack(self.actions_payments_frame, 'Balance Summery', bg='lightblue', relief='ridge', height=100, width=550, anchor='w', fill="x")
       self.total_label = self.ui.create_label_pack(self.balance_summery, f'Total:', bg='#FF0080', fg='#000000', font=("Comic Sans MS", 10, "bold"), anchor='w')
       self.paid_label = self.ui.create_label_pack(self.balance_summery, f'Paid:', bg='#FF0080', fg='#000000', font=("Comic Sans MS", 10, "bold"), anchor='w')
       self.balance_label = self.ui.create_label_pack(self.balance_summery, f'Balance:', bg='#FF0080', fg='#000000', font=("Comic Sans MS", 10, "bold"), anchor='w')

       self.action_btn_frame = self.ui.create_labelframe_pack(self.actions_payments_frame, 'Actions', bg='lightblue', relief='ridge', height=70, width=550, anchor='w', fill="x")
       self.record_payment_btn = self.ui.create_button_grid(self.action_btn_frame, 'Record Payment', row=0, column=0, padx=10, pady=20, bg="#0080FF")
       self.view_receipt_btn = self.ui.create_button_grid(self.action_btn_frame, 'View Receipt', row=0, column=1, padx=10, pady=20, bg="#0080FF")
       self.mark_paid_btn = self.ui.create_button_grid(self.action_btn_frame, 'Mark as Paid', row=0, column=2, padx=10, pady=20, bg="#0080FF")
       self.create_invoice_btn = self.ui.create_button_grid(self.action_btn_frame, 'Create Invoice', row=0, column=3, padx=10, pady=20, bg="#0080FF")
       self.refresh_btn = self.ui.create_button_grid(self.action_btn_frame, 'Refresh', row=0, column=4, padx=10, pady=20, bg="#0080FF")

       # list_box
       self.listbox3 = self.ui.creat_listbox(self.payment_list_frame, 0, 0, 550, 100, '#FFFFFF', '#000000',self.on_listbox3_select_changed)
       self.items=["item1"]
       self.on_listbox3_set_items(self.items)

       self.listbox2 = self.ui.creat_listbox(self.part_list_frame, 0, 0, 550, 200, '#FFFFFF', '#000000',self.on_listbox2_select_changed)
       self.items=["item1"]
       self.on_listbox2_set_items(self.items)

       self.listbox1 = self.ui.creat_listbox(self.invoice_list_frame, 0, 50, 550, 580, '#FFFFFF', '#000000',self.on_listbox1_select_changed)
       self.load_invoices()
    
    # Functions:
    # listbox1
   def on_listbox1_set_items(self,items):
       self.listbox1.delete(0, tk.END)
       for item in items:
           self.listbox1.insert(tk.END, item)
   def on_listbox1_select_changed(self,event):
       selection = self.listbox1.curselection()
       if not selection:
           return

       index = selection[0]
       invoice_id = self.invoice_map.get(index)

       if invoice_id:
           self.load_invoice_details(invoice_id)

   def on_listbox2_set_items(self,items):
       self.listbox2.delete(0, tk.END)
       for item in items:
           self.listbox2.insert(tk.END, item)
   def on_listbox2_select_changed(self,event):
       selected_index = self.listbox2.curselection()
       if selected_index:
           selected_item = self.listbox2.get(selected_index)
           self.ui.show_message(f"{selected_item} selected")

   def on_listbox3_set_items(self,items):
       self.listbox3.delete(0, tk.END)
       for item in items:
           self.listbox3.insert(tk.END, item)
   def on_listbox3_select_changed(self,event):
       selected_index = self.listbox3.curselection()
       if selected_index:
           selected_item = self.listbox3.get(selected_index)
           self.ui.show_message(f"{selected_item} selected")

# Functions:
# button2
   def logout(self):
    def confirm_logout():
        self.mainWindow.destroy()

    self.ui.show_message(
        "Are you sure you want to logout",
        "Confirm Logout",
        style=3,
        command1=confirm_logout,
        command2=lambda:None
    )

if __name__ == "__main__":
   user = User()
   user.mainWindow.mainloop()
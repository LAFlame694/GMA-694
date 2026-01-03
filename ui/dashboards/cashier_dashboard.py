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
   
   def creat_listbox(self, window, x, y, width, height, bg, fg, command, font=None):
        # Create a container frame for better size control
        container = tk.Frame(window, width=width, height=height)
        container.pack_propagate(False)  # Prevent container from shrinking
        container.pack(padx=x, pady=y)
        
        # Set default font if none provided
        if font is None:
            font = ('Arial', 10)  # Default font
        
        control = tk.Listbox(container, bg=bg, fg=fg, font=font)
        control.pack(fill='both', expand=True)
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
    
   def create_button_pack(self, window, text="", **kwargs):
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

        # grid the button
        button.pack(**pack_options)

   def create_entry(self, parent,

           # appearances properties
           bg='white', fg='black',
           font=('Comic Sans MS', 10),
           borderwidth=2, relief='ridge',
           cursor='xterm',

           # text properties
           textvariable=None,
           show=None,
           state='normal',
           justify='left',

           # validation
           validate=None,
           validatecommand=None,
           invalidcommand=None,

           # packing options
           pack_options=None,

           # event binding
           on_enter=None,
           on_focusin=None,
           on_focusout=None,

           # place holder functionality
           placeholder_text="",
           placeholder_color='grey'
        ):
       entry = tk.Entry(
           parent,
           bg=bg,
           fg=fg,
           font=font,
           borderwidth=borderwidth,
           relief=relief,
           cursor=cursor,
           textvariable=textvariable,
           show=show,
           state=state,
           justify=justify,
           validate=validate,
           validatecommand=validatecommand,
           invalidcommand=invalidcommand
       )

       # default packing options
       default_pack_options = {
           'fill': 'none',
           'expand': False,
           'padx': 10,
           'pady': 5,
           'ipadx': 0,
           'ipady': 0,
           'side': 'top',
           'anchor': 'w'
       }

       # update with user options
       if pack_options:
           default_pack_options.update(pack_options)
        
       entry.pack(**default_pack_options)
       return entry

# User:
class User:
   def record_payment(self):
       if not hasattr(self, "current_invoice_id") or not self.current_invoice_id:
           self.ui.show_message(
               "Please select an invoice first",
               "No invoice Selected",
               style=1
           )
           return
       
       amount_text = self.payment_entry.get().strip()
       if not amount_text:
           self.ui.show_message(
               "Please enter payment amount",
               "Missing Amount",
               style=1
           )
           return
       
       try:
           amount = float(amount_text)
           if amount <= 0:
               raise ValueError
       except ValueError:
           self.ui.show_message(
               "Enter a valid positive number",
               "Invalid Amount",
               style=2
            )
           return
       
       from services.payment_service import add_payment

       try:
           paid_total, balance, status = add_payment(self.current_invoice_id, amount)
       except Exception as e:
           self.ui.show_message(
               "Failed to record payment",
               "Error",
               style=2
           )
           return
       
       self.ui.show_message(
           f"Payment recorded successfully\n"
           f"Status: {status}\n"
           f"Balance: KES {balance:.2f}"
       )

       self.payment_entry.delete(0, tk.END)

       self.load_invoice_details(self.current_invoice_id)
       self.load_invoices()

   def load_available_jobs(self):
       from services.job_service import get_completed_uninvoiced_jobs

       self.listbox4.delete(0, tk.END)
       self.job_map = {}

       jobs = get_completed_uninvoiced_jobs()

       for index, job in enumerate(jobs):
           job_id, plate, desc = job
           
           display = f"JOB {job_id} | {plate} |  {desc}"
           self.listbox4.insert(tk.END, display)

           self.job_map[index] = job_id

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
       self.vehicle_plate_label = self.ui.create_label_pack(self.invoice_detail_wrapper, f'Vehicle: {plate}', fg='#000000', font=("Comic Sans MS", 10, "bold"), anchor='w')
       self.job_desc_label = self.ui.create_label_pack(self.invoice_detail_wrapper, f'Job: {job_desc}', fg='#000000', font=("Comic Sans MS", 10, "bold"), anchor='w')
       self.status_label = self.ui.create_label_pack(self.invoice_detail_wrapper, f'Status: {status}', fg='#000000', font=("Comic Sans MS", 10, "bold"), anchor='w')
       self.created_label = self.ui.create_label_pack(self.invoice_detail_wrapper, f'Created: {created_at}', fg='#000000', font=("Comic Sans MS", 10, "bold"), anchor='w')

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
   def create_invoice_action(self):
       if not hasattr(self, "selected_job_id"):
           self.ui.show_message("Please select a job first", "No job selected", style=1)
           return
       
       from services.invoice_service import create_invoice

       invoice_id = create_invoice(self.selected_job_id)

       if invoice_id:
           self.ui.show_message(f"Invoice #{invoice_id} created successfully")
           self.load_invoices()
           self.load_available_jobs()
       else:
           self.ui.show_message("Failed to create invoice", style=2)

   def __init__(self):
       self.init_ui()

   def init_ui(self):
       self.ui = UI()
       self.mainWindow = self.ui.creat_window("mainWindow", 1250, 800,'#D3D3D3')

       self.current_user = {
           "id": 1,
           "username": "George",
           "role": "Cashier"
       }

       self.top_bar_frame = self.ui.create_frame_pack(self.mainWindow, height=40, fill='x', bg='#408080')

       self.logout_btn = self.ui.create_button_pack(
           self.top_bar_frame, 
           'Logout', 
           borderwidth=5, 
           relief='sunken', 
           padx=30, 
           pady=10, 
           bg='red', 
           fg='#ffffff', 
           command=self.logout, 
           anchor='e', 
           font=("Comic Sans MS", 10, "bold")
        )
       
       self.title_label = self.ui.create_label_pack(self.top_bar_frame, f"Logged in as: {self.current_user['username']}", fg='#ffffff', anchor='w', bg='#408080', font=("Comic Sans MS", 20, 'bold'))

       # Main frame
       self.main_frame = self.ui.create_frame_pack(
           self.mainWindow, 
           bg='#00FFFF', 
           expand=True, 
           fill='both',
           borderwidth=5,
           relief='ridge'
        )

       # Invoice list frame
       self.invoice_list_frame = self.ui.create_frame_pack(
           self.main_frame, 
           bg="#008080",
           side='left',
           fill='both',
           expand=True,
           padx=(10, 5),
           pady=10,
           borderwidth=10,
           relief="ridge"
        )
       
       # Right side frame
       self.right_side_frame = self.ui.create_frame_pack(
           self.main_frame, 
           bg="#008080",
           side='right',
           fill='both',
           expand=True,
           padx=(5, 10),
           pady=10,
           borderwidth=10,
           relief="ridge"
        )
       
       # Configure grid weights
       self.main_frame.grid_columnconfigure(0, weight=1) # left frame
       self.main_frame.grid_columnconfigure(0, weight=1) # right frame

       # invoice_list_frame setup...
       self.invoice_list_label = self.ui.create_label_pack(self.invoice_list_frame, 'Invoices', fg='#000000', font=("Comic Sans MS", 10, "bold"), anchor='center')
       self.listbox_frame = self.ui.create_frame_pack(self.invoice_list_frame, fill='both', expand=True)
       self.job_list_frame = self.ui.create_labelframe_pack(self.invoice_list_frame, 'Job List', borderwidth=5, expand=True, fill='both', font=("Comic Sans MS", 10, 'bold'), fg='dodgerblue')

       # right_side_frame setup...
       self.invoice_detail_frame = self.ui.create_frame_pack(self.right_side_frame, fill='both', expand=True)

       self.invoice_detail_label = self.ui.create_label_pack(self.invoice_detail_frame, 'Invoice Details', fg='#000000', font=("Comic Sans MS", 10, "bold"), anchor='center')
       
       self.invoice_detail_wrapper = self.ui.create_labelframe_pack(self.invoice_detail_frame, "Details Wrapper",borderwidth=5, expand=True, anchor='w', fill='both', font=("Comic Sans MS", 10, 'bold'), fg='dodgerblue')

       self.part_list_frame = self.ui.create_labelframe_pack(self.invoice_detail_frame, 'Part List', borderwidth=5, fill='both', expand=True, font=("Comic Sans MS", 10, 'bold'), fg='dodgerblue')
       self.grand_total_label = self.ui.create_label_pack(self.invoice_detail_frame, f'Grand Total: ',  fg='#000000', font=("Comic Sans MS", 10, "bold"), anchor='w')

       self.actions_payments_frame = self.ui.create_frame_pack(self.right_side_frame, bg='#D3D3D3', fill='both', expand=True)
       self.payment_list_frame = self.ui.create_labelframe_pack(self.actions_payments_frame, 'Payments', relief='ridge', fill='both', expand=True, borderwidth=5, font=("Comic Sans MS", 10, 'bold'), fg='dodgerblue')

       self.listbox3 = self.ui.creat_listbox(self.payment_list_frame, 0, 0, 550, 50, '#FFFFFF', '#000000', self.on_listbox3_select_changed, font=("Comic Sans MS", 10))

       self.record_payment_btn = self.ui.create_button_pack(
           self.payment_list_frame,
           'Record Payment', 
           borderwidth=2, 
           relief='sunken', 
           padx=10, 
           pady=7, 
           bg='red', 
           fg='#ffffff', 
           command=self.record_payment, 
           anchor='w', 
           font=("Comic Sans MS", 10, "bold")
        )
       
       self.payment_entry = self.ui.create_entry(self.payment_list_frame)

       self.balance_summery = self.ui.create_labelframe_pack(self.actions_payments_frame, 'Balance Summery', relief='ridge', fill='both', expand=True, anchor='w', borderwidth=5, font=("Comic Sans MS", 10, 'bold'), fg='dodgerblue')
       self.total_label = self.ui.create_label_pack(self.balance_summery, f'Total:', fg='#000000', font=("Comic Sans MS", 10, "bold"), anchor='w')
       self.paid_label = self.ui.create_label_pack(self.balance_summery, f'Paid:', fg='#000000', font=("Comic Sans MS", 10, "bold"), anchor='w')
       self.balance_label = self.ui.create_label_pack(self.balance_summery, f'Balance:', fg='#000000', font=("Comic Sans MS", 10, "bold"), anchor='w')

       self.action_btn_frame = self.ui.create_labelframe_pack(self.actions_payments_frame, 'Actions', relief='ridge', fill='both', expand=True, anchor='w', borderwidth=5, font=("Comic Sans MS", 10, 'bold'), fg='dodgerblue')
       self.view_receipt_btn = self.ui.create_button_grid(self.action_btn_frame, 'View Receipt', row=0, column=1, padx=10, pady=20, bg="#808080", fg='#ffffff', borderwidth=5, relief='sunken', font=("Comic Sans MS", 10, "bold"))
       self.mark_paid_btn = self.ui.create_button_grid(self.action_btn_frame, 'Mark as Paid', row=0, column=2, padx=10, pady=20, bg="#24A021", fg='#ffffff', borderwidth=5, relief='sunken', font=("Comic Sans MS", 10, "bold"))

       self.create_invoice_btn = self.ui.create_button_grid(
           self.action_btn_frame, 
           'Create Invoice', 
           row=0, 
           column=3, 
           padx=10, 
           pady=20, 
           bg="#0080FF", 
           fg='#ffffff', 
           borderwidth=5, 
           relief='sunken', 
           font=("Comic Sans MS", 10, "bold"),
           command=self.create_invoice_action
        )
       
       self.refresh_btn = self.ui.create_button_grid(self.action_btn_frame, 'Refresh', row=0, column=4, padx=10, pady=20, bg="#0080FF", fg='#ffffff', borderwidth=5, relief='sunken', font=("Comic Sans MS", 10, "bold"))

       # list_box
       self.listbox2 = self.ui.creat_listbox(self.part_list_frame, 0, 0, 550, 50, '#FFFFFF', '#000000', self.on_listbox2_select_changed, font=("Comic Sans MS", 10))
       self.items=["item1"]
       self.on_listbox2_set_items(self.items)

       self.listbox1 = self.ui.creat_listbox(self.listbox_frame, 0, 0, 550, 250, '#FFFFFF', '#000000', self.on_listbox1_select_changed, font=("Comic Sans MS", 10))
       self.load_invoices()

       self.listbox4 = self.ui.creat_listbox(self.job_list_frame, 0, 0, 550, 150, '#FFFFFF', '#000000', self.on_listbox4_select_changed, font=("Comic Sans MS", 10))
       self.load_available_jobs()
    
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
           self.current_invoice_id = invoice_id
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
    
   def on_listbox4_set_items(self,items):
       self.listbox4.delete(0, tk.END)
       for item in items:
           self.listbox4.insert(tk.END, item)
   def on_listbox4_select_changed(self,event):
       selection = self.listbox4.curselection()
       if not selection:
           return

       index = selection[0]
       self.selected_job_id = self.job_map.get(index)

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
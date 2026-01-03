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

# User:
class User:
   def __init__(self):
       self.init_ui()
   def init_ui(self):
       self.ui = UI()
       self.mainWindow = self.ui.creat_window("mainWindow", 400, 300,'#24A021')

# Functions:

if __name__ == "__main__":
   user = User()
   user.mainWindow.mainloop()

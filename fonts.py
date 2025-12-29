import tkinter as tk
from tkinter import font as tkfont

def show_font_styles():
    root = tk.Tk()
    root.title("Tkinter Font Styles Demo")
    root.geometry("800x600")
    
    # Create a frame with scrollbar
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    canvas = tk.Canvas(frame)
    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Get available font families (varies by system)
    available_fonts = tkfont.families()
    
    # Common font families (cross-platform)
    common_fonts = [
        ('Arial', 'Arial'),
        ('Times New Roman', 'Times New Roman'),
        ('Courier New', 'Courier New'),
        ('Verdana', 'Verdana'),
        ('Tahoma', 'Tahoma'),
        ('Georgia', 'Georgia'),
        ('Helvetica', 'Helvetica'),
        ('Comic Sans MS', 'Comic Sans MS'),
        ('Impact', 'Impact'),
        ('Trebuchet MS', 'Trebuchet MS')
    ]
    
    # Display system fonts
    tk.Label(scrollable_frame, 
             text="Available Font Families on Your System:",
             font=('Arial', 14, 'bold'),
             fg='blue').pack(anchor='w', pady=(0, 10))
    
    # Show first 20 system fonts
    for i, font_name in enumerate(available_fonts[:20]):
        tk.Label(scrollable_frame, 
                text=f"Sample: {font_name}",
                font=(font_name, 12),
                fg='green' if i % 2 else 'black').pack(anchor='w')
    
    tk.Label(scrollable_frame, 
             text="\nCommon Font Examples:",
             font=('Arial', 14, 'bold'),
             fg='blue').pack(anchor='w', pady=(20, 10))
    
    # Display common fonts
    for font_display, font_family in common_fonts:
        if font_family in available_fonts:
            tk.Label(scrollable_frame, 
                    text=f"{font_display}: The quick brown fox jumps over the lazy dog",
                    font=(font_family, 12),
                    fg='black').pack(anchor='w', pady=2)
    
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    root.mainloop()

show_font_styles()
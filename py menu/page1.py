import tkinter as tk

def create_page():
    
    page = tk.Frame()
    labels = tk.Label(page, text="Página ")
    label = tk.Label(page, text="Página 1")
    
    label.pack()
    labels.pack()
    return page

import tkinter as tk

def create_page():
    page = tk.Frame()
    label = tk.Label(page, text="Página 2")
    label.pack()
    return page

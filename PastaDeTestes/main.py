import tkinter as tk
from tkinter import ttk



def Main(MainFrame):
    from ChangeWindow import ChangeWindow            
    global RegisterButton
    RegisterButton = ttk.Button(MainFrame, text="Register", width=20, command=lambda:ChangeWindow("Main"))    # Register Button
    RegisterButton.grid(row=1, columnspan=1, sticky = tk.W, padx=2, pady=2)
    return
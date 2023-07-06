import tkinter as tk
from tkinter import ttk



def Login(MainFrame): # Receives existing frame and changes it's contents         
    global LoginButton
    LoginButton = ttk.Button(MainFrame, text="Register", width=20)#, command=Register)    # Register Button
    LoginButton.grid(row=1, columnspan=1, sticky = tk.W, padx=2, pady=2)
    return(MainFrame)


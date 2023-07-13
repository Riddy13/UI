import tkinter as tk
from tkinter import ttk
from WindowChange import ChangeWindows
from Warning import AddWarning


def LoginToMain(Frame):
    ChangeWindows(Frame, "Main")


def LoginSection(Frame):
    TitleLabel = ttk.Label(Frame, text = "Login Window", font = 25) #Title 
    TitleLabel.grid(row = 0, columnspan= 2)
    
    global UserAndEmailNameInput
    UserAndEmailNameInput = ttk.Entry(Frame, width= 35)
    UserAndEmailNameInput.grid(row=1, column=1, sticky = tk.W, pady=2)
    UserAndEmailNameInput = ttk.Label(Frame, text="User Name:")
    UserAndEmailNameInput.grid(row=1, column=0, sticky = tk.W, pady=2, padx=2)

    global PasswordInput
    PasswordInput = ttk.Entry(Frame, width = 35)
    PasswordInput.grid(row = 3, column=1, sticky=tk.W, pady=2)
    PasswordLabel = ttk.Label(Frame, text="Password:")
    PasswordLabel.grid(row = 3, column=0, sticky = tk.W, pady=2, padx=2)

    global Register
    Register = ttk.Button(Frame, text="Register", width=20, command= lambda: LoginToMain(Frame))    # Change to register button
    Register.grid(row=4, columnspan=2, sticky = tk.W, padx=2, pady=2)

    global ChangeToLogIn
    ChangeToLogIn = ttk.Button(Frame, text="LogIn", width = 20, command= lambda: AddWarning("TEST")) # Login to main
    ChangeToLogIn.grid(row=4, column=1, sticky = tk.E, pady=2)

    global WarningLabel
    WarningLabel = ttk.Label(Frame, text="", font= 12)

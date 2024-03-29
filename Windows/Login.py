import tkinter as tk
from tkinter import ttk
from Windows.loginToW import ToMain
from UsersInfo.Credentials import EnterCredentials
from Misc.Warning import AddWarning


def ClearFrame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    return frame

def LoginSection(Frame):
    TitleLabel = ttk.Label(Frame, text="Login Window", font=25)  # Title
    TitleLabel.grid(row=0, columnspan=2)
    
    global UserAndEmailNameInput
    UserAndEmailNameInput = ttk.Entry(Frame, width=35)
    UserAndEmailNameInput.grid(row=1, column=1, sticky=tk.W, pady=2)
    UserAndEmailNameInput = ttk.Label(Frame, text="User Name:")
    UserAndEmailNameInput.grid(row=1, column=0, sticky=tk.W, pady=2, padx=2)

    global PasswordInput
    PasswordInput = ttk.Entry(Frame, width=35)
    PasswordInput.grid(row=3, column=1, sticky=tk.W, pady=2)
    PasswordLabel = ttk.Label(Frame, text="Password:")
    PasswordLabel.grid(row=3, column=0, sticky=tk.W, pady=2, padx=2)

    global ChangeToRegister
    ChangeToRegister = ttk.Button(Frame, text="Register", width=20)  # , command= lambda: LoginToRegister())
    ChangeToRegister.grid(row=4, columnspan=2, sticky=tk.W, padx=2, pady=2)

    global Login
    Login = ttk.Button(Frame, text="LogIn", width=20, command=lambda: ToMain(Frame))
    Login.grid(row=4, column=1, sticky=tk.E, pady=2)

    global WarningLabel
    WarningLabel = ttk.Label(Frame, text="", font=12)

def RegisterSection(Frame):
    TitleLabel = ttk.Label(Frame, text="Register Window", font=25)
    TitleLabel.grid(row=0, columnspan=2)
    
    global UserNameInput
    UserNameInput = ttk.Entry(Frame, width=35)
    UserNameInput.grid(row=1, column=1, sticky=tk.W, pady=2)
    UserNameLabel = ttk.Label(Frame, text="User Name:")
    UserNameLabel.grid(row=1, column=0, sticky=tk.W, pady=2, padx=2)

    global EmailInput
    EmailInput = ttk.Entry(Frame, width=35)
    EmailInput.grid(row=2, column=1, sticky=tk.W, pady=2)
    EmailLabel = ttk.Label(Frame, text="E-mail:")
    EmailLabel.grid(row=2, column=0, sticky=tk.W, pady=2, padx=2)

    global PasswordInput
    PasswordInput = ttk.Entry(Frame, width=35)
    PasswordInput.grid(row=3, column=1, sticky=tk.W, pady=2)
    PasswordLabel = ttk.Label(Frame, text="Password:")
    PasswordLabel.grid(row=3, column=0, sticky=tk.W, pady=2, padx=2)

    global Register
    Register = ttk.Button(Frame, text="Register", width=20, command=PreparingToMain(Frame))
    Register.grid(row=4, columnspan=2, sticky=tk.W, padx=2, pady=2)

    global ChangeToLogIn
    ChangeToLogIn = ttk.Button(Frame, text="LogIn", width=20, command=lambda: Warning("TEST"))
    ChangeToLogIn.grid(row=4, column=1, sticky=tk.E, pady=2)

    global WarningLabel
    WarningLabel = ttk.Label(Frame, text="", font=12)

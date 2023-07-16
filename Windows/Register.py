import tkinter as tk
from tkinter import ttk
from UsersInfo.Credentials import SaveCredentials
from Misc.Warning import AddWarning
from GoToMain import GoToMain


def PreparingToMain(Frame):  # Checks and then saves the credentials
    Credentials = {"UserName": UserNameInput.get(), "Email": EmailInput.get(), "Password": PasswordInput.get()}
    Check = SaveCredentials(Credentials)
    if Check:
        GoToMain(Frame)
    # The function below needs the error name, the warning widget label, and the widgets buttons
    elif isinstance(Check, str):
        AddWarning(Check, WarningLabel, Register, ChangeToLogIn)


UserNameInput = None
EmailInput = None
PasswordInput = None
Register = None
ChangeToLogIn = None
WarningLabel = None


# Main Register Window
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

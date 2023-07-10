import tkinter as tk

def AddWarning(WarningType, WarningLabel, Register, ChangeToLogIn): #Change the button's grid placement for text with warning
    print("Calling Warning with error: " + str(WarningType))
    WarningLabel.configure(text = str(WarningType))
    WarningLabel.grid(row=4, columnspan=2, sticky= tk.N)
    Register.grid_forget()
    ChangeToLogIn.grid_forget()
    Register.grid(row=5, columnspan=2, sticky = tk.W, padx=2, pady=2)
    ChangeToLogIn.grid(row=5, column=1, sticky = tk.E, pady=2)
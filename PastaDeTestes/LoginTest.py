import tkinter as tk
from tkinter import ttk



def Login():
    global LoginWindow
    LoginWindow = tk.Tk(className=" Login Window ")   # Root Window
    LoginWindow.geometry("500x500")
    global LoginMainFrame                      
    LoginMainFrame = tk.Frame(LoginWindow)
    LoginMainFrame.place(relx = 0.5, rely = 0.5, anchor= tk.CENTER)
    global LoginButton
    LoginButton = ttk.Button(LoginMainFrame, text="Register", width=20, command=Login)    # Register Button
    LoginButton.grid(row=1, columnspan=1, sticky = tk.W, padx=2, pady=2)
    return(LoginWindow)


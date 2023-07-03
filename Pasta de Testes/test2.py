import tkinter as tk
from tkinter import ttk
from test import Register

def Hello():
    Label = ttk.Label(LoginMainFrame, text="Hello!")
    Label.grid(row=2, column=0)
    RegisterButton.grid()

def Login():
    global LoginWindow
    LoginWindow = tk.Tk(className=" Register Window ")   # Root Window
    LoginWindow.geometry("500x500")
    global LoginMainFrame                      
    LoginMainFrame = tk.Frame(LoginWindow)
    LoginMainFrame.place(relx = 0.5, rely = 0.5, anchor= tk.CENTER)
    global RegisterButton
    RegisterButton = ttk.Button(LoginMainFrame, text="Register", width=20, command=Register)    # Register Button
    RegisterButton.grid(row=1, columnspan=1, sticky = tk.W, padx=2, pady=2)  



if __name__ == "__main__":
    Login()
    LoginWindow.mainloop()
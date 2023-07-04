import tkinter as tk
from tkinter import ttk
from test import Register


def Hello():
    Label = ttk.Label(MainFrame, text="Hello!")
    Label.grid(row=2, column=0)
    RegisterButton.grid()

def CurrentWindow(CurrentWindow, WantedWindow):
    CurrentWindow.destroy()
    if WantedWindow == "Register":
        print("Register window selected")
        i = Register()
        i.mainloop()

    

def Main():
    global MainWindow
    MainWindow = tk.Tk(className=" Main Window ")   # Root Window
    MainWindow.geometry("500x500")
    global MainFrame                      
    MainFrame = tk.Frame(MainWindow)
    MainFrame.place(relx = 0.5, rely = 0.5, anchor= tk.CENTER)
    global RegisterButton
    RegisterButton = ttk.Button(MainFrame, text="Register", width=20, command=lambda:CurrentWindow(MainWindow, "Register"))    # Register Button
    RegisterButton.grid(row=1, columnspan=1, sticky = tk.W, padx=2, pady=2)


Main()
MainWindow.mainloop()
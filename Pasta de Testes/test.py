import tkinter as tk
from tkinter import ttk


def Hello():
    Label = ttk.Label(RegisterMainFrame, text="Hello!")
    Label.grid(row=2, column=0)
    RegisterButton.grid()

def Register():
    global RegisterWindow
    RegisterWindow = tk.Tk(className=" Register Window ")   # Root Window
    RegisterWindow.geometry("500x500")
    global RegisterMainFrame                      
    RegisterMainFrame = tk.Frame(RegisterWindow)
    RegisterMainFrame.place(relx = 0.5, rely = 0.5, anchor= tk.CENTER)
    global RegisterButton
    RegisterButton = ttk.Button(RegisterMainFrame, text="Register", width=20)#, command=Login)    # Register Button
    RegisterButton.grid(row=1, columnspan=1, sticky = tk.W, padx=2, pady=2)
    return(RegisterWindow)



if __name__ == "__main__":
    Register()
    RegisterWindow.mainloop()
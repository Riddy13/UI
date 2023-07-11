import tkinter as tk
from tkinter import ttk

root = tk.Tk(className=" Register Window ")   # Root Window
root.geometry("500x500")                      

MainFrame = tk.Frame(root)
MainFrame.place(relx = 0.5, rely = 0.5, anchor= tk.CENTER)

def LoginToMain():
    


def LoginSection(Frame):
    TitleLabel = ttk.Label(Frame, text = "Register Window", font = 25)  # Title
    TitleLabel.grid(row = 0, columnspan= 2)                                 #
    
    global UserAndEmailNameInput
    UserAndEmailNameInput = ttk.Entry(Frame, width= 35)                      # 
    UserAndEmailNameInput.grid(row=1, column=1, sticky = tk.W, pady=2)           # User Name
    UserAndEmailNameInput = ttk.Label(Frame, text="User Name:")              #
    UserAndEmailNameInput.grid(row=1, column=0, sticky = tk.W, pady=2, padx=2)   #
    global PasswordInput
    PasswordInput = ttk.Entry(Frame, width = 35)                     #
    PasswordInput.grid(row = 3, column=1, sticky=tk.W, pady=2)           # Password
    PasswordLabel = ttk.Label(Frame, text="Password:")               #  
    PasswordLabel.grid(row = 3, column=0, sticky = tk.W, pady=2, padx=2) #
    global Register
    Register = ttk.Button(Frame, text="Register", width=20, command=LoginToMain)    # Register Button
    Register.grid(row=4, columnspan=2, sticky = tk.W, padx=2, pady=2)
    global ChangeToLogIn
    ChangeToLogIn = ttk.Button(Frame, text="LogIn", width = 20, command= lambda: Warning("TEST"))      # LogIn
    ChangeToLogIn.grid(row=4, column=1, sticky = tk.E, pady=2)
    global WarningLabel
    WarningLabel = ttk.Label(Frame, text="", font= 12)



# for tests:
if __name__ == "__main__":
    LoginSection(MainFrame)
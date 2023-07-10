import tkinter as tk            # Interface
from tkinter import ttk
from Credentials import SaveCredentials
from Warning import AddWarning

# Register window
root = tk.Tk(className=" Register Window ")   # Root Window
root.geometry("500x500")                      

MainFrame = tk.Frame(root)
MainFrame.place(relx = 0.5, rely = 0.5, anchor= tk.CENTER)






            
def RegisterToMain():
    Credentials = {"UserName": UserNameInput.get(), "Email": EmailInput.get(), "Password": PasswordInput.get()}
    Check = SaveCredentials(Credentials)
    if Check == True:
        pass # Go to Main
    elif isinstance(Check, str):
        AddWarning(Check, WarningLabel, Register, ChangeToLogIn)        


# Main Register Window
def RegisterSection():
    TitleLabel = ttk.Label(MainFrame, text = "Register Window", font = 25)  # Title
    TitleLabel.grid(row = 0, columnspan= 2)                                 #
    
    global UserNameInput
    UserNameInput = ttk.Entry(MainFrame, width= 35)                      # 
    UserNameInput.grid(row=1, column=1, sticky = tk.W, pady=2)           # User Name
    UserNameLabel = ttk.Label(MainFrame, text="User Name:")              #
    UserNameLabel.grid(row=1, column=0, sticky = tk.W, pady=2, padx=2)   #
    global EmailInput
    EmailInput = ttk.Entry(MainFrame, width = 35)                        #
    EmailInput.grid(row = 2, column=1, sticky = tk.W, pady = 2)          # Email
    EmailLabel = ttk.Label(MainFrame, text="E-mail:")                    #
    EmailLabel.grid(row = 2, column=0, sticky = tk.W, pady=2, padx = 2)  #
    global PasswordInput
    PasswordInput = ttk.Entry(MainFrame, width = 35)                     #
    PasswordInput.grid(row = 3, column=1, sticky=tk.W, pady=2)           # Password
    PasswordLabel = ttk.Label(MainFrame, text="Password:")               #  
    PasswordLabel.grid(row = 3, column=0, sticky = tk.W, pady=2, padx=2) #
    global Register
    Register = ttk.Button(MainFrame, text="Register", width=20, command=RegisterToMain)    # Register Button
    Register.grid(row=4, columnspan=2, sticky = tk.W, padx=2, pady=2)
    global ChangeToLogIn
    ChangeToLogIn = ttk.Button(MainFrame, text="LogIn", width = 20, command= lambda: Warning("TEST"))      # LogIn
    ChangeToLogIn.grid(row=4, column=1, sticky = tk.E, pady=2)
    global WarningLabel
    WarningLabel = ttk.Label(MainFrame, text="", font= 12)
            


if __name__ == "__main__":
    RegisterSection()
    root.mainloop()



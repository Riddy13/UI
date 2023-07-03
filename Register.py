import tkinter as tk            # Interface
from tkinter import ttk
import re                   # Mais funções para strings


# Register window
root = tk.Tk(className=" Register Window ")   # Root Window
root.geometry("500x500")                      

MainFrame = tk.Frame(root)
MainFrame.place(relx = 0.5, rely = 0.5, anchor= tk.CENTER)


def Warning(WarningType): #Change the button's grid placement for text with warning
    print("Calling Warning with error: " + str(WarningType))
    WarningLabel.configure(text = str(WarningType))
    WarningLabel.grid(row=4, columnspan=2, sticky= tk.N)
    Register.grid_forget()
    ChangeToLogIn.grid_forget()
    Register.grid(row=5, columnspan=2, sticky = tk.W, padx=2, pady=2)
    ChangeToLogIn.grid(row=5, column=1, sticky = tk.E, pady=2)



def ValidInfo(Credentials):
    RejecInputs = re.compile("[@_!#$%^&*()<>?/\|}{~:]")
    global ValidCred
    ValidCred = True
    
    # Username
    if RejecInputs.search(Credentials["UserName"]) or not "" in str(Credentials["UserName"]): #special characters and emtpy field
        Warning("Invalid username, don't use special characters") # Email
        ValidCred = False
        return

    elif len(str(Credentials["UserName"])) < 4: # 4 Minimum characters
        Warning("Username needs to be at least 4 characters")
        ValidCred = False
        return
    elif Credentials["UserName"] == "Admin": # Checks for admin
        return

    #  Email
    if "@" not in Credentials["Email"] or not "" in Credentials["Email"]: #  Needs to have a "@"and not be empty
        Warning("Invalid Email")
        ValidCred = False
        return
    elif len(str(Credentials["Email"])) < 3:
        Warning("Email needs to have at least 3 characters")
        ValidCred = False

    #Password
    if RejecInputs.search(Credentials["Password"]) or "" in str(Credentials["UserName"]): #special characters and emtpy field
        Warning("Invalid username, don't use special characters") # Email
        ValidCred = False
        return
    elif len(str(Credentials["UserName"])) < 4: # 4 Minimum characters
        Warning("Username needs to be at least 4 characters")
        ValidCred = False
        return



    # Check for existing credentials
    File = open('Credentials.txt', 'r')
    Lines = File.readlines()
    for line in Lines:
        # Turns the string into Dictionary so it can be used to check
        DataBase = eval(line)
        if DataBase["UserName"] != Credentials["UserName"]:
            ValidCred = True
        else:
            Warning("Username already being used")
            ValidCred = False
            return
        if DataBase["Email"] != Credentials["Email"]:
            ValidCred = True
        else:
            Warning("Email already being used")
            ValidCred = False
            return
            
        


def SaveCredentials():
    global Credentials
    Credentials = {"UserName": UserNameInput.get(), "Email": EmailInput.get(), "Password": PasswordInput.get()}
    print("Calling ValidInfo with: " + str(Credentials))
    
    try:# If file does not exist
        ValidInfo(Credentials)
    except:
        file = open(r'Credentials.txt', 'w') # Creates file
        file.write(str(Credentials) +  "\n")
        file.close
        return # Here should be going to the main window not return

    if ValidCred == True:# If file exists
        file = open(r'Credentials.txt', 'a')
        file.write(str(Credentials) +  "\n")
        file.close
        return # Here should be going to the main window not return




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
    Register = ttk.Button(MainFrame, text="Register", width=20, command=SaveCredentials)    # Register Button
    Register.grid(row=4, columnspan=2, sticky = tk.W, padx=2, pady=2)    
    global ChangeToLogIn
    ChangeToLogIn = ttk.Button(MainFrame, text="LogIn", width = 20, command= lambda: Warning("TEST"))      # LogIn
    ChangeToLogIn.grid(row=4, column=1, sticky = tk.E, pady=2)
    global WarningLabel
    WarningLabel = ttk.Label(MainFrame, text="", font= 12)
            


if __name__ == "__main__":
    RegisterSection()
    root.mainloop()



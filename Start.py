import tkinter as tk
from Windows.Register import RegisterSection
from Windows.Login import LoginSection

try:
    with open("romeo.txt", "r") as file:
        pass
except:
    with open(r'account.txt', 'w') as File:
        RememberAcc = {'Remember': False, 'UserName': '', 'Email': '', 'Password': ''}
        File.write(str(RememberAcc))

File = open(r'account.txt', 'r')
Account = File.readline(-1)
Account = eval(Account)

if Account["Remember"]:
    #go to main page as the account saved
    pass
else:
    pass
    # go to register or login

root = tk.Tk(className=" Register Window ")   # Root Window
root.geometry("500x500")

MainFrame = tk.Frame(root)
MainFrame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


if __name__ == "__main__":
    RegisterSection(MainFrame)
    root.mainloop()








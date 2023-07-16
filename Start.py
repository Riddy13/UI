import tkinter as tk
from Windows.Register import RegisterSection
from Windows.Login import LoginSection
from Windows.Main import MainSection

root = tk.Tk(className=" Register Window ")   # Root Window
root.geometry("1500x850")
MainFrame = tk.Frame(root)
MainFrame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

try:
    with open("account.txt", "r") as file:
        pass
except:
    with open(r'account.txt', 'w') as File:
        RememberAcc = {'Remember': False, 'UserName': '', 'Email': '', 'Password': ''}
        File.write(str(RememberAcc))

with open(r'account.txt', 'r') as File:
    Account = eval(File.readline(-1))

if Account["Remember"] == True:
    MainSection(MainFrame)
elif Account["Remember"] == False:
    LoginSection(MainFrame)
root.mainloop()








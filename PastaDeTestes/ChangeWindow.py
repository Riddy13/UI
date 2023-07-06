import tkinter as tk
from tkinter import ttk
from LoginTest import Login
from main import Main

global Window
Window = tk.Tk()
Window.geometry("250x250")
global MainFrame
MainFrame = tk.Frame(Window)
MainFrame.place(relx = 0.5, rely = 0.5, anchor= tk.CENTER)


def ChangeWindow(WantedWindow): # Destroy 
    for widget in MainFrame.winfo_children():
        widget.destroy()

    if WantedWindow == "Main":
        Window(className="Main")
        Main(Window)
        Window.mainloop()


if __name__ == "__main__":
    Main(Window)
    Main.mainloop()
    



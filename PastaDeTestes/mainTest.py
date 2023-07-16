import tkinter as tk

root = tk.Tk(className=" Register Window ")   # Root Window
root.geometry("500x500")

MainFrame = tk.Frame(root)
MainFrame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

def ChangeSize(Frame):
    root2 = Frame.winfo_toplevel()
    root2.geometry("200x200")


if __name__ == "__main__":
    root.mainloop()
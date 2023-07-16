import tkinter as tk
from tkinter import ttk


root = tk.Tk()


def MainSection(Frame):
    root2 = Frame.winfo_toplevel()
    root2.geometry("1000x850")
    MainLabel = ttk.Label(text="This is the main area!")
    MainLabel.grid(row=1, column=1)


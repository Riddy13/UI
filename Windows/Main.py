import tkinter as tk
from tkinter import ttk


def MainSection(Frame):
    MainLabel = ttk.Label(Frame, text="This is the main area!")
    MainLabel.grid(row=1, column=1)


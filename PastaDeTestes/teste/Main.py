import tkinter as tk
from add_widgets import add_widgets
from replace_widgets import replace_widgets

# Create the main window
window = tk.Tk()

# Create a frame
frame = tk.Frame(window)
frame.pack()

# Create a button to trigger widget replacement
add_widgets(frame)

# Start the Tkinter event loop
window.mainloop()

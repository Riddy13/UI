def ClearFrame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    return frame
from window2 import add_widgets


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def replace_widgets(frame):
    clear_frame(frame)
    add_widgets(frame)

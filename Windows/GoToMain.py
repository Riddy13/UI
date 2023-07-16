from Main import MainSection


def GoToMain(Frame):
    for widget in Frame.winfo_children():
        widget.destroy()
    MainSection(Frame)

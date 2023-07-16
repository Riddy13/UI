from Windows.Main import MainSection


def ClearFrame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def ToMain(frame):
    ClearFrame(frame)
    MainSection(frame)
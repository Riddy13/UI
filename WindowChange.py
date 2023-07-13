
def ChangeWindows(Frame, WantedWindow):
    for widgets in Frame.winfo_children():
      widgets.destroy()
    if WantedWindow == "Register":
        from Register import RegisterSection
        RegisterSection(Frame)

    if WantedWindow == "Login":
        from Login import LoginSection
        LoginSection(Frame)
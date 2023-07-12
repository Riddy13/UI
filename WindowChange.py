
def ChangeWindows(Frame, WantedWindow):
    from Login import LoginSection
    from Register import RegisterSection
    for widgets in Frame.winfo_children():
      widgets.destroy()
    
    if WantedWindow == "Register":
        RegisterSection(Frame)
    if WantedWindow == "Login":
        LoginSection(Frame)
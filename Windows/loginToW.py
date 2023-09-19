from Windows.Main import MainSection
from Windows.Register import RegisterSection
from Windows.clearCurrentFrame import ClearFrame

def ToMain(Frame):
    ClearFrame(Frame)
    MainSection(Frame)

def ToRegister(Frame):
    ClearFrame(Frame)
    RegisterSection(Frame)
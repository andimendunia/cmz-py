import wx
import wx.svg
import os
from cmz_py_ui import frMain

os.environ["WXSUPPRESS_SIZER_FLAGS_CHECK"] = "1"

#### FRAME MAIN ####

class frameMain(frMain):
    def __init__(self, parent):

        # Insiasi parent class
        frMain.__init__(self, parent)

#### MENYALAKAN APLIKASI ####


class MainApp(wx.App):
    def OnInit(self):
        self.frame = frameMain(None)
        self.SetTopWindow(self.frame)
        self.frame.Show(True)
        return True


if __name__ == "__main__":
    app = MainApp(redirect=False)
    app.MainLoop()

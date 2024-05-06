import wx


class MyFrame(wx.MDIParentFrame):
    def __init__(self, parent, title):
        super().__init__(parent, -1, title=title)

        menubar = wx.MenuBar()
        self.SetMenuBar(menubar)

        win = wx.MDIChildFrame(self, -1, 'Child Window', size=(200, 150))
        win.Show()


app = wx.App()

# frame = wx.Frame(None, title='Hello World!')
# frame.Show()

wnd = MyFrame(None, 'Hello World!')
wnd.Center()

wnd.Show()

app.MainLoop()

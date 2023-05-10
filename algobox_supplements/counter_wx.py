import wx

class CounterApp(wx.Frame):
    def __init__(self):
        super().__init__(None, title="CADENCE COUNTER", size=(300, 200))

        self.counter = 0

        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.count_label = wx.StaticText(self.panel, label=str(self.counter))
        self.sizer.Add(self.count_label, flag=wx.ALIGN_CENTER|wx.TOP, border=10)

        self.button_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.inc_button = wx.Button(self.panel, label="+")
        self.inc_button.Bind(wx.EVT_BUTTON, self.increment)
        self.button_sizer.Add(self.inc_button, flag=wx.RIGHT, border=10)

        self.clear_button = wx.Button(self.panel, label="clear")
        self.clear_button.Bind(wx.EVT_BUTTON, self.clear)
        self.button_sizer.Add(self.clear_button, flag=wx.RIGHT, border=10)

        self.dec_button = wx.Button(self.panel, label="-")
        self.dec_button.Bind(wx.EVT_BUTTON, self.decrement)
        self.button_sizer.Add(self.dec_button)

        self.sizer.Add(self.button_sizer, flag=wx.ALIGN_CENTER)

        self.panel.SetSizerAndFit(self.sizer)
        self.Show()

    def increment(self, event):
        self.counter += 1
        self.update_counter()

    def clear(self, event):
        self.counter = 0
        self.update_counter()

    def decrement(self, event):
        self.counter -= 1
        self.update_counter()

    def update_counter(self):
        self.count_label.SetLabel(str(self.counter))

if __name__ == "__main__":
    app = wx.App()
    frame = CounterApp()
    app.MainLoop()

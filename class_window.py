import tkinter as t

class WindowBase(t.Tk):
    def __init__(self, resolution, title, resize_horizontal, resize_vertical, force_focus):
        t.Tk.__init__(self)
        self.geometry(resolution)
        self.title(title)
        self.resizable(resize_horizontal, resize_vertical)
        if force_focus is True:
            self.focus_force()

import tkinter
from tkinter import *
from tkinter import ttk


class RightFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)


class LeftFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.invoke_widgets()

    def invoke_widgets(self):
        self.b1 = Button(self, text="Order").grid(row=0, column=0)
        self.b2 = Button(self, text="Menu").grid(row=0, column=1)
        self.b3 = Button(self, text="Pizza Maintain").grid(row=1, column=0)
        self.b4 = Button(self, text="Help").grid(row=1, column=1)


class MainWindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
# Main Window Configuration
        self.title("RODO Agreement Auto-Filler")
        self.minsize(1000, 400)

        self.invoke_widgets()

    def invoke_widgets(self):
        right_frame = RightFrame(self)
        right_frame.grid(row=0, column=1)

        left_frame = LeftFrame(self)
        left_frame.grid(row=0, column=0)


if __name__ == '__main__':
    m = MainWindow()
    m.mainloop()
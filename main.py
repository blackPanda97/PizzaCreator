import tkinter
import customtkinter as csTK
import left_frame as lf
import right_frame as rf

class MainWindow(csTK.CTk):
    def __init__(self):
        super().__init__()
# Main Window Configuration
        self.title("RODO Agreement Auto-Filler")
        self.minsize(1700, 400)

        right_frame = rf.RightFrame(self)
        right_frame.grid(row=0, column=1)


        left_frame = lf.LeftFrame(self)
        left_frame.grid(row=0, column=0)


if __name__ == '__main__':
    m = MainWindow()
    m.mainloop()
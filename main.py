import customtkinter as csTK
import menu_frame as mf
import order_frame as of
import maintain_frame as mpf
import help_frame as hf
import main_frame as mf


class MainWindow(csTK.CTk):
    def __init__(self):
        super().__init__()

# Main Window Configuration
        self.title("Pizzeria")
        self.minsize(600, 800)

        main = mf.MainFrame(self)
        main.grid(row=0, column=0, sticky='we')

if __name__ == '__main__':
    m = MainWindow()
    m.mainloop()
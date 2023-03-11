import customtkinter as csTK
import main_frame as mf


class MainWindow(csTK.CTk):
    def __init__(self):
        super().__init__()

# Main Window Configuration
        self.title("Pizzeria")
        self.minsize(600, 800)
        self.configure(fg_color="#E6D386")

        main = mf.MainFrame(self)
        main.grid(row=0, column=0, sticky='we')

if __name__ == '__main__':
    m = MainWindow()
    m.mainloop()
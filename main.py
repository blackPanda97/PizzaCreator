import tkinter
import customtkinter as csTK


class RightFrame(csTK.CTkFrame):
    def __init__(self, container):
        super().__init__(container)
        self.invoke_widget()

    def invoke_widget(self):
        self.label = csTK.CTkLabel(self, text="Welcome").grid(row=0, column=0)


class LeftFrame(csTK.CTkFrame):
    def __init__(self, container):
        super().__init__(container)
        self.invoke_widgets()

    def invoke_widgets(self):
# Adding Button Images
        b1_img = tkinter.PhotoImage(file="img/delivery.png")
        b2_img = tkinter.PhotoImage(file="img/menu.png")
        b3_img = tkinter.PhotoImage(file="img/maintain.png")
# Specyfing Button Font
        button_font = csTK.CTkFont(family="Arial", size=40, weight="bold")
# Adding Buttons Themselves
        self.b1 = csTK.CTkButton(self,
                                 text="Order", font=button_font,
                                 image=b1_img.subsample(6,6),
                                 height=200).grid(row=0, column=0, columnspan=2, sticky="we")
        self.b2 = csTK.CTkButton(self,
                                 text="Menu", font=button_font,
                                 image=b2_img.subsample(6,6),
                                 width=200, height=200).grid(row=1, column=0)
        self.b3 = csTK.CTkButton(self,
                                 text="Pizza Maintain", font=button_font,
                                 image=b3_img.subsample(6,6),
                                 width=200, height=200).grid(row=1, column=1)


class MainWindow(csTK.CTk):
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
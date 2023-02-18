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
# Adding Button Functions
        def b1_func():
            print("welcum")

        def b2_func():
            print("welcum")

        def b3_func():
            print("welcum")

# Adding Button Images
        b1_img = tkinter.PhotoImage(file="img/delivery.png")
        b2_img = tkinter.PhotoImage(file="img/menu.png")
        b3_img = tkinter.PhotoImage(file="img/maintain.png")
# Specyfing Button Font, Border Width, Colour
        button_font = csTK.CTkFont(family="Arial", size=40, weight="bold")
        button_bd_width=3
        button_bd_colour="#327F96"
        button_bd_spacing=50
        button_pad=3
# Adding Buttons Themselves
        self.b1 = csTK.CTkButton(self,
                                 text="Order", font=button_font,
                                 image=b1_img.subsample(4,4),  fg_color="#7B3296",
                                 height=200,
                                 border_width=button_bd_width, border_spacing=button_bd_spacing, border_color=button_bd_colour,
                                 command=b1_func).grid(row=0, column=0, columnspan=2, sticky="we", padx=(button_pad), pady=(button_pad))
        self.b2 = csTK.CTkButton(self,
                                 text="Menu", font=button_font,
                                 image=b2_img.subsample(6,6),  fg_color="#964932",
                                 width=200, height=200,
                                 border_width=button_bd_width, border_spacing=button_bd_spacing, border_color=button_bd_colour,
                                 command=b2_func).grid(row=1, column=0, padx=(button_pad), pady=(button_pad))
        self.b3 = csTK.CTkButton(self,
                                 text="Pizza Maintain", font=button_font,
                                 image=b3_img.subsample(6,6),  fg_color="#4D9632",
                                 width=200, height=200,
                                 border_width=button_bd_width, border_spacing=button_bd_spacing, border_color=button_bd_colour,
                                 command=b3_func).grid(row=1, column=1, padx=(button_pad), pady=(button_pad))


class MainWindow(csTK.CTk):
    def __init__(self):
        super().__init__()
# Main Window Configuration
        self.title("RODO Agreement Auto-Filler")
        self.minsize(1700, 400)

        self.invoke_widgets()

    def invoke_widgets(self):
        right_frame = RightFrame(self)
        right_frame.grid(row=0, column=1)

        left_frame = LeftFrame(self)
        left_frame.grid(row=0, column=0)


if __name__ == '__main__':
    m = MainWindow()
    m.mainloop()
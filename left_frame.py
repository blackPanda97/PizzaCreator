import customtkinter
from PIL import Image
from main import *
from right_frame import RightFrame


class LeftFrame(csTK.CTkFrame):

    def __init__(self, container):
        super().__init__(container)
# Adding Button Functions
        def b_func(self, x):
            print(x)

# Specyfing Button Font, Border Width, Colour
        button_font = csTK.CTkFont(family="Arial", size=40, weight="bold")
        button_bd_width = 3
        button_bd_colour = "#327F96"
        button_bd_spacing = 50
        button_pad = 3
        button_img_size = (100, 100)
# Adding Button Images
        b1_img = customtkinter.CTkImage(light_image=Image.open("img/delivery.png"), size=button_img_size)
        b2_img = customtkinter.CTkImage(light_image=Image.open("img/menu.png"), size=button_img_size)
        b3_img = customtkinter.CTkImage(light_image=Image.open("img/maintain.png"), size=button_img_size)
# Adding Buttons Themselves
        self.b1 = csTK.CTkButton(self,
                                 text="Order", font=button_font,
                                 image=b1_img,  fg_color="#7B3296",
                                 height=200,
                                 border_width=button_bd_width, border_spacing=button_bd_spacing, border_color=button_bd_colour,
                                 command=b_func(self, 1)).grid(row=0, column=0, columnspan=2, sticky="we", padx=(button_pad), pady=(button_pad))
        self.b2 = csTK.CTkButton(self,
                                 text="Menu", font=button_font,
                                 image=b2_img,  fg_color="#964932",
                                 width=200, height=200,
                                 border_width=button_bd_width, border_spacing=button_bd_spacing, border_color=button_bd_colour,
                                 command=b_func(self, 2)).grid(row=1, column=0, padx=(button_pad), pady=(button_pad))
        self.b3 = csTK.CTkButton(self,
                                 text="Pizza Maintain", font=button_font,
                                 image=b3_img,  fg_color="#4D9632",
                                 width=200, height=200,
                                 border_width=button_bd_width, border_spacing=button_bd_spacing, border_color=button_bd_colour,
                                 command=b_func(self, 3)).grid(row=1, column=1, padx=(button_pad), pady=(button_pad))

import customtkinter as csTK


class MenuFrame(csTK.CTkFrame):
    def __init__(self):
        menu_lb = csTK.CTkLabel(text="Hello").grid(row=0, column=0)
from main import *


class RightFrame(csTK.CTkFrame):

    def __init__(self, container):
        super().__init__(container)
        self.container = container

    def menu(self, container):
        menu_lb = csTK.CTkLabel(master=container, text="HELLO").grid(row=0, column=0)



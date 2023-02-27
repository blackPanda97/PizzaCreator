from main import *


class OrderFrame(csTK.CTkFrame):

    def __init__(self, container):
        super().__init__(container)

        self.label = csTK.CTkLabel(self, height=300, fg_color="blue", text="Order Frame").grid(row=0, column=0)
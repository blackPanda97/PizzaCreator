from main import *


class MaintainFrame(csTK.CTkFrame):

    def __init__(self, container):
        super().__init__(container)

        self.label = csTK.CTkLabel(self, text="Welcome2").grid(row=0, column=0)
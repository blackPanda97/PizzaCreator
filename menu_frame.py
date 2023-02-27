from main import *


class MenuFrame(csTK.CTkFrame):

    def __init__(self, container):
        super().__init__(container)

        self.label = csTK.CTkLabel(self, height=400, fg_color="brown", text="Menu Frame").grid(row=0, column=0)
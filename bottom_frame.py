from main import *


class BottomFrame(csTK.CTkFrame):

    def __init__(self, container):
        super().__init__(container)

        self.label = csTK.CTkLabel(self, text="Bottom FRAME").grid(row=0, column=0)

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

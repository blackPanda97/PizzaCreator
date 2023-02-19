from main import *

class OrderPage(csTK.CTkScrollableFrame):
    def __init__(self, container):
        super().__init__(container)

        self.l1 = csTK.CTkLabel(OrderPage, text="NOOOOOOOOOOOOOOOOOO").grid(row=0, column=0)
        self.l2 = csTK.CTkLabel(OrderPage, text="PAPAPA").grid(row=1, column=1)
from main import *


class MaintainFrame(csTK.CTkFrame):

    def __init__(self, container):
        super().__init__(container)
        self.configure(self, fg_color="#E6D386")

        main_f = csTK.CTkFont(family="Arial", size=30, weight="bold")

        def b_choice(value):
            print(value)
            if value == "Add":
                e = csTK.CTkEntry(self, )

        def op_choice(value):
            print(value)


        csTK.CTkLabel(self,
                      text="Chose an item to maintain",
                      text_color="black",
                      font=main_f).grid(row=0, column=0, padx=5)

        csTK.CTkOptionMenu(master=self,
                                values=("Meat Toppings", "Veggie Toppings", "Cheese Toppings", "Sauces"),
                                font=main_f, fg_color="#7b3296",
                                dropdown_fg_color="black",
                                dropdown_font=csTK.CTkFont(family="Arial", size=15, weight="bold"),
                                command=op_choice).grid(row=0, column=1, padx=5)

        csTK.CTkLabel(self,
                      text="Id",
                      font=main_f,
                      fg_color="black").grid(row=1, column=0)
        csTK.CTkLabel(self,
                      text="Name",
                      font=main_f,
                      fg_color="black").grid(row=2, column=0)

        csTK.CTkEntry(self,
                      placeholder_text="Id").grid(row=1, column=1)
        csTK.CTkEntry(self,
                      placeholder_text="Name").grid(row=2, column=1)

        csTK.CTkSegmentedButton(self,
                                values=["Add", "Remove"],
                                font=main_f,
                                fg_color="#7b3296",
                                command=b_choice).grid(row=3, column=0, padx=5, columnspan=2)
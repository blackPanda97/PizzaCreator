from main import *


class MaintainFrame(csTK.CTkFrame):

    def __init__(self, container):
        super().__init__(container)
        self.configure(self, fg_color="#E6D386")

#Overall properties of buttons and labels
        main_f = csTK.CTkFont(family="Arial", size=20, weight="bold")
        selected_cl = "#671313"
        unselected_cl = "#D1595A"
        foreground_cl = "#E6D386"
        unselected_hover_cl="#5C7758"

#Add or Remove Button Function
        def b_choice(value, value2=0):
            print(value, value2)

#Segmented Button Function
        def op_choice(value):
            print(value)


        csTK.CTkLabel(self,
                      text="Item to maintain",
                      text_color="black",
                      font=main_f).grid(row=0, column=2, padx=5)

        csTK.CTkOptionMenu(self,
                                values=("Meat Toppings", "Veggie Toppings", "Cheese Toppings", "Sauces"),
                                font=main_f,
                                fg_color=unselected_cl,
                                button_color=unselected_cl,
                                text_color="black",
                                dropdown_fg_color=foreground_cl,
                                dropdown_font=main_f,
                                dropdown_text_color="black",
                                command=op_choice).grid(row=1, column=2, padx=5)

#Entry places and Labels
        csTK.CTkLabel(self,
                      text="Id",
                      text_color="black",
                      font=main_f).grid(row=0, column=0)
        csTK.CTkLabel(self,
                      text="Name",
                      text_color="black",
                      font=main_f).grid(row=1, column=0)

        csTK.CTkEntry(self,
                      placeholder_text="Id",
                      font=main_f).grid(row=0, column=1)
        csTK.CTkEntry(self,
                      placeholder_text="Name",
                      font=main_f).grid(row=1, column=1)

#Buttons to submit the action
        csTK.CTkSegmentedButton(self,
                                values=["Add", "Remove"],
                                font=main_f,
                                fg_color=foreground_cl,
                                selected_color=selected_cl,
                                unselected_color=unselected_cl,
                                unselected_hover_color=unselected_hover_cl,
                                command=b_choice).grid(row=3, column=0, padx=5, columnspan=4)
from main import *
import menu_frame as mf
import order_frame as of
import maintain_frame as mpf
import help_frame as hf

class BottomFrame(csTK.CTkFrame):

    def __init__(self, container):
        super().__init__(container)


        self.label = csTK.CTkLabel(self, text="Bottom FRAME").grid(row=1, column=0)

    # Adding Function to change the Main Frame
    value=0
    def sb_func(self, value):
        #self.bf.clear()

        if value == "Menu":
            print("Menu Chosen")
            menu_frame = mf.MenuFrame(self)
            menu_frame.grid(row=0, column=0)

        elif value == "Order":
            print("Order Chosen")
            order_frame = of.OrderFrame(self)
            order_frame.grid(row=0, column=0)

        elif value == ("Maintain"):
            print("Maintain Chosen")
            maintain_frame = mpf.MaintainFrame(self)
            maintain_frame.grid(row=0, column=0)

        elif value == "Help":
            print("Help Chosen")
            help_frame = hf.HelpFrame(self)
            help_frame.grid(row=0, column=0)

        else:
            print("nothing chosen")

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

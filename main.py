import customtkinter as csTK
import menu_frame as mf
import order_frame as of
import maintain_frame as mpf
import help_frame as hf


class MainWindow(csTK.CTk):
    def __init__(self):
        super().__init__()

# Main Window Configuration
        self.title("Pizzeria")
        self.minsize(600, 800)

# Segmented Button Specification
        b_border_width = 5
        b_fg_color = "#7b3296"
        b_font = csTK.CTkFont(family="Arial", size=30, weight="bold")
        b_corner_radius = 10

# Adding Function to change the Main Frame
        def sb_func(value):
            #for widget in main_frame.winfo_children():
                #widget.destroy()

            if value == "Menu":
                print("Menu Chosen")
                main_frame = mf.MenuFrame(self)
                main_frame.grid(row=1, column=0)

            elif value == "Order":
                print("Order Chosen")
                order_frame = of.OrderFrame(self)
                order_frame.grid(row=1, column=0)

            elif value == ("Maintain"):
                print("Maintain Chosen")
                maintain_frame = mpf.MaintainFrame(self)
                maintain_frame.grid(row=1, column=0)

            elif value == "Help":
                print("Help Chosen")
                help_frame = hf.HelpFrame(self)
                help_frame.grid(row=1, column=0)

            else:
                print("nothing chosen")

# Adding Segmented Button to the Main Window
        self.main_button = csTK.CTkSegmentedButton(self,
                                                   values=["Menu", "Order", "Maintain", "Help"],
                                                   command=sb_func,
                                                   font=b_font,
                                                   border_width=b_border_width,
                                                   fg_color=b_fg_color,
                                                   corner_radius=b_corner_radius).grid(row=0, column=0, sticky="we")

# Adding Main Frame to the Main Window



if __name__ == '__main__':
    m = MainWindow()
    m.mainloop()
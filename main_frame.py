from main import *
import bottom_frame



class MainFrame(csTK.CTkFrame):

    def __init__(self, container):
        super().__init__(container)

# Frame Configuration
        self.configure(self, fg_color="white")

# Adding Bottom Frame Cointaining other frames
        self.bf = bottom_frame.BottomFrame(self)
        self.bf.grid(row=1, column=0, padx=10, pady=10)

        # Segmented Button Specification
        b_border_width = 5
        b_fg_color = "#7b3296"
        b_font = csTK.CTkFont(family="Arial", size=50, weight="bold")
        b_corner_radius = 10
        b_padx = 10
        b_pady = 0

        # Adding Function to change the Main Frame
        def sb_func(value):
            self.bf.clear()

            if value == "Menu":
                print("Menu Chosen")
                menu_frame = mf.MenuFrame(self)
                menu_frame.grid(row=1, column=0)

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

        main_button = csTK.CTkSegmentedButton(self,
                                              values=["Menu", "Order", "Maintain", "Help"],
                                              command=sb_func,
                                              font=b_font,
                                              border_width=b_border_width,
                                              fg_color=b_fg_color,
                                              corner_radius=b_corner_radius).grid(row=0, column=0, padx=b_padx, pady=b_pady)
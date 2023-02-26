from main import *


class MainFrame(csTK.CTkFrame):

    def __init__(self, container):
        super().__init__(container)

        self.configure(self, fg_color="white")

        # Segmented Button Specification
        b_border_width = 5
        b_fg_color = "#7b3296"
        b_font = csTK.CTkFont(family="Arial", size=50, weight="bold")
        b_corner_radius = 10

        # Adding Function to change the Main Frame
        def sb_func(value):
            # for widget in main_frame.winfo_children():
            # widget.destroy()

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

        # Adding Segmented Button to the Main Window
        #self.top_frame = csTK.CTkFrame(self, border_width=b_border_width).grid(row=0, column=0, sticky="we")
        #self.bottom_frame = csTK.CTkFrame(self, border_width=b_border_width).grid(row=1, column=0, sticky="we")
        main_button = csTK.CTkSegmentedButton(self,
                                              values=["Menu", "Order", "Maintain", "Help"],
                                              command=sb_func,
                                              font=b_font,
                                              border_width=b_border_width,
                                              fg_color=b_fg_color,
                                              corner_radius=b_corner_radius,).grid(row=0, column=0)
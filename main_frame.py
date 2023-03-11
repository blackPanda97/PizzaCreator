from main import *
import bottom_frame



class MainFrame(csTK.CTkFrame):

    def __init__(self, container):
        super().__init__(container)

# Frame Configuration
        self.bf = bottom_frame.BottomFrame(self)


        # Segmented Button Specification
        b_border_width = 5
        b_fg_color = "#E6D386"
        b_font = csTK.CTkFont(family="Arial", size=50, weight="bold")
        b_corner_radius = 15
        b_padx = 0
        b_pady = 0

        def b_cm(value):
            print("Wybrano: ", value)
            self.bf.grid(row=1, column=0)

            self.bf.sb_func(value)


        main_button = csTK.CTkSegmentedButton(self,
                                              values=["Menu", "Order", "Maintain", "Help"],
                                              command=b_cm,
                                              font=b_font,
                                              border_width=b_border_width,
                                              fg_color=b_fg_color,
                                              unselected_color="#D1595A",
                                              selected_color="#671313",
                                              unselected_hover_color="#5C7758",
                                              corner_radius=b_corner_radius).grid(row=0, column=0, padx=b_padx, pady=b_pady)

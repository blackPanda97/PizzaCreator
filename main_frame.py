from main import *
import bottom_frame



class MainFrame(csTK.CTkFrame):

    def __init__(self, container):
        super().__init__(container)

# Frame Configuration
        self.configure(self, fg_color="white")
        self.bf = bottom_frame.BottomFrame(self)

# Adding Bottom Frame Cointaining other frames
        #self.bf = bottom_frame.BottomFrame(self)
        #self.bf.grid(row=1, column=0, padx=10, pady=10)

        # Segmented Button Specification
        b_border_width = 5
        b_fg_color = "#7b3296"
        b_font = csTK.CTkFont(family="Arial", size=50, weight="bold")
        b_corner_radius = 10
        b_padx = 10
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
                                              corner_radius=b_corner_radius).grid(row=0, column=0, padx=b_padx, pady=b_pady)
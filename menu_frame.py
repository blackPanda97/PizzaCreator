import database
from main import *
from database import *


class MenuFrame(csTK.CTkFrame):


    def __init__(self, container):
        super().__init__(container)

        self.configure(self, fg_color="red")

        self.grid_info_lbl = csTK.CTkLabel(self,
                                           fg_color="white",
                                           text="Menu Frame").grid(row=0, column=0, columnspan=3)

# Setting menu specification
        m_font = csTK.CTkFont(family="arial", size=20, weight="bold")



        sm = show_menu()
        total_rows = len(sm)
        total_columns = len(sm[0])
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = csTK.CTkEntry(self, font=m_font, fg_color="transparent")

                self.e.grid(row=i, column=j)
                self.e.insert(csTK.END, sm[i][j])






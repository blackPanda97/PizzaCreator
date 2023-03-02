import database
from main import *
from database import *


class MenuFrame(csTK.CTkFrame):

    def show_menu(self):
        print("Showing menu")
        sql_querry = database.show_menu
        for x in sql_querry:
            print(x)

    def __init__(self, container):
        super().__init__(container)

        self.configure(self, fg_color="red", height=500, width=500)

        self.grid_info_lbl = csTK.CTkLabel(self,
                                           fg_color="white",
                                           text="Menu Frame").grid(row=0, column=0, columnspan=3)

        sm = show_menu()
        total_rows = len(sm)
        total_columns = len(sm[0])
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = csTK.CTkEntry(self)

                self.e.grid(row=i, column=j)
                self.e.insert(csTK.END, sm[i][j])






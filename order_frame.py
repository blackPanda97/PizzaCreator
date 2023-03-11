from main import *


class OrderFrame(csTK.CTkFrame):



    def __init__(self, container):
        super().__init__(container)

        m_font = csTK.CTkFont(family="Arial", size=20, weight="bold")

        self.l1 = csTK.CTkLabel(self, text="1st name & Surname", font=m_font).grid(row=0, column=0, padx=(0,20))
        self.name = csTK.CTkEntry(self, placeholder_text="Name").grid(row=0, column=1, padx=10)
        self.surname = csTK.CTkEntry(self, placeholder_text="Surname").grid(row=0, column=2, padx=(10, 0))

        self.l2 = csTK.CTkLabel(self, text="Street name & Street number", font=m_font).grid(row=1, column=0, padx=(0, 20))
        self.str_name = csTK.CTkEntry(self, placeholder_text="Street name").grid(row=1, column=1, padx=10)
        self.str_nr = csTK.CTkEntry(self, placeholder_text="Street number").grid(row=1, column=2, padx=(10, 0))

        self.l3 = csTK.CTkLabel(self, text="House & Flat", font=m_font).grid(row=2, column=0, padx=(0, 20))
        self.house_nr = csTK.CTkEntry(self, placeholder_text="House number").grid(row=2, column=1, padx=10)
        self.flat_nr = csTK.CTkEntry(self, placeholder_text="Flat number").grid(row=2, column=2, padx=(10, 0))

        self.l4 = csTK.CTkLabel(self, text="Phone Number", font=m_font).grid(row=3, column=0, padx=(0, 20))
        self.phone_nr = csTK.CTkEntry(self, placeholder_text="Phone number").grid(row=3, column=1, columnspan=2)



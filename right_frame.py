from main import *



class RightFrame(csTK.CTkFrame):

    def __init__(self, container):
        super().__init__(container)
        self.invoke_widget()

    def invoke_widget(self):
        self.label = csTK.CTkLabel(self, text="Welcome").grid(row=0, column=0)

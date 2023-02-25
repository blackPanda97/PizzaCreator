from main import *



class RightFrame(csTK.CTkFrame):
    right_windows = [w_menu, w_order, w_maintain, w_help]
    w_menu = menu

    def __init__(self, container, choice: int):
        super().__init__(container)
        self.choice = choice
        self.container = container
        def window_to_show(self):


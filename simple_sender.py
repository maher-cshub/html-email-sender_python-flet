from flet import *

class Simple_Sender(UserControl):
    def __init__(self, page: Page):
        super().__init__(self)
        self.text = Text()

    def build(self):
        return self.text

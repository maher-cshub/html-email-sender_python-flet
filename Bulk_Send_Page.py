
import flet as ft



class Bulk_Send_Page(ft.UserControl):
    def __init__(self):
        super().__init__(self)
        self.content = ft.Column(
               
            [
                ft.Row(
                [
                    ft.Text("Comming Later !", size=30)
                    ], 
                alignment=ft.MainAxisAlignment.CENTER
            ),

            ]
        )
        
    def build(self):
        return self.content
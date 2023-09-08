from flet import * ## app, Page, AppBar,Text,IconButton,colors,icons,WEB_BROWSER,Container,animation,UserControl
from simple_sender import  Simple_Sender
from App_Layout import set_layout
from Simple_Send_Page import Simple_Send_Page
from Bulk_Send_Page import Bulk_Send_Page




def main(page: Page):
    set_layout(page)
    
    

    page.add(
        Container(
            content=Column([
                Simple_Send_Page(page),
                
            ])
        )
    )
    



app(port=8550, target=main, view=WEB_BROWSER)
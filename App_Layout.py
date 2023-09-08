from flet import *
from Simple_Send_Page import Simple_Send_Page
from Bulk_Send_Page import Bulk_Send_Page




def change_theme(page):
    print(page)
    if (page.theme_mode == "LIGHT"):
        page.theme_mode = "DARK"
    else:
        page.theme_mode = "LIGHT"
    
def set_layout(page: Page):
    
    def change_view(e):
        page.clean()
        index = e.control.selected_index
        
        if(index == 0):
            page.add(Simple_Send_Page(page))
            
        if(index == 1):
            page.add(Bulk_Send_Page())
        

    ##THEME
    page.theme_mode = "LIGHT"

    ##DIMENSIONS
    page.window_max_height = 1800
    page.window_height = 800
    page.window_max_width = 1800
    page.window_width = 600
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
        "Open Sans": "/fonts/OpenSans-Regular.ttf"
    }
    page.title = "HTML Email Sender"
    page.horizontal_alignment = "center"
    page.appbar = AppBar(
        title=Text("HTML Email Sender"),
        center_title=False,
        bgcolor=colors.CYAN_300,
        actions=[
            IconButton(icons.WB_SUNNY_OUTLINED,on_click=change_theme(page)),
        ],
    )

    ##NAV BAR
    page.navigation_bar = NavigationBar(
        destinations=[
            NavigationDestination(icon=icons.SEND, label="Simple Send"),
            NavigationDestination(icon=icons.FORMAT_LIST_NUMBERED, label="Bulk Send")
        ],
        selected_index=0,
        on_change=change_view,
    
    )
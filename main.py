import flet as ft


def main(page: ft.Page):
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    page.appbar = ft.AppBar(
        leading_width=40,
        title=ft.Text("HTML Email Sender"),
        center_title=False,
        bgcolor=ft.colors.CYAN_300,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
        ],
    )
    page.add(ft.Text("Body!"))

ft.app(port=8550, target=main, view=ft.WEB_BROWSER)
from flet import *
from pages.format_entery_page import format_entry
from pages.Home_page import first_page

def main(page:Page):
    page.title = "Teacher_App"
    page.scroll = "auto"
    page.window.top = 1
    page.window.left = 960
    page.window.width = 390
    page.window.height = 740
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.bgcolor = "#E0F7FA"
    page.theme_mode = ThemeMode.LIGHT
    

    

    def route_change(route):
        page.controls.clear()
        if page.route == "/format_entry":
            page.add(Container(
                content=Column(
                    controls=[

                        format_entry(page)

                    ],alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER
                ),alignment=alignment.center))
        else:
            page.add(Container(
                content=Column(
                    controls=[
                        first_page(page)
                    ],alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER
                ),alignment=alignment.center))
            
        page.update()

    page.on_route_change = route_change
    page.go("/")            



app(main)
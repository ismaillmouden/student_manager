from flet import *

def first_page(page):
    return Column(controls=[
                Row([
                    Image(src="logo.png",
                          width=250,
                          height=250)
                ],alignment=MainAxisAlignment.CENTER),
                Row([
            Text("\n\n\nمرحبا بك في تطبيق الطالب و المعلم",
                 size=20,color="#004D40",
                 weight="bold")   
        ],alignment=MainAxisAlignment.CENTER),
                Row([
                        ElevatedButton(text="إبدأ",
                                    bgcolor="#D32F2F",
                                    color="#FFFFFF",
                                    on_click=lambda _: page.go("/format_entry"),
                                    width=150,
                                    height=50)  
        ],alignment=MainAxisAlignment.CENTER)
    ]

    )
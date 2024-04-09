import flet as ft

def navega_outra_tela():
    pass



meus_pedidos = ft.Container(
    content=ft.Text("MEUS PEDIDOS", color="white"),
    bgcolor="blue",
    border_radius=100,
    width=150,
    height=35,
    alignment=ft.alignment.center,
)

quadrado = ft.Container(bgcolor='blue', width=50, height=50,content=ft.Icon(name=ft.icons.STAR_BORDER, color=ft.colors.WHITE, size=50))

material = ft.Container(
    bgcolor='blue',
    content=ft.Text("TENIS", color="white"),
    border_radius=100,
    width=150,
    height=35,
    alignment=ft.alignment.center
)


def main(page):
    page.add(
        
        ft.Column(
            [
                ft.Row(
                    [
                        meus_pedidos,
                        ft.Icon(name=ft.icons.ADD, color=ft.colors.BLUE, size=50)
                    ]
                ),
                ft.Row([quadrado, material]),
                ft.Row([quadrado, material]),
                ft.Row([quadrado, material]),
                ft.Row([quadrado, material]),
                ft.Row([quadrado, material]),
                ft.Row([quadrado, material]),
                ft.Row([quadrado, material])
            ]
        )
    )


ft.app(target=main)

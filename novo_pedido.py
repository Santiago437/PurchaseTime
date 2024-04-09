import flet as ft




 
logo = ft.Image(src="logo.jpg" , width=100 , height=100)
container = ft.Container(bgcolor='blue',content= logo,
                             shape=ft.BoxShape.CIRCLE,clip_behavior=ft.ClipBehavior.ANTI_ALIAS, )
produto = ft.TextField(bgcolor="blue",border_radius=50,width=120)
fornecedor = ft.TextField(bgcolor="blue",border_radius=50,width=120)
frequencia = ft.TextField(bgcolor="blue",border_radius=50,width=120)
quantidade = ft.TextField(bgcolor="blue",border_radius=50,width=120)
def main(page):

    page.add(
          container,
          ft.Column([
              ft.Row([ft.Text("PRODUTO",width=120,bgcolor="blue"),produto]),
              ft.Row([ft.Text("FORNECEDOR",width=120,bgcolor="blue"),fornecedor]),
              ft.Row([ft.Text("FREQUÊNCIA",width=120,bgcolor="blue"),frequencia]),
              ft.Row([ft.Text("QUANTIDADE",width=120,bgcolor="blue"),quantidade]),
              ft.Row])
            


           )






    
ft.app(target=main)
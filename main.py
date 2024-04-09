import flet as ft
import sqlite3
conn = sqlite3.connect("db/dbcad.db", check_same_thread = False)

def main(page):
    def cadastro(e):
        nome = entrada_nome.value
        senha = entrada_senha.value
        try:
            c = conn.cursor()
            c.execute("INSERT INTO users (email,senha) VALUES(?,?)  ",(nome,senha))
            conn.commit()
            print("Sucesso")
        except Exception as e:
            print(e)
        

    entrada_nome = ft.TextField(label="Digite o seu email",border_radius=100,bgcolor='blue',color='white')
    entrada_senha = ft.TextField(label="Digite a sua senha",border_radius=100,bgcolor='blue')
    logo = ft.Image(src="images.jpg")
    container = ft.Container(bgcolor='red',content= logo,
                             shape=ft.BoxShape.CIRCLE,clip_behavior=ft.ClipBehavior.ANTI_ALIAS, )



    page.add(
        ft.Text("Auxiliar de Compras"),
        container,
        entrada_nome,
        entrada_senha,
        ft.ElevatedButton("Entrar"),
        ft.ElevatedButton("Cadastre - se", on_click=cadastro )
        )
ft.app(target=main)
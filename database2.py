import sqlite3


def create_connection():
  """ Cria uma conexão com o banco de dados. """
  conn = sqlite3.connect('cadastro.db')
  return conn

def create_table(conn):
  """ Cria a tabela 'usuarios' no banco de dados. """
  cursor = conn.cursor()
  cursor.execute('''CREATE TABLE IF NOT EXISTS pedidos (
                      nome text,
                      senha text
                  )''')
  conn.commit()

conn = create_connection()
create_table(conn)
conn.close()
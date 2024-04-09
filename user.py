import sqlite3
conn = sqlite3.connect("db/dbcad.db", check_same_thread = False)

def create_table():
    c = conn.cursor()
    c.execute(""" CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,
              email TEXT,
              senha TEXT,
              ) """)
    conn.commit()
create_table()

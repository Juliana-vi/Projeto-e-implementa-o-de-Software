import sqlite3

conn = sqlite3.connect('estoque.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXIST itens (
    id  INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL
    quantidade INTEGER NOT NULL 
               );
               """)

conn.commit()
conn.close()
print('Banco de Dados criado com sucesso')
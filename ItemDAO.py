import sqlite3
import pandas as pd
from model import Item

DB_ITEM = 'estoque.db'

def get_db_connection():
    conn = sqlite3.connect(estoque.db)
    return conn

def add_item(item:Item):
    #item:Item - item é o parâmetro, Item é o tipo do parametro
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO itens (descricao, quantidade) VALUES (?)",
        # values tem id, por ser autoincrementador não é necessário indicar
        (item.descricao, item.quantidade)
    )
    conn.commit()
    conn.close()

def list_all_itens() -> List[Item]:
    # esse List ajuda a definir o tipo de saída esperada
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM itens ORDER BY id ASC")
    rows = cursor.fetchall()
    conn.close()
    # fecha a conexão pq daqui pra frente o DAO q trabalha
    # parecido com o from_dict do json
    return [
        Item(
            id=row['id'],
            descricao=row['descricao'],
            quantidade=['quantidade']
        ) for row in rows
    ]

# opcional para o caso do banco nao existir
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
    );
    """)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Banco de dados inicializado.")

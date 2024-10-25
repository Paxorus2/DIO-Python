import sqlite3

def criar_banco():
    conn = sqlite3.connect('mercadinho.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

criar_banco()

import sqlite3

conn = sqlite3.connect('condominio.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS encomenda_antigas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    apartamento TEXT,
    bloco TEXT,
    data_entrega TEXT,
    data_retirada TEXT,
    porteiro TEXT,
    cpf TEXT NOT NULL DEFAULT '',
    nome_de_quem_retirou TEXT
)
''')

conn.commit()

# Fechando a conexão
conn.close()
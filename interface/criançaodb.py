import sqlite3

# Conectando ao banco de dados (ou criando se não existir)
conn = sqlite3.connect('condominio.db')
cursor = conn.cursor()

# Criando a tabela de moradores
cursor.execute('''
CREATE TABLE IF NOT EXISTS moradores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL,
    data_nascimento TEXT NOT NULL,
    telefone TEXT NOT NULL,
    bloco TEXT NOT NULL,
    apartamento TEXT NOT NULL,
    placa_carro TEXT NOT NULL
)
''')

# Criando a tabela de visitantes
cursor.execute('''
CREATE TABLE IF NOT EXISTS visitantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    morador_id INTEGER,
    nome_visitante TEXT NOT NULL,
    horario1 TEXT NOT NULL,
    horario2 TEXT NOT NULL,
    data TEXT NOT NULL,
    nome_morador TEXT NOT NULL,
    bloco TEXT NOT NULL,
    apartamento TEXT NOT NULL,
    FOREIGN KEY (morador_id) REFERENCES moradores(id)
)
''')

cursor.execute('''
CREATE TABLE visitantes_antigos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    morador_id INTEGER,
    nome_visitante TEXT NOT NULL,
    horario1 TEXT NOT NULL,
    horario2 TEXT NOT NULL,
    data TEXT NOT NULL,
    nome_morador TEXT NOT NULL,
    bloco TEXT NOT NULL,
    apartamento TEXT NOT NULL,
    FOREIGN KEY (morador_id) REFERENCES moradores(id)
)
''')

# Criando a tabela de encomendas
cursor.execute('''
CREATE TABLE IF NOT EXISTS encomenda (
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

# Inserindo dados na tabela encomenda a partir da tabela moradores
cursor.execute('''
INSERT INTO encomenda (nome, apartamento, bloco)
SELECT 
    nome,
    apartamento,
    bloco
FROM 
    moradores
''')

# Salvando (commit) as mudanças
conn.commit()

# Fechando a conexão
conn.close()


# Criando a tabela de encomendas
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
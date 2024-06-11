import os
import sqlite3


print("Caminho do banco de dados:", os.path.abspath('encomendas.db'))

conn = sqlite3.connect('encomendas.db')

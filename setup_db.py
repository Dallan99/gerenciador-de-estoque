import sqlite3

# Conecta ou cria um novo banco de dados SQLite
conn = sqlite3.connect('estoque_motos.db')
cursor = conn.cursor()

# Criação da tabela de estoque de motos
cursor.execute('''
CREATE TABLE IF NOT EXISTS estoque (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    modelo TEXT,
    ano INTEGER,
    cor TEXT,
    marca TEXT,
    placa TEXT
)
''')

conn.commit()  # Salva as alterações no banco de dados
conn.close()   # Fecha a conexão com o banco de dados

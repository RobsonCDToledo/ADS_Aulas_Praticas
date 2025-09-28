import sqlite3

# Script base para criação de um banco de dados SQLite e uma tabela

conn = sqlite3.connect('meu_banco.db') # Conecta (ou cria) o banco de dados

cursor = conn.cursor() # Cria um cursor para executar comandos SQL

# Comando SQL para criar a tabela
create_table = ''' 
CREATE TABLE IF NOT EXISTS tabela (
    campo1 INTEGER PRIMARY KEY AUTOINCREMENT,
    campo2 TEXT NOT NULL,
    campo3 INTEGER NOT NULL,
    campo4 TEXT NOT NULL UNIQUE
);
''' 

cursor.execute(create_table) # Executa o comando de criação da tabela
conn.commit() # Salva as mudanças
conn.close() # Fecha a conexão com o banco de dados

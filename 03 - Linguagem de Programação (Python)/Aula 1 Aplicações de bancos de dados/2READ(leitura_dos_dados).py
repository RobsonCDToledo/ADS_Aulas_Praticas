# Script para ler dados de uma tabela existente no banco de dados SQLite

import sqlite3

conn = sqlite3.connect('example.db') # Conecta ao banco de dados existente
cursor = conn.cursor() # Cria um cursor para executar comandos SQL

# Comando SQL para ler dados da tabela
read_data = '''
SELECT * FROM tabela;
'''

cursor.execute(read_data) # Executa o comando de leitura
rows = cursor.fetchall() # Obtém todos os resultados

for row in rows:
    print(row) # Exibe cada linha de resultado

conn.close() # Fecha a conexão com o banco de dados

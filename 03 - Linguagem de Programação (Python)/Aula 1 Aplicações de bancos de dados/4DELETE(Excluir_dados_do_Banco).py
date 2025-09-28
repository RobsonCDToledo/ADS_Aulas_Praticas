# Script para excluir dados de uma tabela existente no banco de dados SQLite

import sqlite3

conn = sqlite3.connect('example.db') # Conecta ao banco de dados existente
cursor = conn.cursor() # Cria um cursor para executar comandos SQL

# Comando SQL para excluir dados da tabela
delete_data = '''
DELETE FROM tabela WHERE campo1 = ?;
'''
# ID do registro a ser excluído
record_id = (1,)  # Exemplo: excluir o registro com campo1 igual a 1

cursor.execute(delete_data, record_id) # Executa o comando de exclusão
conn.commit() # Salva as mudanças
conn.close() # Fecha a conexão com o banco de dados 
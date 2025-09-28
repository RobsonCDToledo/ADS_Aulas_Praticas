# Script para atualizar dados em uma tabela existente no banco de dados SQLite

import sqlite3

conn = sqlite3.connect('example.db') # Conecta ao banco de dados existente
cursor = conn.cursor() # Cria um cursor para executar comandos SQL

# Comando SQL para atualizar dados na tabela
update_data = '''
UPDATE tabela SET campo2 = ?, campo3 = ? WHERE campo1 = ?;
'''

# Dados a serem atualizados
new_values = ('Novo Valor', 123, 1)

cursor.execute(update_data, new_values) # Executa o comando de atualização
conn.commit() # Salva as mudanças
conn.close() # Fecha a conexão com o banco de dados
# Script para atualizar dados em uma tabela existente no banco de dados SQLite
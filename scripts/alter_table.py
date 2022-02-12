# 09_alter_table.py
import sqlite3

conn = sqlite3.connect('pollingpoints.db')
cursor = conn.cursor()

# adicionando uma nova coluna na tabela clientes
cursor.execute("""
ALTER TABLE empresas
ADD COLUMN ativa BOOLEAN;
""")

conn.commit()

print('Novo campo adicionado com sucesso.')

conn.close()

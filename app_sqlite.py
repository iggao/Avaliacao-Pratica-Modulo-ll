"""
Avaliação – Python + SQLite
Tema: CRUD em 'alunos'

O que o script deve fazer:
1) Criar 'escola.db'
2) Criar tabela 'alunos' -> Seguindo o diagrama
3) Inserir registros na tabela alunos
4) Listar todos
5) Buscar por id
6) Atualizar registros
7) Deletar registros

"""

import sqlite3
# Conectar/criar o banco d dados
conn = sqlite3.connect("escola.db")
cursor = conn.cursor()

# Passo 2 - Criar tabelas
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idade INTEGER,
    email TEXT
)
""")

print('tabela criada com sucesso!\n')

# Passo 3 - Inserir dados
cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',
               ('Doca',18, 'doca@gmail.com'))
cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',
               ('Marcinho VP',17, 'marcinhovp@gmail.com'))
cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',
               ('JS da Torre',17, 'jsdatorre@gmail.com'))
cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',
               ('Rabicó',18, 'rabico@gmail.com'))
cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',
               ('Fernandinho Beira Mar',17, 'fernandinhobeiramar@gmail.com'))

conn.commit()

print("Dados inseridos!\n")

# Passo 4 - Listar todos
print("Lista de alunos cadastrados:")
cursor.execute("SELECT * FROM alunos")
for linha in cursor.fetchall():
    print(linha)
print()

# Passo 5 - Atualizar um registro
cursor.execute('UPDATE alunos SET email = ? WHERE nome = ?',
               ('doca.dev@gmail.com', 'Doca'))
conn.commit()
print('Após atualização do email do Doca:')
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()

# Passo 6 - Deletar um registro
cursor.execute('DELETE FROM alunos WHERE nome = ?', ('MArcinho VP',))
conn.commit()

print('Após deletar do email do Marcinho VP:')
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()

# Encerrar conexão
conn.close()

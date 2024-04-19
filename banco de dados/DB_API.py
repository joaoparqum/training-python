import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.sqlite')
cur = conexao.cursor()
cur.row_factory = sqlite3.Row

def criar_tabela(conexao, cur):
    cur = conexao.cursor()
    cur.execute("""
                CREATE TABLE clientes 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))
                """)
    conexao.commit()

def inserir_dados(conexao, cur, nome, email):
    data = (nome, email)
    cur.execute("""
               INSERT INTO clientes (nome, email) VALUES 
                (?,?,?);
            """, data)
    conexao.commit()

def atualizar_dados(conexao, cur, id, nome, email):
    data = (nome, email, id)
    cur.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()

def deletar_dados(conexao, cur, id):
    data = id
    cur.execute("DELETE from clientes WHERE id=?;", data)
    conexao.commit()

def inserir_varios(conexao, cur, dados):
    cur.executemany("""
        INSERT INTO clientes (nome, email) VALUES
                (?,?)
        """, data)
    conexao.commit()

def consultar(cur, id):
    cur.execute("SELECT * from clientes WHERE id=?", (id,))
    return cur.fetchone()

def listar_dados(cur):
    return cur.execute("SELECT * from clientes")

result = consultar(cur,1)
print(dict(result))

clientes = listar_dados(cur)
for cliente in clientes:
    print(dict(cliente))
atualizar_dados(conexao, cur, 1, "Guto", "berserko@gmail.com")

data = [("João","joao@gmail.com"),("Camila","camila@gmail.com"),("Doger","doger@gmail.com")]
inserir_varios(conexao, cur, data)
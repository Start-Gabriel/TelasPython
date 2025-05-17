import sqlite3

def conectar_banco(nome_banco="clientes.db"):
    return sqlite3.connect(nome_banco)

def criar_tabela(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf REAL NOT NULL,
            telefone INTEGER NOT NULL,
            endereco INTEGER DEFAULT 0
        )
    """)
    conn.commit()

def cadastrar_cliente(conn, nome, cpf, telefone, endereco):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO clientes (nome, cpf, telefone, endereco)
        VALUES (?, ?, ?, ?)
    """, (nome, cpf, telefone, endereco))
    conn.commit()

def listar_clientes(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    return cursor.fetchall()

def editar_cliente(conn, id_cliente, nome=None, cpf=None, telefone=None, endereco=None):
    cursor = conn.cursor()
    if nome:
        cursor.execute("UPDATE clientes SET nome = ? WHERE id = ?", (nome, id_cliente))
    if cpf is not None:
        cursor.execute("UPDATE clientes SET cpf = ? WHERE id = ?", (cpf, id_cliente))
    if telefone is not None:
        cursor.execute("UPDATE clientes SET telefone = ? WHERE id = ?", (telefone, id_cliente))
    if endereco is not None:
        cursor.execute("UPDATE clientes SET endereco = ? WHERE id = ?", (endereco, id_cliente))
    conn.commit()

def excluir_cliente(conn, id_cliente):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
    conn.commit()

def buscar_cliente(conn, nome_busca):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes WHERE nome LIKE ?", (f"%{nome_busca}%",))
    return cursor.fetchall()

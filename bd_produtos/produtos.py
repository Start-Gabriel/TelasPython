import sqlite3

def conectar_banco(nome_banco="produtos.db"):
    return sqlite3.connect(nome_banco)

def criar_tabela():
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                preco REAL NOT NULL,
                cod INTEGER NOT NULL,
                quantidade INTEGER DEFAULT 0
            )
        """)
        conn.commit()

def cadastrar_produto(nome, preco, cod, quantidade):
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO produtos (nome, preco, cod, quantidade)
            VALUES (?, ?, ?, ?)
        """, (nome, preco, cod, quantidade))
        conn.commit()

def listar_produtos():
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produtos")
        return cursor.fetchall()

def editar_produto(id_produto, nome=None, preco=None, cod= None, quantidade=None):
    with conectar_banco() as conn:
        cursor = conn.cursor()

        if nome:
            cursor.execute("UPDATE produtos SET nome = ? WHERE id = ?", (nome, id_produto))
        if preco is not None:
            cursor.execute("UPDATE produtos SET preco = ? WHERE id = ?", (preco, id_produto))
        if cod is not None:
            cursor.execute("UPDATE produtos SET cod = ? WHERE id = ?", (cod, id_produto))
        if quantidade is not None:
            cursor.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (quantidade, id_produto))

        conn.commit()

def excluir_produto(id_produto):
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
        conn.commit()

def buscar_produto(nome_busca):
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produtos WHERE nome LIKE ?", (f"%{nome_busca}%",))
        return cursor.fetchall()

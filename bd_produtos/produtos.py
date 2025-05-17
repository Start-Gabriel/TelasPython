
import os
import sys
import sqlite3

def resource_path(relative_path):
    """Resolve o caminho do recurso para compatibilidade com PyInstaller."""
    try:
        base_path = sys._MEIPASS  # PyInstaller define isso
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def conectar_banco(cnn=None):
    caminho_db = resource_path(os.path.join("bd_produtos", "produtos.db"))
    conexao = sqlite3.connect(caminho_db)
    return conexao


def criar_tabela(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            cod INTEGER NOT NULL UNIQUE,
            quantidade INTEGER DEFAULT 0
        )
    """)
    conn.commit()

def cadastrar_produto(conn, nome, preco, cod, quantidade):
    cursor = conn.cursor()
    duplicar = buscar_produto(conn=conn,cod=cod)
    print(duplicar)
    if duplicar == []:
        try:
            cursor.execute("""
                INSERT INTO produtos (nome, preco, cod, quantidade)
                VALUES (?, ?, ?, ?)
            """, (nome, preco, cod, quantidade))
            conn.commit()
            return "cadastrado"
        except sqlite3.IntegrityError as e:
            return (f"Produto duplicado")
        except sqlite3.OperationalError as e:
            return (f"erro")
    else:
        return ["codigo duplicado", f"nome:{duplicar[0][1]} cod:{duplicar[0][3]}"]
def listar_produtos(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    return cursor.fetchall()
import sqlite3

def listar_produtos_ordenados(conn):

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos ORDER BY nome ASC")
    return cursor.fetchall()


def editar_produto(conn, id_produto, nome=None, preco=None, cod=None, quantidade=None):
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

def excluir_produto(conn, id_produto):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
    conn.commit()

def buscar_produto(conn, nome = None, cod = None, id = None):
    cursor = conn.cursor()
    if nome:
        cursor.execute("SELECT * FROM produtos WHERE nome LIKE ?", (f"%{nome}%",))
    if cod:
        cursor.execute("SELECT * FROM produtos WHERE cod = ?", (cod,))
    if id:
        cursor.execute("SELECT * FROM produtos WHERE id = ?", (f"%{id}%",))
    return cursor.fetchall()

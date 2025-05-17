import sqlite3
import os
import sys
from datetime import datetime


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def conectar_banco():
    caminho_db = resource_path(os.path.join("bd_vendas", "vendas.db"))
    os.makedirs(os.path.dirname(caminho_db), exist_ok=True)
    return sqlite3.connect(caminho_db)


def criar_tabelas(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_hora TEXT NOT NULL,
            valor_total REAL NOT NULL,
            troco REAL,
            desconto REAL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS itens_venda (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_venda INTEGER NOT NULL,
            nome_produto TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            valor_unitario REAL NOT NULL,
            FOREIGN KEY(id_venda) REFERENCES vendas(id)
        )
    """)
    conn.commit()


def registrar_venda(conn, itens: list, valor_total: float, troco=0.0, desconto=0.0):
    """
    itens: lista de dicionários
    Ex: [{"nome": "Pão", "quantidade": 3, "valor_unitario": 1.5}, ...]
    """
    cursor = conn.cursor()
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        INSERT INTO vendas (data_hora, valor_total, troco, desconto)
        VALUES (?, ?, ?, ?)
    """, (data_hora, valor_total, troco, desconto))
    id_venda = cursor.lastrowid

    for item in itens:
        cursor.execute("""
            INSERT INTO itens_venda (id_venda, nome_produto, quantidade, valor_unitario)
            VALUES (?, ?, ?, ?)
        """, (id_venda, item['nome'], item['quantidade'], item['valor_unitario']))

    conn.commit()
    return id_venda


def listar_vendas(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vendas ORDER BY data_hora DESC")
    return cursor.fetchall()


def listar_itens_da_venda(conn, id_venda):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM itens_venda WHERE id_venda = ?", (id_venda,))
    return cursor.fetchall()


def excluir_venda(conn, id_venda):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM itens_venda WHERE id_venda = ?", (id_venda,))
    cursor.execute("DELETE FROM vendas WHERE id = ?", (id_venda,))
    conn.commit()


def editar_venda(conn, id_venda, valor_total=None, troco=None, desconto=None):
    cursor = conn.cursor()
    if valor_total is not None:
        cursor.execute("UPDATE vendas SET valor_total = ? WHERE id = ?", (valor_total, id_venda))
    if troco is not None:
        cursor.execute("UPDATE vendas SET troco = ? WHERE id = ?", (troco, id_venda))
    if desconto is not None:
        cursor.execute("UPDATE vendas SET desconto = ? WHERE id = ?", (desconto, id_venda))
    conn.commit()

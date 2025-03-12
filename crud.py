import mysql.connector
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

def get_connection():
    return mysql.connector.connect(
        host = MYSQL_HOST,
        user = MYSQL_USER,
        password = MYSQL_PASSWORD,
        database = MYSQL_DATABASE,
    )

def adicionar_fornecedores(nome_fornecedor,endereco,telefone,email,produto):

    conn = get_connection()
    cursor = conn.cursor()
    query = "insert fornecedor (nome_fornecedor,endereco,telefone,email,produto) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (nome_fornecedor,endereco,telefone,email,produto))
    conn.commit()
    cursor.close()
    conn.close()


def atualizar_fornecedor(nome_fornecedor,endereco,telefone,email,produto):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE produto SET produto = %s, descricao = %s, quantidade = %s, valorDeCompra = %s, valorDeVenda = %s, fornecedor = %s WHERE codproduto = %s"
    cursor.execute(query,(nome_fornecedor,endereco,telefone,email,produto))
    conn.commit()
    cursor.close()
    conn.close()

def deletar_fornecedor(idfornecedor):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM produto WHERE idfornecedor = %s"
    cursor.execute(query, (idfornecedor,))
    conn.commit()
    cursor.close()
    conn.close()


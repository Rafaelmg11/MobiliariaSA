import mysql.connector
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

def get_connection():
    return mysql.connector.connect(
        host = MYSQL_HOST,
        user = MYSQL_USER,
        password = MYSQL_PASSWORD,
        database = MYSQL_DATABASE,
    )

def create_produto(produto,descricao,quantidade,valorDeCompra,valorDeVenda,fornecedor):

    conn = get_connection()
    cursor = conn.cursor()
    query = "insert produto (produto,descricao,quantidade,valorDeCompra,valorDeVenda,fornecedor) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (produto,descricao,quantidade,valorDeCompra,valorDeVenda,fornecedor))
    conn.commit()
    cursor.close()
    conn.close()

def read_produto():

    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM produto"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def update_produto(produto,descricao,quantidade,valorDeCompra,valorDeVenda,fornecedor,codigo_produto):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE produto SET produto = %s, descricao = %s, quantidade = %s, valorDeCompra = %s, valorDeVenda = %s, fornecedor = %s WHERE codproduto = %s"
    cursor.execute(query,(produto,descricao,quantidade,valorDeCompra,valorDeVenda,fornecedor,codigo_produto))
    conn.commit()
    cursor.close()
    conn.close()

def delete_produto(codigo_produto):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM produto WHERE codproduto = %s"
    cursor.execute(query, (codigo_produto,))
    conn.commit()
    cursor.close()
    conn.close()

def buscar_produto(self, codigo_produto):
    conn = get_connection()
    try:
        cursor = conn.conexao.cursor()
        cursor.execute ("SELECT * FROM produto WHERE codigo_produto=%s",(codigo_produto))
        produto = cursor.fetchone()
        if produto:
            self.produto,self.descricao,self.quantidade,self.valorDeCompra,self.valorDeVenda,self.fornecedor,self.codigo_produto = produto
        cursor.close()
        return "Busca feita com sucesso!"
    except Exception as e:
        return f"Ocorreu um erro na busca de usuario: {e}"
            

    
  
    



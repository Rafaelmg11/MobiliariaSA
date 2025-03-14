import mysql.connector
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE


def get_connection():
    return mysql.connector.connect(
        host = MYSQL_HOST,
        user = MYSQL_USER,
        password = MYSQL_PASSWORD,
        database = MYSQL_DATABASE,
    )

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#FUNCÕES PRODUTOS:
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

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#FUNÇÕES FUNCIONARIO:
def create_funcionario(nome,cargo,salario):

    conn = get_connection()
    cursor = conn.cursor()
    query = "insert funcionario (nome,cargo,salario) VALUES (%s, %s, %s)"
    cursor.execute(query, (nome,cargo,salario))
    conn.commit()
    cursor.close()
    conn.close()

def read_funcionario():

    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM funcionarios"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def update_funcionario(nome,cargo,salario):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE funcionario SET funcionario = %s, nome = %s, cargo = %s, salario = %s"
    cursor.execute(query,(nome,cargo,salario))
    conn.commit()
    cursor.close()
    conn.close()

def delete_funcionario(idfuncionario):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM funcionario WHERE idfuncionario = %s"
    cursor.execute(query, (idfuncionario,))
    conn.commit()
    cursor.close()
    conn.close()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#FUNÇÕES FORNECEDORES:


def create_fornecedores(idfornecedor, nome_fornecedor, endereco, telefone, email, produto):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO fornecedor (nome_fornecedor, endereco, telefone, email, produto) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (idfornecedor, nome_fornecedor, endereco, telefone, email, produto))
    conn.commit()
    cursor.close()
    conn.close()


def atualizar_fornecedor(idfornecedor, nome_fornecedor, endereco, telefone, email, produto):
    conn = get_connection()
    cursor = conn.cursor()
    query = """UPDATE fornecedor SET nome_fornecedor = %s, endereco = %s, telefone = %s, email = %s, produto = %s WHERE idfornecedor = %s"""
    cursor.execute(query, (idfornecedor, nome_fornecedor, endereco, telefone, email, produto, idfornecedor))
    conn.commit()
    cursor.close()
    conn.close()

def deletar_fornecedor(idfornecedor):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM fornecedores WHERE idfornecedor = %s"
    cursor.execute(query, (idfornecedor,))
    conn.commit()
    cursor.close()
    conn.close()

def listar_fornecedores():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM fornecedor"
    cursor.execute(query)
    fornecedores = cursor.fetchall()
    cursor.close()
    conn.close()
    return fornecedores

    
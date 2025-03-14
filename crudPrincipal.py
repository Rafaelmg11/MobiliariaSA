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
def create_funcionario(nome,cpf,telefone,email,cargo,salario):

    conn = get_connection()
    cursor = conn.cursor()
    query = "insert funcionario (nome,cpf,telefone,email,cargo,salario) VALUES (%s, %s, %s)"
    cursor.execute(query, (nome,cpf,telefone,email,cargo,salario))
    conn.commit()
    cursor.close()
    conn.close()

def read_funcionario():

    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM funcionario"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def update_funcionario(nome,cargo,salario,idfuncionario):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE funcionario SET nome = %s, cargo = %s, salario = %s WHERE idfuncionario = %s"
    cursor.execute(query,(nome,cargo,salario,idfuncionario))
    conn.commit()
    cursor.close()
    conn.close()

def delete_funcionario(id_funcionario):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM funcionario WHERE idfuncionario = %s"
    cursor.execute(query, (id_funcionario,))
    conn.commit()
    cursor.close()
    conn.close()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#FUNÇÕES FORNECEDORES:


def create_fornecedores(nome_fornecedor, endereco, telefone, email, produto):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO fornecedor (nome_fornecedor, endereco, telefone, email, produto) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (nome_fornecedor, endereco, telefone, email, produto))
    conn.commit()
    cursor.close()
    conn.close()


def atualizar_fornecedor( nome_fornecedor, endereco, telefone, email, produto, id_produto):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE fornecedor SET nome_fornecedor = %s, endereco = %s, telefone = %s, email = %s, produto = %s WHERE idfornecedor = %s"
    cursor.execute(query, ( nome_fornecedor, endereco, telefone, email, produto, id_produto ))
    conn.commit()
    cursor.close()
    conn.close()

def deletar_fornecedor(id_fornecedor):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM fornecedor WHERE idfornecedor = %s"
    cursor.execute(query, (id_fornecedor,))
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

    
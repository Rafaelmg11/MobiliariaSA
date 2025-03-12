import mysql.connector
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

def get_connection():
    return mysql.connector.connect(
        host = MYSQL_HOST,
        user = MYSQL_USER,
        password = MYSQL_PASSWORD,
        database = MYSQL_DATABASE,
    )

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

def buscar_funcionario(buscar):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM funcionario WHERE buscar = %s"
    lista = []
    lista.append(query)
    print(lista)
    produto = cursor.fetchone(buscar)
    cursor.execute(query,produto)
    cursor.close()
    conn.close()


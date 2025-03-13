import mysql.connector
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

def get_connection():
    """Get a connection to the MySQL database."""
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
    )

def up_fornecedores(nome_fornecedor, endereco, telefone, email, produto):
    """Insert a new supplier into the database."""
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO fornecedores (nome_fornecedor, endereco, telefone, email, produto) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (nome_fornecedor, endereco, telefone, email, produto))
    conn.commit()
    cursor.close()
    conn.close()

def atualizar_fornecedor(idfornecedor, nome_fornecedor, endereco, telefone, email, produto):
    """Update supplier details in the database."""
    conn = get_connection()
    cursor = conn.cursor()
    query = """UPDATE fornecedores 
               SET nome_fornecedor = %s, endereco = %s, telefone = %s, email = %s, produto = %s 
               WHERE idfornecedor = %s"""
    cursor.execute(query, (nome_fornecedor, endereco, telefone, email, produto, idfornecedor))
    conn.commit()
    cursor.close()
    conn.close()

def deletar_fornecedor(idfornecedor):
    """Delete a supplier from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM fornecedores WHERE idfornecedor = %s"
    cursor.execute(query, (idfornecedor,))
    conn.commit()
    cursor.close()
    conn.close()

def fetch_fornecedores():
    """Fetch all suppliers from the database."""
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM fornecedores"
    cursor.execute(query)
    fornecedores = cursor.fetchall()
    cursor.close()
    conn.close()
    return fornecedores


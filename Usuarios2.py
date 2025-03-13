import mysql.connector
from Banco import Banco  # Make sure Banco is a valid class or module

class Usuarios(object):
    def __init__(self, nome="", senha=""):
        self.info = {}
        self.nome = nome
        self.senha = senha

    def insertUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("INSERT INTO usuario (nome, senha) VALUES (%s, %s)", (self.nome, self.senha))
            banco.conexao.commit()
            c.close()
            return "Usuário cadastrado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção do usuário: {e}"

    def updateUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("UPDATE usuario SET nome=%s, senha=%s WHERE nome=%s", 
                      (self.nome, self.senha, self.nome))  # Added WHERE clause to specify the user
            banco.conexao.commit()
            c.close()
            return "Usuário atualizado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração do usuário: {e}"

    def deleteUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM usuario WHERE nome=%s", (self.nome,))
            banco.conexao.commit()
            c.close()
            return "Usuário excluído com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão do usuário: {e}"

    def selectUser(self, nome):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM usuario WHERE nome=%s", (nome,))
            usuario = c.fetchone()
            if usuario:
                self.nome, self.senha = usuario[0], usuario[1]  # Declarando o index de nome e senha respectivamente
            c.close()
            return {"nome": self.nome, "senha": self.senha} if usuario else "Usuário não encontrado."
        except Exception as e:
            return f"Ocorreu um erro na busca do usuário: {e}"

import mysql.connector
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

class Usuarios(object):
    def get_connection():
        return mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE,
        )

    def __init__(self, nome="", senha=""):
        self.info = {}
        self.nome = nome
        self.senha = senha

    def cadastrar_usuario(self):
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuario (nome, senha) VALUES (%s, %s)", (self.nome, self.senha))
            conn.commit()
            cursor.close()
            return "Usuário cadastrado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção do usuário: {e}"
        finally:
            conn.close()

    def atualizar_usuario(self):
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE usuario SET nome=%s, senha=%s WHERE nome=%s", (self.nome, self.senha, self.nome))
            conn.commit()
            cursor.close()
            return "Usuário atualizado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração do usuário: {e}"
        finally:
            conn.close()

    def deletar_usuario(self):
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM usuario WHERE nome=%s", (self.nome,))
            conn.commit()
            cursor.close()
            return "Usuário excluído com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão do usuário: {e}"
        finally:
            conn.close()

    def selecionar_usuario(self, nome):
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario WHERE nome=%s", (nome,))
            usuario = cursor.fetchone()
            if usuario:
                self.nome, self.senha = usuario[0], usuario[1]
                cursor.close()
                return {"nome": self.nome, "senha": self.senha}
            else:
                return "Usuário não encontrado."
        except Exception as e:
            return f"Ocorreu um erro na busca do usuário: {e}"
        finally:
            conn.close()
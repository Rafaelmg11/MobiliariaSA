import mysql.connector 

#PARA RODAR O PROJETO NAO POSSO ESQUECER DE DIGITAR O CODIGO ABAIXO NO CONSOLE(TELA DE EXECUÇÃO)
# pip install mysql-connector-python

class Database:
    def __init__(self):
        #Conecta o banco de dados:
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "mobiliariasa_db"
        )
        self.cursor = self.conn.cursor() #Cria um cursor

        print("Concetado ao banco de dados!") #Mensagem de confirmação
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

    #REGISTRAR UM NOVO PRODUTO NO BANCO DE DADOS:
    def RegistrarProduto(self,produto,descricao,quantidade,valorDeCompra,valorDeVenda,fornecedor):
        self.cursor.execute("INSERT INTO produto (produto,descricao,quantida,valorDeCompra,valorDeVenda,fornecedor)VALUES (%s,%s,%s,%s,%s,%s)",(produto,descricao,quantidade,valorDeCompra,valorDeVenda,fornecedor)) #INSERE OS DADOS NO BANCO DE DADOS
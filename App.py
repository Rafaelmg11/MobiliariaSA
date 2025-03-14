from Usuarios import Usuarios
from tkinter import *
import mysql.connector


class Application:

    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.titulo = Label(self.container1, text="Informe os dados :")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()

        self.btnBuscar = Button(self.container2, text="Buscar",font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarUsuario
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(self.container3, text="Nome:",font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lblsenha= Label(self.container7, text="Senha:",font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)
        self.txtsenha = Entry(self.container7)
        self.txtsenha["width"] = 25
        self.txtsenha["show"] = "*"
        self.txtsenha["font"] = self.fonte
        self.txtsenha.pack(side=LEFT)
        self.bntInsert = Button(self.container8, text="Inserir",font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirUsuario
        self.bntInsert.pack (side=LEFT)
        self.bntAlterar = Button(self.container8, text="Alterar",font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterar_usuario
        self.bntAlterar.pack (side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir",font=self.fonte, width=12)
        self.bntExcluir["command"] = self.deletar_usuario
        self.bntExcluir.pack (side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

        self.conectarBanco()

    def conectarBanco(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mobiliariasa_db"
        )
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuario (
                                nome VARCHAR(255),
                                senha VARCHAR(255))''')
        self.conn.commit()

    def inserirUsuario(self):
        nome = self.txtnome.get()
        senha = self.txtsenha.get()
        self.cursor.execute("INSERT INTO usuario (nome, senha) VALUES (%s, %s)",
                            (nome,senha))
        self.conn.commit()
        self.lblmsg["text"] = "Usuário inserido com sucesso"
        self.limparCampos()

    def alterar_usuario(self):
        nome = self.txtnome.get()
        senha = self.txtsenha.get()
        self.cursor.execute("UPDATE usuario SET nome=%s,senha=%s",
                            (nome, senha))
        self.conn.commit()
        self.lblmsg["text"] = "Usuário alterado com sucesso"
        self.limparCampos()

    def deletar_usuario(self):
        nome = self.txtnome.get()
        self.cursor.execute("DELETE FROM usuario WHERE nome=%s", (nome,))
        self.conn.commit()
        self.lblmsg["text"] = "Usuário excluído com sucesso"
        self.limparCampos()

    def buscarUsuario(self):
        nome = self.txtidusuario.get()
        self.cursor.execute("SELECT * FROM usuario WHERE nome=%s", (nome,))
        usuario = self.cursor.fetchone()
        if usuario:
            self.txtnome.insert(0, usuario[1])
            self.txtsenha.insert(0, usuario[2])
        else:
            self.lblmsg["text"] = "Usuário não encontrado"
            self.limparCampos()

    def limparCampos(self):
        self.txtnome.delete(0, END)
        self.txtsenha.delete(0, END)

    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    root = Tk()
    Application(root)
    root.mainloop()

from tkinter import* #Importa tudo do tkinter
from tkinter import messagebox #Importa as caixas de mensagem
from crudPrincipal import get_connection
from Tela_Principal import Menu
import mysql.connector
import tkinter as tk

class Tela_Login:
    def __init__(self,root):
        self.root = root
        self.root.title("CADASTRO DE PRODUTOS") #Define o titulo
        self.root.geometry("400x500") #Define o tamanho da janela
        self.root.configure(background = ("#5424A2")) #Configura a cor de fundo da janela
        self.root.resizable(width = False,height = False) #Impede que a janela seja redimensionada 
        #Criação de Widgets
        self.create_widgets()

    def conectarBanco(self):
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "mobiliariasa_db"
        )
        self.cursor = self.conn.cursor()
        self.conn.commit()

    def create_widgets(self):
        #CRIANDO E POSICIONANDO AS LABELS:
        UsuarioLabel = Label(self.root,text="Usuario: ",font=("Georgia",16),bg = "#5424A2",fg = "WHITE") #Cria Label TITULO
        UsuarioLabel.place(x=110,y=200)
        SenhaLabel = Label(self.root,text= "Senha:",font=("Georgia",16),bg = "#5424A2",fg = "WHITE") #Cr
        SenhaLabel.place(x=110,y=260)
        InformaçãoLabel = Label (self.root,text="Sistema Desenvolvido por:\n"
                                                "\n"
                                                "Rafael de Almeida de Magalhães\n"
                                                "Matheus Golanowski\n"
                                                "Matheus Eduardo Souza",font=("Georgia",8),bg = "#5424A2",fg = "WHITE")
        #CRIANDO AS CAIXAS DE ENTRADA:
        UsuarioEntry = tk.Entry(self.root, width=19,font=("Georgia",13))
        UsuarioEntry.place(x=110,y=230)
        SenhaEntry = tk.Entry (self.root, width=19,font=("Georgia",13))
        SenhaEntry.place(x=110,y=290)
        InformaçãoLabel.place(x=110,y=400)

        #LOGO:
        # CARREGAR IMAGEM
        self.logo = PhotoImage(file="icons/LogoMobiliaria.png") #Carrega a imagem da logo
        self.LogoLabel = Label(self.root,image = self.logo, bg = "#5424A2") #Cria um label para a image, do logo
        self.LogoLabel.place(x=105,y=35) #Posiciona o label no frama esquerdo 

        def login():
            usuario = UsuarioEntry.get()
            senha = SenhaEntry().get()

            conn = get_connection() #CONEXÃO COM O BANCO DE DADOS
            self.cursor = conn.cursor()
            self.cursor.execute("SELECT*FROM cadastro WHERE usuario = %s AND senha = %s")
            VerifyLogin = self.cursor.fetchone() #Obtem o resultado da consulta
            if VerifyLogin:
                messagebox.showinfo(title = "INFO LOGIN",message="Acesso Confirmado, Bem Vindo!")#Ebibe mensagem de sucesso

                root_main = tk.Tk()  
                app_main = Menu(root_main, self.root) 
                root_main.mainloop()
                
            else:messagebox.showinfo(title = "INFO LOGIN",message = "Acesso Negado. Verifique se está cadastrado no Sistema!")#Exibe mensagem de erro

        #CRIANDO BOTAO:
        LoginButton =  tk.Button(self.root, text="LOGIN",  width=12, font=("Georgia", 11),command=login)
        LoginButton.place(x=150, y=350)



if __name__ == "__main__":
    root = tk.Tk()
    app = Tela_Login(root)
    root.mainloop()
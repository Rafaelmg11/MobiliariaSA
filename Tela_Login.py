from tkinter import* #Importa tudo do tkinter
from tkinter import messagebox #Importa as caixas de mensagem
from crudPrincipal import get_connection,create_produto, read_produto , update_produto , delete_produto 
import tkinter as tk
import mysql.connector

class Tela_Login:
    def __init__(self,root):
        self.root = root
        self.root.title("CADASTRO DE PRODUTOS") #Define o titulo
        self.root.geometry("400x500") #Define o tamanho da janela
        self.root.configure(background = ("#610061")) #Configura a cor de fundo da janela
        self.root.resizable(width = False,height = False) #Impede que a janela seja redimensionada 
        #Criação de Widgets
        self.create_widgets()

    def create_widgets(self):
        #CRIANDO E POSICIONANDO AS LABELS:
        UsuarioLabel = Label(self.root,text="Usuario: ",font=("Georgia",16),bg = "#610061",fg = "WHITE") #Cria Label TITULO
        UsuarioLabel.place(x=110,y=200)
        SenhaLabel = Label(self.root,text= "Senha:",font=("Georgia",16),bg = "#610061",fg = "WHITE") #Cr
        SenhaLabel.place(x=110,y=260)
        InformaçãoLabel = Label (self.root,text="Sistema Desenvolvido por:\n"
                                                "\n"
                                                "Rafael de Almeida de Magalhães\n"
                                                "Matheus Golanowski\n"
                                                "Matheus Eduardo Souza",font=("Georgia",8),bg = "#610061",fg = "WHITE")
        #CRIANDO AS CAIXAS DE ENTRADA:
        UsuarioEntry = tk.Entry(self.root, width=19,font=("Georgia",13))
        UsuarioEntry.place(x=110,y=230)
        SenhaEntry = tk.Entry (self.root, width=19,font=("Georgia",13))
        SenhaEntry.place(x=110,y=290)
        InformaçãoLabel.place(x=110,y=400)

        #CRIANDO BOTAO:
        LoginButton =  tk.Button(self.root, text="LOGIN", width=12, font=("Georgia", 11))
        LoginButton.place(x=150, y=350)

        #LOGO:
        # CARREGAR IMAGEM
        logo = PhotoImage(file="icons/LogoRafaelMagalhaes.png") #Carrega a imagem da logo
        LogoLabel = Label(image = logo) #Cria um label para a image, do logo
        LogoLabel.place(x=50,y=100) #Posiciona o label no frama esquerdo 

if __name__ == "__main__":
    root = tk.Tk()
    app = Tela_Login(root)
    root.mainloop()
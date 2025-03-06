#IMPORTAR BIBLIOTECAS:
from tkinter import* #Importa tudo do tkinter
from tkinter import messagebox #Importa as caixas de mensagem
from tkinter import ttk #Importa o widgets tematicos do tkinter
from database import Database #Importa a classe Database do modulo database

#CRIAR A JANELA
jan = Tk()
jan.title("Cadastro de produto")#Define o titulo
jan.geometry("600x480") #Define o tamanho da janela
jan.configure(background="white")#Configura a cor de fundo da janela
jan.resizable(width = False,height = False)#Impede que a janela seja redimensionada 

#CARREGAR IMAGEM:
#logo = PhotoImage (file = "icons/LogoMobiliariaSa.png") 

jan.mainloop()
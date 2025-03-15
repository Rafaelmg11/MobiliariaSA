from tkinter import* #Importa tudo do tkinter
from tkinter import messagebox #Importa as caixas de mensagem
from crudPrincipal import create_usuario,read_usuario,get_connection,update_usuario
import tkinter as tk
import mysql.connector

class CADASTRO:
    def __init__(self,root): #PARA EXECUTAR ESSE CODIGO SEPAPARADEMENTE DEVE TIRAR O "main_window"
        self.root = root
        # self.main_window = main_window #PARA EXECUTAR ESSE CODIGO SEPAPARADEMENTE DEVE COMENTAR ESSA LINHA DE CODIGO IRA DAR UM ERROR NO BOTAO VOLTAR
        self.root.title("CADASTRO DE PRODUTOS") #Define o titulo
        self.root.geometry("500x500") #Define o tamanho da janela
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
        #LABELS:
        TituloLabel = Label(self.root,text="CADASTRO: ",font=("Georgia",25),bg = "#5424A2",fg = "WHITE") #Cria Label TITULO
        TituloLabel.pack(pady=40,anchor="center") #POSICIONA O TITULO
        UsuarioLabel = Label(self.root,text = "Usuario: ",font = ("Georgia",16),bg = "#5424A2", fg = "WHITE") #Cria Label Produtos
        UsuarioLabel.place(x=30,y=105)
        SenhaLabel = Label(self.root,text= "Senha: ",font= ("Georgia",16),bg = "#5424A2", fg = "WHITE")#Cria Label Descrição
        SenhaLabel.place(x=30,y=135)
        idusuarioLabel = Label(self.root,text= "ID Usuario: ",font= ("Georgia",16),bg = "#5424A2", fg = "WHITE")#Cria Label Descrição
        idusuarioLabel.place(x=30,y=165)

        #CAMPOS DE ENTRADA:
        self.UsuarioEntry = tk.Entry(self.root, width=20,font=("Georgia",12))
        self.UsuarioEntry.place(x=120,y=110)
        self.SenhaEntry = tk.Entry(self.root, width=20,font=("Georgia",12))
        self.SenhaEntry.place(x=105,y=140)
        self.idusuarioEntry = tk.Entry(self.root, width=20,font=("Georgia",12))
        self.idusuarioEntry.place(x=150,y=170)

        #CRIANDO A LISTA DE CADASTRO DE PRODUTOS:
        self.text_area = tk.Text(self.root, height=9,width=55)
        self.text_area.place(x=25,y=290)

        def voltar_para_principal():
            # Fechar a janela atual de cadastro de produtos e voltar para a janela principal
            self.root.quit()  # Fecha a janela de cadastro de produtos (destrói a instância)
            self.root.destroy()  # Fecha a janela de cadastro de produtos, liberando recursos

            self.main_window.deiconify()  # Reexibe a janela principal

        voltar_button = tk.Button(self.root, text="VOLTAR", width=11, font=("Georgia", 10), command=voltar_para_principal)
        voltar_button.place(x=25, y=450)


        def cadastrar_usuario():
            usuario = self.UsuarioEntry.get()
            senha = self.SenhaEntry.get()

            if usuario and senha:
                create_usuario(usuario,senha)

                #LIMPAR CAMPOS:
                self.UsuarioEntry.delete(0, tk.END)
                self.SenhaEntry.delete(0, tk.END)
                self.idusuarioEntry.delete(0, tk.END)

                messagebox.showinfo("Cadastro Realizado","Cadastro Realizado Com Sucesso!")

            else:
                messagebox.showerror("Error","Todos os campos devem estar preenchidos!")

        cadastroButton = tk.Button (self.root,text = "CADASTRAR",font= ("Georgia",10),width=13,command=cadastrar_usuario)
        cadastroButton.place(x=30,y=230)

        #LISTAR PRODUTO
        def listar_usuario():
            usuarios = read_usuario() #PUXANDO FUNÇÃO DO CRUD
            self.text_area.delete(1.0, tk.END) #ACESSANDO A "LISTA" DA TELA
            for usuario in usuarios: #produto ANDANDO EM produtos
                self.text_area.insert(tk.END, f"idUsuario: {usuario[0]}, Usuario: {usuario[1]}, Senha: {usuario[2]}\n")
        
        listarButton = tk.Button (self.root,text = "LISTAR",font= ("Georgia",10),width=13,command=listar_usuario)
        listarButton.place(x=150,y=230)

        def alterar_produto():
                
                #RECEBENDO VALORES
                usuario = self.UsuarioEntry.get()
                senha = self.SenhaEntry.get()
                id_usuario = self.idusuarioEntry.get()

                id_usuario = self.idusuarioEntry.get() #RECEBENDO O VALOR QUE É PRA SER O CODPRODUTO DA TABELA
                conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
                self.cursor = conn.cursor() #sell.conn TRABALHAR COM A CONEXAO

                try:
                    self.cursor.execute("SELECT * FROM cadastro WHERE idusuario=%s ",(id_usuario,)) 
                    # CONSULTA NO BANCO
                    usuario_pesquisa = self.cursor.fetchone()

                    # Verificando se o produto foi encontrado
                    if usuario_pesquisa:  # SE FOI ENCONTRADO...
                        if id_usuario and usuario and senha :
                            update_usuario(usuario,senha,id_usuario) #PUXANDO A FUNÇÃO DO CRUD E AS VARIAVEIS

                            #LIMPAR CAMPOS
                            self.UsuarioEntry.delete(0, tk.END)
                            self.SenhaEntry.delete(0, tk.END)
                            self.idusuarioEntry.delete(0, tk.END)

                            messagebox.showinfo("Success","Produto alterado com sucesso!")
                        else:
                            messagebox.showerror("Error","Todos os campos são obrigatórios")
                    else:
                        messagebox.showerror("Error","Cadastro de Produto não existe")

                except Exception as e:
                    print(f'Error: {e}') #SE EXEPT, EXIBE O ERRO 

        #BOTÃO ALTERAR
        AlterarButton = tk.Button(self.root,text = "ALTERAR",font= ("Georgia",10),width=13,command=alterar_produto)
        AlterarButton.place(x=270,y=230)  

        
    
        

    

if __name__ == "__main__":
    root = tk.Tk()
    app = CADASTRO(root)
    root.mainloop()




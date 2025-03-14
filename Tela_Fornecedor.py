#IMPORTAR BIBLIOTECAS:
from tkinter import* #Importa tudo do tkinter
from tkinter import messagebox #Importa as caixas de mensagem
from tkinter import ttk #Importa o widgets tematicos do tkinter
from crudPrincipal import get_connection,create_fornecedores, listar_fornecedores, atualizar_fornecedor , deletar_fornecedor
import tkinter as tk
import mysql.connector


class FORNECEDOR:  

    def __init__(self,root,main_window): #PARA EXECUTAR ESSE CODIGO SEPAPARADEMENTE DEVE TIRAR O "main_window"
        self.root = root
        self.main_window = main_window #PARA EXECUTAR ESSE CODIGO SEPAPARADEMENTE DEVE COMENTAR ESSA LINHA DE CODIGO IRA DAR UM ERROR NO BOTAO VOLTAR
        self.root.title("FORNECEDORES") #Define o titulo
        self.root.geometry("700x680") #Define o tamanho da janela
        self.root.configure(background = "#5424A2") #Configura a cor de fundo da janela
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
        #LABELS
        label_titulo_fornecedor= Label(self.root,text = "FORNECEDOR: ",font=("Georgia",25),bg = "#5424A2",fg = "WHITE" ) #Cria Label Produtos
        label_titulo_fornecedor.pack(pady=40,anchor="center") #POSICIONA O TITULO

        label_nome_fornecedor = Label(self.root,text = "Fornecedor: ",font = ("Georgia",16), bg = "#5424A2", fg = "WHITE" ) #Cria Label Produtos
        label_nome_fornecedor.place(x=40,y=105)

        label_endereco = Label(self.root,text = "Endereço: ",font = ("Georgia",16), bg = "#5424A2", fg = "WHITE" ) #Cria Label Produtos
        label_endereco.place(x=40,y=135)

        label_telefone = Label(self.root,text = "Telefone: ",font = ("Georgia",16), bg = "#5424A2", fg = "WHITE" ) #Cria Label Produtos
        label_telefone.place(x=40,y=165)

        label_email = Label(self.root,text = "Email: ",font = ("Georgia",16), bg = "#5424A2", fg = "WHITE" ) #Cria Label Produtos
        label_email.place(x=40,y=195)

        label_produto= Label(self.root,text = "Produto: ",font = ("Georgia",16), bg = "#5424A2", fg = "WHITE" ) #Cria Label Produtos
        label_produto.place(x=40,y=225)

        label_idFornecedor = Label (self.root,text="ID Fornecedor: ",font = ("Georgia",16), bg = "#5424A2", fg = "WHITE" ) #Cria Label Codigo de Produto
        label_idFornecedor.place(x=40,y=255)

        #CAMPOS DE ENTRADA
        self.entry_nome_fornecedor = tk.Entry(self.root, width=30,font=("Georgia",12))
        self.entry_nome_fornecedor.place(x=170,y=111)

        self.entry_endereco = tk.Entry(self.root, width=30,font=("Georgia",12))
        self.entry_endereco.place(x=155,y=141)

        self.entry_telefone = tk.Entry(self.root, width=30,font=("Georgia",12))
        self.entry_telefone.place(x=145,y=171)

        self.entry_email = tk.Entry(self.root, width=30,font=("Georgia",12))
        self.entry_email.place(x=115, y= 201)

        self.entry_produto = tk.Entry(self.root, width=30,font=("Georgia",12))
        self.entry_produto.place(x=140, y= 231)

        self.entry_pesquisa = tk.Entry(self.root, width=53,font= ("Georgia",13))
        self.entry_pesquisa.place(x=143,y=392)


        self.entry_idFornecedor = tk.Entry (self.root, width=30,font = ("Georgia",12)) #Cria Label Codigo de Produto
        self.entry_idFornecedor.place(x=190,y=261)

        #CRIANDO A LISTA DE CADASTRO DE PRODUTOS:
        self.text_area = tk.Text(self.root, height=13,width=82)
        self.text_area.place(x=18,y=423)

        def voltar_para_principal():
            # Fechar a janela atual de cadastro de produtos e voltar para a janela principal
            self.root.quit()  # Fecha a janela de cadastro de produtos (destrói a instância)
            self.root.destroy()  # Fecha a janela de cadastro de produtos, liberando recursos

            self.main_window.deiconify()  # Reexibe a janela principal

        voltar_button = tk.Button(self.root, text="VOLTAR", width=11, font=("Georgia", 10), command=voltar_para_principal)
        voltar_button.place(x=20, y=645)
    
        def cadastrarFornecedor():
            #OBTENDO AS INFORMAÇÕES DOS CAMPOS DE TEXTOS
            nome = self.entry_nome_fornecedor.get()
            endereco = self.entry_endereco.get()
            telefone = self.entry_telefone.get()
            email = self.entry_email.get()
            produto = self.entry_produto.get()
            #VERIFICANDO SE TODOS OS CAMPOS ESTÂO PREENCHIDOS:
            if nome and endereco and telefone and email and produto:
                create_fornecedores(nome,endereco,telefone,email,produto)
            #Limpar campos:
                self.entry_nome_fornecedor.delete(0, tk.END)
                self.entry_endereco.delete(0, tk.END)
                self.entry_telefone.delete(0, tk.END)
                self.entry_email.delete(0, tk.END)
                self.entry_produto.delete(0, tk.END)
                self.entry_idFornecedor.delete(0, tk.END)
                self.entry_pesquisa.delete(0, tk.END)

                messagebox.showinfo("Success","Fornecedor criado com sucesso!")
            else:
                messagebox.showerror("Error","Todos os campos são obrigatórios" )

        botao_adicionar = tk.Button (self.root,text = "CADASTRAR",font= ("Georgia",10),width=13,command=cadastrarFornecedor)
        botao_adicionar.place(x=40,y=330)

        #LISTAR PRODUTO
        def listar_fornecedor():
            fornecedores = listar_fornecedores() #PUXANDO FUNÇÃO DO CRUD
            self.text_area.delete(1.0, tk.END) #ACESSANDO A "LISTA" DA TELA
            for fornecedor in fornecedores: #produto ANDANDO EM produtos
                self.text_area.insert(tk.END, f"id.Fornecedor: {fornecedor[0]}, Fornecedor: {fornecedor[1]}, Endereço: {fornecedor[2]},Telefone: {fornecedor[3]},Email: {fornecedor[4]},Produto: {fornecedor[5]}\n")

        botao_listar  = tk.Button(self.root,text="LISTAR",font= ("Georgia",10),width=13,command=listar_fornecedor)
        botao_listar.place(x=290,y=330)


        
        #FUNÇÃO DE ALTERAR PRODUTO:
        def alterar_fornecedor():
                
                #OBTENDO AS INFORMAÇÕES DOS CAMPOS DE TEXTOS
                nome = self.entry_nome_fornecedor.get()
                endereco = self.entry_endereco.get()
                telefone = self.entry_telefone.get()
                email = self.entry_email.get()
                produto = self.entry_produto.get()
                id_fornecedor=self.entry_idFornecedor.get()
                id_fornecedor = self.entry_idFornecedor.get() #RECEBENDO O VALOR QUE É PRA SER O CODPRODUTO DA TABELA
                conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
                self.cursor = conn.cursor() #sell.conn TRABALHAR COM A CONEXAO

                try:
                    self.cursor.execute("SELECT * FROM fornecedor WHERE idfornecedor=%s ",(id_fornecedor,)) 
                    # CONSULTA NO BANCO
                    fornecedor_pesquisa = self.cursor.fetchone()

                     # Verificando se o produto foi encontrado
                    if fornecedor_pesquisa:  # SE FOI ENCONTRADO...
                        #SE CAMPOS NÃO ESTIVER VAZIOS:
                        if id_fornecedor and nome and endereco and telefone and email and produto:
                            atualizar_fornecedor(nome,endereco,telefone,email,produto,id_fornecedor) #PUXANDO A FUNÇÃO DO CRUD E AS VARIAVEIS

                            #LIMPAR CAMPOS
                            self.entry_nome_fornecedor.delete(0, tk.END)
                            self.entry_endereco.delete(0, tk.END)
                            self.entry_telefone.delete(0, tk.END)
                            self.entry_email.delete(0, tk.END)
                            self.entry_produto.delete(0, tk.END)
                            self.entry_idFornecedor.delete(0, tk.END)
                            self.entry_pesquisa.delete(0, tk.END)
                            messagebox.showinfo("Success","Fornecedor alterado com sucesso!")
                        else:
                            messagebox.showerror("Error","Todos os campos são obrigatórios")   

                    else:
                        messagebox.showerror("Error","Cadastro de Produto não existe")
                except:
                    print("Expect")
        botao_atualizar = tk.Button(self.root,text = "ALTERAR",font= ("Georgia",10),width=13, command=alterar_fornecedor)
        botao_atualizar.place(x=164,y=330)  

        def excluir_fornecedor():
            id_fornecedor = self.entry_idFornecedor.get() #RECEBENDO O VALOR QUE É PRA SER O CODPRODUTO DA TABELA
            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            self.cursor = conn.cursor() #sell.conn TRABALHAR COM A CONEXAO
            try:
                self.cursor.execute("SELECT * FROM fornecedor WHERE idfornecedor=%s ",(id_fornecedor,)) 
                # CONSULTA NO BANCO
                produto_pesquisa = self.cursor.fetchone()
                # Verificando se o produto foi encontrado
                if produto_pesquisa:  # SE FOI ENCONTRADO...

                    if id_fornecedor: #SE codigo_produto RECEBER UM VALOR
                        deletar_fornecedor(id_fornecedor) #PUXANDO FUNÇÃO DO CRUD

                        #LIMPAR CAMPOS
                        self.entry_nome_fornecedor.delete(0, tk.END)
                        self.entry_endereco.delete(0, tk.END)
                        self.entry_telefone.delete(0, tk.END)
                        self.entry_email.delete(0, tk.END)
                        self.entry_produto.delete(0, tk.END)
                        self.entry_idFornecedor.delete(0, tk.END)
                        self.entry_pesquisa.delete(0, tk.END)

                        messagebox.showinfo("Success","Fornecedor excluido com sucesso")
                    else:
                        messagebox.showerror("Error","O ID do Fornecedor é obrigatório")

                else:
                        messagebox.showerror("Error","Cadastro de Produto não existe")
            except:
                print("Expect")


        botao_deletar = tk.Button(self.root,text = "EXCLUIR",font= ("Georgia",10),width=13, command=excluir_fornecedor)
        botao_deletar.place(x=418,y=330)



        #FUNÇÃO DE PESQUISAR :) ;) OBS: NAO TEM RELAÇÃO COM O CRUD
        def pesquisar_fornecedor():
            id_fornecedor = self.entry_pesquisa.get() #CONEXÃO COM O BANCO DE DADOS
            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            self.cursor = conn.cursor() #sell.conn TRABALHAR COM A CONEXAO
            try:
                
                self.cursor.execute("SELECT nome_fornecedor, endereco, telefone, email, produto, idfornecedor FROM fornecedor WHERE idfornecedor=%s or endereco=%s or nome_fornecedor=%s or telefone=%s or email=%s or produto=%s", (id_fornecedor,id_fornecedor,id_fornecedor,id_fornecedor,id_fornecedor,id_fornecedor,)) 
                # ACIMA SELECIONA AS COLUNAS DA TABELA SE codproduto OU produto OU descricao == codigo_produto
                # codproduto E produto E descricao PERMITE FAZER A BUSCA POR PRODUTO,DESCRICAO, E CODIGO DE PRODUTO
                #EM OUTROS CASOS PODERIA SER CPF E NÚMERO DE TELEFONE

                # CONSULTA NO BANCO
                fornecedor_pesquisa = self.cursor.fetchone()
        
                # Verificando se o produto foi encontrado
                if fornecedor_pesquisa:  # SE FOI ENCONTRADO...
                    nome_fornecedor, endereco, telefone, email, produto, id_fornecedor  = fornecedor_pesquisa #ESSAS VARIAVEIS VAI RECEBER OS VALORES DA COLUNA DE ACORDO COM A ORDEM

                    #LIMPAR CAMPOS
                    self.entry_nome_fornecedor.delete(0, tk.END)
                    self.entry_endereco.delete(0, tk.END)
                    self.entry_telefone.delete(0, tk.END)
                    self.entry_email.delete(0, tk.END)
                    self.entry_produto.delete(0, tk.END)
                    self.entry_idFornecedor.delete(0, tk.END)
                    self.entry_pesquisa.delete(0, tk.END)

                    # Inserindo os dados nas entradas (Entry)
                    self.entry_nome_fornecedor.insert(0, nome_fornecedor )
                    self.entry_endereco.insert(0, endereco )
                    self.entry_telefone.insert(0,telefone )
                    self.entry_email.insert(0,email )
                    self.entry_produto.insert(0,produto )
                    self.entry_idFornecedor.insert(0,id_fornecedor )
                    messagebox.showinfo("Success", "Produto encontrado")
                else:
                    messagebox.showwarning("Não encontrado", "Produto não encontrado")

            except Exception as e:
                print(f'Error: {e}') #SE EXEPT, EXIBE O ERRO (SALVOU O CODIGO)


        #BOTAO DE PESQUISA :)
        PesquisarButton = tk.Button(self.root,text = "Pesquisar",font= ("Georgia",10),width=13,command=pesquisar_fornecedor)
        PesquisarButton.place(x = 20,y=390)

        #FUNÇÃO DE LIMPAR
        def limparCampos():
            #LIMPAR CAMPOS
            self.entry_nome_fornecedor.delete(0, tk.END)
            self.entry_endereco.delete(0, tk.END)
            self.entry_telefone.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.entry_produto.delete(0, tk.END)
            self.entry_idFornecedor.delete(0, tk.END)
            self.entry_pesquisa.delete(0, tk.END)
        #BOTÃO DE LIMPAR
        limparButton = tk.Button(self.root,text = "LIMPAR",font= ("Georgia",10),width=13,command=limparCampos)
        limparButton.place(x = 547,y=330)

if __name__ == "__main__":
    root = tk.Tk()
    app = FORNECEDOR(root)
    root.mainloop()



                    
            


        





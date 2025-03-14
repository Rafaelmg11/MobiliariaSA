#IMPORTAR BIBLIOTECAS:
from tkinter import* #Importa tudo do tkinter
from tkinter import messagebox #Importa as caixas de mensagem
from tkinter import ttk #Importa o widgets tematicos do tkinter
from crudPrincipal import get_connection,create_fornecedores, listar_fornecedores, atualizar_fornecedor , deletar_fornecedor
import tkinter as tk
import mysql.connector


class PRODUTO:  

    def __init__(self,root,main_window):
        self.root = root
        self.main_window = main_window
        self.root.title("FORNECEDORES") #Define o titulo
        self.root.geometry("600x630") #Define o tamanho da janela
        self.root.configure(background = "BLUE") #Configura a cor de fundo da janela
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
        label_nome_fornecedor = Label(self.root,text = "Fornecedor: ",font = ("Century Gothic",13)) #Cria Label Produtos
        label_nome_fornecedor.place(x=50,y=100)

        label_endereco = Label(self.root,text = "Endereço: ",font = ("Century Gothic",13)) #Cria Label Produtos
        label_endereco.place(x=50,y=130)

        label_telefone = Label(self.root,text = "Telefone: ",font = ("Century Gothic",13)) #Cria Label Produtos
        label_telefone.place(x=50,y=160)

        label_email = Label(self.root,text = "Email: ",font = ("Century Gothic",13)) #Cria Label Produtos
        label_email.place(x=50,y=190)

        label_produto= Label(self.root,text = "Produto: ",font = ("Century Gothic",13)) #Cria Label Produtos
        label_produto.place(x=50,y=220)

        #CAMPOS DE ENTRADA
        self.entry_nome_fornecedor = tk.Entry(self.root, width=30,font=("Century Gothic",13))
        self.entry_nome_fornecedor.place(x=135,y=101)

        self.entry_endereco = tk.Entry(self.root, width=30,font=("Century Gothic",13))
        self.entry_endereco.place(x=155,y=131)

        self.entry_telefone = tk.Entry(self.root, width=30,font=("Century Gothic",13))
        self.entry_telefone.place(x=175,y=161)

        self.entry_email = tk.Entry(self.root, width=30,font=("Century Gothic",13))
        self.entry_email.place(x=217, y= 191)

        self.entry_produto = tk.Entry(self.root, width=30,font=("Century Gothic",13))
        self.entry_produto.place(x=205, y= 221)

        self.entry_pesquisa = tk.Entry(self.root, width=47,font= ("Century Gothic",13))
        self.entry_pesquisa.place(x=155,y=405)


        self.entry_idFornecedor = Label (self.root,text="ID Fornecedor: ",font = ("Century Gothic",13)) #Cria Label Codigo de Produto
        self.entry_idFornecedor.place(x=50,y=280)

        #CRIANDO A LISTA DE CADASTRO DE PRODUTOS:
        self.text_area = tk.Text(self.root, height=11,width=70)
        self.text_area.place(x=18,y=440)

        # Botões de ação
        botao_adicionar = tk.Button (self.root,text = "CADASTRAR",width=15,command=cadastrarFornecedor)
        botao_adicionar.place(x=178,y=330)

        botao_atualizar = tk.Button(self.root, text="EDITAR", command=alterar_fornecedor)
        botao_atualizar.place(x=312,y=330)  

        botao_deletar = tk.Button(self.root, text="EXCLUIR", command=excluir_fornecedor)
        botao_deletar.place(x=312,y=365)

        botao_listar  = tk.Button (self.root,text="LISTARR",width=15,command=listar_fornecedor)
        botao_listar.place(x=178,y=365)

    
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

                messagebox.showinfo("Success","Fornecedor criado com sucesso!")
            else:
                messagebox.showerror("Error","Todos os campos são obrigatórios" )

        #LISTAR PRODUTO
        def listar_fornecedor():
            fornecedores = listar_fornecedores() #PUXANDO FUNÇÃO DO CRUD
            self.text_area.delete(1.0, tk.END) #ACESSANDO A "LISTA" DA TELA
            for fornecedor in fornecedores: #produto ANDANDO EM produtos
                self.text_area.insert(tk.END, f"id.Fornecedor: {fornecedor[0]}, Fornecedor: {fornecedor[1]}, Endereço: {fornecedor[2]},Telefone: {fornecedor[3]},Email: {fornecedor[4]},Produto: {fornecedor[5]}\n")

        
        #FUNÇÃO DE ALTERAR PRODUTO:
        def alterar_fornecedor():
                
                #OBTENDO AS INFORMAÇÕES DOS CAMPOS DE TEXTOS
                nome = self.entry_nome_fornecedor.get()
                endereco = self.entry_endereco.get()
                telefone = self.entry_telefone.get()
                email = self.entry_email.get()
                produto = self.entry_produto.get()
                id_fornecedor=self.entry_idFornecedor.get()
                
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
                    messagebox.showinfo("Success","Fornecedor alterado com sucesso!")
                else:
                    messagebox.showerror("Error","Todos os campos são obrigatórios")

        def excluir_fornecedor():
            id_fornecedor = self.entry_idFornecedor.get() #RECEBENDO O VALOR QUE É PRA SER O CODPRODUTO DA TABELA
            if id_fornecedor: #SE codigo_produto RECEBER UM VALOR
                deletar_fornecedor(id_fornecedor) #PUXANDO FUNÇÃO DO CRUD

                #LIMPAR CAMPOS
                self.entry_nome_fornecedor.delete(0, tk.END)
                self.entry_endereco.delete(0, tk.END)
                self.entry_telefone.delete(0, tk.END)
                self.entry_email.delete(0, tk.END)
                self.entry_produto.delete(0, tk.END)
                self.entry_idFornecedor.delete(0, tk.END)

                messagebox.showinfo("Success","Fornecedor excluido com sucesso")
            else:
                messagebox.showerror("Error","O ID do Fornecedor é obrigatório")



        #FUNÇÃO DE PESQUISAR :) ;) OBS: NAO TEM RELAÇÃO COM O CRUD
        def pesquisar_fornecedor():
            id_fornecedor = self.entry_pesquisa.get() #CONEXÃO COM O BANCO DE DADOS
            conn = get_connection() #VARIAVEL PARA RECEBER A CONEXÃO
            self.cursor = conn.cursor() #sell.conn TRABALHAR COM A CONEXAO
            try:
                
                self.cursor.execute("SELECT produto, descricao, quantidade, valorDeCompra, valorDeVenda, fornecedor, codproduto FROM produto WHERE codproduto=%s or produto=%s or descricao=%s", (codigo_produto,codigo_produto,codigo_produto)) 
                # ACIMA SELECIONA AS COLUNAS DA TABELA SE codproduto OU produto OU descricao == codigo_produto
                # codproduto E produto E descricao PERMITE FAZER A BUSCA POR PRODUTO,DESCRICAO, E CODIGO DE PRODUTO
                #EM OUTROS CASOS PODERIA SER CPF E NÚMERO DE TELEFONE

                # CONSULTA NO BANCO
                produto_pesquisa = self.cursor.fetchone()
        
                # Verificando se o produto foi encontrado
                if produto_pesquisa:  # SE FOI ENCONTRADO...
                    produto, descricao, quantidade, valorDeCompra, valorDeVenda, fornecedor, codigo_produto = produto_pesquisa #ESSAS VARIAVEIS VAI RECEBER OS VALORES DA COLUNA DE ACORDO COM A ORDEM

                    #LIMPA TODOS OS CAMPOS ANTES DE RECEBER AS INFORMAÇOES
                    self.ProdutoEntry.delete(0, tk.END)
                    self.DescricaoEntry.delete(0, tk.END)
                    self.QuantidadeEntry.delete(0, tk.END)
                    self.ValorDeCompraEntry.delete(0, tk.END)
                    self.ValorDeVendaEntry.delete(0, tk.END)
                    self.FornecedorEntry.delete(0, tk.END)
                    self.CodigoEntry.delete(0, tk.END)

                    # Inserindo os dados nas entradas (Entry)
                    self.ProdutoEntry.insert(0, produto)
                    self.DescricaoEntry.insert(0, descricao)
                    self.QuantidadeEntry.insert(0, quantidade)
                    self.ValorDeCompraEntry.insert(0, valorDeCompra)
                    self.ValorDeVendaEntry.insert(0, valorDeVenda)
                    self.FornecedorEntry.insert(0, fornecedor)
                    self.CodigoEntry.insert(0, codigo_produto)
            
                    messagebox.showinfo("Success", "Produto encontrado")
                else:
                    messagebox.showwarning("Não encontrado", "Produto não encontrado")

            except Exception as e:
                print(f'Error: {e}') #SE EXEPT, EXIBE O ERRO (SALVOU O CODIGO)


        #BOTAO DE PESQUISA :)
        PesquisarButton = tk.Button(self.root,text = "Pesquisar",width = 15,command=pesquisar_produto)
        PesquisarButton.place(x = 20,y=405)

                    
            


        





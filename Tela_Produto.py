#IMPORTAR BIBLIOTECAS:
from tkinter import* #Importa tudo do tkinter
from tkinter import messagebox #Importa as caixas de mensagem
from tkinter import ttk #Importa o widgets tematicos do tkinter
from crudPrincipal import get_connection,create_produto, read_produto , update_produto , delete_produto 
import tkinter as tk
import mysql.connector


class PRODUTO:  

    def __init__(self,root): #main_window
        self.root = root
        # self.main_window = main_window
        self.root.title("CADASTRO DE PRODUTOS") #Define o titulo
        self.root.geometry("700x680") #Define o tamanho da janela
        self.root.configure(background = ("#00B2BF")) #Configura a cor de fundo da janela
        #ROXO #001703'''  #5424A2'''
        #VERDE LESBICO "#266F5A''
        #CIANO/VERDE #00D9CC  #32A8A0 ###2FCDC3
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

        #CARREGAR IMAGEM:
        #logo = PhotoImage (file = "icons/LogoMobiliariaSa.png") 

        # #ADICIONAR LOGO:
        # LogoLabel = Label(image = logo,bg = "PINK") #Cria um label para a imagem
        # LogoLabel.place(x=50,y=100)#Posiciona o label da imagem

        #CRIANDO LABELS:
        TituloLabel = Label(self.root,text="PRODUTOS: ",font=("Georgia",25),bg = "#00B2BF",fg = "WHITE") #Cria Label TITULO
        ##1D201F  ###040C24  ###1A1A1A  ###001703
        ProdutoLabel = Label(self.root,text = "Produto: ",font = ("Georgia",16),bg = "#00B2BF", fg = "WHITE") #Cria Label Produtos
        DescricaoLabel = Label(self.root,text= "Descrição: ",font= ("Georgia",16),bg = "#00B2BF", fg = "WHITE")#Cria Label Descrição
        QuantidadeLabel = Label (self.root,text= "Quantidade: ",font = ("Georgia",16),bg = "#00B2BF", fg = "WHITE") #Cria Label Quantidade
        ValorDeCompraLabel = Label(self.root,text="Valor de Compra: ",font=("Georgia",16),bg = "#00B2BF", fg = "WHITE") #Cria Label Valor de Compra
        ValorDeVendaLabel = Label (self.root,text="Valor de Venda: ",font=("Georgia",16),bg = "#00B2BF", fg = "WHITE") #Cria Label Valor de Venda
        FornecedorLabel = Label (self.root,text="Fornecedor: ",font = ("Georgia",16),bg = "#00B2BF", fg = "WHITE") #Cria Label Fornecedor
        CodigoLabel = Label (self.root,text="Codigo de Produto: ",font = ("Georgia",16),bg = "#00B2BF", fg = "WHITE") #Cria Label Codigo de Produto

        #POSICIONANDO LABELS:
        TituloLabel.pack(pady=40,anchor="center") #POSICIONA O TITULO

        ProdutoLabel.place(x=40,y=105)
        DescricaoLabel.place(x=40,y=135)
        QuantidadeLabel.place(x=40,y=165)
        ValorDeCompraLabel.place(x=40,y=195)
        ValorDeVendaLabel.place(x=40,y=225)
        FornecedorLabel.place(x=40,y=255)
        CodigoLabel.place(x=40,y=285)

        #CRIANDO CAMPOS DE ENTRADAS:
        self.ProdutoEntry = tk.Entry(self.root, width=50,font=("Century Gothic",11))
        self.DescricaoEntry = tk.Entry(self.root, width=48,font=("Century Gothic",11))
        self.QuantidadeEntry = tk.Entry(self.root, width=46,font=("Century Gothic",11))
        self.ValorDeCompraEntry = tk.Entry(self.root, width=21,font=("Century Gothic",11))
        self.ValorDeVendaEntry = tk.Entry(self.root, width=23,font=("Century Gothic",11))
        self.FornecedorEntry = tk.Entry(self.root, width=27,font=("Century Gothic",11))
        self.CodigoEntry = tk.Entry(self.root, width=21,font=("Century Gothic",11))
        self.PesquisaEntry = tk.Entry(self.root, width=66,font= ("Century Gothic",11))

        #POSICIONA OS CAMPOS DE ENTRADAS:
        self.ProdutoEntry.place(x=135,y=108)
        self.DescricaoEntry.place(x=151, y= 139)
        self.QuantidadeEntry.place(x=166, y= 169)
        self.ValorDeCompraEntry.place(x=217, y= 198)
        self.ValorDeVendaEntry.place(x=205, y= 228)
        self.FornecedorEntry.place(x=165, y= 258)
        self.CodigoEntry.place(x=233,y=288)
        self.PesquisaEntry.place(x=145,y=390)

        #CRIANDO A LISTA DE CADASTRO DE PRODUTOS:
        self.text_area = tk.Text(self.root, height=11,width=82)
        self.text_area.place(x=18,y=423)

        def voltar_para_principal():
            # Fechar a janela atual de cadastro de produtos e voltar para a janela principal
            self.root.quit()  # Fecha a janela de cadastro de produtos (destrói a instância)
            self.root.destroy()  # Fecha a janela de cadastro de produtos, liberando recursos

            self.main_window.deiconify()  # Reexibe a janela principal

        # voltar_button = tk.Button(self.root, text="Voltar para Tela Principal", width=15, font=("Century Gothic", 12), command=voltar_para_principal)
        # voltar_button.place(x=160, y=320)

    
        

    #FUNÇÃO PRA REGISTRAR NO BANCO DE DADOS:

        def cadastrarProduto():
            #OBTENDO AS INFORMAÇÕES DOS CAMPOS DE TEXTOS
            produto = self.ProdutoEntry.get()
            descricao = self.DescricaoEntry.get()
            quantidade = self.QuantidadeEntry.get()
            valorDeCompra = self.ValorDeCompraEntry.get()
            valorDeVenda = self.ValorDeVendaEntry.get()
            fornecedor = self.FornecedorEntry.get()

            #VERIFICANDO SE TODOS OS CAMPOS ESTÂO PREENCHIDOS:
            if produto and descricao and quantidade and valorDeCompra and valorDeVenda and fornecedor:
                create_produto(produto,descricao,quantidade,valorDeCompra,valorDeVenda,fornecedor)
            #Limpar campos:
                self.ProdutoEntry.delete(0, tk.END)
                self.DescricaoEntry.delete(0, tk.END)
                self.QuantidadeEntry.delete(0, tk.END)
                self.ValorDeCompraEntry.delete(0, tk.END)
                self.ValorDeVendaEntry.delete(0, tk.END)
                self.FornecedorEntry.delete(0, tk.END)
                self.CodigoEntry.delete(0, tk.END)

                messagebox.showinfo("Success","Produto criado com sucesso!")
            else:
                messagebox.showerror("Error","Todos os campos são obrigatórios" )

        #BOTÃO DE PRODUTO
        CadastrarButton = tk.Button (self.root,text = "CADASTRAR",width=15,command=cadastrarProduto)
        CadastrarButton.place(x=40,y=335)

        #LISTAR PRODUTO
        def listar_produto():
            produtos = read_produto() #PUXANDO FUNÇÃO DO CRUD
            self.text_area.delete(1.0, tk.END) #ACESSANDO A "LISTA" DA TELA
            for produto in produtos: #produto ANDANDO EM produtos
                self.text_area.insert(tk.END, f"COD.PRODUTO: {produto[0]}, Produto: {produto[1]}, Descricao: {produto[2]},Quantidade: {produto[3]},Valor de compra: {produto[4]},Valor de Venda: {produto[5]},Fornecedor: {produto[6]}\n")
    
        #BOTÃO DE LISTAR:
        ListarButton = tk.Button (self.root,text="LISTAR",width=15,command=listar_produto)
        ListarButton.place(x=290,y=335)
        #FUNÇÃO DE ALTERAR PRODUTO:
        def alterar_produto():
                
                #RECEBENDO VALORES
                produto = self.ProdutoEntry.get()
                descricao = self.DescricaoEntry.get()
                quantidade = self.QuantidadeEntry.get()
                valorDeCompra = self.ValorDeCompraEntry.get()
                valorDeVenda = self.ValorDeVendaEntry.get()
                fornecedor = self.FornecedorEntry.get()
                codigo_produto = self.CodigoEntry.get()
                
                #SE CAMPOS NÃO ESTIVER VAZIOS:
                if codigo_produto and produto and descricao and quantidade and valorDeCompra and valorDeVenda and fornecedor:
                    update_produto(produto,descricao,quantidade,valorDeCompra,valorDeVenda,fornecedor,codigo_produto) #PUXANDO A FUNÇÃO DO CRUD E AS VARIAVEIS

                    #LIMPAR CAMPOS
                    self.ProdutoEntry.delete(0, tk.END)
                    self.DescricaoEntry.delete(0, tk.END)
                    self.QuantidadeEntry.delete(0, tk.END)
                    self.ValorDeCompraEntry.delete(0, tk.END)
                    self.ValorDeVendaEntry.delete(0, tk.END)
                    self.FornecedorEntry.delete(0, tk.END)
                    self.CodigoEntry.delete(0, tk.END)
                    messagebox.showinfo("Success","Produto alterado com sucesso!")
                else:
                    messagebox.showerror("Error","Todos os campos são obrigatórios")
        
        #BOTÃO ALTERAR
        AlterarButton = tk.Button(self.root,text = "ALTERAR",width=15,command=alterar_produto)
        AlterarButton.place(x=164,y=335)  

        #FUNÇÃO DE EXCLUIR
        def excluir_produto():
            codigo_produto = self.CodigoEntry.get() #RECEBENDO O VALOR QUE É PRA SER O CODPRODUTO DA TABELA
            if codigo_produto: #SE codigo_produto RECEBER UM VALOR
                delete_produto(codigo_produto) #PUXANDO FUNÇÃO DO CRUD

                #LIMPAR CAMPOS
                self.ProdutoEntry.delete(0, tk.END)
                self.DescricaoEntry.delete(0, tk.END)
                self.QuantidadeEntry.delete(0, tk.END)
                self.ValorDeCompraEntry.delete(0, tk.END)
                self.ValorDeVendaEntry.delete(0, tk.END)
                self.FornecedorEntry.delete(0, tk.END)
                self.CodigoEntry.delete(0, tk.END)
                messagebox.showinfo("Success","Produto excluido com sucesso")
            else:
                messagebox.showerror("Error","O Codigo de Produto é obrigatório")

        #BOTAO DE EXCLUIR
        ExcluirButton = tk.Button(self.root,text = "EXCLUIR",width = 15,command=excluir_produto)
        ExcluirButton.place(x=418,y=335)
  

        #FUNÇÃO DE PESQUISAR :) ;) OBS: NAO TEM RELAÇÃO COM O CRUD
        def pesquisar_produto():
            codigo_produto = self.PesquisaEntry.get() #CONEXÃO COM O BANCO DE DADOS
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
        PesquisarButton.place(x = 20,y=390)

        #FUNÇÃO DE LIMPAR
        def limparCampos():
                self.ProdutoEntry.delete(0, tk.END)
                self.DescricaoEntry.delete(0, tk.END)
                self.QuantidadeEntry.delete(0, tk.END)
                self.ValorDeCompraEntry.delete(0, tk.END)
                self.ValorDeVendaEntry.delete(0, tk.END)
                self.FornecedorEntry.delete(0, tk.END)
                self.CodigoEntry.delete(0, tk.END)
        #BOTÃO DE LIMPAR
        limparButton = tk.Button(self.root,text = "LIMPAR",width = 15,command=limparCampos)
        limparButton.place(x = 547,y=335)



if __name__ == "__main__":
    root = tk.Tk()
    app = PRODUTO(root)
    root.mainloop()



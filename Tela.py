#IMPORTAR BIBLIOTECAS:
from tkinter import* #Importa tudo do tkinter
from tkinter import messagebox #Importa as caixas de mensagem
from tkinter import ttk #Importa o widgets tematicos do tkinter
from crudPrincipal import get_connection,create_produto,read_produto,update_produto,delete_produto,create_funcionario,read_funcionario,update_funcionario,delete_funcionario
import tkinter as tk
import mysql.connector


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#PRODUTO:
class PRODUTO:  
    
    #CRIANDO TELA PRODUTOS
    def __init__(self,root):
        self.root = root
        self.root.title("CADASTRO DE PRODUTOS") #Define o titulo
        self.root.geometry("600x630") #Define o tamanho da janela
        self.root.configure(background = "BLUE") #Configura a cor de fundo da janela
        self.root.resizable(width = False,height = False) #Impede que a janela seja redimensionada 
        #Criação de Widgets
        self.create_widgets()

    #CONECTANDO NO BANCO E CRIANDO CURSOR
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
        TituloLabel = Label(self.root,text="PRODUTOS: ",font=("Century Gothic",25),bg = "BLACK",fg = "WHITE") #Cria Label TITULO

        ProdutoLabel = Label(self.root,text = "Produto: ",font = ("Century Gothic",13)) #Cria Label Produtos
        DescricaoLabel = Label(self.root,text= "Descrição: ",font= ("Century Gothic",13))#Cria Label Descrição
        QuantidadeLabel = Label (self.root,text= "Quantidade: ",font=("Century Gothic",13)) #Cria Label Quantidade
        ValorDeCompraLabel = Label(self.root,text="Valor de Compra: ",font=("Century Gothic",13)) #Cria Label Valor de Compra
        ValorDeVendaLabel = Label (self.root,text="Valor de Venda: ",font=("Century Gothic",13)) #Cria Label Valor de Venda
        FornecedorLabel = Label (self.root,text="Fornecedor: ",font = ("Century Gothic",13)) #Cria Label Fornecedor
        CodigoLabel = Label (self.root,text="Codigo de Produto: ",font = ("Century Gothic",13)) #Cria Label Codigo de Produto

        #POSICIONANDO LABELS:
        TituloLabel.pack(pady=40,anchor="center") #POSICIONA O TITULO

        ProdutoLabel.place(x=50,y=100)
        DescricaoLabel.place(x=50,y=130)
        QuantidadeLabel.place(x=50,y=160)
        ValorDeCompraLabel.place(x=50,y=190)
        ValorDeVendaLabel.place(x=50,y=220)
        FornecedorLabel.place(x=50,y=250)
        CodigoLabel.place(x=50,y=280)

        #CRIANDO CAMPOS DE ENTRADAS:
        self.ProdutoEntry = tk.Entry(self.root, width=30,font=("Century Gothic",13))
        self.DescricaoEntry = tk.Entry(self.root, width=28,font=("Century Gothic",13))
        self.QuantidadeEntry = tk.Entry(self.root, width=25,font=("Century Gothic",13))
        self.ValorDeCompraEntry = tk.Entry(self.root, width=21,font=("Century Gothic",13))
        self.ValorDeVendaEntry = tk.Entry(self.root, width=23,font=("Century Gothic",13))
        self.FornecedorEntry = tk.Entry(self.root, width=27,font=("Century Gothic",13))
        self.CodigoEntry = tk.Entry(self.root, width=21,font=("Century Gothic",13))
        self.PesquisaEntry = tk.Entry(self.root, width=47,font= ("Century Gothic",13))

        #POSICIONA OS CAMPOS DE ENTRADAS:
        self.ProdutoEntry.place(x=135,y=101)
        self.DescricaoEntry.place(x=155, y= 131)
        self.QuantidadeEntry.place(x=175, y= 161)
        self.ValorDeCompraEntry.place(x=217, y= 191)
        self.ValorDeVendaEntry.place(x=205, y= 221)
        self.FornecedorEntry.place(x=165, y= 251)
        self.CodigoEntry.place(x=233,y=281)
        self.PesquisaEntry.place(x=155,y=405)

        #CRIANDO A LISTA DE CADASTRO DE PRODUTOS:
        self.text_area = tk.Text(self.root, height=11,width=70)
        self.text_area.place(x=18,y=440)
    
        

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

                messagebox.showinfo("Success","Usuario criado com sucesso!")
            else:
                messagebox.showerror("Error","Todos os campos são obrigatórios" )

        #BOTÃO DE PRODUTO
        CadastrarButton = tk.Button (self.root,text = "CADASTRAR",width=15,command=cadastrarProduto)
        CadastrarButton.place(x=178,y=330)

        #LISTAR PRODUTO
        def listar_produto():
            produtos = read_produto() #PUXANDO FUNÇÃO DO CRUD
            self.text_area.delete(1.0, tk.END) #ACESSANDO A "LISTA" DA TELA
            for produto in produtos: #produto ANDANDO EM produtos
                self.text_area.insert(tk.END, f"COD.PRODUTO: {produto[0]}, Produto: {produto[1]}, Descricao: {produto[2]},Quantidade: {produto[3]},Valor de compra: {produto[4]},Valor de Venda: {produto[5]},Fornecedor: {produto[6]}\n")
    
        #BOTÃO DE LISTAR:
        ListarButton = tk.Button (self.root,text="LISTAR",width=15,command=listar_produto)
        ListarButton.place(x=178,y=365)

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
        AlterarButton.place(x=312,y=330)  

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
        ExcluirButton.place(x=312,y=365)
  

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
        PesquisarButton.place(x = 20,y=405)

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
        limparButton.place(x = 440,y=200)
        


if __name__ == "__main__":
    root = tk.Tk()
    app = PRODUTO(root)
    root.mainloop()

#FIM PRODUTO: Rafael de Almeida de Magalhaes
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#





#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#FUNCIONARIO
class FUNCIONARIO:

    def __init__(self,root):
        self.root = root
        self.root.title("CADASTRO DE FUNCIONARIOS") #Define o titulo
        self.root.geometry("600x630") #Define o tamanho da janela
        self.root.configure(background = "BLUE") #Configura a cor de fundo da janela
        self.root.resizable(width = False,height = False) #Impede que a janela seja redimensionada 
        #Criação de Widgets
        self.create_widgets()


    def create_widgets(self):

        #CARREGAR IMAGEM:
        #logo = PhotoImage (file = "icons/LogoMobiliariaSa.png") 

        # #ADICIONAR LOGO:
        # LogoLabel = Label(image = logo,bg = "PINK") #Cria um label para a imagem
        # LogoLabel.place(x=50,y=100)#Posiciona o label da imagem

        #CRIANDO LABELS:
        TituloLabel = Label(self.root,text="CADASTRAR FUNCIONÁRIOS: ",font=("Century Gothic",25),bg = "BLACK",fg = "WHITE") #Cria Label TITULO

        nome = Label(self.root,text = "Nome: ",font = ("Century Gothic",13)) #Cria Label Nome
        cargo = Label(self.root,text= "Cargo: ",font= ("Century Gothic",13))#Cria Label Salario
        salario = Label (self.root,text= "Salário: ",font=("Century Gothic",13)) #Cria Label Cargo
      
        #POSICIONANDO LABELS:
        TituloLabel.pack(pady=40,anchor="center") #POSICIONA O TITULO

        nome.place(x=50,y=100)
        cargo.place(x=50,y=130)
        salario.place(x=50,y=160)

        #CRIANDO CAMPOS DE ENTRADAS:
        self.NomeEntry = tk.Entry(self.root, width=30,font=("Century Gothic",13))
        self.CargoEntry = tk.Entry(self.root, width=30,font=("Century Gothic",13))
        self.SalarioEntry = tk.Entry(self.root, width=30,font=("Century Gothic",13))

        #POSICIONA OS CAMPOS DE ENTRADAS:
        self.NomeEntry.place(x=135,y=101)
        self.CargoEntry.place(x=135,y=131)
        self.SalarioEntry.place(x=135,y=161)
     
        #CRIANDO A LISTA DE CADASTRO DE FUNCIONARIOS:
        self.text_area = tk.Text(self.root, height=11,width=70)
        self.text_area.place(x=18,y=440)
        

        #FUNÇÃO PRA REGISTRAR NO BANCO DE DADOS:

        def cadastrarFuncionario():
            #OBTENDO AS INFORMAÇÕES DOS CAMPOS DE TEXTOS
            nome = self.NomeEntry.get()
            cargo = self.CargoEntry.get()
            salario = self.SalarioEntry.get()

            #VERIFICANDO SE TODOS OS CAMPOS ESTÂO PREENCHIDOS:
            if nome and cargo and salario:
                create_funcionario(nome,cargo,salario)
                #Limpar campos:
                self.NomeEntry.delete(0, tk.END)
                self.CargoEntry.delete(0, tk.END)
                self.SalarioEntry.delete(0, tk.END)

                messagebox.showinfo("Success","Usuario criado com sucesso!")
            else:
                messagebox.showerror("Error","Todos os campos são obrigatórios")

        CadastrarButton = tk.Button (self.root,text = "CADASTRAR",width=15,command=cadastrarFuncionario)
        CadastrarButton.place(x=178,y=330)


        def listar_funcionario():
            funcionarios = read_funcionario()
            self.text_area.delete(1.0, tk.END)
            for funcionario in funcionarios:
                self.text_area.insert(tk.END, f"idfuncionario: {funcionario[0]}, Nome: {funcionario[1]}, Cargo: {funcionario[2]},Salário: {funcionario[3]}\n")
    
        ListarButton = tk.Button (self.root,text="LISTAR",width=15,command=listar_funcionario)
        ListarButton.place(x=178,y=365)

        def alterar_funcionario():
                
                nome = self.NomeEntry.get()
                cargo = self.CargoEntry.get()
                salario= self.SalarioEntry.get()
                                
                if nome and cargo and salario:
                    update_funcionario(nome,cargo,salario)
                    self.NomeEntry.delete(0, tk.END)
                    self.CargoEntry.delete(0, tk.END)
                    self.SalarioEntry.delete(0, tk.END)
                    messagebox.showinfo("Success","Funcionário alterado com sucesso!")
                else:
                    messagebox.showerror("Error","Todos os campos são obrigatórios")
            
        AlterarButton = tk.Button(self.root,text = "ALTERAR",width=15,command=alterar_funcionario)
        AlterarButton.place(x=312,y=330)  

        def excluir_funcionario():
            idfuncionario = 2#self.CodigoEntry.get()
            if idfuncionario:
                delete_funcionario(idfuncionario)
                self.NomeEntry.delete(0, tk.END)
                self.CargoEntry.delete(0, tk.END)
                self.SalarioEntry.delete(0, tk.END)

                messagebox.showinfo("Success","Funcionario excluido com sucesso")
            else:
                messagebox.showerror("Error","O ID do funcionario é obrigatório")

        ExcluirButton = tk.Button(self.root,text = "EXCLUIR",width = 15,command=excluir_funcionario)
        ExcluirButton.place(x=312,y=365)


if __name__ == "__main__":
    root = tk.Tk()
    app = FUNCIONARIO(root)
    root.mainloop()








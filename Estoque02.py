#IMPORTAR BIBLIOTECAS:
from tkinter import* #Importa tudo do tkinter
from tkinter import messagebox #Importa as caixas de mensagem
from tkinter import ttk #Importa o widgets tematicos do tkinter
from crud import create_produto, read_produto
import tkinter as tk


class CRUDApp:

    def __init__(self,root):
        self.root = root
        self.root.title("PRODUTOS")

        #Criação de Widgets
        self.create_widgets()


    def create_widgets(self):

        #CRIAR A JANELA
        jan = Tk()
        jan.title("Cadastro de produto")#Define o titulo
        jan.geometry("600x600") #Define o tamanho da janela
        jan.configure(background="BLUE")#Configura a cor de fundo da janela
        jan.resizable(width = False,height = False)#Impede que a janela seja redimensionada 

        #CARREGAR IMAGEM:
        #logo = PhotoImage (file = "icons/LogoMobiliariaSa.png") 

        # #ADICIONAR LOGO:
        # LogoLabel = Label(image = logo,bg = "PINK") #Cria um label para a imagem
        # LogoLabel.place(x=50,y=100)#Posiciona o label da imagem

        #CRIANDO LABELS:
        TituloLabel = Label(text="PRODUTOS: ",font=("Century Gothic",25),bg = "BLACK",fg = "WHITE") #Cria Label TITULO

        ProdutoLabel = Label(text = "Produto: ",font = ("Century Gothic",13)) #Cria Label Produtos
        DescricaoLabel = Label(text= "Descrição: ",font= ("Century Gothic",13))#Cria Label Descrição
        QuantidadeLabel = Label (text= "Quantidade: ",font=("Century Gothic",13)) #Cria Label Quantidade
        ValorDeCompraLabel = Label(text="Valor de Compra: ",font=("Century Gothic",13)) #Cria Label Valor de Compra
        ValorDeVendaLabel = Label (text="Valor de Venda: ",font=("Century Gothic",13)) #Cria Label Valor de Venda
        FornecedorLabel = Label (text="Fornecedor: ",font = ("Century Gothic",13)) #Cria Label Fornecedor

        #POSICIONANDO LABELS:
        TituloLabel.pack(pady=40,anchor="center") #POSICIONA O TITULO

        ProdutoLabel.place(x=50,y=100)
        DescricaoLabel.place(x=50,y=130)
        QuantidadeLabel.place(x=50,y=160)
        ValorDeCompraLabel.place(x=50,y=190)
        ValorDeVendaLabel.place(x=50,y=220)
        FornecedorLabel.place(x=50,y=250)

        #CRIANDO CAMPOS DE ENTRADAS:
        ProdutoEntry = ttk.Entry(width=30)
        DescricaoEntry = ttk.Entry(width=30)
        QuantidadeEntry = ttk.Entry(width=30)
        ValorDeCompraEntry = ttk.Entry(width=30)
        ValorDeVendaEntry = ttk.Entry(width=30)
        FornecedorEntry = ttk.Entry(width=30)

        #POSICIONA OS CAMPOS DE ENTRADAS:
        ProdutoEntry.place(x=135,y=105)
        DescricaoEntry.place(x=155, y= 135)
        QuantidadeEntry.place(x=175, y= 165)
        ValorDeCompraEntry.place(x=217, y= 195)
        ValorDeVendaEntry.place(x=205, y= 225)
        FornecedorEntry.place(x=165, y= 255)

        #CRIANDO A LISTA DE CADASTRO DE PRODUTOS:
        text_area = tk.Text(height = 10,width = 70)
        text_area.place(x=18,y=400)

        #CRIANDO BOTÃO:
        #CadastrarButton = ttk.Button(text = "CADASTRAR",width=15,command=cadastrarProduto())
        #AlterarButton = ttk.Button(text = "ALTERAR",width=15)
        ExcluirButton = ttk.Button(text = "EXCLUIR",width = 15)
        ListarButton = ttk.Button(text = "LISTAR",width=15)

        #POSICIONANDO OS BOTOES:
        #CadastrarButton.place(x=178,y=300)
        #AlterarButton.place(x=312,y =300)
        ListarButton.place(x=178,y=335)
        ExcluirButton.place(x=312,y=335)

        #FUNÇÃO PRA REGISTRAR NO BANCO DE DADOS:
        def cadastrarProduto():
            #OBTENDO AS INFORMAÇÕES DOS CAMPOS DE TEXTOS
            produto = ProdutoEntry.get()
            descricao = DescricaoEntry.get()
            quantidade = QuantidadeEntry.get()
            valorDeCompra = ValorDeCompraEntry.get()
            valorDeVenda = ValorDeVendaEntry.get()
            fornecedor = FornecedorEntry.get()

            #VERIFICANDO SE TODOS OS CAMPOS ESTÂO PREENCHIDOS:
            if produto and descricao and quantidade and valorDeCompra and valorDeVenda and fornecedor:
                create_produto(produto,descricao,quantidade,valorDeCompra,valorDeVenda,fornecedor)
                
             
                #Limpar campos:
                ProdutoEntry.delete(0,END)
                DescricaoEntry.delete(0,END)
                QuantidadeEntry.delete(0,END)
                ValorDeCompraEntry.delete(0,END)
                ValorDeVendaEntry.delete(0,END)
                FornecedorEntry.delete(0,END)


        CadastrarButton = ttk.Button(text = "CADASTRAR",width=15,command=cadastrarProduto)
        CadastrarButton.place(x=178,y=300)



        # def listar_produto():

        #     produtos = listar_produto()
        #     text_area.delete(1.0, tk.END)
        #     for produto in produtos:
        #         text_area.insert(tk.END, f" Produto: {produto[0]}, Descrição: {produto[1]}, Quantidade: {produto[2]}, Valor de Compra: {produto[3]}, Valor de Venda: {produto[4]}, Fornecedor: {produto[5]}")
                

        # AlterarButton = ttk.Button(text = "ALTERAR",width=15,command=listar_produto)
        # AlterarButton.place(x=312,y =300)

if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDApp(root)
    root.mainloop()



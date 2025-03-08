#IMPORTAR BIBLIOTECAS:
from tkinter import* #Importa tudo do tkinter
from tkinter import messagebox #Importa as caixas de mensagem
from tkinter import ttk #Importa o widgets tematicos do tkinter
from crud import create_produto, read_produto
import tkinter as tk


class CRUDApp:

    def __init__(self,root):
        self.root = root
        self.root.title("CADASTRO DE PRODUTOS") #Define o titulo
        self.root.geometry("600x600") #Define o tamanho da janela
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
        self.ProdutoEntry = tk.Entry(self.root, width=30)
        self.DescricaoEntry = tk.Entry(self.root, width=30)
        self.QuantidadeEntry = tk.Entry(self.root, width=30)
        self.ValorDeCompraEntry = tk.Entry(self.root, width=30)
        self.ValorDeVendaEntry = tk.Entry(self.root, width=30)
        self.FornecedorEntry = tk.Entry(self.root, width=30)

        #POSICIONA OS CAMPOS DE ENTRADAS:
        self.ProdutoEntry.place(x=135,y=105)
        self.DescricaoEntry.place(x=155, y= 135)
        self.QuantidadeEntry.place(x=175, y= 165)
        self.ValorDeCompraEntry.place(x=217, y= 195)
        self.ValorDeVendaEntry.place(x=205, y= 225)
        self.FornecedorEntry.place(x=165, y= 255)

        #CRIANDO A LISTA DE CADASTRO DE PRODUTOS:
        self.text_area = tk.Text(self.root, height=10,width=70)
        self.text_area.place(x=18,y=400)
    
        #CRIANDO BOTÃO:
        #CadastrarButton = ttk.Button(text = "CADASTRAR",width=15,command=cadastrarProduto())
        #AlterarButton = ttk.Button(text = "ALTERAR",width=15)
        ExcluirButton = tk.Button(text = "EXCLUIR",width = 15)
        #ListarButton = tk.Button(text = "LISTAR",width=15,command = read_produto)
        tk.Button(self.root, text="Listar",command=self.read_produto).place(x=178,y=335)

        #POSICIONANDO OS BOTOES:
        #CadastrarButton.place(x=178,y=300)
        #AlterarButton.place(x=312,y =300)
        #ListarButton.place(x=178,y=335)
        ExcluirButton.place(x=312,y=335)

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
                messagebox.showinfo("Success","Usuario criado com sucesso!")
            else:
                messagebox.showerror("Error","Todos os campos são obrigatórios" )

        CadastrarButton = ttk.Button(text = "CADASTRAR",width=15,command=cadastrarProduto)
        CadastrarButton.place(x=178,y=300)


    def read_produto(self):
        produtos = read_produto()
        self.text_area.delete(1.0, tk.END)
        for produto in produtos:
            self.text_area.insert(tk.END, f"COD: {produto[0]}, Produto: {produto[1]}, Descricao: {produto[2]},Quantidade: {produto[3]},Valor de compra: {produto[4]},Valor de Venda: {produto[5]},Fornecedor: {produto[6]}\n")
    
            

if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDApp(root)
    root.mainloop()



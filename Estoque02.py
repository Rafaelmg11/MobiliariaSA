#IMPORTAR BIBLIOTECAS:
from tkinter import* #Importa tudo do tkinter
from tkinter import messagebox #Importa as caixas de mensagem
from tkinter import ttk #Importa o widgets tematicos do tkinter
from crud import create_produto, read_produto , update_produto
import tkinter as tk


class CRUDApp:

    def __init__(self,root):
        self.root = root
        self.root.title("CADASTRO DE PRODUTOS") #Define o titulo
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

        #POSICIONA OS CAMPOS DE ENTRADAS:
        self.ProdutoEntry.place(x=135,y=101)
        self.DescricaoEntry.place(x=155, y= 131)
        self.QuantidadeEntry.place(x=175, y= 161)
        self.ValorDeCompraEntry.place(x=217, y= 191)
        self.ValorDeVendaEntry.place(x=205, y= 221)
        self.FornecedorEntry.place(x=165, y= 251)
        self.CodigoEntry.place(x=233,y=281)

        #CRIANDO A LISTA DE CADASTRO DE PRODUTOS:
        self.text_area = tk.Text(self.root, height=11,width=70)
        self.text_area.place(x=18,y=415)
    
        #CRIANDO BOTÃO:
        #CadastrarButton = ttk.Button(text = "CADASTRAR",width=15,command=cadastrarProduto())
        #AlterarButton = ttk.Button(text = "ALTERAR",width=15)
        ExcluirButton = tk.Button(text = "EXCLUIR",width = 15)
        #ListarButton = tk.Button(text = "LISTAR",width=15,command = read_produto)
        #tk.Button(self.root, text="LISTAR", width= 15,command=self.read_produto).place(x=178,y=365)

        #POSICIONANDO OS BOTOES:
        #CadastrarButton.place(x=178,y=300)
        #AlterarButton.place(x=312,y =300)
        #ListarButton.place(x=178,y=335)
        ExcluirButton.place(x=312,y=365)

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

        CadastrarButton = tk.Button (self.root,text = "CADASTRAR",width=15,command=cadastrarProduto)
        CadastrarButton.place(x=178,y=330)


        def listar_produto():
            produtos = read_produto()
            self.text_area.delete(1.0, tk.END)
            for produto in produtos:
                self.text_area.insert(tk.END, f"COD.PRODUTO: {produto[0]}, Produto: {produto[1]}, Descricao: {produto[2]},Quantidade: {produto[3]},Valor de compra: {produto[4]},Valor de Venda: {produto[5]},Fornecedor: {produto[6]}\n")
    
        ListarButton = tk.Button (self.root,text="LISTAR",width=15,command=listar_produto)
        ListarButton.place(x=178,y=365)

        def alterar_produto():
                
                produto = self.ProdutoEntry.get()
                descricao = self.DescricaoEntry.get()
                quantidade = self.QuantidadeEntry.get()
                valorDeCompra = self.ValorDeCompraEntry.get()
                valorDeVenda = self.ValorDeVendaEntry.get()
                fornecedor = self.FornecedorEntry.get()
                codigo_produto = self.CodigoEntry.get()
        

                verificar = self.CodigoEntry.get()
                
                
                if codigo_produto and produto and descricao and quantidade and valorDeCompra and valorDeVenda and fornecedor:
                    update_produto(produto,descricao,quantidade,valorDeCompra,valorDeVenda,fornecedor,codigo_produto)
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
            
        AlterarButton = tk.Button(self.root,text = "ALTERAR",width=15,command=alterar_produto)
        AlterarButton.place(x=312,y=330)        


if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDApp(root)
    root.mainloop()



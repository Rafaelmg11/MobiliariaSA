#IMPORTAR BIBLIOTECAS:
from tkinter import* #Importa tudo do tkinter
from tkinter import messagebox #Importa as caixas de mensagem
from tkinter import ttk #Importa o widgets tematicos do tkinter
from database import Database #Importa a classe Database do modulo database

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
TituloLabel = Label (text="PRODUTOS: ",font=("Century Gothic",25),bg = "BLACK",fg = "WHITE") #Cria Label TITULO

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

#CRIANDO BOTÃO:
#CadastrarButton = ttk.Button(text = "CADASTRAR",width=15)
AlterarButton = ttk.Button(text = "ALTERAR",width=15)
ExcluirButton = ttk.Button(text = "EXCLUIR",width = 15)
ListarButton = ttk.Button(text = "LISTAR",width=15)

#POSICIONANDO OS BOTOES:
#CadastrarButton.place(x=178,y=300)
AlterarButton.place(x=312,y =300)
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
    if produto == '' or descricao == '' or quantidade == '' or valorDeCompra == '' or valorDeVenda == '' or fornecedor == '':
        messagebox.showerror(title = "Erro de Registro",message = "PREENCHA TODOS OS CAMPOS") #Exibe mensagem de erro
    else:
        db = Database()
        db.cadastrarProduto(produto,descricao,quantidade,valorDeCompra,valorDeVenda,fornecedor)#Chama os metodos para registrar no banco de dados
        messagebox.showinfo("Success","Usuario registrado com sucesso!") #Exibe mensagem de confirmação e sucesso

        #Limpar campos:
        ProdutoEntry.delete(0,END)
        DescricaoEntry.delete(0,END)
        QuantidadeEntry.delete(0,END)
        ValorDeCompraEntry.delete(0,END)
        ValorDeVendaEntry.delete(0,END)
        FornecedorEntry.delete(0,END)

# FUNÇÃO BOTÃO DE CADASTRO:
# CadastrarButton = command=cadastrarProduto

CadastrarButton = ttk.Button(text = "CADASTRAR",width=15,command=cadastrarProduto)
CadastrarButton.place(x=178,y=300)
jan.mainloop()



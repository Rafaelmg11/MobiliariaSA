#IMPORTAR BIBLIOTECAS:
from tkinter import* #Importa tudo do tkinter
from tkinter import messagebox #Importa as caixas de mensagem
from tkinter import ttk #Importa o widgets tematicos do tkinter
from database import Database #Importa a classe Database do modulo database

#CRIAR A JANELA
jan = Tk()
jan.title("Cadastro de produto")#Define o titulo
jan.geometry("600x480") #Define o tamanho da janela
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
#TituloLabel.pack(pady=40,anchor="center") #POSICIONA O TITULO

ProdutoLabel.place(x=50,y=100)
DescricaoLabel.place(x=50,y=130)
QuantidadeLabel.place(x=50,y=160)
ValorDeCompraLabel.place(x=50,y=190)
ValorDeVendaLabel.place(x=50,y=220)
FornecedorLabel.place(x=50,y=250)

#CRIANDO CAMPOS DE ENTRADAS:
ProdutoEntry = ttk.Entry(width=30)
Descricao = ttk.Entry(width=30)
Quantidade = ttk.Entry(width=30)
ValorDeCompra = ttk.Entry(width=30)
ValorDeVenda = ttk.Entry(width=30)
Fornecedor = ttk.Entry(width=30)

#POSICIONA OS CAMPOS DE ENTRADAS:

ProdutoEntry.place(x=135,y=100)
jan.mainloop()
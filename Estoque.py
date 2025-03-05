#DECLARANDO AS LISTAS:
produtos = []
quantidade = []
valorDeCompra = []
valorDeVenda = []
fornecedor = []

#CADASTRO DE PRODUTO:
cont = int(input("Digite quantos produtos você deseja cadastrar: "))

for i in range(cont):

    produtos.append(input("Digite qual é o produto: "))
    quantidade.append(input("Digite a quantia para o estoque"))
    valorDeCompra.append(float (input("Digite qual é o valor de compra desse produto(valor do fornecidor): ")))
    valorDeVenda.append(float (input("Digite o valor de venda desse produto: ")))
    fornecedor.append(input ("Digite qual é o fornecedor: "))

#VERIFICANDO SE O USUARIO DESEJA CADASTRAR MAIS PRODUTOS
inf = input("Deseja cadastrar mais produtos? ")

while inf == 'sim' or inf == 's':

    cont = int(input("Digite quantos produtos você deseja cadastrar: "))

    for i in range(cont):

        produtos.append(input("Digite qual é o produto: "))
        quantidade.append(input("Digite a quantia para o estoque"))
        valorDeCompra.append(float (input("Digite qual é o valor de compra desse produto(valor do fornecidor): ")))
        valorDeVenda.append(float (input("Digite o valor de venda desse produto: ")))
        fornecedor.append(input ("Digite qual é o fornecedor: "))

        inf = input("Deseja cadastrar mais produtos? ")

print("FIM CADASTRO")
print("INCIO EDITAR")
#EDITAR PRODUTO:
pesquisarProduto = input("Digite o produto que você deseja pesquisar: ")
try:
    if pesquisarProduto in produtos:
        i = produtos.index(pesquisarProduto)
        respostaEditarP = input("Você deja alterar {} ?".format(pesquisarProduto))
        respostaEditarP.lower()
        if respostaEditarP == "sim" or "s":
            produtos[i] = (input("Digite qual é o produto: "))
            valorDeCompra[i] = (float (input("Digite qual é o valor de compra desse produto(valor do fornecidor): ")))
            valorDeVenda[i] = (float (input("Digite o valor de venda desse produto: ")))
            fornecedor[i] = (input ("Digite qual é o fornecedor: "))

            print (produtos)
            print(valorDeCompra)
            print(valorDeVenda)
            print(fornecedor)
except:
    print(oi)






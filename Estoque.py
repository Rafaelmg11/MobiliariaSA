#DECLARANDO AS LISTAS:
produtos = []
valorDeCompra = []
valorDeVenda = []
fornecedor = []

#CADASTRO DE PRODUTO:
cont = int(input("Digite quantos produtos você deseja cadastrar: "))

for 
produtos.append(input("Digite qual é o produto: "))
valorDeCompra.append(float (input("Digite qual é o valor de compra desse produto(valor do fornecidor): ")))
valorDeVenda.append(float (input("Digite o valor de venda desse produto: ")))
fornecedor.append(input ("Digite qual é o fornecedor: "))

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






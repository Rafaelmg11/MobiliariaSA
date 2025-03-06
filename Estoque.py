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
        fornecedor.append(input ("Digite qual é o fornecedor:\n "))

    
    inf = input("Deseja cadastrar mais produtos? ")

print("FIM CADASTRO")
print("INCIO EDITAR")

#EDITAR PRODUTO:

inf = input("Você deseja editar algum produto? ")

while inf == 'sim' or inf == 's':

    pesquisarProduto = input("Digite o produto que você deseja editar: ")
    try:
        i = produtos.index(pesquisarProduto)
        if pesquisarProduto in produtos:
            respostaEditarP = input("Você deja alterar {} ?".format(pesquisarProduto))
            respostaEditarP.lower()
            if respostaEditarP == "sim" or "s":
                produtos[i] = (input("Digite qual é o produto: "))
                quantidade[i] = int(input("Digite a quantidade de ".format(produtos[i])))
                valorDeCompra[i] = (float (input("Digite qual é o valor de compra desse produto(valor do fornecidor): ")))
                valorDeVenda[i] = (float (input("Digite o valor de venda desse produto: ")))
                fornecedor[i] = (input ("Digite qual é o fornecedor: "))

                print("Informações alteradas com sucesso! ")

                print("Produtos: {}".format(produtos))
                print("Estoque: {}".format(quantidade))
                print("Valores de compra: {}".format(valorDeCompra))
                print("Valores de venda: {}".format(valorDeVenda))
                print("Fornecedores: {}".format(fornecedor))

                inf = input("Você deseja editar algum produto? ")

                # print(produtos)
                # print(quantidade)
                # print(valorDeCompra)
                # print(valorDeVenda)
                # print(fornecedor)


                
    except:
        print("Produto invalido!!")
        inf = input("Deseja tentar novamente? ")


#EXCLUIR PRODUTO:

inf = input("Você deseja excluir algum produto? ")

while inf == 'sim' or inf == 's':

    excluirProduto = input("Digite o produto que você deseja excluir: ")
    try:
        i = produtos.index(excluirProduto)
        if excluirProduto in produtos:
            inf("Você deseja exlcuir {}? ".format(produtos[i]))
            if inf == 'sim' or inf == 's':
                produtos.pop(i)
                quantidade.pop(i)
                valorDeCompra.pop(i)
                valorDeVenda.pop(i)
                fornecedor.pop(i)

                inf = input("Você deseja excluir mais algum produto? ")

                print(produtos)
                print(quantidade)
                print(valorDeCompra)
                print(valorDeVenda)
                print(fornecedor)

    except:
        print("Produto invalido!!")
        inf = input("Deseja tentar novamente? ")





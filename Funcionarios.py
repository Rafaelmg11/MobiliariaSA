funcionarios = []
def adicionar_funcionario():
     
    adicionar_nomes = list(funcionarios)
    cont = int(input('Deseja adicionar quantos funcionários? '))

    for i in range(cont):
        nome = input('Insira o {}° nome: '.format(i+1))
        adicionar_nomes.append(nome)
        funcionarios = (adicionar_nomes)

        confirmacao = input('Deseja adicionar mais um nome? (S ou N) ').upper()

    if confirmacao == 'S':
        while confirmacao == 'S':
            nome = input('Insira o nome: ')
            adicionar_nomes.append(nome)
            funcionarios = (adicionar_nomes)
            confirmacao = input('Deseja adicionar mais um nome? (S ou N): ').upper()
        if confirmacao != 'S':
            print('Alterações feitas:')
            print(funcionarios)
    elif confirmacao == 'N':
            print(funcionarios)
def excluir_funcionario():
     
escolhido = input('Digite um dos nomes da lista para excluir: ')
if funcionarios[i] == escolhido

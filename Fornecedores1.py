import tkinter as tk
from tkinter import messagebox

#Lista
fornecedores = []

# Função para adicionar
def adicionar_fornecedores():
    nome_fornecedor = entry_nome_fornecedor.get()
    endereco = entry_endereco.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    produto = entry_produto.get()

    if not nome_fornecedor or not endereco or not telefone or not email or not produto:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return

    fornecedor = {
        "nome_fornecedor": nome_fornecedor,
        "endereco": endereco,
        "telefone": telefone,
        "email": email,
        "produto": produto
    }

    fornecedores.append(fornecedor)
    atualizar_lista_fornecedores()

    entry_nome_fornecedor.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_produto.delete(0, tk.END)

    messagebox.showinfo("Sucesso", "Funcionário adicionado com sucesso!")

# Função para atualizar a lista de funcionários
def atualizar_lista_fornecedores():
    listbox_fornecedores.delete(0, tk.END)
    for fornecedor in fornecedores:
        listbox_fornecedores.insert(tk.END, f"Fornecedor: {fornecedor['nome_fornecedor']}   Endereço: {fornecedor['endereco']}   Telefone: {fornecedor['telefone']}   Email: {fornecedor['email']}   Produto: {fornecedor['produto']}")

# Função para selecionar o funcionário da lista e carregar nos campos
def selecionar_fornecedor(event):
    try:
        indice_selecionado = listbox_fornecedores.curselection()[0]
        fornecedor = fornecedores[indice_selecionado]
        entry_nome_fornecedor.delete(0, tk.END)
        entry_nome_fornecedor.insert(tk.END, fornecedor['nome_fornecedor'])

        entry_endereco.delete(0, tk.END)
        entry_endereco.insert(tk.END, fornecedor['endereco'])

        entry_telefone.delete(0, tk.END)
        entry_telefone.insert(tk.END, fornecedor['telefone'])

        entry_email.delete(0, tk.END)
        entry_email.insert(tk.END, fornecedor['email'])

        entry_produto.delete(0, tk.END)
        entry_produto.insert(tk.END, fornecedor['produto'])
    except IndexError:
        pass

# Função para atualizar as informações do funcionário selecionado
def atualizar_fornecedor():
    try:
        indice_selecionado = listbox_fornecedores.curselection()[0]
        fornecedor = fornecedores[indice_selecionado]
        
        fornecedor['nome_fornecedor'] = entry_nome_fornecedor.get()
        fornecedor['endereco'] = entry_endereco.get()
        fornecedor['telefone'] = entry_telefone.get()
        fornecedor['email'] = entry_telefone.get()
        fornecedor['produto'] = entry_produto.get()

        atualizar_lista_fornecedores()

        entry_nome_fornecedor.delete(0, tk.END)
        entry_endereco.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_produto.delete(0, tk.END)

        messagebox.showinfo("Sucesso", "Fornecedor atualizado com sucesso!")
    except IndexError:
        messagebox.showerror("Erro", "Selecione um fornecedor da lista.")

#Função para deletar
def deletar_fornecedor():
    try:
        indice_selecionado = listbox_fornecedores.curselection()[0]
        del fornecedores[indice_selecionado]
        atualizar_lista_fornecedores()

        entry_nome_fornecedor.delete(0, tk.END)
        entry_endereco.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_produto.delete(0, tk.END)

        messagebox.showinfo("Sucesso", "Fornecedor deletado com sucesso!")
    except IndexError:
        messagebox.showerror("Erro", "Selecione um fornecedor da lista.")
#Função para limpar os campos
def limpar_campos():
        entry_nome_fornecedor.delete(0, tk.END)
        entry_endereco.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_produto.delete(0, tk.END)

#Janela principal
root = tk.Tk()
root.title("Fornecedores")

#Tamanho da janela
root.geometry("1920x1080")

# Labels
label_nome_fornecedor = tk.Label(root, text="Fornecedor :")
label_nome_fornecedor.place(x=650,y=40)

label_endereco = tk.Label(root, text="Endereço :")
label_endereco.place(x=650,y=70)

label_telefone = tk.Label(root, text="Telefone :")
label_telefone.place(x=650,y=100)

label_email = tk.Label(root, text="Email :")
label_email.place(x=650,y=130)

label_produto = tk.Label(root, text="Produto :")
label_produto.place(x=650,y=160)

# Entradas de texto
entry_nome_fornecedor = tk.Entry(root)
entry_nome_fornecedor.place(x=730,y=40)

entry_endereco = tk.Entry(root)
entry_endereco.place(x=730,y=70)

entry_telefone = tk.Entry(root)
entry_telefone.place(x=730,y=100)

entry_email = tk.Entry(root)
entry_email.place(x=730,y=130)

entry_produto = tk.Entry(root)
entry_produto.place(x=730,y=160)


# Botões de ação
botao_adicionar = tk.Button(root, text="Adicionar Fornecedor", command=adicionar_fornecedores)
botao_adicionar.place(x=650,y=240)

botao_atualizar = tk.Button(root, text="Atualizar Fornecedor", command=atualizar_fornecedor)
botao_atualizar.place(x=800,y=240)

botao_deletar = tk.Button(root, text="Deletar Fornecedor", command=deletar_fornecedor)
botao_deletar.place(x=650,y=280)

botao_limpar = tk.Button(root, text="Limpar campos", command=limpar_campos)
botao_limpar.place(x=800,y=280)

# Lista de funcionários
listbox_fornecedores = tk.Listbox(root, width=130, height=30)
listbox_fornecedores.place(x=650,y=360)
listbox_fornecedores.bind("<ButtonRelease-1>", selecionar_fornecedor)

# Inicializa a lista
atualizar_lista_fornecedores()

# Iniciando a interface
root.mainloop()
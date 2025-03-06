import tkinter as tk
from tkinter import messagebox

#Lista
funcionarios = []

# Função para adicionar
def adicionar_funcionario():
    nome = entry_nome.get()
    cargo = entry_cargo.get()
    salario = entry_salario.get()

    if not nome or not cargo or not salario:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return

    funcionario = {
        "nome": nome,
        "cargo": cargo,
        "salario": salario
    }

    funcionarios.append(funcionario)
    atualizar_lista_funcionarios()

    entry_nome.delete(0, tk.END)
    entry_cargo.delete(0, tk.END)
    entry_salario.delete(0, tk.END)

    messagebox.showinfo("Sucesso", "Funcionário adicionado com sucesso!")

# Função para atualizar a lista de funcionários
def atualizar_lista_funcionarios():
    listbox_funcionarios.delete(0, tk.END)
    for funcionario in funcionarios:
        listbox_funcionarios.insert(tk.END, f"Nome: {funcionario['nome']}    Cargo: {funcionario['cargo']}    Salário: {funcionario['salario']}")

# Função para selecionar o funcionário da lista e carregar nos campos
def selecionar_funcionario(event):
    try:
        indice_selecionado = listbox_funcionarios.curselection()[0]
        funcionario = funcionarios[indice_selecionado]
        entry_nome.delete(0, tk.END)
        entry_nome.insert(tk.END, funcionario['nome'])
        entry_cargo.delete(0, tk.END)
        entry_cargo.insert(tk.END, funcionario['cargo'])
        entry_salario.delete(0, tk.END)
        entry_salario.insert(tk.END, funcionario['salario'])
    except IndexError:
        pass

# Função para atualizar as informações do funcionário selecionado
def atualizar_funcionario():
    try:
        indice_selecionado = listbox_funcionarios.curselection()[0]
        funcionario = funcionarios[indice_selecionado]
        
        funcionario['nome'] = entry_nome.get()
        funcionario['cargo'] = entry_cargo.get()
        funcionario['salario'] = entry_salario.get()

        atualizar_lista_funcionarios()

        entry_nome.delete(0, tk.END)
        entry_cargo.delete(0, tk.END)
        entry_salario.delete(0, tk.END)

        messagebox.showinfo("Sucesso", "Funcionário atualizado com sucesso!")
    except IndexError:
        messagebox.showerror("Erro", "Selecione um funcionário da lista.")

#Função para deletar
def deletar_funcionario():
    try:
        indice_selecionado = listbox_funcionarios.curselection()[0]
        del funcionarios[indice_selecionado]
        atualizar_lista_funcionarios()

        entry_nome.delete(0, tk.END)
        entry_cargo.delete(0, tk.END)
        entry_salario.delete(0, tk.END)

        messagebox.showinfo("Sucesso", "Funcionário deletado com sucesso!")
    except IndexError:
        messagebox.showerror("Erro", "Selecione um funcionário da lista.")
#Função para limpar os campos
def limpar_campos():
        entry_nome.delete(0, tk.END)
        entry_cargo.delete(0, tk.END)
        entry_salario.delete(0, tk.END)

#Janela principal
root = tk.Tk()
root.title("Funcionários")

#Tamanho da janela
root.geometry("1920x1080")

# Labels
label_nome = tk.Label(root, text="Nome:")
label_nome.place(x=850,y=10)

label_cargo = tk.Label(root, text="Cargo:")
label_cargo.place(x=850,y=40)

label_salario = tk.Label(root, text="Salário:")
label_salario.place(x=850,y=70)

# Entradas de texto
entry_nome = tk.Entry(root)
entry_nome.place(x=900,y=11)

entry_cargo = tk.Entry(root)
entry_cargo.place(x=900,y=41)

entry_salario = tk.Entry(root)
entry_salario.place(x=900,y=71)

# Botões de ação
botao_adicionar = tk.Button(root, text="Adicionar Funcionário", command=adicionar_funcionario)
botao_adicionar.place(x=889,y=110)

botao_atualizar = tk.Button(root, text="Atualizar Funcionário", command=atualizar_funcionario)
botao_atualizar.place(x=891,y=150)

botao_deletar = tk.Button(root, text="Deletar Funcionário", command=deletar_funcionario)
botao_deletar.place(x=896,y=190)

botao_limpar = tk.Button(root, text="Limpar campos", command=limpar_campos)
botao_limpar.place(x=905,y=230)

# Lista de funcionários
listbox_funcionarios = tk.Listbox(root, width=50, height=20)
listbox_funcionarios.place(x=800,y=275)
listbox_funcionarios.bind("<ButtonRelease-1>", selecionar_funcionario)

# Inicializa a lista
atualizar_lista_funcionarios()

# Iniciando a interface
root.mainloop()
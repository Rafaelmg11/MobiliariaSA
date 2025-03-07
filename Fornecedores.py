import tkinter as tk
from tkinter import messagebox

class fornecedores:
    def __init__(self,root):
        self.root = root
        self.root.title("ADICIONAR FORNECEDORES")

        #Criação de WIDGETS
        self.create_widgets()
        pass

    def create_widgets(self):
        #Labels
        tk.Label(self.root,text="Nome:").grid(row=0, column=0)
        tk.Label(self.root,text="Telefone:").grid(row=1, column=0)
        tk.Label(self.root,text="Email:").grid(row=2, column=0)
        tk.Label(self.root,text="Endereço:").grid(row=3, column=0)
        tk.Label(self.root,text="Produto:").grid(row=4, column=0)

        #Cria as caixas para digitar os valores
        self.nome_entry = tk.Entry(self.root)
        self.telefone_entry = tk.Entry(self.root)
        self.email_entry = tk.Entry(self.root)
        self.endereco_entry = tk.Entry(self.root)
        self.produtos_entry = tk.Entry(self.root)
        

        self.nome_entry.grid(row=0, column=1)
        self.telefone_entry.grid(row=1, column=1)
        self.email_entry.grid(row=2, column=1)
        self.endereco_entry.grid(row=3, column=1)
        self.produtos_entry.grid(row=4, column=1)

        #Botoes do crud
        tk.Button(self.root,text="Adicionar Fornecedor", command=self.add_fornecedores).grid(row=6, column=0, columnspan=1)
        tk.Button(self.root,text="Listar Fornecedor", command=self.add_fornecedores).grid(row=6, column=1, columnspan=1)
        tk.Button(self.root,text="Alterar Fornecedor", command=self.add_fornecedores).grid(row=7, column=0, columnspan=1)
        tk.Button(self.root,text="Excluir Fornecedor", command=self.add_fornecedores).grid(row=7, column=1, columnspan=1)

        self.text_area = tk.Text(self.root, height=10, width=80)
        self.text_area.grid(row=10, column=0, columnspan=4)

    def add_fornecedores(self):
        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()
        endereco = self.endereco_entry.get()
        produtos = self.produtos_entry.get()
        

        if nome and telefone and email and endereco and produtos:
            add_fornecedores(nome,telefone,email,endereco,produtos)
            self.nome_entry.delete(0,tk.END)
            self.telefone_entry.delete(0,tk.END)
            self.email_entry.delete(0,tk.END)
            self.endereco_entry.delete(0,tk.END)
            self.produtos_entry.delete(0,tk.END)
            messagebox.showinfo("susseso","usuario criado com sussesso")

        else:
            messagebox.showerror("erro","todos os campos sao obrigatorios")
    
    def lista_fornecedores(self):
        fornecedores = lista_fornecedores()
        self.text_area.delete(1.0,tk.END)
        for user in fornecedores:
            self.text_area.insert(tk.END,f"id: {user[0]},nome: {user[1]},telefone: {user[2]},emdereço: {user[3]}\n")

    def update_user(self):
        user_id = self.user_id_entry.get()
        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()
        endereco = self.endereco_entry.get()
        produtos = self.produtos_entry.get()

        if user_id and nome and telefone and email and endereco and produtos:
            add_fornecedores(user_id,nome,telefone,email,endereco,produtos,user_id)
            self.nome_entry.delete(0,tk.END)
            self.telefone_entry.delete(0,tk.END)
            self.email_entry.delete(0,tk.END)
            self.endereco_entry.delete(0,tk.END)
            self.produtos_entry.delete(0,tk.END)
            messagebox.showinfo("susseso","usuario alterado com sussesso")

        else:
            messagebox.showerror("erro","todos os campos sao obrigatorios")   


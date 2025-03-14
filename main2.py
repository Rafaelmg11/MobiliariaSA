import tkinter as tk
from Tela_Produto import PRODUTO  # Importa a classe PRODUTO do arquivo produto.py
from Funcionario import FUNCIONARIO
from Tela_Fornecedor import FORNECEDOR

#TEM QUE FAZER O FUNCIONARIO FECHAR
#TEM QUE FAZER O FORNECEDOR ABRIR E FECHAR
#ARRUMAR OS FRONT ENDS
#TELA DE LOGIN
#TELA DE FATURA

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Tela Principal")
        self.root.geometry("500x500")
        self.root.configure(background="lightblue")  # Cor de fundo da janela principal
        
        # Criando um botão para abrir a janela do PRODUTO
        abrir_produto_button = tk.Button(self.root, text="Abrir Cadastro de Produto", width=30, font=("Century Gothic", 13), command=self.abrir_produto)
        abrir_produto_button.place(x=20,y=150)

        abrir_funcionario_button = tk.Button(self.root, text="Abrir Cadastro de Funcionario", width=30, font=("Century Gothic", 13), command=self.abrir_funcionario)
        abrir_funcionario_button.place(x=20,y=50)

        abrir_fornecedor_button = tk.Button(self.root, text="Abrir Aba de Fornecedor", width=30, font=("Century Gothic", 13), command=self.abrir_fornecedor)
        abrir_fornecedor_button.place(x=20,y=250)

    def abrir_produto(self):
        # Oculta a janela principal
        self.root.withdraw()

        # Cria uma nova janela Tkinter para o cadastro de produto
        root_produto = tk.Tk()  # Cria a nova instância da janela para o cadastro de produto
        app_produto = PRODUTO(root_produto, self.root)  # Passa a referência da janela principal (self.root)
        root_produto.protocol("WM_DELETE_WINDOW", lambda: self.reabrir_janela())  # Fechar corretamente ao fechar a janela de cadastro
        root_produto.mainloop()  # Inicia a execução da janela do PRODUTO

    def abrir_funcionario(self):
        # Cria uma nova janela Tkinter para o cadastro de produto
        root_funcionario = tk.Tk()  # Cria a nova instância da janela para o cadastro de produto
        app_funcionario = FUNCIONARIO(root_funcionario,self.root)  # Cria a instância da classe PRODUTO
        root_funcionario.protocol("WM_DELETE_WINDOW", lambda: self.reabrir_janela())  # Fechar corretamente ao fechar a janela de cadastro
        root_funcionario.mainloop()  # Inicia a execução da janela do PRODUTO

    def abrir_fornecedor(self):
        # Cria uma nova janela Tkinter para o cadastro de produto
        root_fornecedor = tk.Tk()  # Cria a nova instância da janela para o cadastro de produto
        app_fornecedor = FORNECEDOR(root_fornecedor,self.root)  # Cria a instância da classe PRODUTO
        root_fornecedor.protocol("WM_DELETE_WINDOW", lambda: self.reabrir_janela())  # Fechar corretamente ao fechar a janela de cadastro
        root_fornecedor.mainloop()  # Inicia a execução da janela do PRODUTO

    def reabrir_janela(self):
        self.root.deiconify()  # Reexibe a janela principal
        self.root.quit()  # Encerra o loop de eventos da janela de cadastro

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()
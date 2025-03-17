import tkinter as tk
from Tela_Produto import PRODUTO  # Importa a classe PRODUTO do arquivo produto.py
from Tela_Fornecedor import FORNECEDOR


class Menu2:
    def __init__(self, root,main_window):
        self.root = root
        self.main_window = main_window
        self.root.title("Tela Principal")
        self.root.geometry("600x600")
        self.root.configure(background="#5424A2")  # Cor de fundo da janela principal
        
        # ABRINDO OUTRAS JANELAS:
        abrir_produto_button = tk.Button(self.root, text="Abrir Cadastro de Produto", width=30, font=("Century Gothic", 13), command=self.abrir_produto)
        abrir_produto_button.place(x=150,y=350)
       
        abrir_fornecedor_button = tk.Button(self.root, text="Abrir Cadastro de Fornecedor", width=30, font=("Century Gothic", 13), command=self.abrir_fornecedor)
        abrir_fornecedor_button.place(x=150,y=450)

        #LOGO:
        # CARREGAR IMAGEM
        self.logo = tk.PhotoImage(file="icons/LogoMobiliaria.png") #Carrega a imagem da logo
        self.LogoLabel = tk.Label(self.root,image = self.logo, bg = "#5424A2") #Cria um label para a image, do logo
        self.LogoLabel.place(x=205,y=100) #Posiciona o label no frama esquerdo 

    def abrir_produto(self):
        # Oculta a janela principal
        self.root.withdraw()
        # Cria uma nova janela Tkinter para o cadastro de produto
        root_produto = tk.Tk()  # Cria a nova instância da janela para o cadastro de produto
        app_produto = PRODUTO(root_produto, self.root)  # Passa a referência da janela principal (self.root)
        root_produto.protocol("WM_DELETE_WINDOW", lambda: self.reabrir_janela())  # Fechar corretamente ao fechar a janela 
        root_produto.mainloop()  # Inicia a execução da janela do PRODUTO

    def abrir_fornecedor(self):
        # Oculta a janela principal
        self.root.withdraw()
        # Cria uma nova janela Tkinter para o cadastro de fornecedor
        root_fornecedor = tk.Tk()  # Cria a nova instância da janela para o cadastro de produto
        app_fornecedor = FORNECEDOR(root_fornecedor,self.root)  # Cria a instância da classe FORNECEDOR
        root_fornecedor.protocol("WM_DELETE_WINDOW", lambda: self.reabrir_janela())  # Fechar corretamente ao fechar a janela de cadastro
        root_fornecedor.mainloop()  # Inicia a execução da janela de fornecedor


    def reabrir_janela(self):
        self.root.deiconify()  # Reexibe a janela principal
        self.root.quit()  # Encerra o loop de eventos da janela de cadastro

if __name__ == "__main__":
    root = tk.Tk()
    app = Menu2(root)
    root.mainloop()
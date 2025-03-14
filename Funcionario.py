#IMPORTAR BIBLIOTECAS:
from tkinter import* #Importa tudo do tkinter
from tkinter import messagebox #Importa as caixas de mensagem
from tkinter import ttk #Importa o widgets tematicos do tkinter
from crudPrincipal import create_funcionario, read_funcionario, update_funcionario , delete_funcionario 
import tkinter as tk


class FUNCIONARIO:

    def __init__(self,root):
        self.root = root
        self.root.title("CADASTRO DE FUNCIONARIOS") #Define o titulo
        self.root.geometry("600x630") #Define o tamanho da janela
        self.root.configure(background = "BLUE") #Configura a cor de fundo da janela
        self.root.resizable(width = False,height = False) #Impede que a janela seja redimensionada 
        #Criação de Widgets
        self.create_widgets()


    def create_widgets(self):

        #CARREGAR IMAGEM:
        #logo = PhotoImage (file = "icons/LogoMobiliariaSa.png") 

        # #ADICIONAR LOGO:
        # LogoLabel = Label(image = logo,bg = "PINK") #Cria um label para a imagem
        # LogoLabel.place(x=50,y=100)#Posiciona o label da imagem

        #CRIANDO LABELS:
        TituloLabel = Label(self.root,text="CADASTRAR FUNCIONÁRIOS: ",font=("Century Gothic",25),bg = "BLACK",fg = "WHITE") #Cria Label TITULO

        nome = Label(self.root,text = "Nome: ",font = ("Century Gothic",13)) #Cria Label Nome
        cargo = Label(self.root,text= "Cargo: ",font= ("Century Gothic",13))#Cria Label Salario
        salario = Label (self.root,text= "Salário: ",font=("Century Gothic",13)) #Cria Label Cargo
      
        #POSICIONANDO LABELS:
        TituloLabel.pack(pady=40,anchor="center") #POSICIONA O TITULO

        nome.place(x=50,y=100)
        cargo.place(x=50,y=130)
        salario.place(x=50,y=160)

        #CRIANDO CAMPOS DE ENTRADAS:
        self.NomeEntry = tk.Entry(self.root, width=30,font=("Century Gothic",13))
        self.CargoEntry = tk.Entry(self.root, width=30,font=("Century Gothic",13))
        self.SalarioEntry = tk.Entry(self.root, width=30,font=("Century Gothic",13))

        #POSICIONA OS CAMPOS DE ENTRADAS:
        self.NomeEntry.place(x=135,y=101)
        self.CargoEntry.place(x=135,y=131)
        self.SalarioEntry.place(x=135,y=161)
     
        #CRIANDO A LISTA DE CADASTRO DE FUNCIONARIOS:
        self.text_area = tk.Text(self.root, height=11,width=70)
        self.text_area.place(x=18,y=440)
        

        #FUNÇÃO PRA REGISTRAR NO BANCO DE DADOS:

        def cadastrarFuncionario():
            #OBTENDO AS INFORMAÇÕES DOS CAMPOS DE TEXTOS
            nome = self.NomeEntry.get()
            cargo = self.CargoEntry.get()
            salario = self.SalarioEntry.get()

            #VERIFICANDO SE TODOS OS CAMPOS ESTÂO PREENCHIDOS:
            if nome and cargo and salario:
                create_funcionario(nome,cargo,salario)
                #Limpar campos:
                self.NomeEntry.delete(0, tk.END)
                self.CargoEntry.delete(0, tk.END)
                self.SalarioEntry.delete(0, tk.END)

                messagebox.showinfo("Success","Usuario criado com sucesso!")
            else:
                messagebox.showerror("Error","Todos os campos são obrigatórios")

        CadastrarButton = tk.Button (self.root,text = "CADASTRAR",width=15,command=cadastrarFuncionario)
        CadastrarButton.place(x=178,y=330)


        def listar_funcionario():
            funcionarios = read_funcionario()
            self.text_area.delete(1.0, tk.END)
            for funcionario in funcionarios:
                self.text_area.insert(tk.END, f"idfuncionario: {funcionario[0]}, Nome: {funcionario[1]}, Cargo: {funcionario[2]},Salário: {funcionario[3]}\n")
    
        ListarButton = tk.Button (self.root,text="LISTAR",width=15,command=listar_funcionario)
        ListarButton.place(x=178,y=365)

        def alterar_funcionario():
                
                nome = self.NomeEntry.get()
                cargo = self.CargoEntry.get()
                salario= self.SalarioEntry.get()

                verificar = self.idusuario.get()
                
                
                if nome and cargo and salario:
                    update_funcionario(nome,cargo,salario)
                    self.NomeEntry.delete(0, tk.END)
                    self.CargoEntry.delete(0, tk.END)
                    self.SalarioEntry.delete(0, tk.END)
                    messagebox.showinfo("Success","Funcionário alterado com sucesso!")
                else:
                    messagebox.showerror("Error","Todos os campos são obrigatórios")
            
        AlterarButton = tk.Button(self.root,text = "ALTERAR",width=15,command=alterar_funcionario)
        AlterarButton.place(x=312,y=330)  

        def excluir_funcionario():
            idfuncionario = self.CodigoEntry.get()
            if idfuncionario:
                delete_funcionario(idfuncionario)
                self.NomeEntry.delete(0, tk.END)
                self.CargoEntry.delete(0, tk.END)
                self.SalarioEntry.delete(0, tk.END)

                messagebox.showinfo("Success","Funcionario excluido com sucesso")
            else:
                messagebox.showerror("Error","O ID do funcionario é obrigatório")

        ExcluirButton = tk.Button(self.root,text = "EXCLUIR",width = 15,command=excluir_funcionario)
        ExcluirButton.place(x=312,y=365)


if __name__ == "__main__":
    root = tk.Tk()
    app = FUNCIONARIO(root)
    root.mainloop()
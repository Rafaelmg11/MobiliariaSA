from tkinter import* 
from tkinter import messagebox 
from tkinter import ttk

jan = Tk() 
jan.title("SL Sytens - Painel de Acesso") 
jan.geometry("600x300") 
jan.configure(background="white") 
jan.resizable(width=False,height=False) 

#COMANDO PARA DEIXAR A TELA TRANSPARENTE
jan.attributes("-alpha", 0.9) 


#CRIAR FRAME
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise") 
LeftFrame.pack(side = LEFT) 
RightFrame = Frame(jan,width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side = RIGHT)

#ADICIONAR CAMPOS DE USUARIO E SENHA
UsuarioLabel = Label(RightFrame, text="Usuario: ",font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White")
UsuarioLabel.place(x=5,y=100)
UsuarioEntry = ttk.Entry(RightFrame,width=30)
UsuarioEntry.place(x=120, y=115)
SenhaLabel = Label(RightFrame,text="Senha: ",font=("Century Gothic",20), bg="MIDNIGHTBLUE", fg="White")
SenhaLabel.place(x=5,y=150)
SenhaEntry = ttk.Entry(RightFrame, width = 30, show =".")
SenhaEntry.place(x=120, y=165)

#FUNÇÃO DE LOGIN 
def Login():
    usuario = UsuarioEntry.get()
    senha =SenhaEntry.get()

    # Conecta ao banco de dados
    db = DataBase()
    db.cursor.execute("""SELECT*FROM usuario WHERE usuario = %s AND senha = %s""",(usuario,senha))
    VerifyLogin = db.cursor.fetchone() 
    
    if VerifyLogin:
        messagebox.showinfo(title="INFO LOGIN", message="Acesso Confirmado. Bem Vindo!")

    else:
        messagebox.showerror(title="INFO LOGIN",message="Acesso Negado. Verifique se está cadastrado no Sistema!")

#CRIANDO BOTÕES
LoginButton = ttk.Button(RightFrame, text = "LOGIN", width=15, command=Login)
LoginButton.place(x=150, y=225)

#FUNÇÃO PARA REGISTRAR NOVO USUARIO
def Registrar():
    #REMOVER BOTÕES DE LOGIN
    LoginButton.place(x=5000)
    Registrar.Button.place(x=5000)

    #INSERINDO WIDGETS DE CADASTRO
    NomeLabel = Label(RightFrame, text="Nome", font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White")
    NomeLabel.place(x=5, y=5)
    NomeEntry = ttk.Entry(RightFrame, width=30)
    NomeEntry.place(x=120, y=20)

    EmailLabel = Label(RightFrame, text="Email", font=("Century Gothic",20),bg="MIDNIGHTBLUE",fg="White")
    EmailLabel.place(x=5, y=40)
    EmailEntry = ttk.Entry(RightFrame, width=30)
    EmailEntry.place(x=120, y=55)

#FUNÇÃO PARA REGISTRAR NO BANCO DE DADOS
    def RegistrarNoBanco(): 
        nome = NomeEntry.get() 
        email = EmailEntry.get() 
        usuario = UsuarioEntry.get() 
        senha = SenhaEntry.get() 

    #Verifica se todos os campos estão preenchidos
        if nome == "" or email == "" or usuario == "" or senha == "":
            messagebox.showerror(title="Erro de regidtro", message="PREENCHA TODOS OS CAMPOS") 
        else:
            db = DataBase() 
            db.RegistrarNoBanco(nome,email,usuario,senha) 
            messagebox.showinfo("Sucesso", "Usuario registrado com sucesso!") 

            #Limpar os campos após o registro
            NomeEntry.delete(0,END) 
            EmailEntry.delete(0,END) 
            UsuarioEntry.delete(0,END) 
            SenhaEntry.delete(0,END) 
Register = ttk.Button(RightFrame,text="REGISTRAR", width=15)
Register.place(x=150, y=225)

#FUNÇÃO PARA VOLTAR Á TELA DE LOGIN
def VoltarLogin():
        NomeLabel.place(x=5000) 
        EmailLabel.place(x=5000)
        Register.place(x=5000) 
        Voltar.place(x=5000)

    #TRAZENDO DE VOLTA OS WIDGETS
        LoginButton.place(x=150) 
        Registrar.Button.place(x=150) 

Voltar = ttk.Button(RightFrame, text="VOLTAR", width=15, command=VoltarLogin) 
Voltar.place(x=150, y=225) 

#INICIAR O LOOP PRINCIPAL
jan.mainloop()
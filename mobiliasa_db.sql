create database mobiliaria_db

create table produto(
	codproduto int not null auto_increment,
    produto text,
    descricao text,
    quantidade text,
    valordecompra text,
    valordevenda text,
    fornecedor text,
    primary key (codproduto)

);

create table fornecedor(
    idfornecedor int not null auto_increment,
    nome_fornecedor text,
    endereco text,
    telefone text,
    email text,
    produto text,
    primary key (idfornecedor)
);

create table funcionario(
    idfuncionario int not null auto_increment,
    nome text,
    cpf text,
    telefone,
    email text,
    cargo text,
    salario text,
    primary key (idfuncionario)
);

create table cadastro(
    idusuario int not null auto_increment,
    nome text,
    usuario text,
    email text,
    telefone text
    senha text,
    primary key (idusuario)
);


# pip install mysql-connector-python


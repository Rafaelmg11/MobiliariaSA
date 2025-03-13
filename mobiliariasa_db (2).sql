create database mobiliaria_db

create table produto(
	codproduto int not null auto_increment,
    produto text,
    descricao text,
    quantidade int,
    valordecompra float,
    valordevenda float,
    fornecedor text,
    primary key (codproduto)

);

create table fornecedor(
    idfornecedor int null auto_increment,
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
    cargo text,
    salario text,
    primary key (idfuncionario)
);



# pip install mysql-connector-python


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

# pip install mysql-connector-python


create database mobiliasa_db

create table produto(
	codproduto int not null auto_increment,
    produto text,
    descricao text,
    quantidade int,
    valordecompra float,
    valordevenda float,
    primary key (codproduto)

);

# pip install mysql-connector-python


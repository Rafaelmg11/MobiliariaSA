create database mobiliasa_db

create table produto(
	codproduto int not null auto_increment,
    produto text,
    descrição text,
    quantidade int,
    valordecompra float,
    valordevenda float,
    primary key (codproduto)

);


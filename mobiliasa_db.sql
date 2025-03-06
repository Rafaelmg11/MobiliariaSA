create database mobiliasa_db

create table produto(
	codproduto int not null auto_increment,
    produto text,
    descrição text,
    quantidade text,
    valordecompra text,
    valordevenda text,
    primary key (codproduto)

);


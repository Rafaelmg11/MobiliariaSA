create database mobiliariasa_db

create table fornecedor(
	idfornecedor int not null auto_increment,
    nome_impressa text,
    telefone text,
    endereco text,
    produto text,
    primary key (idfornecedor)

);

# pip install mysql-connector-python

create table cliente(
CPF integer primary key not null,
Nome varchar(30) not null,
Endereço varchar(30) not null,
Idade integer(2));

create table vendedor(
ID_FUncional integer primary key not null,
Nome_Vendedor varchar(30) not null);

create table veículo(
Renavan integer primary key not null,
Marca varchar(30) not null,
Modelo varchar(30) not null,
Preço decimal (7,2) not null,
Ano integer(4));

create table pedido(
Codigo integer primary key not null,
CPF_Cliente integer not null,
ID_Func_Vendedor integer not null,
Renavan_Veiculo integer not null,

foreign key (CPF_Cliente) references cliente(CPF),
foreign key (ID_Func_Vendedor) references vendedor(ID_FUncional),
foreign key (Renavan_Veiculo) references veículo(Renavan));

INSERT INTO cliente (CPF, Nome, Endereço, Idade) VALUES ("123456", "Leo", "Rua X", "18");
INSERT INTO cliente (CPF, Nome, Endereço, Idade) VALUES ("543214", "Ana", "Rua D", "22");
INSERT INTO cliente (CPF, Nome, Endereço, Idade) VALUES ("634892", "João", "Rua X", "51");

INSERT INTO vendedor(ID_Funcional, Nome_Vendedor) VALUES ("6431", "Pedro");
INSERT INTO vendedor(ID_Funcional, Nome_Vendedor) VALUES ("4456", "Carla");

INSERT INTO veículo(Renavan, Marca, Modelo, Preço, Ano) VALUES ("15474", "Renault", "Sandero", "35000,00", "2015");
INSERT INTO veículo(Renavan, Marca, Modelo, Preço, Ano) VALUES ("67853", "Ford", "Mustang", "90000,00", "1997");
INSERT INTO veículo(Renavan, Marca, Modelo, Preço, Ano) VALUES ("87293", "Honda", "Civic", "30000,00", "2008");
INSERT INTO veículo(Renavan, Marca, Modelo, Preço, Ano) VALUES ("43260", "Fiat", "Uno", "25000,00", "2011");
INSERT INTO veículo(Renavan, Marca, Modelo, Preço, Ano) VALUES ("52728", "Volkswagen", "beetle", "20000,00", "2001");
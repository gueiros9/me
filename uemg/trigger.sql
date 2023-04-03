create table produto (
idProduto int not null auto_increment,
Nome_produto varchar(45) null,
Preco_normal decimal (10,2) null,
Preco_desconto decimal (10,2) null,
primary key (idProduto));

create trigger tr_desconto before insert
on produto
for each row
set new.Preco_desconto = (new.Preco_normal * 0.90);

insert into produto (Nome_produto, Preco_normal)
values ('Monitor', 350.00), ('DVD', 1.00), ('Pendriver', 18.00;

select * from produto;

create table Setor(
	cod Int primary key not null,
	titulo varchar(50) not null
	);

create table Cargo(
	cod int primary key,
	titulo varchar(50),
	Setor int
	);

create table Funcionario(
	cod int primary key,
	nome varchar(50),
	Cargo int,
	salario decimal(9,2)
	);

create table Dependente(
	cod int primary key,
	nome varchar(50),
	Funcionario int
	);

alter table Cargo
ADD CONSTRAINT FK_Setor
FOREIGN KEY (Setor) REFERENCES Setor(cod)

alter table Funcionario
ADD CONSTRAINT FK_Cargo
FOREIGN KEY (Cargo) REFERENCES Cargo(cod)

alter table Dependente
ADD CONSTRAINT FK_Funcionario
FOREIGN KEY (Funcionario) REFERENCES Funcionario(cod)

INSERT INTO Setor (cod, titulo)
VALUES ('1','administrativo');
INSERT INTO Setor (cod, titulo)
VALUES ('2','financeiro');
INSERT INTO Setor (cod, titulo)
VALUES ('3','recursos humanos');
INSERT INTO Setor (cod, titulo)
VALUES ('4','comercial');
INSERT INTO Setor (cod, titulo)
VALUES ('5','operacional');

INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('1','Diretoria','1');
INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('7','Gerência','1');
INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('13','Coordenação','1');
INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('18','Analista','1');
INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('25','Auxiliar','1');
INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('26','Assistente','1');

INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('2','Diretoria','2');
INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('8','Gerência','2');
INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('14','Coordenação','2');
INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('19','Analista','2');
INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('27','Auxiliar','2');
INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('28','Assistente','2');

INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('3','Diretoria','3');
INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('9','Gerência','3');
INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('15','Coordenação','3');
INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('20','Analista','3');

INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('4','Diretoria','4');
INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('10','Gerência','4');
INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('16','Coordenação','4');
INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('21','Analista','4');
INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('29','Auxiliar','4');
INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('30','Assistente','4');

INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('5','Diretoria','5');
INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('11','Gerência','5');
INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('17','Coordenação','5');
INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('22','Analista','5');
INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('23','Auxiliar','5');
INSERT INTO Cargo (cod, titulo, Setor)
VALUES ('24','Assistente','5');

INSERT INTO Funcionario (cod, nome, Cargo, salario)
VALUES ('1','Ana','1','21411');
INSERT INTO Funcionario (cod, nome, Cargo, salario)
VALUES ('2','João','2','21411');
INSERT INTO Funcionario (cod, nome, Cargo, salario)
VALUES ('3','Carlos','3','21411');
INSERT INTO Funcionario (cod, nome, Cargo, salario)
VALUES ('4','Maria','4','21411');
INSERT INTO Funcionario (cod, nome, Cargo, salario)
VALUES ('5','Diego','5','21411');

INSERT INTO Funcionario (cod, nome, Cargo, salario)
VALUES ('6','Pedro','7','7283');
INSERT INTO Funcionario (cod, nome, Cargo, salario)
VALUES ('7','Claudio','7','7283');
INSERT INTO Funcionario (cod, nome, Cargo, salario)
VALUES ('8','Carla','8','7283');
INSERT INTO Funcionario (cod, nome, Cargo, salario)
VALUES ('9','Jorge','9','7283');
INSERT INTO Funcionario (cod, nome, Cargo, salario)
VALUES ('10','Paulo','10','7283');

INSERT INTO Funcionario (cod, nome, Cargo, salario)
VALUES ('11','Mateus','18','2783');
INSERT INTO Funcionario (cod, nome, Cargo, salario)
VALUES ('12','Lucas','19','2783');
INSERT INTO Funcionario (cod, nome, Cargo, salario)
VALUES ('13','Laura','20','2783');
INSERT INTO Funcionario (cod, nome, Cargo, salario)
VALUES ('14','Clara','21','2783');
INSERT INTO Funcionario (cod, nome, Cargo, salario)
VALUES ('15','Ada','22','2783');

INSERT INTO Funcionario (cod, nome, Cargo, salario)
VALUES ('16','Andre','25','1330');
INSERT INTO Funcionario (cod, nome, Cargo, salario)
VALUES ('17','Marcos','27','1110');
INSERT INTO Funcionario (cod, nome, Cargo, salario)
VALUES ('18','Bruna','29','1350');

INSERT INTO Dependente (cod, nome, Funcionario)
VALUES ('1','Paulo','1');
INSERT INTO Dependente (cod, nome, Funcionario)
VALUES ('2','Marcos','1');
INSERT INTO Dependente (cod, nome, Funcionario)
VALUES ('3','Pedro','6');
INSERT INTO Dependente (cod, nome, Funcionario)
VALUES ('4','Andre','7');
INSERT INTO Dependente (cod, nome, Funcionario)
VALUES ('5','Vitoria','10');
INSERT INTO Dependente (cod, nome, Funcionario)
VALUES ('6','Ana','12');
INSERT INTO Dependente (cod, nome, Funcionario)
VALUES ('7','Clarice','12');
INSERT INTO Dependente (cod, nome, Funcionario)
VALUES ('8','Paulo','15');
INSERT INTO Dependente (cod, nome, Funcionario)
VALUES ('9','Vinicius','18');
INSERT INTO Dependente (cod, nome, Funcionario)
VALUES ('10','Carlos','16');
INSERT INTO Dependente (cod, nome, Funcionario)
VALUES ('11','Luis','16');
INSERT INTO Dependente (cod, nome, Funcionario)
VALUES ('12','Emanuel','3');
INSERT INTO Dependente (cod, nome, Funcionario)
VALUES ('13','Eduarda','3');

select * from Funcionario
select * from Setor
select * from Cargo
select * from Dependente

select cod,nome
from Funcionario
update Funcionario
set nome = 'Jorge' where cod = 2;

select nome 
from Funcionario where Cargo = 1;

select titulo from Setor
order by titulo ASC;

select SUM(salario) As SomaTotaldosSalarios from Funcionario

select MAX(salario) As MaiorSalario from Funcionario

select nome 
from Funcionario where Cargo = 3;

select Funcionario.nome, Cargo.titulo, Dependente.nome
from Funcionario Join Cargo
on Funcionario.Cargo = Cargo.cod
Join Dependente
on Funcionario.cod = Dependente.Funcionario;

UPDATE Dependente 
   SET nome = NULL 
 WHERE Funcionario = 3
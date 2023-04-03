RESPOSTAS

1 - A
2 - B

3 -

create table Professor (
	numero_prof int primary key, 
	profnome varchar(50), 
	profrua varchar(100), 
	profcidade varchar(50)
);

create table Aluno (
	numero_aluno int primary key, 
	alunome varchar(50), 
	alurua varchar(100), 
	alucidade varchar(50)
);

create table Matricula (
	numero_aluno int,	
	codigo_disc int,
	ano int
);

create table Disciplina (
	codigo_disc int primary key,
	nome_disciplina varchar(50),
	nome_curso varchar(50), 
	quant_aulas int
);

create table ProfDisc (
	codigo_disc int,
	numero_prof int, 
	ano int
);


alter table Matricula
ADD CONSTRAINT FK_aluno
FOREIGN KEY (numero_aluno) REFERENCES Aluno(numero_aluno)

alter table ProfDisc
ADD CONSTRAINT FK_disc
FOREIGN KEY (codigo_disc) REFERENCES Disciplina(codigo_disc)

alter table ProfDisc
ADD CONSTRAINT FK_prof
FOREIGN KEY (numero_prof) REFERENCES Professor(numero_prof)

4 -

INSERT INTO Aluno VALUES (1, ' Tiago Mateus Junior', '210', 'Palmas');

INSERT INTO Aluno VALUES (2, 'Luciana Gomes', '202', 'Palmas');

INSERT INTO Aluno VALUES (3, 'João Mateus', '2300', 'Gurupi');

INSERT INTO Aluno VALUES (4, 'José Silva', '1024', 'Paraíso');

INSERT INTO Aluno VALUES (5, 'Juraci', '106', 'Miranorte');

INSERT INTO Aluno VALUES (6, 'Paulo', '101', 'Goianorte');

INSERT INTO Aluno VALUES (7, 'Adriana Calcanhoto', 'rua Alvorada', 'Paraíso');

INSERT INTO Aluno VALUES (8, 'Rosane', 'rua das flores', 'Guaraí');

INSERT INTO Aluno VALUES (9, 'Mara', 'rua das águas', 'Porto Nacional');

INSERT INTO Aluno VALUES (10, 'Julia', 'rua de madeira', 'Paraíso');

INSERT INTO Aluno VALUES (11, 'Julia', 'rua de madeira', 'Palmas');

INSERT INTO professor VALUES (1, 'João José', '103', 'Palmas');

INSERT INTO professor VALUES (2, 'Maria José', '201', 'Palmas');

INSERT INTO professor VALUES (3, 'Bruno', '305', 'Paraiso');

INSERT INTO professor VALUES (4, 'José Ricardo', '1106', 'Porto Nacional');

INSERT INTO professor VALUES (5, 'Manuela', '120', 'Araguaína');

INSERT INTO professor VALUES (6, 'Bruno', '1003', 'Porto Nacional');

INSERT INTO professor VALUES (7, 'Luciana', ' 100', 'Miracema');

INSERT INTO professor VALUES (8, 'Paulo', ' 150', 'Palmas');

INSERT INTO professor VALUES (9, 'Lual', '1006', 'Paraíso');

INSERT INTO professor VALUES (10, 'Antonio Marcos', '170', 'Araguaína');

INSERT INTO disciplina (codigo_disc, nome_disciplina, nome_curso, quant_aulas) VALUES (1, ' Química', 'Ensino Médio', 4);

INSERT INTO disciplina (codigo_disc, nome_disciplina, nome_curso, quant_aulas) VALUES (2, ' Biologia', 'Ensino Médio', 4);

INSERT INTO disciplina (codigo_disc, nome_disciplina, nome_curso, quant_aulas) VALUES (3, 'História', 'Ensino Médio', 2);

INSERT INTO disciplina (codigo_disc, nome_disciplina, nome_curso, quant_aulas) VALUES (4, ' Religião', 'Ensino Médio', 2);

INSERT INTO disciplina (codigo_disc, nome_disciplina, nome_curso, quant_aulas) VALUES (5, ' Português', 'Ensino Pós Médio', 4);

INSERT INTO disciplina (codigo_disc, nome_disciplina, nome_curso, quant_aulas) VALUES (6, 'Física', 'Ensino Pós Médio', 6);

INSERT INTO disciplina (codigo_disc, nome_disciplina, nome_curso, quant_aulas) VALUES (7, 'Matemática', 'Ensino Pós Médio', 4);

INSERT INTO disciplina (codigo_disc, nome_disciplina, nome_curso, quant_aulas) VALUES (8, 'Geografia ', 'Ensino Pós Médio', 2);

INSERT INTO disciplina (codigo_disc, nome_disciplina, nome_curso, quant_aulas) VALUES (9, 'Informática Aplicada', 'CST Sistemas para Internet', 4);

INSERT INTO disciplina (codigo_disc, nome_disciplina, nome_curso, quant_aulas) VALUES (10, 'Banco de dados', 'CST Sistemas para Internet', 4);

INSERT INTO disciplina (codigo_disc, nome_disciplina, nome_curso, quant_aulas) VALUES (11, 'Programação de Banco de dados', 'Computação', 4);

INSERT INTO matricula (numero_aluno, codigo_disc, ano) VALUES (1, 10, '2018');

INSERT INTO matricula (numero_aluno, codigo_disc, ano) VALUES (1, 4, '2018');

INSERT INTO matricula (numero_aluno, codigo_disc, ano) VALUES (1, 6, '2018');

INSERT INTO matricula (numero_aluno, codigo_disc, ano) VALUES (5, 3, '2018');

INSERT INTO matricula (numero_aluno, codigo_disc, ano) VALUES (6, 1, '2018');

INSERT INTO matricula (numero_aluno, codigo_disc, ano) VALUES (2, 6, '2018');

INSERT INTO matricula (numero_aluno, codigo_disc, ano) VALUES (7, 9, '2018');

INSERT INTO matricula (numero_aluno, codigo_disc, ano) VALUES (8, 10, '2018');

INSERT INTO matricula (numero_aluno, codigo_disc, ano) VALUES (9, 1, '2018');

INSERT INTO matricula (numero_aluno, codigo_disc, ano) VALUES (2, 2, '2018');

INSERT INTO matricula (numero_aluno, codigo_disc, ano) VALUES (11, 11, '2018');

INSERT INTO profdisc (codigo_disc, numero_prof, ano) VALUES (1, 10, '2018');

INSERT INTO profdisc (codigo_disc, numero_prof, ano) VALUES (2, 5, '2018');

INSERT INTO profdisc (codigo_disc, numero_prof, ano) VALUES (3, 7, '2018');

INSERT INTO profdisc (codigo_disc, numero_prof, ano) VALUES (4, 4, '2018');

INSERT INTO profdisc (codigo_disc, numero_prof, ano) VALUES (5, 9, '2018');

INSERT INTO profdisc (codigo_disc, numero_prof, ano) VALUES (6, 2, '2018');

INSERT INTO profdisc (codigo_disc, numero_prof, ano) VALUES (7, 3, '2018');

INSERT INTO profdisc (codigo_disc, numero_prof, ano) VALUES (8, 9, '2018');

INSERT INTO profdisc (codigo_disc, numero_prof, ano) VALUES (9, 6, '2018');

INSERT INTO profdisc (codigo_disc, numero_prof, ano) VALUES (10, 3, '2018');

INSERT INTO profdisc (codigo_disc, numero_prof, ano) VALUES (11, 5, '2018');


5 -

select Professor.profnome
from Professor 
JOIN Disciplina
on Professor.numero_prof = Disciplina.Codigo_disc
where nome_curso = 'CST Sistemas para Internet'

select Aluno.alunome
from Aluno
JOIN Matricula
on Aluno.numero_aluno = Matricula.numero_aluno
where ano = '2018'

select Professor.profnome, avg(Disciplina.quant_aulas)
from Professor 
JOIN Disciplina
on Professor.numero_prof = Disciplina.Codigo_disc
group by profnome

select profnome from Professor
where profcidade = 'Palmas'

select Aluno.alunome, Disciplina.nome_curso, Disciplina.nome_disciplina, Disciplina.codigo_disc
from Matricula
INNER JOIN
Aluno on Aluno.numero_aluno = Matricula.numero_aluno
INNER JOIN
Disciplina on Matricula.codigo_disc = Disciplina.codigo_disc


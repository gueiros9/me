SELECT * FROM trabalho.cidade;
insert into cidade (cod_cid, nome_cid, sigla_uf) values ("145", "Recife", "PE");

SELECT * FROM trabalho.cliente;
insert into cliente (cod_cli, nome_cli, nm_bairro, nr_cep, cod_cid) values ("543", "João", "Jd Brasilia", "38400000", "623");
insert into cliente (cod_cli, nome_cli, nm_bairro, nr_cep, cod_cid) values ("189", "Mateus", "Martins", "38445000", "623");
insert into cliente (cod_cli, nome_cli, nm_bairro, nr_cep, cod_cid) values ("214", "Ana", "Universitario", "38302172", "885");
insert into cliente (cod_cli, nome_cli, nm_bairro, nr_cep, cod_cid) values ("786", "Carla", "Centro", "01034030", "791");
insert into cliente (cod_cli, nome_cli, nm_bairro, nr_cep, cod_cid) values ("963", "Otavio", "Boa Viagem", "51111000", "145");
insert into cliente (cod_cli, nome_cli, nm_bairro, nr_cep, cod_cid) values ("342", "Maria", "Realengo", "21735352", "427");
insert into cliente (cod_cli, nome_cli, nm_bairro, nr_cep, cod_cid) values ("218", "Jorge", "Leblon", "22441040", "427");

select nome_cli, cod_cid from trabalho.cliente;

SELECT * FROM trabalho.classe;
insert into classe (cod_cla, nome_cla) values ("153","A");
insert into classe (cod_cla, nome_cla) values ("436","B");
insert into classe (cod_cla, nome_cla) values ("722","C");

SELECT * FROM trabalho.venda;
insert into venda (cod_ven, data_ven, valor_ven, cod_cli) values ("5475","10022021","324,12","189");
insert into venda (cod_ven, data_ven, valor_ven, cod_cli) values ("4521","10022021","644,87","189");
insert into venda (cod_ven, data_ven, valor_ven, cod_cli) values ("1556","05022021","1277,34","214");
insert into venda (cod_ven, data_ven, valor_ven, cod_cli) values ("5642","01022021","235,67","218");
insert into venda (cod_ven, data_ven, valor_ven, cod_cli) values ("8765","07022021","86,34","342");
insert into venda (cod_ven, data_ven, valor_ven, cod_cli) values ("9877","04022021","732,22","543");

select valor_ven, cod_cli from venda where valor_ven > 500;

SELECT * FROM trabalho.produto;
insert into produto (cod_pro, valor_pro, qtde_pro, cod_cla) values ("4","1277","130","153");
insert into produto (cod_pro, valor_pro, qtde_pro, cod_cla) values ("5","644","589","436");
insert into produto (cod_pro, valor_pro, qtde_pro, cod_cla) values ("1","324","5000","436");
insert into produto (cod_pro, valor_pro, qtde_pro, cod_cla) values ("6","235","1300","153");
insert into produto (cod_pro, valor_pro, qtde_pro, cod_cla) values ("3","86","3500","722");
insert into produto (cod_pro, valor_pro, qtde_pro, cod_cla) values ("2","732","480","722");

select valor_pro, qtde_pro from produto where qtde_pro < 1000;

SELECT * FROM trabalho.produto_vendido;
insert into produto_vendido (cod_ven, cod_pro, qt_ven) values ("1556","4","22");
insert into produto_vendido (cod_ven, cod_pro, qt_ven) values ("4521","5","100");
insert into produto_vendido (cod_ven, cod_pro, qt_ven) values ("5475","1","1000");
insert into produto_vendido (cod_ven, cod_pro, qt_ven) values ("5642","6","670");
insert into produto_vendido (cod_ven, cod_pro, qt_ven) values ("8765","3","500");
insert into produto_vendido (cod_ven, cod_pro, qt_ven) values ("9877","2","90");

select cod_pro, qt_ven from produto_vendido where qt_ven < 500;

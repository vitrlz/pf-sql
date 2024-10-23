create database petshop;
use petshop;
create table petshop(
	id INT PRIMARY KEY IDENTITY,
	tipo_pet VARCHAR(30),
	nome_pet VARCHAR(30),
	idade INT
);

select * from petshop;
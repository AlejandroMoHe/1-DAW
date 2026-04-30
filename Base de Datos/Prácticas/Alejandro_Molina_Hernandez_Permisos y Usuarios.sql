-- Práctica de permisos Alejando Molina
drop database Clientes;
create database Clientes;
use Clientes;

create table personas(idpersonas int primary key, nombre varchar(30), domicilio varchar(50));
create table ciudades (id_ciudad int primary key, nombre varchar(30), capital varchar(50));
insert into personas values (1, 'Juan', 'Veléz');
insert into personas values (2, 'Fran', 'Motril');
insert into personas values (3, 'Marta', 'Salobreña');
select * from personas;

insert into ciudades values (1, 'Motril', 'Granada');
insert into ciudades values (2, 'Salobreña', 'Granada');
insert into ciudades values (3, 'Almuñecar', 'Granada');
insert into ciudades values (4, 'Torrenueva', 'Granada');

select * from ciudades;
delete from ciudades where id=4;

grant create on Clientes.* to 'user1'@'%';
grant insert on Clientes.* to 'user1'@'%';
grant select on Clientes.personas to 'user1'@'%';
grant insert on Clientes.ciudades to 'user2'@'%';
grant delete on Clientes.ciudades to 'user2'@'%';
grant all on Clientes.ciudades to 'user3'@'%';

flush privileges;



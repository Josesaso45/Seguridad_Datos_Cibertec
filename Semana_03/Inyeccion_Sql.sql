/*curso de seguridad de aplicaciones*/

create database ciber_2026

use ciber_2026

create table usuario(
usuario varchar (50),
clave varchar(50)
)

insert into usuario values ('admin','1234')

select * from usuario
where usuario= 'admin' and clave='1234'

select * from usuario
where usuario = 'admin' and clave='' or '0'='0'

select * from usuario
where usuario ='admin'

go
exec sp_executesql
N'select * from usuario where usuario =	@u and clave=@c',
N'@u varchar(50),@c varchar(50)',
@u='admin',
@c='1234'
CREATE DATABASE CIBER
GO
USE CIBER
GO
CREATE TABLE USUARIO(
usuario VARCHAR(50),
clave VARCHAR(50)
)
go
INSERT INTO USUARIO VALUES('admin','1234')
go
select * from USUARIO
where usuario='admin' and clave='1234'
go
/*
go
admin
'or' '1'='1'
*/
select * from USUARIO
where usuario='admin' and clave='' or '0'='0'

go

select * from USUARIO where usuario='admin'

admin' AND 1=1 --
--LA PAGINA FUNCIONA BIEN
admin' and 1=2--

admin' if (1=1) waitfor delay '00:00:05'--

go
EXEC sp_executesql
N'select * from USUARIO where usuario =@u and clave=@c',
N'@u varchar(50),@c varchar(50)',
@u='admin',
@c='1234'


-- Relacion 9 de Alejandro Molina Hernandez
-- Consulta 1
select apellido, oficio, dept_no from emple;

-- Consulta 2
select * from depart;

-- Consulta 3
select * from emple;

-- Consulta 4
select * from emple
order by apellido;

-- Consulta 5
select * from emple
order by dept_no desc;

-- Consulta 6
select * from emple
order by dept_no desc, apellido asc;


-- Consulta 8
select * from emple
where salario > 2000000;

-- Consulta 9
select * from emple
where oficio like "Analista";

-- Consulta 10
select apellido, oficio from emple
where dept_no = 20;

-- Consulta 11
select * from emple
order by apellido;

-- Consulta 12
select * from emple
where oficio like "Vendedor" order by apellido;

-- Consulta 13
select * from emple
where dept_no = 10 and oficio like "Analista" 
order by apellido;

-- Consulta 14
select * from emple
where salario > 200000 or dept_no = 20;

-- Consulta 15
select * from emple
order by oficio asc;

-- Consulta 16
select * from emple
where apellido like "A%";

-- Consulta 17
select * from emple
where apellido like "%Z";

-- Consulta 18
select * from emple
where apellido like "A%" and oficio like "%E%";

-- Consulta 19
select * from emple
where salario between 100000 and 200000;

-- Consulta 20
select * from emple
where oficio = "Vendedor" and comision > 100000;

-- Consulta 21
select * from emple 
order by dept_no, apellido;

-- Consulta 22
select emp_no, apellido from emple
where apellido like "%z" and salario > 300000;

-- Consulta 23
select * from depart
where localidad like 'B%';

-- Consulta 24
select * from emple
where oficio = 'empleado' and salario > 100000 and dept_no = 10;

-- Consulta 25
select apellido from emple
where comision is null;

-- Consulta 26
select apellido from emple
where comision is null and apellido like 'J%';

-- Consulta 27
select apellido from emple
where oficio in ('vendedor', 'analista', 'empleado');

-- Consulta 28
select apellido from emple
where oficio not in('analista', 'empleado') and salario > 200000;

-- Consulta 29
select * from emple
where salario between 2000000 and 3000000;

-- Consulta 30
select apellido, salario, dept_no from emple
where salario > 200000 and dept_no in (10, 30);

-- Consulta 31
select apellido, emp_no from emple
where salario not between 100000 and 200000;

-- Consulta 32
select lower(apellido) from emple;

-- Consulta 33
select concat(apellido, ' - ', oficio) from emple;

-- Consulta 34
select apellido, length(apellido) as longitud from emple
order by longitud desc;

-- Consulta 35
select year(fecha_alt) from emple;

-- Consulta 36
select * from emple
where year(fecha_alt) = 1992;

-- Consulta 37
select * from emple
where monthname(fecha_alt) = 'Febrero';

-- Consulta 38
select apellido, greatest(salario, ifnull(comision, 0)) as mayor_importante from emple;

-- Consulta 39
select * from emple
where apellido like 'A%' and year(fecha_alt) = 1990;

-- Consulta 40
select * from emple
where dept_no = 10 and comision is null;

-- crear la tabla

create table person
(
    name str,
    age  int,
    id   int
);


-- insertar un elemento en la tabla
INSERT INTO person (name, age, id) VALUES ('Maria', 18, 2)


-- selecionar un elemento en la tabla
SELECT * FROM person

SELECT * FROM person WHERE id = 2

-- actualizar un registro
UPDATE person SET age = 17 WHERE name = 'Maria' AND age = 18 AND id = 2

-- eliminar un elemento
DELETE FROM person WHERE id = 2
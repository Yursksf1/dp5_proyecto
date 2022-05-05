-- crear la tabla

create table game
(
    id        int,
    localtion str,
    date      str
);

create table person
(
    name str,
    age  int,
    id   int
);

create table game_player
(
    id        int,
    puntos    int,
    faltas    int,
    id_person int
        constraint game_player_person_id_fk
            references person (id),
    id_game   int
        constraint game_player_game_id_fk
            references game (id)
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
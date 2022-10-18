USE poke_tracker;

CREATE TABLE pokemon(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256),
    height INT,
    weight INT
);

CREATE TABLE trainer(
    name VARCHAR(256) PRIMARY KEY,
    town VARCHAR(256)
);

CREATE TABLE type(
    name VARCHAR(256) PRIMARY KEY
);

CREATE TABLE owned_by(
    trainer_name VARCHAR(256),
    pokemon_id INT,
    FOREIGN KEY(trainer_name) REFERENCES trainer(name),
    FOREIGN KEY(pokemon_id) REFERENCES pokemon(id),
    PRIMARY KEY(trainer_name,pokemon_id)
);

CREATE TABLE type_of(
    type_name VARCHAR(256),
    pokemon_id INT,
    FOREIGN KEY(type_name) REFERENCES type(name),
    FOREIGN KEY(pokemon_id) REFERENCES pokemon(id),
    PRIMARY KEY(type_name,pokemon_id)
);
USE poke_tracker;

CREATE TABLE pokemon(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256),
    type VARCHAR(256),
    height INT,
    weight INT
);

CREATE TABLE trainer(
    name VARCHAR(256),
    town VARCHAR(256)
    PRIMARY KEY(name, town)
);

CREATE TABLE owned_by(
    trainer_name VARCHAR(256),
    trainer_town VARCHAR(256),
    pokemon_name VARCHAR(256),
    FOREIGN KEY(trainer_name) REFERENCES trainer(name),
    FOREIGN KEY(trainer_town) REFERENCES trainer(town),
    FOREIGN KEY(pokemon_name) REFERENCES pokemon(name),
    PRIMARY KEY(trainer_name, trainer_town,pokemon_name)

);
from fastapi.testclient import TestClient
from server import app
import pytest

from unittest.mock import patch

client = TestClient(app)

pokemon_names = ["bulbasaur", "squirtle", "weedle"]
pokemons_and_types = [("bug", "pinsir"), ("grass", "bulbasaur"), ("poison", "bulbasaur"), ("normal", "eevee")]
pokemons_and_trainers = [("Diantha", "pinsir"), ("Ash", "bulbasaur"), ("Archie", "bulbasaur"), ("Gary", "eevee")]


@pytest.mark.parametrize("name", pokemon_names)
def test_pokemon_name(name):
    response = client.get(f"/pokemons/{name}")
    pokemon = response.json()
    assert response.status_code == 200
    assert name == pokemon["name"]
    
    
@pytest.mark.parametrize("type", "pokemon", pokemons_and_types)    
def test_pokemon_type(type, pokemon):
    response = client.get(f"/pokemons?type={type}")
    type_pokemons = response.json()
    assert response.status_code == 200
    assert pokemon in type_pokemons  # ["name"] ?
    
    
@pytest.mark.parametrize("trainer", "pokemon", pokemons_and_types)    
def test_pokemon_trainer(trainer, pokemon):
    response = client.get(f"/pokemons?trainer={trainer}")
    trainer_pokemons = response.json()
    assert response.status_code == 200
    assert pokemon in trainer_pokemons  # ["name"] ?

    
def test_pokemon_type_and_trainer(type, trainer, pokemnon):
    pass
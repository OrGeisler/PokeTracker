from fastapi.testclient import TestClient
from server import app
import pytest
   
from unittest.mock import patch

client = TestClient(app)

pokemon_names = ["bulbasaur", "squirtle", "weedle"]
pokemons_and_types = [("bug", "pinsir"), ("grass", "bulbasaur"), ("poison", "bulbasaur"), ("normal", "eevee")]
pokemons_and_trainers = [("Diantha", "pinsir"), ("Ash", "bulbasaur"), ("Archie", "bulbasaur"), ("Gary", "eevee")]
pokemons_and_types_and_trainers = [("bug", "Diantha", "pinsir"), ("grass", "Ash", "bulbasaur")]


@pytest.mark.parametrize("name", pokemon_names)
def test_get_pokemon_by_name(name):
    response = client.get(f"/pokemons/{name}")
    pokemon = response.json()
    assert response.status_code == 200
    assert name == pokemon["name"]
    
    
def test_get_pokemon_bad_name():
    response = client.get(f"/pokemons/not_a_pokemon")
    response_message = response.json()
    assert response.status_code == 404
    assert "detail" in response_message
    
    
@pytest.mark.parametrize("type, pokemon", pokemons_and_types)    
def test_get_pokemon_by_type(type, pokemon):
    response = client.get(f"/pokemons?type={type}")
    type_pokemons = response.json()
    pokemon_names = [poke["name"] for poke in type_pokemons]
    assert response.status_code == 200
    assert pokemon in pokemon_names

    
@pytest.mark.parametrize("trainer, pokemon", pokemons_and_trainers)    
def test_get_pokemon_by_trainer(trainer, pokemon):
    response = client.get(f"/pokemons?trainer={trainer}")
    trainer_pokemons = response.json()
    pokemon_names = [poke["name"] for poke in trainer_pokemons]
    assert response.status_code == 200
    assert pokemon in pokemon_names 


@pytest.mark.parametrize("type, trainer, pokemon", pokemons_and_types_and_trainers)    
def test_pokemon_by_type_and_trainer(type, trainer, pokemon):
    response = client.get(f"/pokemons?type={type}&trainer={trainer}")
    trainer_and_type_pokemons = response.json()
    pokemon_names = [poke["name"] for poke in trainer_and_type_pokemons]
    assert response.status_code == 200
    assert pokemon in pokemon_names 
    
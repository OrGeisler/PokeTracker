from fastapi import APIRouter
from . import pokemon_utils

# sys.path.append('./api_utils')
from ..api_utils import querys 
from ..api_utils.db_proxy import db_proxy 

db = db_proxy()
pokemonsRoute = APIRouter()

@pokemonsRoute.get('/pokemons/{pokemon_name}')
def pokemonByName(pokemon_name):
    pokemon_types = pokemon_utils.get_pokemon_types(pokemon_name)
    type_list = pokemon_utils.extract_types(pokemon_types)
    pokemon_id = db.execute_select_one_query(querys.sql_get_pokemon_id,pokemon_name)['id']
    for type in type_list:
        db.execute_insert_query(querys.sql_insert_type,type)
        db.execute_insert_query(querys.sql_insert_type_of,(type,pokemon_id))

    pokemon = db.execute_select_one_query(querys.sql_get_pokemon_by_name,pokemon_name)
    pokemon_types_from_db = db.execute_select_all_query(querys.sql_get_pokemon_type_by_id,pokemon_id)
    pokemon_with_types = pokemon_utils.add_types_to_pokemon(pokemon,pokemon_types_from_db)
    return pokemon_with_types


@pokemonsRoute.get('/pokemons')
def pokemonByField(type = None,trainer =None):
    if type and trainer:
        pokemons_list = db.execute_select_all_query(querys.sql_get_pokemon_by_trainer_and_type,(trainer,type))
        pokemon_list_with_types = pokemon_utils.add_types_to_pokemon_list(pokemons_list)
        return pokemon_list_with_types

    elif (not type) and (trainer):
        pokemons_list = db.execute_select_all_query(querys.sql_get_pokemon_by_trainer,trainer)
        pokemon_list_with_types = pokemon_utils.add_types_to_pokemon_list(pokemons_list)
        return pokemon_list_with_types

    elif type and (not trainer):
        pokemons_list = db.execute_select_all_query(querys.sql_get_pokemon_by_type,type)
        pokemon_list_with_types = pokemon_utils.add_types_to_pokemon_list(pokemons_list)
        return pokemon_list_with_types

    else:
        pokemons_list = db.execute_select_all_query(querys.sql_get_all_pokemons)
        pokemon_list_with_types = pokemon_utils.add_types_to_pokemon_list(pokemons_list)
        return pokemon_list_with_types


@pokemonsRoute.post('/pokemons/{pokemon_name}/trainers/{trainer_name}')
def addPokemonToTrainer(pokemon_name,trainer_name):
    pokemon_id = db.execute_select_one_query(querys.sql_get_pokemon_id,pokemon_name)['id']
    db.execute_insert_query(querys.sql_insert_pokemon_to_trainer,(trainer_name,pokemon_id))

@pokemonsRoute.delete('/pokemons/{pokemon_name}/trainers/{trainer_name}')
def addPokemonToTrainer(pokemon_name,trainer_name):
    pokemon_id = db.execute_select_one_query(querys.sql_get_pokemon_id,pokemon_name)['id']
    db.execute_insert_query(querys.sql_delete_pokemon_of_trainer,(trainer_name,pokemon_id))


from fastapi import APIRouter , status , Response
from . import pokemon_utils
from fastapi.responses import JSONResponse

from ..api_utils import querys 
from ..api_utils.db_proxy import db_proxy 

db = db_proxy()
pokemonsRoute = APIRouter()

@pokemonsRoute.get('/pokemons/{pokemon_name}',response_class= JSONResponse , status_code= status.HTTP_200_OK)
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
    pokemon_with_types_and_trainers = pokemon_utils.add_trainers_to_pokemon(pokemon_with_types)
    return pokemon_with_types_and_trainers


@pokemonsRoute.get('/pokemons',response_class= JSONResponse , status_code= status.HTTP_200_OK)
def pokemonByField(type = None,trainer =None):
    if type and trainer:
        pokemons_list = db.execute_select_all_query(querys.sql_get_pokemon_by_trainer_and_type,(trainer,type))
        pokemon_list_with_types = pokemon_utils.add_types_to_pokemon_list(pokemons_list)
        pokemon_with_types_and_trainers = pokemon_utils.add_trainers_to_pokemon_list(pokemon_list_with_types)
        return pokemon_with_types_and_trainers

    elif (not type) and (trainer):
        pokemons_list = db.execute_select_all_query(querys.sql_get_pokemon_by_trainer,trainer)
        pokemon_list_with_types = pokemon_utils.add_types_to_pokemon_list(pokemons_list)
        pokemon_with_types_and_trainers = pokemon_utils.add_trainers_to_pokemon_list(pokemon_list_with_types)
        return pokemon_with_types_and_trainers

    elif type and (not trainer):
        pokemons_list = db.execute_select_all_query(querys.sql_get_pokemon_by_type,type)
        pokemon_list_with_types = pokemon_utils.add_types_to_pokemon_list(pokemons_list)
        pokemon_with_types_and_trainers = pokemon_utils.add_trainers_to_pokemon_list(pokemon_list_with_types)
        return pokemon_with_types_and_trainers

    else:
        pokemons_list = db.execute_select_all_query(querys.sql_get_all_pokemons)
        pokemon_list_with_types = pokemon_utils.add_types_to_pokemon_list(pokemons_list)
        pokemon_with_types_and_trainers = pokemon_utils.add_trainers_to_pokemon_list(pokemon_list_with_types)
        return pokemon_with_types_and_trainers


@pokemonsRoute.post('/pokemons/{pokemon_name}/trainers/{trainer_name}', response_class= JSONResponse , status_code= status.HTTP_201_CREATED)
def addPokemonToTrainer(pokemon_name,trainer_name):
    pokemon_id = db.execute_select_one_query(querys.sql_get_pokemon_id,pokemon_name)['id']
    db.execute_insert_query(querys.sql_insert_pokemon_to_trainer,(trainer_name,pokemon_id))
    return {
            "success": True,
            "payload": {
                        f'Added {pokemon_name} to {trainer_name}'
                    }
            }

@pokemonsRoute.delete('/pokemons/{pokemon_name}/trainers/{trainer_name}', response_class= JSONResponse , status_code= status.HTTP_204_NO_CONTENT)
def deletePokemonFromTrainer(pokemon_name,trainer_name):
    pokemon_id = db.execute_select_one_query(querys.sql_get_pokemon_id,pokemon_name)['id']
    db.execute_delete_query(querys.sql_delete_pokemon_of_trainer,(trainer_name,pokemon_id))
    return {
            "success": True,
            "payload": {
                        f'Deleted {pokemon_name} from {trainer_name}'
                    }
            }

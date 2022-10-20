from typing import List
from fastapi import APIRouter
import requests
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

from fastapi import HTTPException
import requests
from ..api_utils import querys 
from ..api_utils.db_proxy import db_proxy 

db = db_proxy()



def get_pokemon_types(pokemon_name):
    try:
        pokemon_types= requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}').json()['types']
        return pokemon_types
    except:
        raise HTTPException(status_code=404, detail="Cant find the pokemon in the external API")

def extract_types(types):
    type_list = []
    for i in types:
        type_list.append(i['type']['name'])
    return type_list

def add_types_to_pokemon(pokemon,pokemon_types_from_db):
    for type in pokemon_types_from_db:
        type_name = type['type_name']
        if 'type' in pokemon:
            pokemon['type'].append(f'{type_name}')
        else:
            pokemon['type'] = [f'{type_name}']
    return pokemon

def add_types_to_pokemon_list(pokemons_list):
    pokemon_list_with_types = []
    for pokemon in pokemons_list:
        pokemon_types_from_db = db.execute_select_all_query(querys.sql_get_pokemon_type_by_id,pokemon['id'])
        pokemon_with_types = add_types_to_pokemon(pokemon,pokemon_types_from_db)
        pokemon_list_with_types.append(pokemon_with_types)
    return pokemon_list_with_types

from fastapi import HTTPException
import requests




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


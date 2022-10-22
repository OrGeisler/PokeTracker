from fastapi import HTTPException
import requests
from ..api_utils import querys 
from ..api_utils.db_proxy import db_proxy 

db = db_proxy()



def get_pokemon_species_url(pokemon_name):
    try:
        species_url= requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}').json()['species']['url']
        return species_url
    except:
        raise HTTPException(status_code=404, detail="Cant find the pokemon in the external API")

def get_pokemon_evolution_chain_url(url):
    try:
        evolution_chain_url= requests.get(url).json()['evolution_chain']['url']
        return evolution_chain_url
    except:
        raise HTTPException(status_code=404, detail="Cant find the evolution_chain url in the external API")

def get_pokemon_evolution_chain(url):
    try:
        evolution_chain= requests.get(url).json()['chain']
        return evolution_chain
    except:
        raise HTTPException(status_code=404, detail="Cant find the evolution_chain url in the external API")

def get_evolution(pokemon_name,evolution_chain):
    try:
        current_pokemon = evolution_chain["species"]["name"]
        while (current_pokemon != pokemon_name and len(evolution_chain["evolves_to"]) != 0):
            evolution_chain = evolution_chain["evolves_to"][0]
            current_pokemon = evolution_chain["species"]["name"]

        if len(evolution_chain["evolves_to"]) == 0:
            return pokemon_name
        else:
            return evolution_chain["evolves_to"][0]["species"]["name"]
    except Exception as e:
        return e

def envolve(pokemon_name):
    species_url = get_pokemon_species_url(pokemon_name)
    evolution_chain_url = get_pokemon_evolution_chain_url(species_url)
    evolution_chain = get_pokemon_evolution_chain(evolution_chain_url)
    envolved_pokemon = get_evolution(pokemon_name,evolution_chain)
    return envolved_pokemon

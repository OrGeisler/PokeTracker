from fastapi import APIRouter
from . import trainers_utils

from ..api_utils import querys 
from ..api_utils.db_proxy import db_proxy 

db = db_proxy()
trainersRoute = APIRouter()

@trainersRoute.get('/trainers/{pokemon_name}')
def trainersOfPokemon(pokemon_name):
    pokemon_id = db.execute_select_one_query(querys.sql_get_pokemon_id,pokemon_name)['id']
    trainers = db.execute_select_all_query(querys.sql_get_trainers_of_pokemon,pokemon_id)
    return trainers
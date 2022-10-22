from asyncio.windows_events import NULL
from fastapi import APIRouter , status , Response
from . import envolve_utils
import requests
from fastapi.responses import JSONResponse

from ..api_utils import querys 
from ..api_utils.db_proxy import db_proxy 

db = db_proxy()
envolveRoute = APIRouter()


@envolveRoute.patch('/envolve',response_class= JSONResponse , status_code= status.HTTP_200_OK)
def envolvePokemon(pokemon_name = NULL , trainer_name = NULL):
    envolved_pokemon = envolve_utils.envolve(pokemon_name)
    pokemon_id = db.execute_select_one_query(querys.sql_get_pokemon_id,pokemon_name)['id']
    envolved_pokemon_id = db.execute_select_one_query(querys.sql_get_pokemon_id,envolved_pokemon)['id']
    db.execute_delete_query(querys.sql_delete_pokemon_of_trainer,(trainer_name,pokemon_id))
    db.execute_insert_query(querys.sql_insert_pokemon_to_trainer,(trainer_name,envolved_pokemon_id))    
    return {
            "success": True,
            "payload": {
                        f'Envolved {trainer_name}"s {pokemon_name} to {envolved_pokemon}'
                    }
            }



from fastapi import APIRouter,status
from . import trainers_utils
from fastapi.responses import JSONResponse


from ..api_utils import querys 
from ..api_utils.db_proxy import db_proxy 

db = db_proxy()
trainersRoute = APIRouter()

@trainersRoute.get('/trainers/{pokemon_name}',response_class= JSONResponse , status_code= status.HTTP_200_OK)
def trainersOfPokemon(pokemon_name):
    pokemon_id = db.execute_select_one_query(querys.sql_get_pokemon_id,pokemon_name)['id']
    trainers = db.execute_select_all_query(querys.sql_get_trainers_of_pokemon,pokemon_id)
    return trainers

@trainersRoute.post('/trainers', response_class= JSONResponse , status_code= status.HTTP_201_CREATED)
def addTrainer(trainer_name,trainer_town):
    db.execute_insert_query(querys.sql_insert_trainer,(trainer_name,trainer_town))
    return {
            "success": True,
            "payload": {
                        f'Added {trainer_name} to DB'
                    }
            }
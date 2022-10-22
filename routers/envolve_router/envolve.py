from asyncio.windows_events import NULL
from fastapi import APIRouter , status , Response
from . import envolve_utils
from fastapi.responses import JSONResponse

from ..api_utils import querys 
from ..api_utils.db_proxy import db_proxy 

db = db_proxy()
envolveRoute = APIRouter()


@envolveRoute.patch('/envolve',response_class= JSONResponse , status_code= status.HTTP_200_OK)
def envolvePokemon(pokemon_name = NULL , trainer_name = NULL):
    envolved_pokemon = envolve_utils.envolve(pokemon_name)
    return envolved_pokemon


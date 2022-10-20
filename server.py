from fastapi import FastAPI,APIRouter,HTTPException
import uvicorn
import requests
from routers.pokemons_router.pokemon import pokemonsRoute



app = FastAPI()

app.include_router(pokemonsRoute)


@app.get('/sanity')
def root():
    return {"message":"Server is up and running"}



if __name__ == "__main__":
    uvicorn.run("server:app",host="localhost", port=8000,reload=True)


# @app.get('/trainers')
# def trainersOfpokemon(pokemon):
#     pass 
# @app.post('/trainers')
# def addTrainer(name,town):
#     pass 

# @app.delete('/pokemons/{pokeId}/trainers/{trainerId}')
# def deletePokemonFromTrainer(name,town):
#     pass 
from ast import Raise
from fastapi import FastAPI
import uvicorn
import MySQLdb as my


app = FastAPI()

@app.get('/sanity')
def root():
    return {"message":"Server is up and running"}


@app.get('/pokemons/{pokemonName}')
def pokemonByName():
    try:
        with connection.cursor() as cursor:
            query = "SELECT *  \
                    FROM pokemon p \
                    WHERE p.weight = (SELECT MAX(p.weight) FROM pokemon p)"
            cursor.execute(query)
            result = cursor.fetchall()
            return result

    except my.Error as e:
        print(e)
    pass 

@app.get('/pokemons')
def pokemonBytypeAndTrainer(type = None,trainer =None):
    pass 

@app.get('/trainers')
def trainersOfpokemon(pokemon):
    pass 
@app.post('/trainers')
def addTrainer(name,town):
    pass 

@app.delete('/pokemons/{pokeId}/trainers/{trainerId}')
def deletePokemonFromTrainer(name,town):
    pass 

if __name__ == "__main__":
    uvicorn.run("server:app",host="0.0.0.0", port=8000,reload=True)
from fastapi import FastAPI,APIRouter,HTTPException ,status , Response
import uvicorn
from routers.pokemons_router.pokemon import pokemonsRoute
from routers.trainers_router.trainers import trainersRoute
from routers.envolve_router.envolve import envolveRoute
from fastapi.responses import JSONResponse


app = FastAPI()

app.include_router(pokemonsRoute)
app.include_router(trainersRoute)
app.include_router(envolveRoute)

@app.get('/sanity' , response_class= JSONResponse , status_code= status.HTTP_200_OK)
def root():
    return {"message":"Server is up and running"}



if __name__ == "__main__":
    uvicorn.run("server:app",host="localhost", port=8000,reload=True)

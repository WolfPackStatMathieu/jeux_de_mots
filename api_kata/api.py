from fastapi import FastAPI
import uvicorn
from src.dao.joueur_dao import JoueurDAO
from src.dao.liste_dao import ListeDAO
from router import joueur_get
from router import liste_get
from router import mot_get
from router import partie_get, partie_post

kata=FastAPI()
kata.include_router(joueur_get.router)
kata.include_router(liste_get.router)
kata.include_router(mot_get.router)
# kata.include_router(partie_get.router)
# kata.include_router(partie_post.router)


@kata.get("/")
async def root():
    return({"message":"bonjour"})






if __name__=='__main__':
    uvicorn.run(kata, host="127.0.0.1", port=80)

"""_summary_
"""
from fastapi import FastAPI
import uvicorn
# from src.dao.joueur_dao import JoueurDAO
# from src.dao.liste_dao import ListeDAO

from router import joueur
from router import liste
from router import mot
from router import top10

kata=FastAPI()
kata.include_router(joueur.router)
kata.include_router(liste.router)
kata.include_router(mot.router)
kata.include_router(top10.router)



@kata.get("/")
async def root():
    """endpoint à la racine du webservice
    """
    return{"message":"bonjour"}


if __name__=='__main__':
    uvicorn.run(kata, host="127.0.0.1", port=80)

from fastapi import FastAPI, status, Response
import uvicorn
from src.dao.joueur_dao import JoueurDAO
kata=FastAPI()

@kata.get("/",
          tags=['accueil'],
          summary='accueil de l api kata',
          description='cette api permet de jouer avec des mots',
          response_description='un message d accueil')
async def root():

    return({"message":"bonjour"})

@kata.get("/joueur/{id_joueur}",
          response_description='la string du pseudo du joueur demandé')
async def get_joueur_by_id(id_joueur):
    """permet de récupérer le pseudo d'un joueur par son id

    - **id_joueur** paramètre de chemin obligatoire
    """
    joueur_dao=JoueurDAO()
    return joueur_dao.get_pseudo_by_id(id_joueur)

@kata.post("/joueur/{pseudo}")
async def get_joueur_by_id(pseudo):
    joueur_dao=JoueurDAO()
    return joueur_dao.create(pseudo)


if __name__=='__main__':
    uvicorn.run(kata, host="127.0.0.1", port=80)

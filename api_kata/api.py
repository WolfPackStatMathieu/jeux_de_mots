from fastapi import FastAPI
import uvicorn
from src.dao.joueur_dao import JoueurDAO
from src.dao.liste_dao import ListeDAO
kata=FastAPI()

@kata.get("/")
async def root():
    return({"message":"bonjour"})


#ENDPOINTS JOUEUR
@kata.get("/joueur/{id_joueur}")
async def get_joueur_by_id(id_joueur):
    joueur_dao=JoueurDAO()
    return joueur_dao.get_pseudo_by_id(id_joueur)

@kata.post("/joueur/{pseudo}")
async def create_joueur(pseudo):
    joueur_dao=JoueurDAO()
    return joueur_dao.create(pseudo)

@kata.get("/joueur/{id_joueur}/liste")
async def get_liste_by_id_joueur(id_joueur):
    liste_dao=ListeDAO()
    return liste_dao.get_liste_by_id_joueur(id_joueur)


#ENDPOINTS LISTE
@kata.get("/liste/{id_liste}")
async def get_mots_by_id_liste( id_liste):
    liste_dao=ListeDAO()
    return liste_dao.get_mots_by_id_liste(id_liste)


    
    
if __name__=='__main__':
    uvicorn.run(kata, host="127.0.0.1", port=80)

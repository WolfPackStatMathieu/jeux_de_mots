from fastapi import FastAPI
import uvicorn
from src.dao.joueur_dao import JoueurDAO
kata=FastAPI()

@kata.get("/")
async def root():
    return({"message":"bonjour"})

@kata.get("/joueur/{id_joueur}")
async def get_joueur_by_id(id_joueur):
    joueur_dao=JoueurDAO()
    return joueur_dao.get_pseudo_by_id(id_joueur)

@kata.post("/joueur/{pseudo}")
async def get_joueur_by_id(pseudo):
    joueur_dao=JoueurDAO()
    return joueur_dao.create(pseudo)
    
    
if __name__=='__main__':
    uvicorn.run(kata, host="127.0.0.1", port=80)

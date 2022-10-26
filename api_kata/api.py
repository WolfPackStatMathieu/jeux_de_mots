from fastapi import FastAPI
from src.dao.joueur_dao import JoueurDAO
kata=FastAPI()

@app.get("/joueur/{id_joueur}")
async def get_joueur_by_id(id_joueur):
    joueur_dao=JoueurDAO()
    return joueur_dao.get_pseudo_by_id(id_joueur)

@app.post("/joueur/{pseudo}")
async def get_joueur_by_id(pseudo):
    joueur_dao=JoueurDAO()
    return joueur_dao.create(pseudo)
    
    
if __name__=='__main__':
    uvicorn.run(app, host="1.9.8.0", port=80)
from fastapi import APIRouter
from fastapi import FastAPI, status, Response
from src.dao.joueur_dao import JoueurDAO

router = APIRouter(
    prefix='/joueur',
    tags=['joueur']
)

@router.get("/{id_joueur}",
          response_description='la string du pseudo du joueur demandé')
async def get_joueur_by_id(id_joueur):
    """permet de récupérer le pseudo d'un joueur par son id

    - **id_joueur** paramètre de chemin obligatoire
    """
    joueur_dao=JoueurDAO()
    return joueur_dao.get_pseudo_by_id(id_joueur)

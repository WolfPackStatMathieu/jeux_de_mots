from fastapi import APIRouter
from fastapi import FastAPI, status, Response
from src.dao.joueur_dao import JoueurDAO

router = APIRouter(
    prefix='/joueur',
    tags=['joueur']
)

#Obtenir le pseudo d'un joueur
@router.get("/{id_joueur}",
          response_description='la string du pseudo du joueur demandé')
async def get_joueur_by_id(id_joueur):
    """permet de récupérer le pseudo d'un joueur par son id

    - **id_joueur** paramètre de chemin obligatoire
    """
    joueur_dao=JoueurDAO()
    return joueur_dao.get_pseudo_by_id(id_joueur)

#Créer un joueur
@router.post("/{pseudo}")
async def create_joueur(pseudo):
    joueur_dao=JoueurDAO()
    joueur_dao.create(pseudo)

#Obtenir le nom des listes d'un joueur
@router.get("/{id_joueur}/liste")
async def get_liste_by_id_joueur(id_joueur):
    liste_dao=ListeDAO()
    return liste_dao.get_liste_by_id_joueur(id_joueur)

#Créer une liste associée à un joueur
@router.create("/{id_joueur}/liste/{name}")
async def create_by_name(name):
    liste_dao=ListeDAO()
    liste_dao.supprimer(id_joueur, name)
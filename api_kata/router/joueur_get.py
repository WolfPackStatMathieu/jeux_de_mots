from fastapi import APIRouter
from fastapi import *
from src.dao.joueur_dao import JoueurDAO
from src.dao.liste_dao import ListeDAO

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

#Obtenir l'id d'un joueur par son pseudo
@router.get("/pseudo/{pseudo}")
async def get_joueur_by_pseudo(pseudo):
    joueur_dao=JoueurDAO()
    return(joueur_dao.get_id_by_pseudo(pseudo))

#Créer un joueur
@router.post("/{pseudo}")
async def create_joueur(pseudo):
    joueur_dao=JoueurDAO()
    return(joueur_dao.create(pseudo))

#Obtenir le nom des listes d'un joueur
@router.get("/{id_joueur}/liste")
async def get_liste_by_id_joueur(id_joueur):
    liste_dao=ListeDAO()
    return liste_dao.get_liste_by_id_joueur(id_joueur)

#Créer une liste associée à un joueur
@router.post("/{id_joueur}/liste/{name}")
async def create_by_name(id_joueur, name):
    liste_dao=ListeDAO()
    return(liste_dao.creer(id_joueur, name))
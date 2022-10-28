from fastapi import APIRouter
from fastapi import *
from src.dao.joueur_dao import JoueurDAO
from src.dao.liste_dao import ListeDAO
from src.dao.score_dao import ScoreDAO

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

#Obtenir les listes d'un joueur (nom et contenu)
@router.get("/{id_joueur}/liste")
async def get_liste_by_id_joueur(id_joueur):
    liste_dao=ListeDAO()
    nom=liste_dao.get_liste_by_id_joueur(id_joueur)
    contenu=[]
    for nom_liste in nom:
        contenu.append(liste_dao.get_mots_by_nom_liste(nom_liste))
    return(nom, contenu)

#Créer une liste associée à un joueur
@router.post("/{id_joueur}/liste/{name}")
async def create_by_name(id_joueur, name):
    liste_dao=ListeDAO()
    return(liste_dao.creer(id_joueur, name))

#Ajouter un score à un joueur
@router.post("/{id_joueur}/score/{score}")
async def ajoute_score_joueur(id_joueur, score):
    score_dao=ScoreDAO()
    return(score_dao.ajouter(id_joueur, score))

#Obtenir le top 10 des meilleurs scores d'un joueur
@router.get("/{id_joueur}/score")
async def get_best_score(id_joueur):
    score_dao=ScoreDAO()
    return(score_dao.get_top_10_perso(id_joueur))
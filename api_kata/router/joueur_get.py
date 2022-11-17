"""Endpoints de l'api_kata pour les joueurs
"""

from fastapi import APIRouter
# from fastapi import *
from src.dao.joueur_dao import JoueurDAO
from src.dao.liste_dao import ListeDAO
from src.dao.score_dao import ScoreDAO
from src.dao.partie_dao import PartieDAO
from src.dao.proposition_dao import PropositionDAO

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

#Obtenir l'id et le top ten d'un joueur par son pseudo
@router.get("/pseudo/{pseudo}")
async def get_joueur_by_pseudo(pseudo):
    """crée un endpoint permettant de récupérer l'id d'un joueur par son pseudo

    Parameters
    ----------
    pseudo : str
        le pseudo du joueur

    Returns
    -------
    int
        l'id du joueur
    """
    joueur_dao=JoueurDAO()
    score_dao=ScoreDAO()
    id_joueur=joueur_dao.get_id_by_pseudo(pseudo)
    # top_ten=score_dao.get_top_10_perso(id_joueur)
    return id_joueur

#Créer un joueur
@router.post("/{pseudo}")
async def create_joueur(pseudo):
    joueur_dao=JoueurDAO()
    return joueur_dao.create(pseudo)

#Obtenir les listes d'un joueur (nom et contenu)
@router.get("/{id_joueur}/liste")
async def get_liste_by_id_joueur(id_joueur):
    liste_dao=ListeDAO()
    nom=liste_dao.get_liste_by_id_joueur(id_joueur)[0]
    id=liste_dao.get_liste_by_id_joueur(id_joueur)[1]
    contenu=[]
    for nom_liste in nom:
        contenu.append(liste_dao.get_mots_by_nom_liste(nom_liste))
    return(nom, contenu, id)

#Créer une liste associée à un joueur
@router.post("/{id_joueur}/liste/{name}")
async def create_by_name(id_joueur, name):
    liste_dao=ListeDAO()
    return liste_dao.creer(id_joueur, name)


#Obtenir le top 10 des meilleurs scores d'un joueur
@router.get("/{id_joueur}/score")
async def get_best_score(id_joueur):
    score_dao=ScoreDAO()
    return score_dao.get_top_10_perso(id_joueur)

#Obtenir la partie en cours d'un joueur 
@router.get("/{id_joueur}/partie_en_cours")
async def get_partie_by_joueur(id_joueur):
    partie_dao=PartieDAO()
    propositiondao=PropositionDAO()
    id=partie_dao.get_id_partie_en_cours_joueur(id_joueur)
    partie=partie_dao.get_partie_by_id(id)
    proposition=propositiondao.get_by_id_partie(id)
    return(id,partie, proposition)

#Sauvegarder la partie en cours d'un joueur
#Ca marche pas : j'ai pas réussi à créer une partie dans la bdd
@router.post("/{id_joueur}/partie")
async def create_partie_by_joueur(id_joueur, partie):
    partie_dao=PartieDAO()
    nom_partie = partie.nom
    score_final = partie.score 
    mot_objectif=partie.mot_objectif
    temps_max = partie.difficultes.temps
    nb_tentatives_max = partie.difficultes.nb_tentatives 
    indice = partie.difficultes.indice
    liste_perso = partie.est_liste_perso
    id_liste=partie.id_liste
    partie_dao.creer(id_joueur, nom_partie, score_final, mot_objectif, temps_max, nb_tentatives_max, indice, liste_perso, id_liste)


#Ajouter un score à un joueur
#Ca marche pas 
@router.post("/{id_joueur}/score/{score}")
async def ajoute_score_joueur(id_joueur, score):
    score_dao=ScoreDAO()
    return(score_dao.ajouter(id_joueur, score))

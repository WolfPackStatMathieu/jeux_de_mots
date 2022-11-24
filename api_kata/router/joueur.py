"""routeurs contenant les endpoints concernant le joueur
"""
# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
from fastapi import APIRouter
from pydantic import BaseModel
from src.dao.joueur_dao import JoueurDAO
from src.dao.liste_dao import ListeDAO
from src.dao.score_dao import ScoreDAO
from src.dao.partie_dao import PartieDAO
from src.dao.proposition_dao import PropositionDAO

router = APIRouter(
    prefix='/joueur',
    tags=['joueur']
)

#Créer un joueur
@router.post("/{pseudo}")
async def create_joueur(pseudo):
    """endpoint POST pour créer un joueur

    Parameters
    ----------
    pseudo : str
        pseudo du joueur

    Returns
    -------
    function
        fonction de création d'un joueur en BDD
    """
    joueur_dao=JoueurDAO()
    return joueur_dao.creer(pseudo)

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
    """endpoint pour obtenir un joueur en fournissant son pseudo

    Parameters
    ----------
    pseudo : string
        pseudo du joueur

    Returns
    -------
    int
        id du joueur
    """
    joueur_dao=JoueurDAO()
    # score_dao=ScoreDAO()
    id_joueur=joueur_dao.get_id_by_pseudo(pseudo)
    # top_ten=score_dao.get_top_10_perso(id_joueur)
    return id_joueur

#Créer une liste associée à un joueur
@router.post("/{id_joueur}/liste/{name}")
async def create_by_name(id_joueur, name):
    """endpoint POST pour créer une liste associée à un joueur

    Parameters
    ----------
    id_joueur : int
        id du joueur
    name : str
        nom de la liste créée

    Returns
    -------
    function
        lance la création de la liste associée à un joueur en BDD
    """
    liste_dao=ListeDAO()
    return liste_dao.creer(id_joueur, name)

#Obtenir les listes d'un joueur (noms et contenus des listes)
@router.get("/{id_joueur}/liste")
async def get_liste_by_id_joueur(id_joueur):
    """endpoint GET pour obtenir les listes de mots d'un joueur

    Parameters
    ----------
    id_joueur : int
        id du joueur
    """
    liste_dao=ListeDAO()
    nom = liste_dao.get_liste_by_id_joueur(id_joueur)[0]
    id = liste_dao.get_liste_by_id_joueur(id_joueur)[1]
    contenu = []
    for id_liste in id:
        contenu.append(liste_dao.get_mots_by_id_liste(id_liste))
    return(nom, contenu, id)


class PartieCreation(BaseModel):
    # pylint: disable=too-few-public-methods
    """classe PartieCreation pour la transmission d'informations

    Parameters
    ----------
    BaseModel : BaseModel
        classe mère
    """
    mot_objectif : str
    nb_tentatives_max : int
    indice : bool
    liste_perso : bool
    temps_max : int

#Sauvegarder la partie en cours d'un joueur
@router.post("/{id_joueur}/partie")
async def create_partie_by_joueur(id_joueur, partie : PartieCreation):
    """_summary_

    Parameters
    ----------
    id_joueur : int
        _description_
    partie : PartieCreation
        _description_
    """
    partie_dao=PartieDAO()
    mot_objectif=partie.mot_objectif
    nb_tentatives_max=partie.nb_tentatives_max
    indice=partie.indice
    liste_perso=partie.liste_perso
    temps_max=partie.temps_max
    return(partie_dao.creer(id_joueur,
                            mot_objectif,
                            nb_tentatives_max,
                            indice, liste_perso, temps_max))

#Obtenir la partie en cours d'un joueur
@router.get("/{id_joueur}/partie_en_cours")
async def get_partie_by_joueur(id_joueur):
    """endpoint GET pour obtenir la partie en cours d'un joueur

    Parameters
    ----------
    id_joueur : int
        id du joueur
    """
    partie_dao=PartieDAO()
    propositiondao=PropositionDAO()
    identifiant=partie_dao.get_id_partie_en_cours_joueur(id_joueur)
    partie=partie_dao.get_partie_by_id(identifiant)
    proposition=propositiondao.get_by_id_partie(identifiant)
    return(identifiant,partie, proposition)

#Supprimer la partie d'un joueur
@router.delete("/{id_joueur}/partie")
async def delete_partie_by_joueur(id_joueur):
    """endpoint DELETE pour supprimer la partie d'un joueur

    Parameters
    ----------
    id_joueur : int
        id du joueur

    Returns
    -------
    fucntion
        supprime la partie du joueur en BDD
    """
    partie_dao=PartieDAO()
    id_partie=partie_dao.get_id_partie_en_cours_joueur(id_joueur)
    return partie_dao.supprimer(id_partie)

#Créer une proposition d'un joueur dans une partie
@router.post("/{id_joueur}/proposition/{proposition}")
async def create_proposition_by_joueur(id_joueur, proposition):
    """endpoint POST pour créer une proposition d'un joueur

    Parameters
    ----------
    id_joueur : int
        id du joueur
    proposition : str
        mot proposé par le joueur

    Returns
    -------
    function
        lance la création d'une proposition en BDD
    """
    partie_dao=PartieDAO()
    proposition_dao=PropositionDAO()
    id_partie=partie_dao.get_id_partie_en_cours_joueur(id_joueur)
    return proposition_dao.creer(id_partie, proposition)

#Ajouter un score à un joueur
@router.post("/{id_joueur}/score/{score}")
async def ajoute_score_joueur(id_joueur, score):
    """endpoint POST pour ajouter un score à un joueur

    Parameters
    ----------
    id_joueur : int
        id du joueur
    score : int
        score à ajouter

    Returns
    -------
    function
        ajoute le score du joueur en BDD
    """
    score_dao=ScoreDAO()
    return score_dao.ajouter(id_joueur, score)

#Obtenir le top 10 des meilleurs scores d'un joueur
@router.get("/{id_joueur}/score")
async def get_best_score(id_joueur):
    """endpoint pour obtenir les 10 meilleurs scores d'un joueur

    Parameters
    ----------
    id_joueur : int
        id du joueur

    Returns
    -------
    function
        lance la requête en BDD pour obtenir le top10 du joueur
    """
    score_dao=ScoreDAO()
    return score_dao.get_top_10_perso(id_joueur)

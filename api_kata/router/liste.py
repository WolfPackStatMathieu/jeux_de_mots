"""routeur qui contient tous les endpoints concernant les listes
"""
from fastapi import APIRouter
from src.dao.liste_dao import ListeDAO

#Routeur pour endpoint intermediaire /liste
router = APIRouter(
    prefix='/liste',
    tags=['liste']
)

#Obtenir le nom d'une liste et le contenu de la liste par son identifiant
@router.get("/{id_liste}")
async def get_mots_by_id_liste(id_liste):
    """permet d'obtenir les mots d'une liste

    Parameters
    ----------
    id_liste : int
        id de la liste
    """
    liste_dao=ListeDAO()
    nom=liste_dao.get_nom_by_id(id_liste)
    contenu=liste_dao.get_mots_by_id_liste(id_liste)
    return(nom, contenu)

#Ajouter un mot dans une liste
@router.post("/{id_liste}/mot/{id_mot}")
async def ajouter_mot(id_liste, id_mot):
    """endpoint POST pour ajouter un mot dans une liste

    Parameters
    ----------
    id_liste : int
        id de la liste
    id_mot : int
        id du mot

    Returns
    -------
    function
        lance une requête en BDD pour supprimer le mot de la liste
    """
    liste_dao=ListeDAO()
    return liste_dao.ajouter_mot(id_liste, id_mot)

#Supprimer un mot dans une liste
@router.delete("/{id_liste}/mot/{id_mot}")
async def supprimer_mot(id_liste, id_mot):
    """endpoint DELETE pour supprimer un mot dans une liste

    Parameters
    ----------
    id_liste : int
        id de la liste
    id_mot : int
        id du mot

    Returns
    -------
    function
        lance une fonction pour supprimer le mot de la liste en BDD
    """
    liste_dao=ListeDAO()
    return liste_dao.supprimer_mot(id_mot, id_liste)

#Supprimer une liste
@router.delete("/{id_liste}")
async def delete_by_id_liste( id_liste):
    """endpoint DELETE pour supprimer une liste

    Parameters
    ----------
    id_liste : int
        id de la liste

    Returns
    -------
    function
        lance une fonction qui supprime la liste en BDD
    """
    liste_dao=ListeDAO()
    return liste_dao.supprimer(id_liste)

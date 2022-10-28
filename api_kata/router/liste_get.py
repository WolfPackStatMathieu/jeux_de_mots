from fastapi import APIRouter
from fastapi import *
from src.dao.liste_dao import ListeDAO

router = APIRouter(
    prefix='/liste',
    tags=['liste']
)

#Obtenir une liste par son identifiant
@router.get("/{id_liste}")
async def get_mots_by_id_liste(id_liste):
    liste_dao=ListeDAO()
    nom=liste_dao.get_nom_by_id(id_liste)
    contenu=liste_dao.get_mots_by_id_liste(id_liste)
    return(nom, contenu)

#Ajouter un mot dans une liste
@router.post("/{id_liste}/mot/{id_mot}")
async def ajouter_mot(id_liste, id_mot):
    liste_dao=ListeDAO()
    return(liste_dao.ajouter_mot(id_liste, id_mot))

#Supprimer un mot dans une liste
@router.delete("/{id_liste}/mot/{id_mot}")
async def supprimer_mot(id_liste, id_mot):
    liste_dao=ListeDAO()
    return(liste_dao.supprimer_mot(id_mot, id_liste))

#Supprimer une liste
@router.delete("/{id_liste}")
async def delete_by_id_liste( id_liste):
    liste_dao=ListeDAO()
    return liste_dao.supprimer(id_liste)
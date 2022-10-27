from fastapi import APIRouter
from fastapi import FastAPI, status, Response
from src.dao.joueur_dao import JoueurDAO

router = APIRouter(
    prefix='/liste',
    tags=['liste']
)

#Obtenir les mots d'une liste
@router.get("/{id_liste}")
async def get_mots_by_id_liste( id_liste):
    liste_dao=ListeDAO()
    return liste_dao.get_mots_by_id_liste(id_liste)

#Ajouter un mot dans une liste
@router.create("/{id_liste}/mot/{id_mot}")
async def ajouter_mot(id_liste, id_mot):
    liste_dao=ListeDAO()
    liste_dao.ajouter_mot(id_liste, id_mot)

#Supprimer un mot dans une liste
@router.delete("/{id_liste}/mot/{id_mot}")
async def supprimer_mot(id_liste, id_mot):
    liste_dao=ListeDAO()
    liste_dao.supprimer_mot(id_mot, id_list)

#Supprimer une liste
@router.delete("/{id_liste}")
async def delete_by_id_liste( id_liste):
    liste_dao=ListeDAO()
    return liste_dao.creer(id_liste)
from fastapi import APIRouter
from fastapi import *
from src.dao.mot_dao import MotDAO

router = APIRouter(
    prefix='/mot',
    tags=['mot']
)

#Creer un mot
@router.post("/contenu/{mot}")
async def create_mot(mot):
    mot_dao=MotDAO()
    return(mot_dao.creer(mot))

#Obetnir l'id d'un mot
# @router.get("/{mot}")
# async def create_mot(mot):
#     mot_dao=MotDAO()
#     return(mot_dao.get_id_by_mot(mot))

#Obtenir l'id d'un mot
@router.get("/mot/{mot}")
async def get_id_by_mot(mot):
    mot_dao=MotDAO()
    id_mot=mot_dao.get_id_by_mot(mot)
    return(id_mot)
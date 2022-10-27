from fastapi import APIRouter
from fastapi import *
from src.dao.partie_dao import PartieDAO

router = APIRouter(
    prefix='/partie',
    tags=['partie']
)

#Obtenir l'id d'une partie

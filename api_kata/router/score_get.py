from fastapi import APIRouter
from fastapi import *
from src.dao.liste_dao import ListeDAO

router = APIRouter(
    prefix='/score',
    tags=['score']
)

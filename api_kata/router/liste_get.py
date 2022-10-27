from fastapi import APIRouter
from fastapi import FastAPI, status, Response
from src.dao.joueur_dao import JoueurDAO

router = APIRouter(
    prefix='/liste',
    tags=['liste']
)
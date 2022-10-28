from fastapi import APIRouter
from fastapi import *
from src.dao.score_dao import ScoreDAO

router = APIRouter(
    prefix='/top10',
    tags=['top10']
)

#Obtenir le top 10 général
@router.get("/top10")
async def get_top10():
    top10 = ScoreDAO.get_top_10_general()
    return (top10)
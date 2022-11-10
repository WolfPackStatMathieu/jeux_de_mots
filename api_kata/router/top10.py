from fastapi import APIRouter
from fastapi import *
from src.dao.score_dao import ScoreDAO

router = APIRouter(
    prefix='/top10',
    tags=['top10']
)

#Obtenir le top 10 général
@router.get("")
async def get_top10():
    score_dao=ScoreDAO()
    top10 = score_dao.get_top_10_general()
    return (top10)


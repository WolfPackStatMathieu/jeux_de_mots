"""routeur contenant les endpoints à propos du top10 des scores
"""

from fastapi import APIRouter
from src.dao.score_dao import ScoreDAO

router = APIRouter(
    prefix='/top10',
    tags=['top10']
)

#Obtenir le top 10 général
@router.get("")
async def get_top10():
    """endpont GET pour obtenir le top10 des scores

    Returns
    -------
    List(List)
        une liste de listes contenant chacune le score, l'id et le pseudo du joueur
    """
    score_dao=ScoreDAO()
    top10 = score_dao.get_top_10_general()
    return top10

"""routeur contenant tous les endpoint en lien avec les mots
"""

from fastapi import APIRouter, Query
from src.dao.mot_dao import MotDAO

router = APIRouter(
    prefix='/mot',
    tags=['mot']
)

#Creer un mot
@router.post("/contenu/{mot}")
async def create_mot(mot: str =  Query(min_length=1, max_length=50,regex="^[A-Za-z]+$")):
    """endpoint POST pour créer un mot en BDD

    Parameters
    ----------
    mot : str
        un mot à créer, by default Query(min_length=1, max_length=50,regex="^[A-Za-z]+$")
        i.e. que des lettres majuscules ou minuscules

    Returns
    -------
    function
        lance la création du mot en BDD
    """
    mot_dao=MotDAO()
    return mot_dao.creer(mot)




#Obetnir l'id d'un mot
# @router.get("/{mot}")
# async def create_mot(mot):
#     mot_dao=MotDAO()
#     return(mot_dao.get_id_by_mot(mot))

#Obtenir l'id d'un mot
@router.get("/mot/{mot}")
async def get_id_by_mot(mot):
    """endpoint GET pour obtenir un mot par son id

    Parameters
    ----------
    mot : str
        mot dont on veut l'id

    Returns
    -------
    int
        id du mot
    """
    mot_dao=MotDAO()
    id_mot=mot_dao.get_id_by_mot(mot)
    return id_mot

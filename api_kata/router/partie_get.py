# from fastapi import APIRouter
# from fastapi import *
# from src.dao.partie_dao import PartieDAO

# router = APIRouter(
#     prefix='/partie',
#     tags=['partie']
# )

# #Obtenir l'id d'une partie
# @router.get("/{id_partie}",
#             response_description='récupère la partie par son id_partie')
# async def get_partie_by_id(id_partie):
#     """permet de récupérer une partie par son id

#     - **id_partie** paramètre de chemin obligatoire
#     """
#     partie_dao = PartieDAO()

#     return partie_dao.get_partie_by_id(id_partie)
from fastapi import FastAPI
import uvicorn
from src.dao.joueur_dao import JoueurDAO
from src.dao.liste_dao import ListeDAO
from router import joueur_get
from router import liste_get
kata=FastAPI()
kata.include_router(joueur_get.router)


@kata.get("/")
async def root():
    return({"message":"bonjour"})


# #########   ENDPOINTS JOUEUR  ##################

# #Obtenir le pseudo d'un joueur
# @kata.get("/joueur/{id_joueur}")
# async def get_joueur_by_id(id_joueur):
#     joueur_dao=JoueurDAO()
#     return joueur_dao.get_pseudo_by_id(id_joueur)

# #Créer un joueur
# @kata.post("/joueur/{pseudo}")
# async def create_joueur(pseudo):
#     joueur_dao=JoueurDAO()
#     joueur_dao.create(pseudo)

# #Obtenir le nom des listes d'un joueur
# @kata.get("/joueur/{id_joueur}/liste")
# async def get_liste_by_id_joueur(id_joueur):
#     liste_dao=ListeDAO()
#     return liste_dao.get_liste_by_id_joueur(id_joueur)

# #Créer une liste associée à un joueur
# @kata.create("/joueur/{id_joueur}/liste/{name}")
# async def create_by_name(name):
#     liste_dao=ListeDAO()
#     liste_dao.supprimer(id_joueur, name)



# #########    ENDPOINTS LISTE  ###############


# #Obtenir les mots d'une liste
# @kata.get("/liste/{id_liste}")
# async def get_mots_by_id_liste( id_liste):
#     liste_dao=ListeDAO()
#     return liste_dao.get_mots_by_id_liste(id_liste)

# #Ajouter un mot dans une liste
# @kata.create("/liste/{id_liste}/mot/{id_mot}")
# async def ajouter_mot(id_liste, id_mot):
#     liste_dao=ListeDAO()
#     liste_dao.ajouter_mot(id_liste, id_mot)

# #Supprimer un mot dans une liste
# @kata.delete("/liste/{id_liste}/mot/{id_mot}")
# async def supprimer_mot(id_liste, id_mot):
#     liste_dao=ListeDAO()
#     liste_dao.supprimer_mot(id_mot, id_list)

# #Supprimer une liste
# @kata.delete("/liste/{id_liste}")
# async def delete_by_id_liste( id_liste):
#     liste_dao=ListeDAO()
#     return liste_dao.creer(id_liste)



if __name__=='__main__':
    uvicorn.run(kata, host="127.0.0.1", port=80)

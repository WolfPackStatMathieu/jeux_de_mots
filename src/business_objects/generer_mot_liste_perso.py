from src.business_objects.abstract_generer_mot import AbstractGenererMot
from src.dao.liste_dao import ListeDAO

class GenererMotListePerso(AbstractGenererMot):
    def __init__(self, id_liste):
        self.id_liste=id_liste


    def generer(self):
        dao_liste=ListeDAO()
        return(dao_liste.get_mots_by_id_liste(self.id_liste))

generation_perso=GenererMotListePerso(1)
print(generation_perso.generer())
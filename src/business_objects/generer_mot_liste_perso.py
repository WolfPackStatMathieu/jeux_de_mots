from src.business_objects.abstract_generer_mot import AbstractGenererMot
from src.dao.liste_dao import ListeDAO
import random

class GenererMotListePerso(AbstractGenererMot):
    def __init__(self, id_liste):
        self.id_liste=id_liste


    def generer(self):
        dao_liste=ListeDAO()
        liste=dao_liste.get_mots_by_id_liste(self.id_liste)
        num=random.randint(0,len(liste)-1)
        return(liste[num])

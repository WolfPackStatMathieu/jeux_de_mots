from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from src.view.abstractview import AbstractView
from src.view.session import Session

class SupprimerMotView (AbstractView) :
    def __init__(self):
        from src.dao.liste_dao import ListeDAO
        listedao = ListeDAO()
        id_liste = listedao.get_id_by_nom(Session().liste)
        liste_mots = listedao.get_mots_by_id_liste(id_liste)

        self.__questions = inquirer.select(
            message=f'Quel mot veux tu supprimer à ta liste {Session().liste}?'
            , choices = [Choice(mot) for mot in liste_mots]
        )
        
    
    def display_info(self):
        pass

    def make_choice(self):
        reponse = self.__questions.execute()
        from src.dao.mot_dao import MotDAO
        id_mot = MotDAO.id(self, reponse)
        from src.dao.liste_dao import ListeDAO
        ListeDAO.supprimer_mot(self, id_mot, id_liste)
        if len(liste_mots) == 1 :
            ListeDAO.supprimer(self, id_liste)

        

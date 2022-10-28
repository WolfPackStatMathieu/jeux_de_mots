from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from src.view.abstractview import AbstractView
from src.view.session import Session


class ConsulterListePersoView (AbstractView) :
    
    def __init__(self):
        from src.dao.joueur_dao import JoueurDAO
        joueurdao = JoueurDAO()
        id_joueur = joueurdao.get_id_by_pseudo(Session().pseudo)
        from src.dao.liste_dao import ListeDAO
        listedao = ListeDAO()
        listes = listedao.get_liste_by_id_joueur(id_joueur)

        self.__questions = inquirer.select(
            message=f'Quelle liste veux tu sélectionner?'
            , choices = [Choice(liste) for liste in listes]
        )

    def display_info(self):
        pass

    def make_choice(self):
        nom_liste = self.__questions.execute()
        Session().liste = nom_liste
        from src.dao.liste_dao import ListeDAO
        liste_mots = ListeDAO.get_mots_by_nom_liste(self, nom_liste)
        for mot in liste_mots :
            print(mot)
        from src.view.modificationlisteview import ModificationListeView
        return ModificationListeView()
        

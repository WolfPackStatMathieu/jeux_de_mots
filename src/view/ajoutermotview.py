from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from src.view.abstractview import AbstractView
from src.view.session import Session

ASK_MOT=inquirer.text(message = f'Quel mot veux tu ajouter à ta liste {Session().liste}?')


class ConsulterListePersoView (AbstractView) :
    
    def display_info(self):
        pass

    def make_choice(self):
        mot = ASK_MOT.execute()
        from src.dao.mot_dao import MotDAO
        if not MotDAO.find() :
            MotDAO.creer(self, mot)
        id_mot = MotDAO.id()
        from src.dao.liste_dao import ListeDAO
        id_liste = ListeDAO.id(self, Session().liste)
        ListeDAO.ajouter_mot(self, id_liste, id_mot)
        for mot in liste_mots :
            print(mot)
        from src.view.modificationlisteview import ModificationListeView
        return ModificationListeView()
        

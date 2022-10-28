from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from src.view.abstractview import AbstractView
from src.view.session import Session

ASK_MOT=inquirer.text(message = f'Quel mot veux tu ajouter à ta liste {Session().liste}?')


class AjouterMotView (AbstractView) :
    
    def display_info(self):
        pass

    def make_choice(self):
        mot = ASK_MOT.execute()
        #On transforme ensuite le mot pour supprimer les accents et mettre en majuscule
        from src.business_objects.proposition import Proposition
        mot = Proposition(mot)
        mot = Proposition.mot
        
        from src.dao.mot_dao import MotDAO
        motdao = MotDAO()
        if not motdao.find(mot) :
            motdao.creer(mot)
        id_mot = motdao.get_id_by_mot(mot)
        from src.dao.liste_dao import ListeDAO
        listedao = ListeDAO()
        id_liste = listedao.id(self, Session().liste)
        listedao.ajouter_mot(self, id_liste, id_mot)
        for mot in liste_mots :
            print(mot)
        from src.view.modificationlisteview import ModificationListeView
        return ModificationListeView()
        

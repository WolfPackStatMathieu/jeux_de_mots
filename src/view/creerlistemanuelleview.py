from email.message import Message
from pprint import pprint


from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from src.view.abstractview import AbstractView
from src.view.session import Session




ASK_NOM_LISTE=inquirer.text(message = 'Quel est le nom de ta nouvelle liste?')
ASK_PREMIER_MOT=inquirer.text(message = 'Quel est le premier mot de la liste?')


class CreerListeManuelleView(AbstractView):


    def display_info(self):
        print(f"Création d'une liste")

    def make_choice(self):
        nom_liste = ASK_NOM_LISTE.execute()
        premier_mot = ASK_PREMIER_MOT.execute()

        from src.dao.joueur_dao import JoueurDAO
        id_joueur = JoueurDAO.get_id_by_pseudo(self, Session().pseudo)

        from src.dao.liste_dao import ListeDAO
        ListeDAO.creer(self, id_joueur, nom_liste)

        from src.dao.mot_dao import MotDAO
        if not MotDAO.find() :
            MotDAO.creer(self, mot)
        id_mot = MotDAO.id()
        id_liste = ListeDAO.id(self, Session().liste)
        ListeDAO.ajouter_mot(self, id_liste, id_mot)

        from src.view.accueilpersoview import AccueilPersoView
        return AccueilPersoView()


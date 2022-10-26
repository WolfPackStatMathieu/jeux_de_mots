from email.message import Message
from pprint import pprint


from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from src.view.abstractview import AbstractView
from src.view.session import Session




ASK_PSEUDO=inquirer.text(message = 'Quel est ton pseudo?')



class ConnectionView(AbstractView):


    def display_info(self):
        print(f"Connexion au compte")

    def make_choice(self):
        pseudo = ASK_PSEUDO.execute()
        from src.dao.joueur_dao import JoueurDAO
        if JoueurDAO.pseudo_existe(self, pseudo) :
            #Compléter les infos de la session
            from src.business_objects.joueur import Joueur
            joueur = Joueur(10, 'Mathis', [])
            print(joueur)
            from src.view.session import Session
            session = Session(pseudo)
            print(session.pseudo)
            from src.view.accueilpersoview import AccueilPersoView
            return AccueilPersoView()
           
        else :
            print("Le pseudo n'existe pas") 
            from src.view.accueilkataview import AccueilKataView
            return AccueilKataView()
            
        
        

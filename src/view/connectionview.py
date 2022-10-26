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
        if 1 == 1 or pseudo_existe(pseudo) :
            from src.view.accueilpersoview import AccueilPersoView
            return AccueilPersoView()
            #Compléter les infos de la session
            Session().pseudo = user.pseudo
        else :
            print("Le pseudo n'existe pas") 
            return AccueilKataView()
            
        
        

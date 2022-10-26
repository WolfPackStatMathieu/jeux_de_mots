from email.message import Message
from pprint import pprint


from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from src.view.abstractview import AbstractView
from src.view.session import Session




ASK_PSEUDO=inquirer.text(message = 'Entre un pseudo')



class CreerCompteView(AbstractView):


    def display_info(self):
        print(f"Création du compte")

    def make_choice(self):
        pseudo = ASK_PSEUDO.execute()
        if not pseudo_existe(pseudo) :
            #Le joueur est inséré dans la base de données 
            from src.dao.joueur_dao import JoueurDAO
            create(pseudo)
        else :
            #Message d'erreur
            print("Le pseudo existe déjà")
        #Dans tous les cas, on revient ensuite à l'écran d'accueil
        from src.view.accueilkataview import AccueilKataView
        return AccueilKataView()
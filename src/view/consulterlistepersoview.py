from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from src.view.abstractview import AbstractView
from src.view.session import Session


class ConsulterListePersoView (AbstractView) :

    def __init__(self):
        self.__questions = inquirer.select(
            message=f'Bonjour {Session().pseudo}'
            , choices=[
                Choice('Voir ma liste personnelle')
                ,Choice('Ajouter un mot à ma liste')
                ,Choice('Supprimer un mot de ma liste')]
        )
    
    def display_info(self):
        pass

    def make_choice(self):
        reponse = self.__questions.execute()
        if reponse == 'Nothing':
            pass
        elif reponse== 'Voir ma liste personnelle':
            from src.view.listepersoview import ListePersoView
            return ListePersoView()
        elif reponse== 'Ajouter un mot à ma liste':
            from src.view.ajoutermotview import AjouterMotView
            return AjouterMotView()
        elif reponse== 'Supprimer un mot de ma liste':
            from src.view.supprimermotview import SupprimerMotView
            return SupprimerMotView()
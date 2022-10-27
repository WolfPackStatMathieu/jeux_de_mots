from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from src.view.abstractview import AbstractView
from src.view.session import Session


class ModificationListeView (AbstractView) :

    def __init__(self):
        self.__questions = inquirer.select(
            message=f'Que souhaites tu faire maintenant?'
            , choices=[
                Choice('Ajouter un mot')
                ,Choice('Supprimer un mot')
                ,Choice("Retour à l'accueil")
                ]
        )
    
    def display_info(self):
        pass

    def make_choice(self):
        reponse = self.__questions.execute()
        if reponse == 'Nothing':
            pass
        elif reponse== 'Ajouter un mot':
            from src.view.ajoutermotview import AjouterMotView
            return AjouterMotView()
        elif reponse== 'Supprimer un mot':
            from src.view.supprimermotview import SupprimerMotView
            return SupprimerMotView()
        elif reponse== "Retour à l'accueil":
            from src.view.accueilpersoview import AccueilPersoView
            return AccueilPersoView()
    
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from src.view.abstractview import AbstractView
from src.view.session import Session


class CreerListePersoView (AbstractView) :

    def __init__(self):
        self.__questions = inquirer.select(
            message=f'Bonjour {Session().pseudo}'
            , choices=[
                Choice('Créer une liste manuellement')
                ,Choice('Importer une liste')]
        )
    
    def display_info(self):
        pass

    def make_choice(self):
        reponse = self.__questions.execute()
        if reponse == 'Nothing':
            pass
        elif reponse== 'Créer une liste manuellement':
            from src.view.listemanuelleview import ListeManuelleView
            return ListeManuelleView()
        elif reponse== 'Importer une liste':
            from src.view.listeimporteeview import ListeImporteeView
            return ListeImporteeView()
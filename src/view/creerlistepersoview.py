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
                ,Choice('Importer une liste CSV')
                ,Choice('Importer une liste JSON')]
        )
    
    def display_info(self):
        pass

    def make_choice(self):
        reponse = self.__questions.execute()
        if reponse == 'Nothing':
            pass
        elif reponse== 'Créer une liste manuellement':
            from src.view.creerlistemanuelleview import CreerListeManuelleView
            return CreerListeManuelleView()
        elif reponse== 'Importer une liste CSV':
            from src.view.listeimporteecsvview import ListeImporteeCSVView
            return ListeImporteeCSVView()
        elif reponse== 'Importer une liste JSON':
            from src.view.listeimporteejsonview import ListeImporteeJSONView
            return ListeImporteeJSONView()
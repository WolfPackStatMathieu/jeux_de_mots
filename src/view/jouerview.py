from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from src.view.abstractview import AbstractView
from src.view.session import Session


class JouerView (AbstractView) :

    def __init__(self):
        self.__questions = inquirer.select(
            message=f'Bonjour {Session().pseudo}'
            , choices=[
                Choice('Définir la difficulté de la partie')
                ,Choice('Voir proposition')]
        )
    
    def display_info(self):
        pass

    def make_choice(self):
        reponse = self.__questions.execute()
        if reponse == 'Nothing':
            pass
        elif reponse== 'Définir la difficulté de la partie':
            from src.view.difficulteview import DifficulteView
            return DifficulteView()
        elif reponse== 'Voir proposition':
            from src.view.propositionview import PropositionView
            return PropositionView()
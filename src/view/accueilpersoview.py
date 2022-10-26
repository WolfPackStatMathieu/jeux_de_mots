from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from src.view.abstractview import AbstractView
from src.view.session import Session


class AccueilPersoView (AbstractView) :

    def __init__(self):
        self.__questions = inquirer.select(
            message=f'Bonjour {Session().user_name}'
            , choices=[
                Choice('Jouer')
                ,Choice('Créer une liste perso')
                ,Choice('Consulter une liste perso')
                ,Choice('Meilleurs scores')]
        )
    
    def display_info(self):
        pass

    def make_choice(self):
        reponse = self.__questions.execute()
        if reponse == 'Nothing':
            pass
        elif reponse== 'Jouer':
            from src.view.jouerview import JouerView
            return JouerView()
        elif reponse== 'Créer une liste perso':
            from src.view.creerlistepersoview import CreerListePersoView
            return CreerListePersoView()
        elif reponse== 'Consulter une liste perso':
            from src.view.consulterlistepersoview import ConsulterListePersoView
            return ConsulterListePersoView()
        elif reponse == 'Meilleurs scores' :
            from src.view.toptenpersoview import TopTenPersoView
            return TopTenPersoView()
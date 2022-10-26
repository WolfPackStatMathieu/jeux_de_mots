from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from src.view.abstractview import AbstractView
from src.view.session import Session

ASK_NB_TENTATIVES=inquirer.text(message = 'Quel est le nombre maximum de tentatives que tu veux?')
ASK_TEMPS=inquirer.text(message = 'Quel est le temps maximum souhaité pour faire une proposition?')
ASK_NB_LETTRES=inquirer.text(message = 'Combien veux tu que ton mot comporte de lettres? (15 maximum)')


class DifficulteView (AbstractView) :
    def __init__(self):
        self.__questions = inquirer.select(
            message=f'Veux tu connaitre la première lettre du mot?'
            , choices=[
                Choice('Oui')
                ,Choice('Non')
            ])
    
    def display_info(self):
        pass

    def make_choice(self):
        reponse = self.__questions.execute()
        if reponse == 'Oui' :
            indice = True
        else :
            indice = False
        nb_tentatives = ASK_NB_TENTATIVES.execute()
        temps = ASK_TEMPS.execute()
        nb_lettres = ASK_NB_LETTRES.execute()
        from src.business_objects.difficultes import Difficultes
        difficultes = Difficultes(nb_tentatives, temps, indice, nb_lettres)
        print(difficultes)
        from src.view.propositionview import PropositionView
        return PropositionView()

            
        
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from src.view.abstractview import AbstractView
from src.view.session import Session

from dao.liste_dao import ListeDAO
from dao.joueur_dao import JoueurDAO

class ListePersoView (AbstractView) :
    def __init__(self) -> None:
        self.__questions = inquirer.select(
            message=f'Vous choisissez une liste parmi tous vos listes suivantes :'
            , choices=[
                Choice(f'{liste}') for liste in get_liste_by_id_joueur(get_id_by_pseudo(Session().pseudo))
            ])
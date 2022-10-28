from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from src.view.abstractview import AbstractView
from src.view.session import Session



class ViewTopTenPerso(AbstractView):


    def display_info(self):
        print(f"Voici tes 10 meilleurs scores") 

    def make_choice(self):
        from src.dao.consultertoptenperso import ConsulterTopTenPerso
        consultertoptenperso()
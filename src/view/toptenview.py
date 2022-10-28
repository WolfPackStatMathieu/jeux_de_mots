from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from src.view.abstractview import AbstractView
from src.view.session import Session



class ViewTopTen(AbstractView):


    def display_info(self):
        print(f"Voici les 10 meilleurs scores") 

    def make_choice(self):
        from src.dao.consultertopten import ConsulterTopTen
        consultertopten()
            
        
        

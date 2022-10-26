from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from src.view.abstractview import AbstractView
from src.view.session import Session

ASK_PROPOSITION =inquirer.text(message = 'Quel mot veux tu proposer?')



class PropositionView(AbstractView) :
    
    def display_info(self):
        pass

    def make_choice(self):
        proposition = ASK_PROPOSITION.execute()
        
        print(proposition)



        
        
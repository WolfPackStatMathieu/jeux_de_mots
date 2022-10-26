from email.message import Message
from pprint import pprint


from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from view.abstract_view import AbstractView
from view.session import Session
from business_object.user import User



ASK_PSEUDO=inquirer.text(message = 'Quel pseudo veux-tu?')



class ConnexionView(AbstractView):


    def display_info(self):
        print(f"Connexion au compte")

    def make_choice(self):
        pseudo = ASK_PSEUDO.execute()
        user = User(pseudo = pseudo
        )
        print(user)
        Session().user_name = user.pseudo
        from view.start_view import StartView
        return StartView()

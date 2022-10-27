from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from src.view.abstractview import AbstractView
from src.view.session import Session

<<<<<<< HEAD
class JouerView (AbstractView) :
    def __init__(self):
        if 1 == 1 or partie_en_cours :

            self.__questions = inquirer.select(
                message=f'Bonjour {Session().pseudo}, que souhaites-tu faire?'
                , choices=[
                    Choice('Nouvelle partie')
                    ,Choice('Reprendre la partie')
                ]
        )
        else :
            from src.view.difficulteview import DifficulteView
            return DifficulteView()
=======

class JouerView (AbstractView) :

    def __init__(self):
        self.__questions = inquirer.select(
            message=f'Bonjour {Session().pseudo}'
            , choices=[
                Choice('Définir la difficulté de la partie')
                ,Choice('Voir proposition')]
        )
>>>>>>> 21fa9cb7166ab44bf13dc6260659f7845455ef07
    
    def display_info(self):
        pass

    def make_choice(self):
        reponse = self.__questions.execute()
<<<<<<< HEAD
        if reponse == 'Nouvelle partie':
            from src.view.difficulteview import DifficulteView
            return DifficulteView()
        elif reponse == 'Reprendre la partie':
            #partie = #Importer la partie
            mots_proposes = partie.liste_mots_proposes
            for mot in liste_mots_proposes :
                print(partie.verifie_proposition(mot))
            from scr.view.propositionview import PropositionView
            return PropositionView()
            
        
=======
        if reponse == 'Nothing':
            pass
        elif reponse== 'Définir la difficulté de la partie':
            from src.view.difficulteview import DifficulteView
            return DifficulteView()
        elif reponse== 'Voir proposition':
            from src.view.propositionview import PropositionView
            return PropositionView()
>>>>>>> 21fa9cb7166ab44bf13dc6260659f7845455ef07

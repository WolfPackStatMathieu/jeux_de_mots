from email.message import Message
from pprint import pprint


from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from src.view.abstractview import AbstractView
from src.view.session import Session




ASK_NOM_LISTE=inquirer.text(message = 'Quel est le nom de ta nouvelle liste?')
ASK_LIEN_dossier=inquirer.text(message = 'Quel est le lien du dossier où se trouve ta liste?')
ASK_LIEN_fichier=inquirer.text(message = 'Quel est le lien du fichier où se trouve ta liste?')

class ListeImporteeJSONView(AbstractView):


    def display_info(self):
        print(f"Création d'une liste JSON")

    def make_choice(self):
        nom_liste = ASK_NOM_LISTE.execute()
        lien_dossier = ASK_LIEN_dossier.execute()
        lien_fichier = ASK_LIEN_fichier.execute()

        from src.importation_objects.importationCsv import ImportationJson
        importation = ImportationJson()
        liste_mots = importation.creer(lien_fichier, lien_dossier)

        from src.dao.joueur_dao import JoueurDAO
        joueurdao = JoueurDAO()
        id_joueur = joueurdao.get_id_by_pseudo(Session().pseudo)
        
        from src.dao.liste_dao import ListeDAO
        listedao = ListeDAO()
        listedao.creer(id_joueur, nom_liste)
        id_liste = listedao.id(Session().liste)


        from src.dao.mot_dao import MotDAO
        motdao = MotDAO()
        from src.business_objects.proposition import Proposition
        for mot in liste_mots :
            #On transforme ensuite le mot pour supprimer les accents et mettre en majuscule
            mot = Proposition(mot)
            mot = Proposition.mot
        
        
            if not motdao.find(mot) :
                motdao.creer(mot)
            id_mot = motdao.get_id_by_mot(mot)
            listedao.ajouter_mot(self, id_liste, id_mot)

        from src.view.listeimporteejsonview import ListeImporteeJSONView
        return ListeImporteeJSONView()


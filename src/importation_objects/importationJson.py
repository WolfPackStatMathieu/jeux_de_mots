"""classe pour importer des listes de mot sous format .json
La structure du fichier est :
{"liste_mots": [
    {"mot": "mon_mot1},
    {"mot": "mon_mot2},
    {"mot": "mon_mot3},
]}

"""

import json
from src.importation_objects.abstract_importation_liste import AbstractImportationListe

class ImportationJson(AbstractImportationListe):
    """_summary_
    """
    def __init__(self,):
        """constructeur de ImportationJson
        """
        super.__init__(self)

    def creer(self, fichier : str, dossier, encodage)

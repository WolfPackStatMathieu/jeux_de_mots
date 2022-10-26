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

        Examples
        --------
        >>> import json
        >>> from src.importation_objects.abstract_importation_liste import AbstractImportationListe
        >>> ma_liste = ImportationJson()
        >>> isinstance(ma_liste, ImportationJson)
        True
        """
        super().__init__()


    def creer(self, fichier : str, dossier : str, encodage: str = ' utf-8'):
        """permet de créer une liste de mots à partir d'un fichier Json et après instanciation
        d'un objet ImportationJson.

        Parameters
        ----------
        fichier : str
            nom du fichier
        dossier : str
            chemin absolu du dossier où se trouve le fichier
        encodage : str
            encodage du fichier, par défaut UTF-8

        Returns
        -------
        liste_mots : list[str]

        Examples
        --------
        >>> import json
        >>> from src.importation_objects.abstract_importation_liste import AbstractImportationListe
        >>> ma_liste = ImportationJson()

        """

if __name__ == '__main__':
    import doctest
    doctest.testmod()

liste_exemple = {"mots":[
    {"mot": "Apolinne"},
    {"mot": "Linh-da"},
    {"mot": "Mathieu"},
    {"mot": "Mathis"},
    {"mot": "Oussama"},
]}
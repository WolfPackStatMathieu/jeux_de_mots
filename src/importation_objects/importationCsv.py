"""classe pour importer des fichiers CSV
structurés :
"Apolinne"
"Linh-Da"
"Mathieu"
"Mathis"
"Oussama"
"""

import csv
from src.importation_objects.abstract_importation_liste import AbstractImportationListe

class ImportationCsv(AbstractImportationListe):
    """permet d'importer des Csv (au format simpliste: pas de titre, mots mis ligne à ligne entre '"')

    Parameters
    ----------
    Example
    -------

    """

    def __init__(self):
        """_summary_

        Parameters
        ----------
        fichier : str
            nom du fichier avec l'extension .csv
        dossier : str
            chemin du dossier
        encodage : str, optional
            encodage du fichier, by default ' utf-8'

        Example
        -------
        >>> import json
        >>> from src.importation_objects.abstract_importation_liste import AbstractImportationListe
        >>> ma_liste = ImportationCsv()
        >>> isinstance(ma_liste, ImportationCsv)
        """
        super().__init__()

        def creer(self,  fichier : str, dossier : str, encodage: str = ' utf-8', separateur : str = ','):
            """retourne une liste de mos à partir d'un fichier CSV

            Parameters
            ----------
            fichier : str
                nom du fichier
            dossier : str
                nom du dossier
            encodage : str, optional
                encodage, by default ' utf-8'
            separateur : str, optional
                séparateur, by default ','

            Returns
            -------
            liste_mots : list[str]

            Examples
            --------
            >>> import csv
            >>> from src.importation_objects.abstract_importation_liste import AbstractImportationListe
            >>> ma_liste = ImportationCvs()
            """
            with open(f'{dossier}/{fichier}', newline='') as csvfile:

...     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
...     for row in spamreader:
...         print(', '.join(row))
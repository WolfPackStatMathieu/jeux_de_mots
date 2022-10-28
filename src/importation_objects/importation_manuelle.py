"""classe ImportationManuelle pour créer une liste personnalisée à la main
"""

from src.importation_objects.abstract_importation_liste import AbstractImportationListe
from src.business_objects.proposition import Proposition

class ImportationManuelle(AbstractImportationListe):
    """permet d'importer une liste manuellement
    """
    def __init__(self):
        """_summary_
        """
        pass

    def ajouter_mot(self, nouveau_mot):
        """permet d'ajouter un mot.

        Parameters
        ----------
        nouveau_mot : str
            le mot à ajouter

        Returns
        -------
        str
            le mot ajouté par l'utilisateur
        """
        #on réutilise la classe Proposition pour gérer les accents et minuscules
        mon_mot = Proposition(nouveau_mot)

        return mon_mot.mot



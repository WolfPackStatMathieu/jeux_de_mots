"""classe ImportationManuelle pour créer une liste personnalisée à la main
"""

from src.importation_objects.abstract_importation_liste import AbstractImportationListe

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
        return mot


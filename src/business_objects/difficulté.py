"""_summary_
"""
from numpy import Infinity


class Difficulte :
    """_summary_
    """
    def __init__(self,nb_lettres_indices : int ,langue : str = 'Anglais',
                longueur_mot : int = 6, temps_max = Infinity, nb_tentatives_max : int = 6 ) -> None:
        """_summary_

        Args:
            nb_lettres_indices (int): ici on met l'indice de la lettre qu'on veut savoir par rapport au mot objectif
            langue (str, optional): la langue est qui est généralement l'anglais
            longueur_mot (int, optional): la longueur du mot objectif. Defaults to 6.
            temps_max (_type_, optional): le temps maximal de la partie. Defaults to Infinity.
            nb_tentatives_max (int, optional): le nombre de tentatives maximals. Defaults to 6.
        """
        self.nb_lettres_indices = nb_lettres_indices
        self.langue = langue
        self.longueur_mot = longueur_mot
        self.temps_max = temps_max
        self.nb_tentatives_max = nb_tentatives_max
    
    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
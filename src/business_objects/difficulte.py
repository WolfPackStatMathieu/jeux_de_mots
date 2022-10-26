"""
Création de la classe Difficulte
"""
from numpy import Infinity

class Difficulte :
    """
    Cette classe sert à définir un niveau de difficulté en se basant sur les critères suivants :
         - l'indice d'une lettre du mot objectif dans le cas ou le joueur veut savoir une lettre pour faciliter la partie
         - la longueur de mot objectif
         - le temps maximal de la partie
         - le nombre de tentatives maximals
    """
    def __init__(self,nb_lettres_indices : int = 0,langue : str = 'Anglais',
                longueur_mot : int = 6, temps_max = Infinity, nb_tentatives_max : int = 6 ) -> None:
        """_summary_

        Args:
            nb_lettres_indices (int, optional): ici on met l'indice de la lettre qu'on veut savoir par rapport au mot objectif
            langue (str, optional): la langue est qui est généralement l'anglais
            longueur_mot (int, optional): la longueur du mot objectif. Defaults to 6.
            temps_max (_type_, optional): le temps maximal de la partie. Defaults to Infinity.
            nb_tentatives_max (int, optional): le nombre de tentatives maximals. Defaults to 6.
        EXAMPLE
        -------
        >>> difficulte1=Difficulte()
        >>> difficulte1.nb_lettres_indices
        0
        >>> difficulte1.langue
        'Anglais'
        >>> difficulte1.longueur_mot
        6
        >>> difficulte1.temps_max
        inf
        >>> difficulte1.nb_tentatives_max
        6
        """
        self.nb_lettres_indices = nb_lettres_indices
        self.langue = langue
        self.longueur_mot = longueur_mot
        self.temps_max = temps_max
        self.nb_tentatives_max = nb_tentatives_max
    
    def __str__(self) -> str:
        """_summary_

        Returns:
            str: l'affichage de l'indice de la lettre demandé par le joueur, la langue, la longueur de mot objectif, le temps maximal d'une partie et le nombre de tentatives maximals dans la partie
        EXAMPLE
        -------
        >>> difficulte1=Difficulte()
        >>> print(difficulte1)
        il n y a pas un indice de lettre demandé par le joueur
        la langue est fixée sur Anglais
        la longueur de mot est : 6 lettres
        le temps maximal de la partie est : inf
        le nombre de tentatives maximals est : 6 tentatives
        """
        affichage_lettres_indices = ""
        if self.nb_lettres_indices == 0 :
            affichage_lettres_indices = "il n y a pas un indice de lettre demandé par le joueur"
        else :
            affichage_lettres_indices = f"la lettre {self.nb_lettres_indices} du mot objectif est demandé par le joueur"
        return f"{affichage_lettres_indices}\nla langue est fixée sur {self.langue}\nla longueur de mot est : {self.longueur_mot} lettres\nle temps maximal de la partie est : {self.temps_max}\nle nombre de tentatives maximals est : {self.nb_tentatives_max} tentatives"

if __name__ == "__main__" :
    import doctest
    doctest.testmod()
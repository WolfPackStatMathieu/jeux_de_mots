"""
Création de la classe Joueur
"""
class Joueur :
    """c'est la classe Joueur définissant un joueur par son identifiant, 
    son nom et la liste des top ten
    """
    def __init__(self, id_joueur : int, nom_joueur : str, topten : list()) -> None:
        """_summary_

        Args:
            id_joueur (int): c'est l'identifiant du joueur
            nom_joueur (str): c'est le nom du joueur
            topten (list): c'est la liste des 10 meilleurs scores du joueur
        EXAMPLE
        -------
        >>> joueur1=Joueur(1,"oussama",[1])
        >>> joueur1.id_joueur
        1
   
        """
        self.id_joueur = id_joueur
        self.nom_joueur = nom_joueur
        self.topten = topten

    def __str__(self) -> str:
        """_summary_

        Returns:
            str: l'identifiant du joueur et le nom du joueur
        EXAMPLE
        -------
        >>> joueur1=Joueur(1,"oussama",[1])
        >>> print(joueur1)
        l'identifiant du joueur est 1
        le nom du joueur est oussama
        la liste des top ten est [1]
        """
        return f"l'identifiant du joueur est {self.id_joueur}\nle nom du joueur est {self.nom_joueur}\nla liste des top ten est {self.topten}"

if __name__ == "__main__" :
    import doctest
    doctest.testmod()

"""
Création de la classe Liste
"""
class Liste :
    """c'est la classe liste définissant un objet liste par un identifiant de la liste,le nom de la liste et la liste des mots
    """
    def __init__(self,id_liste : int, liste : list(str), nom : str) :
        """_summary_

        Args:
            id_liste (_type_): c'est l'identifiant de notre liste
            liste (_type_): c'est notre liste des mots
            nom (_type_): c'est le nom de notre liste
        
        EXAMPLE
        -------
        >>> liste1 = Liste(1,"liste_oussama",10)
        >>> liste1.id_liste
        1
        >>> liste1.nom_liste
        liste_oussama
        >>> liste1.id_joueur
        10
        """
        self.id_liste = id_liste
        self.liste = liste
        self.nom = nom

def __str__(self) : 
    """_summary_

    Returns:
        str: l'identifiant de la liste, le nom de la liste et la liste des mots
    EXAMPLE
    -------
    >>> liste1 = Liste(1,["jouer","tester"],"liste_oussama")
    print(liste1)
    l'identifiant de la liste est : 1
    le nom de la liste est : ["jouer","tester"]
    la liste des mots est : 
    """
    return f"l'identifiant de la liste est : {self.id_liste}\nle nom de la liste est : {self.nom}\nla liste des mots est : {self.liste}"

if __name__ == "__main__" :
    import doctest
    doctest.testmod()
    

    

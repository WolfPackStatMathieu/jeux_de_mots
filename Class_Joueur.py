class Joueur :
    def __init__(self, id_joueur : int, nom_joueur : str, topten : list(float)) -> None:
        self.id = id_joueur
        self.nom = nom_joueur
        self.topten = topten
    
    def __str__(self) -> str:
        return f"l'identifiant du joueur est {self.id} \n le nom du joueur est {self.nom} \n la liste des top ten est {self.topten}"
        

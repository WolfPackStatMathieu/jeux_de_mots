class Joueur :
    def __init__(self, id_joueur : int, nom_joueur : str, topten : list()) -> None:
        self.id = id_joueur
        self.nom = nom_joueur
        self.topten = topten
    
    def __str__(self) -> str:
        return f"l'identifiant du joueur est {self.id}\nle nom du joueur est {self.nom}\nla liste des top ten est {self.topten}"
        
j= Joueur(2,"oussama",[1,2,3])
print(j)
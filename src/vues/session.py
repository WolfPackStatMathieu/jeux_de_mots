from src.utils.singleton import Singleton


class Session(metaclass=Singleton):
    def __init__(self, id_joueur, pseudo, id_partie = None):
        """
        Définition des variables que l'on stocke en session

        Attributes
        ----------
        id_joueur : int
        Identifiant du joueur connecté

        pseudo : str
        Pseudo du joueur connecté

        id_partie : int
        Identifiant de la partie en cours du joueur connecté
        Si le joueur n'a pas de partie en cours, id_partie vaut None
        """
        self.id_joueur = id_joueur
        self.pseudo = pseudo
        self.id_partie = id_partie
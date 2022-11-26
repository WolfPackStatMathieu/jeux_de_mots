"""module DAO pour le joueur
"""
from src.utils.singleton import Singleton
from src.dao.db_connection import DBConnection

class JoueurDAO(metaclass=Singleton):
    """classe DAO pour interagir avec la BDD au niveau du joueur
    """
    def get_pseudo_by_id(self, id_joueur):
        # pylint: disable=no-self-use

        '''Méthode get_pseudo_by_id

        Permet de retourner le pseudo correspondant à un id_joueur

        Parameters
        ----------
        identifiant : int
            Identifiant du joueur

        Returns
        --------
        pseudo :
            Pseudo du joueur, None si le joueur n'est pas trouvé

        '''

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT pseudo FROM joueur WHERE id_joueur = %(id_joueur)s"
                , {"id_joueur": id_joueur}
            )

            res = cursor.fetchone()

            pseudo = res["pseudo"]

        return pseudo


    def creer(self, pseudo):
        # pylint: disable=no-self-use
        '''Méthode créer

        Permet de créer un joueur

        Parameters
        ----------
        id : int
            Identifiant du joueur

        pseudo :
            Pseudo saisi par le joueur

        '''

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                    "INSERT INTO joueur(pseudo)"
                    " VALUES (%(pseudo)s) RETURNING id_joueur, pseudo;"
                    ,{"pseudo": pseudo})

            cursor.execute("commit;")


    def get_id_by_pseudo(self, pseudo):
        # pylint: disable=no-self-use
        '''Méthode get_id_by_pseudo

        Permet de retourner le id_joueur correspondant à un pseudo

        Parameters
        ----------
        pseudo : str
            Pseudo du joueur

        Returns
        --------
        id_joueur : int
            id_joueur du joueur, None si le pseudo n'est pas trouvé

        '''

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT id_joueur FROM joueur WHERE pseudo = %(pseudo)s"
                , {"pseudo": pseudo}
            )
            res = cursor.fetchone()
            id_joueur=None
            if res :
                id_joueur = res['id_joueur']

        return id_joueur

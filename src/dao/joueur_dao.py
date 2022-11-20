"""module DAO pour le joueur
"""

from src.dao.db_connection import DBConnection

class JoueurDAO():
    """classe DAO pour interagir avec la BDD au niveau du joueur
    """
    def get_pseudo_by_id(self, identifiant):
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
                "SELECT pseudo FROM joueur WHERE id_joueur = %(identifiant)s"
                , {"id": identifiant}
            )

            res = cursor.fetchone()

            pseudo = res["pseudo"]

        return pseudo

# sans doute à supprimer car fait la même chose que
# get_id_by_pseudo (si None => pseudo n'existe pas)
    def pseudo_existe(self, pseudo):
        # pylint: disable=no-self-use
        '''Méthode vérifiant si un pseudo existe

        '''

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT id_joueur FROM joueur WHERE pseudo = %(pseudo)s"
                , {"pseudo": pseudo}
            )

            res = cursor.fetchone()

        if res :
            return True

        return False



    def create(self, pseudo):
        # pylint: disable=no-self-use
        '''Méthode create

        Permet de créer un joueur

        Parameters
        ----------
        id : int
            Identifiant du joueur

        pseudo :
            Pseudo saisi par le joueur

        Returns
        --------
        joueur :


        '''

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                    "INSERT INTO joueur(pseudo)"
                    " VALUES (%(pseudo)s) RETURNING id_joueur, pseudo;"
                    ,{"pseudo": pseudo})

                #res = cursor.fetchone()
            cursor.execute("commit;")
        #return res


    def get_all_joueurs(self):
        # pylint: disable=no-self-use
        """permet d'obtenir tous les joueurs de la BDD

        Returns
        -------
        list[list]
            la liste de tous les joueurs avec leur id
        """

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT * FROM joueur " )

            res = cursor.fetchall()

        return res

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

"""permet d'accéder aux propositions en BDD
"""
from src.utils.singleton import Singleton
from src.dao.db_connection import DBConnection

class PropositionDAO(metaclass=Singleton):
    """classe permettant d'accéder aux propositions en BDD
    """
    def get_by_id_partie(self,id_partie):
        # pylint: disable=no-self-use
        """permet d'accéder aux propositions faites durant une partie
        en fournissant l'identifiant de la partie

        Parameters
        ----------
        id_partie : int
            identifiant de la partie

        Returns
        -------
        list
            liste des mots proposés au cours de la partie
        """
        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT proposition FROM proposition"
                " WHERE id_partie = (%(id_partie)s) ;"
                , {"id_partie": id_partie}
            )
            res = cursor.fetchall()
            liste_propositions = []
            for row in res:
                liste_propositions.append(row["proposition"])

        return liste_propositions

    def creer(self, id_partie, proposition):
        # pylint: disable=no-self-use
        '''Méthode créer
        Permet d'ajouter une proposition

        Parameters
        ----------
        proposition : str
            Mot entré par le joueur


        '''

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "INSERT INTO proposition(id_partie,proposition)"
                " VALUES (%(id_partie)s, %(proposition)s) RETURNING id_proposition ;"
                ,{"id_partie" : id_partie, "proposition": proposition}
            )

            cursor.execute("commit;")

    def supprimer_all(self, id_partie):
        # pylint: disable=no-self-use
        '''Méthode supprimer_all

        Permet de supprimer toutes les propositions liées à une partie

        Parameters
        ----------

        id_partie : int
            Identifiant de la partie


        '''

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "DELETE FROM proposition"
                " WHERE id_partie = (%(id_partie)s) ;"
                , {"id_partie": id_partie}
            )
            cursor.execute("commit;")

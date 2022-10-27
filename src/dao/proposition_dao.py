from src.utils.singleton import Singleton
from src.dao.db_connection import DBConnection

class PropositionDAO():
    def get_by_id_partie(self,id_partie):
        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT proposition FROM proposition"
                " WHERE id_partie = (%(id_partie)s) ;"
                , {"id_partie": id_partie}
            )
            res = cursor.fetchall()
            liste = []
            for row in res:
                liste.append(row["proposition"])

        return liste

    def creer(self, id_partie, proposition):

        '''Méthode créer
        
        Permet d'ajouter une proposition 
        
        Parameters
        ----------
        proposition : str
            Mot entré par le joueur
        
        Returns
        --------


        '''

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "INSERT INTO proposition(id_partie,proposition)"
                " VALUES (%(id_partie)s, %(proposition)s) RETURNING id_proposition ;"
                ,{"id_partie" : id_partie, "proposition": proposition}
            )

            res = cursor.fetchone()
            cursor.execute("commit;")

    def supprimer_all(self, id_partie):

        '''Méthode supprimer_all
        
        Permet de supprimer toutes les propositions liées à une partie
        
        Parameters
        ----------
        
        id_partie : int
            Identifiant de la partie 
        
        
        Returns
        --------

        '''

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "DELETE FROM proposition"
                " WHERE id_partie = (%(id_partie)s) ;"
                , {"id_partie": id_partie}
            )
            cursor.execute("commit;")
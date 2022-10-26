from src.utils.singleton import Singleton
from src.dao.db_connection import DBConnection

class ListeDAO():

    def get_liste_by_id_joueur(self, id):

        '''Méthode get_liste_by_id_joueur
        
        Permet de retourner les listes associées à un id_joueur
        
        Parameters
        ----------
        id : int
            Identifiant du joueur
        
        Returns
        --------
        liste : list
            Liste des listes de mots du joueur

        '''

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT * FROM liste WHERE id_joueur = %(id)s"
                , {"id": id}
            )

            res = cursor.fetchall()

        return res

    def ajouter(self, id_joueur, nom_liste):

        '''Méthode ajouter
        
        Permet d'ajouter une nouvelle liste associée à un joueur
        
        Parameters
        ----------

        id_joueur : int
            Identifiant du joueur

        nom_liste : str
            Nom de la liste saisi par le joueur
        
        Returns
        --------
        liste : list
            Une liste vide

        '''

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "INSERT INTO liste(nom_liste, id_joueur)"
                " VALUES (%(nom_liste)s, id_joueur) RETURNING id_liste, mot;"
                , {"nom_liste": nom}
            )

            res = cursor.fetchone()
            cursor.execute("commit;")

        return res
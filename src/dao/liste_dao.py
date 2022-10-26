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

    def creer(self, id_joueur, nom_liste):

        '''Méthode créer
        
        Permet de créer une nouvelle liste associée à un joueur
        
        Parameters
        ----------

        id_joueur : int
            Identifiant du joueur

        nom_liste : str
            Nom de la liste saisi par le joueur
        
        Returns
        --------
        liste : dict
            Une liste vide

        '''

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "INSERT INTO liste(nom_liste, id_joueur)"
                " VALUES (%(nom_liste)s, %(id_joueur)s) RETURNING id_liste, id_joueur;"
                , {"nom_liste": nom_liste, "id_joueur" : id_joueur}
            )

            res = cursor.fetchone()
            cursor.execute("commit;")

        return res
    
    def ajouter_mot(self, id_liste, id_mot):

        '''Méthode ajouter_mot
        
        Permet d'ajouter un mot à une liste
        
        Parameters
        ----------
        id_mot : int
            Identifiant du mot
        
        id_liste : int
            Identifiant de la liste de mots 
        
        Returns
        --------
        liste : list

        '''

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "INSERT INTO passage_liste_mot(id_liste, id_mot)"
                " VALUES (%(id_liste)s, %(id_mot)s) ;"
                , {"id_liste": id_liste, "id_mot" : id_mot}
            )
            cursor.execute("commit;")

    

    def get_mots_by_id_liste(self, id):

        '''Méthode get_mots_by_id_liste
        
        Permet de retourner les mots associés à une liste
        
        Parameters
        ----------
        id : int
            Identifiant de la liste
        
        Returns
        --------
        liste : list
            Mots de la liste

        '''

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT mot FROM liste JOIN passage_liste_mot ON liste.id_liste = passage_liste_mot.id_liste"
                                     " JOIN mots on passage_liste_mot.id_mot = mots.id_mot"
                                     " WHERE liste.id_liste= %(id)s"
                , {"id": id}
            )

            res = cursor.fetchall()

        return res
from src.utils.singleton import Singleton
from src.dao.db_connection import DBConnection

class MotDAO():

    def creer(self, mot):

        '''Méthode créer
        
        Permet d'ajouter un mot 
        
        Parameters
        ----------
        mot : str
            Mot à créer
        
        Returns
        --------
        mot : str
            Le mot créé

        '''

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "INSERT INTO mots(mot)"
                " VALUES (%(mot)s) RETURNING id_mot, mot;"
                , {"mot": mot}
            )

            res = cursor.fetchone()
            cursor.execute("commit;")

        return res

    def supprimer(self, id_mot, id_liste):

        '''Méthode supprimer 
        
        Permet de supprimer un mot d'une liste (supprime le lien entre le mot et la liste dans la table passage_liste_mot)
        
        Parameters
        ----------
        id_mot : int
            Identifiant du mot à supprimer
        
        id_liste : int
            Identifiant de la liste à laquelle le mot appartient
        
        
        Returns
        --------

        '''

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "DELETE FROM passage_liste_mot"
                " WHERE id_mot = (%(id_mot)s) AND id_liste = (%(id_liste)s) ;"
                , {"id_mot": id_mot, "id_liste" : id_liste}
            )
            cursor.execute("commit;")

    def find(self, mot):

        '''Méthode find
        
        Permet de chercher un mot 
        
        Parameters
        ----------
        mot : str
            Mot à chercher
        
        Returns
        --------
         : bool
            True si le mot existe

        '''

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT id_mot"
                " FROM mots WHERE mot=(%(mot)s) ;"
                , {"mot": mot}
            )

            res = cursor.fetchone()
            
            trouve = None
            if res :
                trouve = True
            else :
                trouve = False
        return trouve
    

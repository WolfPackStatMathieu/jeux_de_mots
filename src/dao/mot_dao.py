from src.utils.singleton import Singleton
from src.dao.db_connection import DBConnection

class MotDAO():

    def get_id_by_mot(self, mot):

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT id_mot FROM mots WHERE mot = %(mot)s"
                , {"mot": mot}
            )

            res = cursor.fetchone()
            id_mot = res["id_mot"]

        return id_mot

 
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
    

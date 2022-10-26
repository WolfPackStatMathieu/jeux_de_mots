from src.utils.singleton import Singleton
from src.dao.db_connection import DBConnection

class MotDAO():

    def get_mots_by_id_liste(self, id):

        '''Méthode get_mots_by_id_liste
        
        Permet de retourner les mots associés à un id_liste
        
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

    

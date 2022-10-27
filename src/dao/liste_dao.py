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
                "SELECT nom_liste FROM liste WHERE id_joueur = %(id)s"
                , {"id": id}
            )

            res = cursor.fetchall()
            liste=[]
            for row in res:
                liste.append(row["nom_liste"])
        return liste


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

            cursor.execute("commit;")

    
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
            liste = []
            for row in res:
                liste.append(row["mot"])

        return liste

    def supprimer_mot(self, id_mot, id_liste):

        '''Méthode supprimer_mot
        
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


    def supprimer(self, id_liste):

        '''Méthode supprimer 
        
        Permet de supprimer une liste (supprime tous les liens dans la table de passage passage_liste_mot puis supprime la liste de la table liste)
        
        Parameters
        ----------

        id_liste : int
            Identifiant de la liste à supprimer
        
        
        Returns
        --------

        '''

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "DELETE FROM passage_liste_mot"
                " WHERE id_liste = (%(id_liste)s) ;"
                "DELETE FROM liste"
                " WHERE id_liste = (%(id_liste)s) ;"
                , {"id_liste" : id_liste})
            
            cursor.execute("commit;")


    def get_mots_by_nom_liste(self, nom_liste):

        '''Méthode get_mots_by_nom_liste
        
        Permet de retourner les mots associés à une liste
        
        Parameters
        ----------
        nom_liste : str
            Nom de la liste
        
        Returns
        --------
        liste : dict
            Mots de la liste

        '''

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT mot FROM liste JOIN passage_liste_mot ON liste.id_liste = passage_liste_mot.id_liste"
                                     " JOIN mots on passage_liste_mot.id_mot = mots.id_mot"
                                     " WHERE liste.nom_liste= %(nom_liste)s"
                , {"nom_liste": nom_liste}
            )

            res = cursor.fetchall()
            liste = []
            for row in res:
                liste.append(row["mot"])

        return liste

   
    
    def get_id_by_nom(self, nom_liste):

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT id_liste FROM liste WHERE nom_liste = %(nom_liste)s"
                , {"nom_liste": nom_liste}
            )

            res = cursor.fetchall()
            liste=[]
            for row in res:
                liste.append(row["id_liste"])
        return liste
    
    def get_nom_by_id(self, id_liste):

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT id_liste FROM liste WHERE nom_liste = %(id_liste)s"
                , {"id_liste": id_liste}
            )

            res = cursor.fetchall()
            liste=[]
            for row in res:
                liste.append(row["nom_liste"])
        return liste
<<<<<<< HEAD
=======

<<<<<<< HEAD
liste_dao=ListeDAO()
res = liste_dao.get_mots_by_id_liste(5)
print(res)
print(type(res))
print(type(res[0]))
=======
# liste_dao=ListeDAO()
# liste_dao.ajouter_mot(5,6)
>>>>>>> 270d6c632d218b17c3120ea3b9a233f5d0406009
>>>>>>> b40226daf4107b0f34ad7bfbd4e08b3b0653c38c

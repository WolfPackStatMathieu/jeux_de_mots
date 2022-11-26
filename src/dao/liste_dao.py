"""Module DAO pour les listes
"""
from src.utils.singleton import Singleton
from src.dao.db_connection import DBConnection

class ListeDAO(metaclass=Singleton):
    """classe pour accéder aux informations des listes en BDD
    """
    # pylint: disable=no-self-use
    def get_liste_by_id_joueur(self, id_joueur):

        '''Méthode get_liste_by_id_joueur

        Permet de retourner les listes associées à un id_joueur

        Parameters
        ----------
        id_joueur : int
            Identifiant du joueur

        Returns
        --------
        liste : list
            Liste des listes de mots du joueur

        '''

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT id_liste, nom_liste FROM liste WHERE id_joueur = %(id_joueur)s"
                , {"id_joueur": id_joueur}
            )

            res = cursor.fetchall()
            liste1=[]
            liste2=[]
            for row in res:
                liste1.append(row["nom_liste"])
                liste2.append(row["id_liste"])
        return ([liste1, liste2])


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


    def get_mots_by_id_liste(self, id_liste):

        '''Méthode get_mots_by_id_liste

        Permet de retourner les mots associés à une liste

        Parameters
        ----------
        id_liste : int
            Identifiant de la liste

        Returns
        --------
        liste : list
            Mots de la liste

        '''

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT mot FROM liste "
                    "JOIN passage_liste_mot ON liste.id_liste = passage_liste_mot.id_liste"
                    " JOIN mot on passage_liste_mot.id_mot = mot.id_mot"
                    " WHERE liste.id_liste= %(id_liste)s"
                , {"id_liste": id_liste}
            )

            res = cursor.fetchall()
            liste = []
            for row in res:
                liste.append(row["mot"])

        return liste

    def supprimer_mot(self, id_mot, id_liste):

        '''Méthode supprimer_mot

        Permet de supprimer un mot d'une liste (supprime le
        lien entre le mot et la liste dans la table passage_liste_mot)

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

        Permet de supprimer une liste (supprime tous
        les liens dans la table de passage passage_liste_mot
        puis supprime la liste de la table liste)

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


    def get_nom_by_id(self, id_liste):
        """permet d'obtenir le nom d'une liste en fournissant son identifiant

        Parameters
        ----------
        id_liste : int
            identifiant de la liste

        Returns
        -------
        str
            nom de la liste
        """
        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT nom_liste FROM liste WHERE id_liste = %(id_liste)s"
                , {"id_liste": id_liste}
            )

            res = cursor.fetchone()
            nom_liste = res['nom_liste']

        return nom_liste

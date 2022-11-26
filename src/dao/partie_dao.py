"""permet d'accéder aux parties en BDD
"""
from src.utils.singleton import Singleton
from src.dao.db_connection import DBConnection
from src.dao.proposition_dao import PropositionDAO

class PartieDAO(metaclass=Singleton):
    # pylint: disable=no-self-use
    """permet d'accéder aux partie en BDD
    """

    def creer(self, id_joueur, mot_objectif, nb_tentatives_max, indice, liste_perso, temps_max) :
        #pylint: disable=too-many-arguments

        '''Méthode créer

        Permet de créer une nouvelle partie liée à un joueur

        Parameters
        ----------

        id_joueur : int
            Identifiant du joueur
        Returns
        --------


        '''

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "INSERT INTO partie(id_joueur, "
                "mot_objectif, temps_max,"
                "nb_tentatives_max, indice, liste_perso)"
                " VALUES ("
                "%(id_joueur)s, "
                "%(mot_objectif)s,"
                "%(temps_max)s , "
                "%(nb_tentatives_max)s, "
                "%(indice)s, "
                "%(liste_perso)s); "
                ,{"id_joueur": id_joueur,
                "mot_objectif" : mot_objectif,
                "nb_tentatives_max" : nb_tentatives_max,
                "temps_max": temps_max,
                "indice" : indice,
                "liste_perso" : liste_perso}
            )
            cursor.execute("commit;")


    def supprimer(self, id_partie):

        '''Méthode supprimer

        Permet de supprimer une partie

        Parameters
        ----------
        id_partie : int
            Identifiant de la partie


        Returns
        --------

        '''
        #On supprime d'abord toutes les propositions liées à la partie de la table proposition
        PropositionDAO().supprimer_all(id_partie)
        #Puis on supprime la partie de la table partie
        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "DELETE FROM partie"
                " WHERE id_partie = (%(id_partie)s) ;"
                , {"id_partie": id_partie}
            )
            cursor.execute("commit;")

    def get_partie_by_id(self, id_partie):
        """permet d'obtenir une Partie en fournissant son identifiant

        Parameters
        ----------
        id_partie : int
            identifiant de la partie

        Returns
        -------
        list
            attributs d'une Partie
        """
        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT * FROM partie WHERE id_partie = %(id_partie)s"
                , {"id_partie": id_partie}
            )

            res = cursor.fetchall()
            liste=[]
            for row in res:
                liste.append(row["id_joueur"])
                liste.append(row["mot_objectif"])
                liste.append(row["nb_tentatives_max"])
                liste.append(row["indice"])
                liste.append(row["liste_perso"])
                liste.append(row["temps_max"])
        return liste


    def get_id_partie_en_cours_joueur(self,id_joueur):
        """permet d'obtenir l'identifiant de la partie en cours d'un joueur

        Parameters
        ----------
        id_joueur : int
            identifiant du joueur

        Returns
        -------
        id_partie : int
            identifiant de la partie du joueur
        """
        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT id_partie FROM partie JOIN joueur ON partie.id_joueur = joueur.id_joueur"
                                     " WHERE partie.id_joueur= %(id_joueur)s"
                , {"id_joueur": id_joueur}
            )
            res=cursor.fetchone()
            id_partie=None
            if res :
                id_partie = res['id_partie']

        return id_partie

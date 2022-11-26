"""module pour accéder aux scores en BDD
"""
from src.utils.singleton import Singleton
from src.dao.db_connection import DBConnection
from src.dao.joueur_dao import JoueurDAO
# pylint: disable=no-self-use
class ScoreDAO(metaclass=Singleton):
    """permet d'accéder aux scores en BDD
    """
    def ajouter(self, id_joueur, score):
        """permet d'ajouter un score attribué à un joueur en BDD
        si ce score fait partie du top 10 perso

        Parameters
        ----------
        id_joueur : int
            identifiant du joueur
        score : int
            score à ajouter
        """
        score=float(score)
        if len(ScoreDAO().get_top_10_perso(id_joueur)) == 10 :

            if score > ScoreDAO().get_dernier_meilleur_score(id_joueur)[0]:
                id_score_a_supprimer = ScoreDAO().get_dernier_meilleur_score(id_joueur)[1]
                ScoreDAO().supprimer(id_score_a_supprimer)

                connection = DBConnection().connection
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO score(id_joueur, score)"
                        " VALUES (%(id_joueur)s, %(score)s ) ;",
                        {"id_joueur": id_joueur, "score": score})
                    cursor.execute("commit;")
        else :
            connection = DBConnection().connection
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO score(id_joueur, score)"
                    " VALUES (%(id_joueur)s, %(score)s ) ;",
                    {"id_joueur": id_joueur, "score": score})
                cursor.execute("commit;")

    def supprimer(self, id_score):
        """permet de supprimer un score en BDD

        Parameters
        ----------
        id_score : int
            identifiant du score à supprimer
        """
        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "DELETE FROM score"
                " WHERE id_score = (%(id_score)s) ;"
                ,{"id_score": id_score})

            cursor.execute("commit;")

    def get_top_10_general(self):
        """permet d'obtenir les 10 meilleurs scores existants

        Returns
        -------
        list[list]
            liste de listes contenant le score, l'identifiant du joueur et son pseudo
        """
        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT *"
                " FROM score"
                " ORDER BY score DESC ;")

            res=cursor.fetchmany(10)
            liste_top_10=[]
            for row in res:
                liste=[]
                liste.append(row["score"])
                identifiant_joueur=row["id_joueur"]
                joueur_dao=JoueurDAO()
                pseudo=joueur_dao.get_pseudo_by_id(identifiant_joueur)
                liste.append(pseudo)
                liste_top_10.append(liste)
        return liste_top_10

    def get_top_10_perso(self, id_joueur):
        """permet d'obtenir le top10 des scores d'un joueur en particulier

        Parameters
        ----------
        id_joueur : int
            identifiant du joueur

        Returns
        -------
        list
            liste des 10 meilleurs scores du joueur
        """
        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT score"
                " FROM score"
                " WHERE id_joueur = (%(id_joueur)s)"
                " ORDER BY score DESC ;"
                ,{"id_joueur": id_joueur})

            res=cursor.fetchmany(10)
            top_10_perso=[]
            for row in res:
                top_10_perso.append(row["score"])
        return top_10_perso

    def get_dernier_meilleur_score(self, id_joueur):
        """permet d'obtenir le dernier meilleur score d'un joueur
        i.e. le 10ème meilleur score (ou le dernier du top10 perso)

        Parameters
        ----------
        id_joueur : int
            identifiant du joueur

        Returns
        -------
        tuple
            (score, id_score)
        """
        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT score, id_score FROM score "
                "WHERE id_joueur = (%(id_joueur)s) "
                "ORDER BY score ASC ;"
                , {"id_joueur": id_joueur})

            res = cursor.fetchmany(10)
            dernier_meilleur_score = res[0]
        return ([dernier_meilleur_score["score"], dernier_meilleur_score["id_score"]])

"""module DAO pour accéder aux mots en BDD
"""
import re #import regex
from src.utils.singleton import Singleton
from src.dao.db_connection import DBConnection

class MotDAO(metaclass=Singleton):
    # pylint: disable=no-self-use
    """permet d'accéder aux mots en BDD
    """
    def get_id_by_mot(self, mot):

        """permet d'obtenir l'identifiant d'un mot

        Parameters
        ----------
        mot : str
            le mot dont on veut l'identifiant

        Returns
        -------
        int
            l'identifiant du mot
        """
        id_mot = None

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT id_mot FROM mot WHERE mot = %(mot)s"
                , {"mot": mot}
            )
            id_mot=None
            res = cursor.fetchone()
        if res:
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

        regex = "^[A-zÀ-ú]+$"
        mot_a_tester = mot
        resultat = re.match(regex, mot_a_tester)

        if resultat is None :
            print("Ce mot n'est pas correct (caractères spéciaux et espaces non autorisés).")
            nouveau_mot = None

        else :

            connection = DBConnection().connection
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO mot(mot)"
                    " VALUES (%(mot)s) RETURNING id_mot, mot;"
                    , {"mot": mot}
                )
                res = cursor.fetchone()
                cursor.execute("commit;")

            if res :
                nouveau_mot = res

        return nouveau_mot

from src.utils.singleton import Singleton
from src.dao.db_connection import DBConnection

class JoueurDAO():
    ''
    def creer(joueur):
        connection = DBConnection().connection
        with connection.cursor() as cursor :
            curseur.execute(
                "INSERT INTO joueur(id_joueur, nom_joueur)"
                " VALUES (id_joueur, nom_joueur)",
                { "id_joueur" : joueur.id_joueur,
                "nom_joueur" : joueur.nom_joueur}
            )
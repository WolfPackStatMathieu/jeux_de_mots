from src.utils.singleton import Singleton
from src.dao.db_connection import DBConnection

class ScoreDAO():
    
    def creer(self, id_joueur):
        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                    "INSERT INTO score(id_joueur)"
                    " VALUES (%(id_joueur)s) RETURNING id_score ;"
                    ,{"id_joueur": id_joueur})

            res = cursor.fetchone()
            cursor.execute("commit;")
        return res
    
    def update(self, id_score, score):
        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                    "UPDATE score"
                    " SET score = (%(score)s)"
                    " WHERE id_score = (%(id_score)s);"
                    ,{"id_score": id_score, "score" : score})

            cursor.execute("commit;")
    
    def supprimer(self, id_score):
        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                    "DELETE FROM score"
                    " WHERE id_score = (%(id_score)s) ;"
                    ,{"id_score": id_score})

            cursor.execute("commit;")

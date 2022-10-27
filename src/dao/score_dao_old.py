from src.utils.singleton import Singleton
from src.dao.db_connection import DBConnection


class ScoreDAO_old():


        def creer(self, id_joueur, score):
                connection = DBConnection().connection
                with connection.cursor() as cursor:
                        cursor.execute(
                        "INSERT INTO score(id_joueur, score)"
                        " VALUES (%(id_joueur)s, %(score)s ) ;", {"id_joueur": id_joueur, "score": score})

                cursor.execute("commit;")

        def get_meilleur_score(self, id_joueur):
                connection = DBConnection().connection
                with connection.cursor() as cursor:
                        cursor.execute(
                        "SELECT * FROM score "
                        "ORDER BY score ASC "
                        "WHERE id_joueur = (%(id_joueur)s)"
                        "RETURNING score ;", {"id_joueur": id_joueur})
                res = cursor.fetchone()
                return res

        #def update(self, id_score, score):
                #connection = DBConnection().connection
                #with connection.cursor() as cursor :
                      #  cursor.execute(
                      #  "UPDATE score"
                       # " SET score = (%(score)s)"
                       # " WHERE id_score = (%(id_score)s);"
                       # ,{"id_score": id_score, "score" : score})

               # cursor.execute("commit;")

        def supprimer(self, id_score):
                connection = DBConnection().connection
                with connection.cursor() as cursor:
            cursor.execute(
                    "DELETE FROM score"
                    " WHERE id_score = (%(id_score)s) ;"
                    ,{"id_score": id_score})

            cursor.execute("commit;")
    
        def get_top_10(self):
                connection = DBConnection().connection
                with connection.cursor() as cursor :
                        cursor.execute(
                        "SELECT score"
                        " FROM score"
                        " ORDER BY score DESC ;")

                        res=cursor.fetchall()
        
                return res
        

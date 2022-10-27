from src.utils.singleton import Singleton
from src.dao.db_connection import DBConnection

class ScoreDAO():

    def creer(self, id_joueur, score):

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "INSERT INTO score(id_joueur, score)"
                " VALUES (%(id_joueur)s, %(score)s ) ;", {"id_joueur": id_joueur, "score": score})

            cursor.execute("commit;")

 
    def get_meilleur_score(self, id_joueur):

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT score FROM score "
                "WHERE id_joueur = (%(id_joueur)s) "
                "ORDER BY score ASC ;"
                , {"id_joueur": id_joueur})

            res = cursor.fetchone()
            meilleur_score = res["score"]

        return meilleur_score


    def supprimer(self, id_score):

        connection = DBConnection().connection
        with connection.cursor() as cursor :
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
                
            res=cursor.fetchmany(10)
            liste=[]
            for row in res:
                liste.append(row["score"])
        return liste

            

    

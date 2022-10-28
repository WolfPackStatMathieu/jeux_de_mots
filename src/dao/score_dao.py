from src.utils.singleton import Singleton
from src.dao.db_connection import DBConnection

class ScoreDAO():

    def ajouter(self, id_joueur, score):

        if score > ScoreDAO().get_dernier_meilleur_score(id_joueur)['score']:

            if len(ScoreDAO().get_top_10_perso(id_joueur)) >= 10 :

                id_score_a_supprimer = ScoreDAO().get_dernier_meilleur_score(id_joueur)['id_score']
                ScoreDAO().supprimer(id_score_a_supprimer)
                
                connection = DBConnection().connection
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO score(id_joueur, score)"
                        " VALUES (%(id_joueur)s, %(score)s ) ;", {"id_joueur": id_joueur, "score": score})
                    cursor.execute("commit;")
            else :
                connection = DBConnection().connection
                with connection.cursor() as cursor :
                    cursor.execute(
                        "INSERT INTO score(id_joueur, score)"
                        " VALUES (%(id_joueur)s, %(score)s ) ;", {"id_joueur": id_joueur, "score": score})
                    cursor.execute("commit;")
                        
        else :
            pass
       

    def supprimer(self, id_score):

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "DELETE FROM score"
                " WHERE id_score = (%(id_score)s) ;"
                ,{"id_score": id_score})

            cursor.execute("commit;")

    def get_top_10_general(self):

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
    
    def get_top_10_perso(self, id_joueur):

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

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT score, id_score FROM score "
                "WHERE id_joueur = (%(id_joueur)s) "
                "ORDER BY score ASC ;"
                , {"id_joueur": id_joueur})

            res = cursor.fetchmany(10)
            dernier_meilleur_score = res[0]
        
        return dernier_meilleur_score
    
    def get_all_perso(self, id_joueur):

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT score"
                " FROM score"
                " WHERE id_joueur = (%(id_joueur)s)"
                " ORDER BY score DESC ;"
                ,{"id_joueur": id_joueur})
                
            res=cursor.fetchall()
            liste=[]
            for row in res:
                liste.append(row["score"])
        return liste

    

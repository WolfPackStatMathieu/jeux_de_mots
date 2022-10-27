from src.utils.singleton import Singleton
from src.dao.db_connection import DBConnection

class ScoreDAO():

#à rajouter dans la fonction : on ajoute le score dans tous les cas si le joueur a moins de 10 scores 
#à rajouter dans la fonction : supprimer le dernier si après ajout le joueur a plus que 10 scores
    def ajouter(self, id_joueur, score):

        if score > ScoreDAO().get_dernier_meilleur_score(id_joueur):
            print('OK')

            connection = DBConnection().connection
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO score(id_joueur, score)"
                    " VALUES (%(id_joueur)s, %(score)s ) ;", {"id_joueur": id_joueur, "score": score})
                cursor.execute("commit;")
        
        else :
            print('rien')

 
    def get_dernier_meilleur_score(self, id_joueur):

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
            liste=[]
            for row in res:
                liste.append(row["score"])
        return liste


            


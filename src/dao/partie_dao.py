from src.utils.singleton import Singleton
from src.dao.db_connection import DBConnection
from src.dao.proposition_dao import PropositionDAO

class PartieDAO():
    
    
    def creer(self, id_joueur, nom_partie, score_final, mot_objectif, temps_max,
    nb_tentatives_max, indice, liste_perso, id_liste) :

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
                "INSERT INTO partie(id_joueur, nom_partie, score_final, mot_objectif, temps_max,"
                 "nb_tentatives_max, indice, liste_perso, id_liste)"
                " VALUES (%(id_joueur)s, %(nom_partie)s, %(score_final)s, %(mot_objectif)s,"
                          "%(temps_max)s , %(nb_tentatives_max)s, %(indice)s, %(liste_perso)s, %(id_liste)s) ;"
                ,{"id_joueur": id_joueur, "nom_partie" : nom_partie, "score_final" : score_final, "mot_objectif" : mot_objectif,
                "nb_tentatives_max" : nb_tentatives_max, "temps_max": temps_max, "indice" : indice, "liste_perso" : liste_perso, "id_liste" : id_liste}
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

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT * FROM partie WHERE id_partie = %(id_partie)s"
                , {"id_partie": id_partie}
            )

            res = cursor.fetchall()
            liste=[]
            for row in res:
                liste.append(row["score_final"])
                liste.append(row["nom_partie"])
                liste.append(row["id_joueur"])
                liste.append(row["mot_objectif"])
                liste.append(row["temps_max"])
                liste.append(row["nb_tentatives_max"])
                liste.append(row["indice"])
                liste.append(row["liste_perso"])
                liste.append(row["id_liste"])                        
        return liste


    def get_id_partie_en_cours_joueur(self,id_joueur):
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

    

# partie_dao=PartieDAO()
# id=partie_dao.get_id_partie_en_cours_joueur(5)
# print(partie_dao.get_partie_by_id(id))
# partie_dao.creer(2, "test", 0.0, "ESSAI", 8, 6, True, False, None)

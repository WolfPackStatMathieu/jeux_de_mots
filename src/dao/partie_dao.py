from src.utils.singleton import Singleton
from src.dao.db_connection import DBConnection
from src.dao.proposition_dao import PropositionDAO

class PartieDAO():
    
    
    def creer(self, id_joueur, nom_partie, score_final, mot_objectif, temps_max, langue, 
    nb_tentatives_max, indice, liste_perso) :

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
                "INSERT INTO partie(id_joueur, nom_partie, score_final, mot_objectif, temps_max, langue,"
                 "nb_tentatives_max, indice, liste_perso)"
                " VALUES (%(id_joueur)s, %(nom_partie)s, %(score_final)s, %(mot_objectif)s,"
                          "%(temps_max)s , %(langue)s, %(nb_tentatives_max)s, %(indice)s, %(liste_perso)s) ;"
                ,{"id_joueur": id_joueur, "nom_partie" : nom_partie, "score_final" : score_final, "mot_objectif" : mot_objectif,
                "nb_tentatives_max" : nb_tentatives_max, "temps_max": temps_max, "langue" : langue, "indice" : indice, "liste_perso" : liste_perso}
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
    
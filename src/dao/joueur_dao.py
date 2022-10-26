from src.utils.singleton import Singleton
from src.dao.db_connection import DBConnection

class JoueurDAO():
    ''

    def get_pseudo_by_id(self, id):

        '''Méthode get_pseudo_by_id
        
        Permet de retourner le pseudo correspondant à un id_joueur
        
        Parameters
        ----------
        id : int
            Identifiant du joueur
        
        Returns
        --------
        pseudo : 
            Pseudo du joueur, None si le joueur n'est pas trouvé

        '''

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT pseudo FROM joueur WHERE id_joueur = %(id)s"
                , {"id": id}
            )

            res = cursor.fetchone()

        pseudo = None 

        if res :
            pseudo = res

        return pseudo

    def create(self, pseudo):

        '''Méthode create
        
        Permet de créer un joueur
        
        Parameters
        ----------
        id : int
            Identifiant du joueur
        
        pseudo : 
            Pseudo saisi par le joueur

        Returns
        --------
        joueur : 
            

        '''

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "INSERT INTO joueur(pseudo)"
                " VALUES (%(pseudo)s) RETURNING id_joueur"
                ,{"pseudo": pseudo}
            )
            res = cursor.fetchone()

        print(res)

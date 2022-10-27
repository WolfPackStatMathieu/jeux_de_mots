from src.utils.singleton import Singleton
from src.dao.db_connection import DBConnection

class JoueurDAO():

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

# sans doute à supprimer car fait la même chose que get_id_by_pseudo (si None => pseudo n'existe pas)
    def pseudo_existe(self, pseudo):

        '''Méthode vérifiant si un pseudo existe

        '''

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT id_joueur FROM joueur WHERE pseudo = %(pseudo)s"
                , {"pseudo": pseudo}
            )

            res = cursor.fetchone()

        if res :
            return True
        else : 
            return False



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
        if JoueurDAO().pseudo_existe(pseudo) == True :
            print('Ce pseudo est déjà utilisé.')
        
        if JoueurDAO().pseudo_existe(pseudo) == False :

            connection = DBConnection().connection
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO joueur(pseudo)"
                    " VALUES (%(pseudo)s) RETURNING id_joueur, pseudo;"
                    ,{"pseudo": pseudo})

                res = cursor.fetchone()
                cursor.execute("commit;")
            return res

   
    def get_all_joueurs(self):


        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT * FROM joueur " )

            res = cursor.fetchall()

        return res

    def get_id_by_pseudo(self, pseudo):

        '''Méthode get_id_by_pseudo
        
        Permet de retourner le id_joueur correspondant à un pseudo
        
        Parameters
        ----------
        pseudo : str
            Pseudo du joueur
        
        Returns
        --------
        id_joueur : int
            id_joueur du joueur, None si le pseudo n'est pas trouvé

        '''

        connection = DBConnection().connection
        with connection.cursor() as cursor :
            cursor.execute(
                "SELECT id_joueur FROM joueur WHERE pseudo = %(pseudo)s"
                , {"pseudo": pseudo}
            )

            res = cursor.fetchone()

        id_joueur = None 

        if res :
            id_joueur = res

        return id_joueur
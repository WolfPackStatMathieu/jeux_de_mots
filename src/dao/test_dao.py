from src.utils.singleton import Singleton
from src.dao.db_connection import DBConnection
from src.dao.joueur_dao import JoueurDAO
from src.dao.liste_dao import ListeDAO
from src.dao.mot_dao import MotDAO



#print(JoueurDAO().get_pseudo_by_id(4))
#print(JoueurDAO().get_pseudo_by_id(16))

#a=JoueurDAO().pseudo_existe('Linh-Da')
#print(a)
#b=JoueurDAO().pseudo_existe('blabla')
#print(b)

#JoueurDAO().create('Linh-Da')
#JoueurDAO().create('Tota')
#c=JoueurDAO().pseudo_existe('Toto')
#print(c)


#print(ListeDAO().get_liste_by_id_joueur(1))
#print(ListeDAO().get_liste_by_id_joueur(3))

#print(MotDAO().get_mots_by_id_liste(1))
#print(MotDAO().get_mots_by_id_liste(2))

#MotDAO().ajouter('voiture')

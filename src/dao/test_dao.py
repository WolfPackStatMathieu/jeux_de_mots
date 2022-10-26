from src.utils.singleton import Singleton
from src.dao.db_connection import DBConnection
from src.dao.joueur_dao import JoueurDAO
from src.dao.liste_dao import ListeDAO
from src.dao.mot_dao import MotDAO
from src.dao.proposition_dao import PropositionDAO

PropositionDAO().supprimer_all(1)
PropositionDAO().creer(1, 'radydelipe')
#ListeDAO().creer(5, 'nouvelle liste')
#print(ListeDAO().get_mots_by_nom_liste('nouvelle liste'))

#ListeDAO().ajouter(3, "ma liste")
#print(ListeDAO().get_liste(1))


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



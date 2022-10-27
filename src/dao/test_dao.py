from src.utils.singleton import Singleton
from src.dao.db_connection import DBConnection
from src.dao.joueur_dao import JoueurDAO
from src.dao.liste_dao import ListeDAO
from src.dao.mot_dao import MotDAO
from src.dao.proposition_dao import PropositionDAO
from src.dao.partie_dao import PartieDAO
from src.dao.score_dao import ScoreDAO

#print(ScoreDAO().get_top_10_perso(5))
print(ScoreDAO().get_meilleur_score(5))
from unittest import TestCase
from src.business_objects.generer_mot_liste_perso import GenererMotListePerso
from src.dao.liste_dao import ListeDAO

class TestGenererMotListePerso(TestCase) :
    def test_generer_mot(self) :
        id_liste = 1

        liste = ListeDAO()

        objetTest = GenererMotListePerso(id_liste)
        
        self.assertEqual("toto", objetTest.generer())
    
if __name__ == "__main__" :
    test=TestGenererMotListePerso()
    print(test.test_generer_mot())
    

from unittest import TestCase
from src.business_objects.generer_mot_liste_perso import GenererMotListePerso
from src.dao.liste_dao import ListeDAO

class TestGenererMotListePerso(TestCase) :
    def test_generer_mot(self) :
        id_liste = 2

        objetTest = GenererMotListePerso(id_liste)
        liste = ListeDAO()
        
        self.assertIn(objetTest.generer, ['titi', 'voiture', 'chocolat', 'Gateau', 'CHAISE', 'TABLE', 'STYLO'])
    
if __name__ == "__main__" :
    test=TestGenererMotListePerso()
    print(test.test_generer_mot())
    

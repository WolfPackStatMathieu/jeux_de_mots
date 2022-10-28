from unittest import TestCase
from src.business_objects.liste import Liste

class TestListe(TestCase) :
    def test__init__liste(self) :
        id_liste = 10
        liste = ["jouer","tester"]
        nom = "liste_oussama"

        liste1 = Liste(id_liste, liste, nom)

        self.assertEqual(10, liste1.id_liste)
        self.assertEqual(["jouer","tester"], liste1.liste)
        self.assertEqual("liste_oussama", liste1.nom)
        self.assertEqual("l'identifiant de la liste est : 10\nle nom de la liste est : liste_oussama\nla liste des mots est : ['jouer', 'tester']", liste1.__str__())
    
if __name__ == "__main__" :
    test1 = TestListe().test__init__liste()
    print(test1)
    
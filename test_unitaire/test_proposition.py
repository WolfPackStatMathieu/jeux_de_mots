from unittest import TestCase
from src.business_objects.proposition import Proposition

class TestProposition(TestCase) :
    def test_est_autorise(self) :
        mot1 = "uhujhbj"
        mot2 = "Sky"

        prop1 = Proposition(mot1)
        prop2 = Proposition(mot2)

        self.assertEqual(False, prop1.est_autorise())
        self.assertEqual(True, prop2.est_autorise())
    
    def test_majuscule(self) :
        mot = "hEllO WorLD"

        prop = Proposition(mot)

        self.assertEqual("HELLO WORLD", prop.majuscule())
    
    def test_supprime_accent(self) :
        mot = "éàlîêmc"

        prop = Proposition(mot)

        self.assertEqual("ealiemc", prop.supprime_accent())
    
    def test_transforme_proposition(self) :
        mot = "EyêLmîkà"

        prop = Proposition(mot)
        prop.transforme_proposition()

        self.assertEqual("EYELMIKA", prop.mot)


if __name__ == "__main__" :
    test = TestProposition()

    print("test est_autorise()")
    print(test.test_est_autorise())

    print("test majuscule()")
    print(test.test_majuscule())

    print("test supprime_accent()")
    print(test.test_supprime_accent())

    print("test transforme_proposition()")
    print(test.test_transforme_proposition()) 
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


if __name__ == "__main__" :
    print("test est_autorise()")
    test = TestProposition()
    print(test.test_est_autorise())

if __name__ == "__main__" :
    print("test majuscule()")
    test = TestProposition()
    print(test.test_majuscule())

if __name__ == "__main__" :
    print("test supprime_accent()")
    test = TestProposition()
    print(test.test_supprime_accent())

    
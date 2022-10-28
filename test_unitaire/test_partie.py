from unittest import TestCase
from src.business_objects.partie import Partie
from src.business_objects.proposition import Proposition
from src.business_objects.difficultes import Difficultes

#class TestPartie(TestCase) :
    #def test_donne_mot_obj(self) :
        #id_partie = 1
        #liste_mots_proposes = []
        #est_liste_perso = True
        #id_liste = 4
        #difficultes = Difficultes()

        #partie1 = Partie(id_partie, liste_mots_proposes, est_liste_perso, id_liste, difficultes)
    
    def test_occurence_lettres(self) :
        id_partie = 1
        liste_mots_proposes = []
        est_liste_perso = True
        id_liste = 4
        difficultes = Difficultes()

        partie1 = Partie(id_partie, liste_mots_proposes, est_liste_perso, id_liste, difficultes)
        """
        ici on sait que la liste perso d'identifiant n°4 est la suivante : ['VOITURE', 'BATEAU', 'ANIMAL']
        et alors on sait que le mot objectif dans ce cas est l'un des mots de cette liste, et par la suite
        on attend que le résultat de la méthode << occurence_lettres() >> est l'une des listes suivantes :
          - [['A', 2],['N', 1],['I',1],['M',1],['L',1]]
          - [['B',1],['A',2],['T',1],['E',1],['U',1]]
          - [['V',1],['O',1],['I',1],['T',1],['U',1],['R',1],['E',1]]
        ainsi on ajoute ces liste dans une variable << container >>
        et on teste si le résultat de la méthode << occurence_lettres() >> est l'un des élèment du << container >>

        """
        container = [[['A', 2],['N', 1],['I',1],['M',1],['L',1]], [['B',1],['A',2],['T',1],['E',1],['U',1]],[['V',1],['O',1],['I',1],['T',1],['U',1],['R',1],['E',1]]]
        self.assertIn(partie1.occurence_lettres(), container)


if __name__ == "__main__" :
    test = TestPartie()
    print(test.test_occurence_lettres())
from compileall import compile_dir

from src.business_objects.proposition import Proposition
from src.business_objects.code_lettre import CodeLettre
from src.business_objects.proposition_verifiee import PropositionVerifiee
from src.business_objects.difficultes import Difficultes
from src.business_objects.generer_mot_api import GenererMotApi
from src.business_objects.generer_mot_liste_perso import GenererMotListePerso

class Partie :
    '''Classe implémentant une partie

    attributes
    ----------
    id_partie : int
    mot_objectif : str
    liste_mots_proposes : list(Proposition)
    est_liste_perso : bool
    id_liste : int
    difficultes : Difficultes
    score : float
    '''
    def __init__(self, id_partie, liste_mots_proposes, est_liste_perso, id_liste, difficultes):
        self.id_partie=id_partie
        self.liste_mots_proposes=liste_mots_proposes
        self.est_liste_perso=est_liste_perso
        self.id_liste=id_liste
        self.difficultes=difficultes
        self.score=0
        self.mot_objectif=self.donne_mot_obj()


    def donne_mot_obj(self):
        '''donne le mot objectif de la partie, soit par l'api random-word-api, soit un mot dans la liste perso
        return
        ------
        le mot objectif  : str
        '''
        if self.est_liste_perso==True:
            generer=GenererMotListePerso(self.id_liste)
        else : 
            generer=GenererMotApi(self.difficultes.nb_lettres)
        return(generer.generer())


    def occurence_lettres(self):
        '''retourne une liste avec pour chaque lettre apparaissant dans le mot objectif, l'occurence de cette lettre dans le mot objectif
        '''
        lettres=[]
        for lettre in self.mot_objectif:
            if lettre not in lettres:
                lettres.append(lettre)
        print(lettres)
        L=[[]*i for i in range(len(lettres))]
        for i in range(len(lettres)):
            L[i].append(lettres[i])
            L[i].append(0)
            for lettre in self.mot_objectif:
                if lettre==lettres[i]:
                    L[i][1]+=1
        return(L)


    def lettres_bien_placées(self, mot_propose):
        '''retourne une liste avec chaque lettre du mot_propose et True si la lettre est bien placee et False sinon
        '''
        L=[]
        for i in range(len(mot_propose.mot)):
            if mot_propose.mot[i]==self.mot_objectif[i]:
                L.append([mot_propose.mot[i], True])
            else: 
                L.append([mot_propose.mot[i], False])
        return L


    def lettres_mal_placées(self, mot_propose):
        '''retourne une liste avec chaque lettre du mot propose, True si la lettre est bien placée, 'Mal placée' si mal placée et False si la lettre n'est pas dans le mot objectif
        '''
        bien_placées=self.lettres_bien_placées(mot_propose)
        occurence=self.occurence_lettres()
        print(occurence)
        for i in range(len(mot_propose.mot)):
            lettre=bien_placées[i][0]
            if bien_placées[i][1]==True:
                for elm in occurence:
                    if elm[0]==lettre:
                        elm[1]-=1
            if bien_placées[i][1]==False:
                for elm in occurence:
                    if elm[0]==lettre:
                        if elm[1]!=0:
                            bien_placées[i][1]="Mal placee"
                            elm[1]-=1
        return(bien_placées)

    def verifie_proposition(self, mot_propose):
        '''Vérifie une proposition
        return
        ------
        La proposition vérifiée (PropositionVerifiee)
        '''
        verification=self.lettres_mal_placées(mot_propose)
        liste_lettres=[]
        for elt in verification:
            lettre=CodeLettre(elt[0],elt[1])
            liste_lettres.append(lettre)
        return(PropositionVerifiee(liste_lettres))

    def calcul_score(self):
        '''calcul le score selon les paramètres de difficulté de la partie
        '''
        coeff_tentatives_max = 1 + 0.1 * (6 - self.difficultes.nb_tentatives)
        coeff_longueur = 1 + 0.1 *(self.difficultes.nb_lettres - 6)
        coeff_limite_temps = (self.difficultes.temps - 8) / 8
        self.score=100 + coeff_tentatives_max * coeff_tentatives_max * coeff_longueur * coeff_limite_temps



# difficultes=Difficultes(6,8,True,10)
# partie=Partie(1, [], False, None, difficultes)
# print(partie.mot_objectif)
# proposition=Proposition("ABCDEFGHIJ")
# print(partie.verifie_proposition(proposition))


# difficultes=Difficultes(6,8,True,None)
# partie=Partie(1, [], True,1 , difficultes)
# print(partie.mot_objectif)
# print("Faites une proposition : ")
# proposition=Proposition(input())
# print(partie.verifie_proposition(proposition))
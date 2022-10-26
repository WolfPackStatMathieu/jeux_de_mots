from compileall import compile_dir

from src.business_objects.proposition import Proposition
from src.business_objects.code_lettre import CodeLettre
from src.business_objects.proposition_verifiee import PropositionVerifiee
from src.business_objects.difficultes import Difficultes
from src.business_objects.generer_mot_api import GenererMotApi
from src.business_objects.generer_mot_liste_perso import GenererMotListePerso

class Partie :
    '''
    '''
    def __init__(self, id_partie, mot_objectif, liste_mots_proposes, est_liste_perso, id_liste, difficultes,score):
        self.id_partie=id_partie
        self.mot_objectif=mot_objectif
        self.liste_mots_proposes=liste_mots_proposes
        self.est_liste_perso=est_liste_perso
        self.id_liste=id_liste
        self.difficultes=difficultes
        self.score=score


    def donne_mot_obj(self):
        if self.est_liste_perso:
            generer=GenererMotListePerso(self.id_liste)
        else : 
            generer=GenererMotApi(self.difficultes.nb_lettres)
        self.mot_objectif=generer.generer()



    def occurence_lettres(self):
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
        L=[]
        for i in range(len(mot_propose.mot)):
            if mot_propose.mot[i]==self.mot_objectif[i]:
                L.append([mot_propose.mot[i], True])
            else: 
                L.append([mot_propose.mot[i], False])
        return L


    def lettres_mal_placées(self, mot_propose):
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
        verification=self.lettres_mal_placées(mot_propose)
        liste_lettres=[]
        for elt in verification:
            lettre=CodeLettre(elt[0],elt[1])
            liste_lettres.append(lettre)
        return(PropositionVerifiee(liste_lettres))

    def calcul_score(self):
        coeff_tentatives_max = 1 + 0.1 * (6 - self.difficultes.nb_tentatives)
        coeff_longueur = 1 + 0.1 *(self.difficultes.nb_lettres - 6)
        coeff_limite_temps = (self.difficultes.temps - 8) / 8
        self.score=100 + coeff_tentatives_max * coeff_tentatives_max * coeff_longueur * coeff_limite_temps



difficultes=Difficultes(6,8,True,6)
partie1=Partie(1,"HELLO",[], None, None, difficultes, None)
partie1.calcul_score()
print(partie1.score)
proposition=Proposition("école")

# bien_placées=partie1.lettres_mal_placées(proposition)
# print(bien_placées)

print(partie1.verifie_proposition(proposition))


partie2=Partie(1,None,[], None, None, difficultes, None)
partie2.donne_mot_obj()
print(partie2.mot_objectif)
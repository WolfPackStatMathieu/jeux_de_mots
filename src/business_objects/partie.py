from compileall import compile_dir

from src.business_objects.proposition import Proposition
from src.business_objects.code_lettre import CodeLettre
from src.business_objects.proposition_verifiee import PropositionVerifiee

class Partie :
    '''
    '''
    def __init__(self, id_partie, mot_objectif, liste_mots_proposes, est_liste_perso, id_liste, score):
        self.id_partie=id_partie
        self.mot_objectif=mot_objectif
        self.liste_mots_proposes=liste_mots_proposes
        self.est_liste_perso=est_liste_perso
        self.id_liste=id_liste
        self.score=score


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




partie1=Partie(1,"HELLO",[], None, None, None)

proposition=Proposition("école")

# bien_placées=partie1.lettres_mal_placées(proposition)
# print(bien_placées)

print(partie1.verifie_proposition(proposition))

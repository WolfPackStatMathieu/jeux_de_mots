from compileall import compile_dir


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





    def majuscule(self, chaine):
        '''Remplace les minuscules en majuscules d'une chaîne de caractères
        
        parameters : str 

        return : str 
        La chaîne en majuscule
        '''
        s=''
        if chaine==None:
            return(None)
        else:
            for caractere in chaine:
                s+=caractere.upper()
            return(s)

    def supprime_accent(self,chaine):
        '''Supprime les accents d'une chaîne de caracteres
        
        parameters : str 

        return : str 
        La chaîne sans les accents
        '''
        s=""
        if chaine==None:
            return(None)
        else : 
            copie=''
            for caractere in chaine:
                copie+=caractere.lower()
            for caractere in copie:
                if caractere=='é':
                    s+='e'
                elif caractere=='è':
                    s+='e'
                elif caractere=='à':
                    s+='a'
                elif caractere=='ù':
                    s+='u'
                elif caractere=='î':
                    s+='i'
                elif caractere=='ï':
                    s+='i'
                elif caractere=='ç':
                    s+='c'
                elif caractere=='â':
                    s+='a'
                elif caractere=='ô':
                    s+='o'
                elif caractere=='ê':
                    s+='e'
                else:
                    s+=caractere
            return(s)

    def transforme_proposition(self, mot_propose):
        mot_propose=self.supprime_accent(mot_propose)
        mot_propose=self.majuscule(mot_propose)
        return(mot_propose)

    def nombre_occurences(self, lettre):
        compteur=0
        for caractere in self.mot_objectif:
            if caractere==lettre:
                compteur+=1


    def lettres_bien_placées(self, mot_propose):
        L=[]
        for i in range(len(mot_propose)):
            if mot_propose[i]==self.mot_objectif[i]:
                L[i].append([mot_propose[i], True])
            else: 
                L[i].append([mot_propose[i], False])
        return L

    # def lettres_mal_placées(self, mot_propose):
    #     L=[]
    #     for caractere in mot_propose:
            



partie1=Partie(1,"HELLO",[], None, None, None)
mot='école'
modif=partie1.supprime_accent(mot)
modif2=partie1.majuscule(modif)
modif3=partie1.transforme_proposition(mot)
print(modif3)
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

    # def transforme_proposition(mot_propose):
    #     for caractere in mot_propose:
    #         if 
    
    # def verifier_mot(mot_propose):
    #     for caractere in mot_propose:



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



partie1=Partie(1,"HELLO",[], None, None, None)
mot='école'
modif=partie1.majuscule(mot)
print(modif)
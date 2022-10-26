from src.business_objects.code_lettre import CodeLettre

class PropositionVerifiee :
    '''Classe implémentant une proposition vérifiée 

    attributes
    ----------
    liste_lettres : list(CodeLettre)
    '''
    def __init__(self, liste_lettres):
        self.liste_lettres=liste_lettres

    def __str__(self):
        '''affiche la proposition vérifiée avec des couleurs pour chaque lettres : 
        vert si la lettre est bien placée
        rouge si la lettre est présente mais mal placée
        noir si la lettre ne fait pas partie du mot objectif
        '''
        affichage_prop=self.liste_lettres[0].affichage
        for i in range(1,len(self.liste_lettres)):
            affichage_prop+= self.liste_lettres[i].affichage
        return(affichage_prop)


# liste_lettres=[CodeLettre('E', 'Mal placee'),CodeLettre('C', False),CodeLettre('O', 'Mal placee'),CodeLettre('L', True),CodeLettre('E', False)]
# prop_verif=PropositionVerifiee(liste_lettres)
# print(prop_verif)

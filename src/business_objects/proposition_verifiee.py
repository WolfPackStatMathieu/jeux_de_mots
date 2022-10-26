from src.business_objects.code_lettre import CodeLettre

class PropositionVerifiee :
    def __init__(self, liste_lettre):
        self.liste_lettres=liste_lettres

    def __str__(self):
        affichage_prop=self.liste_lettres[0].affichage
        for i in range(1,len(self.liste_lettres)):
            affichage_prop+= self.liste_lettres[i].affichage
        return(affichage_prop)


liste_lettres=[CodeLettre('E', 'Mal placee'),CodeLettre('C', False),CodeLettre('O', 'Mal placee'),CodeLettre('L', True),CodeLettre('E', False)]
prop_verif=PropositionVerifiee(liste_lettres)
print(prop_verif)

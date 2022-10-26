from colorama import *
init()
class CodeLettre :
    def __init__(self,lettre, code_couleur):
        self.lettre=lettre
        self.code_couleur=code_couleur
        self.affichage=self.afficher()

    def afficher(self):
        if self.code_couleur==True:
            couleur='\x1b[1;37;42m'
        if self.code_couleur==False:
            couleur='\x1b[1;37;40m'
        if self.code_couleur=='Mal placee':
            couleur='\x1b[1;37;41m' 
        return(couleur + ' ' + self.lettre + ' ' +'\x1b[0m')

    # def __str__(self):
    #     if self.code_couleur==True:
    #         return('\x1b[1;37;42m' + ' ' + self.lettre + ' ' +'\x1b[0m')
    #     if self.code_couleur==False:
    #         return('\x1b[1;37;41m' + ' ' + self.lettre+ ' ' +'\x1b[0m')
    #     if self.code_couleur=='Mal placee':
    #         return('\x1b[1;37;40m' + ' ' + self.lettre+ ' ' +'\x1b[0m')
    


# lettre1=CodeLettre('A',True)
# print(lettre1)

# lettre2=CodeLettre('A',False)
# print(lettre2)

# lettre3=CodeLettre('A','Mal placee')
# print(lettre3)


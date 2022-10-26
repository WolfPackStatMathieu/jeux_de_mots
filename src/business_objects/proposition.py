import requests as requests
class Proposition :
    '''Classe implémentant une proposition de mot (faite par le joueur)

    attributes
    ---------
    mot : str
    '''
    def __init__(self, mot):
        self.mot=mot
        self.transforme_proposition()

    def est_autorise(self):
        '''Vérifie si la proposition existe dans le dictionnaire par l'intermédiaire de l'API dictionaryapi
        return : bool
        True si le mot existe
        False sinon
        '''
        req=requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(self.mot)) 
        res=req.json()
        if type(res)==dict:
            return False
        return True


    def majuscule(self):
        '''Remplace les minuscules en majuscules d'une chaîne de caractères
        
        parameters : str 

        return : str 
        La chaîne en majuscule
        '''
        s=''
        if self.mot==None:
            return(None)
        else:
            for caractere in self.mot:
                s+=caractere.upper()
            return(s)

    
    def supprime_accent(self):
        '''Supprime les accents d'une chaîne de caracteres
        
        parameters : str 

        return : str 
        La chaîne sans les accents
        '''
        s=""
        if self.mot==None:
            return(None)
        else : 
            copie=''
            for caractere in self.mot:
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

    def transforme_proposition(self):
        '''Met en majuscule et enlève les accents de la proposition
        '''
        self.mot=self.supprime_accent()
        self.mot=self.majuscule()

    def __str__(self):
        '''affiche la proposition
        '''
        return(self.mot)


# proposition=Proposition("hkzbef")
# print(proposition)

# print(proposition.est_autorise())

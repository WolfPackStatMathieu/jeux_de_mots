import requests as requests
from src.business_objects.abstract_generer_mot import AbstractGenererMot

class GenererMotApi(AbstractGenererMot):
    def __init__(self, nb_lettres):
        self.nb_lettres=nb_lettres

    def generer(self):
        req=requests.get("https://random-word-api.herokuapp.com/word?length={}".format(self.nb_lettres))
        if req.status_code==200:
            res=req.json()[0]
            mot=''
            for lettre in res:
                mot+=lettre.upper()
        return(mot)

# generation=GenererMotApi(5)
# print(generation.generer())

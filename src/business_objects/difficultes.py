class Difficultes:
    def __init__(self,nb_tentatives=6, temps=8, indice=True, nb_lettres=6):
        self.nb_tentatives=nb_tentatives
        self.temps=temps
        self.indice=indice
        self.nb_lettres=nb_lettres

    def __str__(self):
         avec_indice=""
         if self.indice==True:
             avec_indice="avec indice"
         else:
             avec_indice="sans indice"
         return("{} tentatives, {} secondes par tentatives, {}, mot de {} lettres".format(self.nb_tentatives, self.temps, avec_indice,self.nb_lettres ))


difficultes=Difficultes(None, None ,False,8)

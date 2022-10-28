import csv
from src.importation_objects.abstract_importation_liste import AbstractImportationListe


dossier = "C:/Users/mathi/Documents/Ensai/2A/S1/Projet informatique"
fichier = "listeformatCSV.csv"



liste_res = []
with open(f'{dossier}/{fichier}','r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter= ',')
    for row in reader:
        liste_res.append(row[0])
print(liste_res)

import json
from eleveC import Eleve

def lecture():
    with open("list_elev.json", "r") as f:
        data = json.load(f)
        return data

def sauvegarde():
    with open("list_elev.json", "w") as f:
        json.dump(liste_eleves, f)
        
liste_eleves = lecture()


def ajouter_eleves():
    new_eleves = Eleve()
    ne= new_eleves.r_eleve()
    liste_eleves.append(ne)
    sauvegarde()

def info_eleves():
    x= input("Entre le nom de l'eleve que tu souhaite consulter :\n=>")
    for element in liste_eleves:
        if x==element["nom"]:
            
            print(f"nom: {element['nom']}\nClasse: {element['classe']}\nnotes de maths: {element['math']}\nnotes de svt: {element['svt']}")
            print("inscrit")
            break

info_eleves()